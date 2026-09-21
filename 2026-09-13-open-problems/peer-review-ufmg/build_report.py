"""Render the consolidated review and full panel as static HTML, without JS."""

import html
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
IDEAS = {
    1: ("Zswap: Merkle → KZG/Caulk+", "swap-kzg"),
    2: ("Zswap: agregação com SnarkPack", "swap-aggregation"),
    3: ("Empréstimo: certificado de garantia por faixa", "loan-interval"),
    4: ("Atualização privada de witnesses KZG", "kzg"),
    5: ("Revogação privada de credenciais", "revogacao"),
    6: ("Recuperação de pagamentos após ficar offline", "carteira"),
}
CSS = """
body { max-width: 90ch; margin: 0 auto; padding: 1rem; font-family: system-ui, sans-serif; line-height: 1.6; overflow-wrap: break-word; }
h1, h2, h3 { line-height: 1.25; }
h2 { margin-top: 2.5rem; }
table { border-collapse: collapse; width: 100%; font-size: .9rem; }
th, td { text-align: left; padding: .4rem; border-bottom: 1px solid; vertical-align: top; }
td, th { overflow-wrap: anywhere; }
li { margin-block: .6rem; }
pre { overflow-x: auto; }
footer { margin-top: 3rem; border-top: 1px solid; }
"""


def number(value, digits=1):
    value = Decimal(str(round(value, 8))).quantize(
        Decimal("1").scaleb(-digits), rounding=ROUND_HALF_UP
    )
    return f"{value:.{digits}f}".replace(".", ",")


def page(title, markdown):
    renderer = MarkdownIt("commonmark", {"html": False}).enable("table")
    body = renderer.render(markdown)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>{CSS}</style>
</head>
<body>
  <nav aria-label="Navegação"><a href="../">Voltar às seis ideias</a> · <a href="./">Ranking</a> · <a href="panel.html">Painel completo</a></nav>
  <main>{body}</main>
  <footer><p>Consulta: 14/09/2026. Avaliação de ideias por agentes de IA; não é parecer oficial da UFMG.</p></footer>
</body>
</html>
"""


def main():
    scores = json.loads((ROOT / "scores.json").read_text())
    assert scores["rewrite_reviews_complete"], "Complete all 30 cross-reviews before publication"
    panel = json.loads((ROOT / "panel.json").read_text())
    mapping = json.loads((ROOT / "anonymization.json").read_text())

    ranking = [
        "| Posição | Ideia | Nota / 10 | Menor–maior parecer |",
        "|---|---|---:|---:|",
    ]
    criteria = [
        "| Ideia | Problema / aderência (35%) | Originalidade / coerência (35%) | Viabilidade (30%) |",
        "|---|---:|---:|---:|",
    ]
    for row in scores["ideas"]:
        idea_id = row["id"]
        name, anchor = IDEAS[idea_id]
        score = row["score"]
        ranking.append(
            f"| {row['rank']}º | [Ideia {idea_id} — {name}](../#{anchor}) | "
            f"**{number(score['mean'])}** | {number(score['min'], 2)}–{number(score['max'], 2)} |"
        )
        criteria.append(
            f"| Ideia {idea_id} | "
            + " | ".join(number(row["criteria"][key]["mean"]) for key in ("relevance", "originality", "feasibility"))
            + " |"
        )

    report = (ROOT / "report.md").read_text()
    report = report.replace("<!-- RANKING_TABLE -->", "\n".join(ranking))
    report = report.replace("<!-- CROSS_REVIEW_SYNTHESIS -->", (ROOT / "synthesis.md").read_text().strip())
    report = report.replace(
        "<!-- PANEL_LINKS -->",
        "## Notas por critério e pareceres\n\n" + "\n".join(criteria)
        + "\n\n[Os seis pareceres, reescritas e 30 críticas cruzadas](panel.html) · "
        "[Dados das notas](scores.json) · [Método](methodology.md) · "
        "[Fontes institucionais](sources.json) · [Edital local, página 15](edital-ppgcc-2026.pdf#page=15) · "
        "[Relatório em Markdown](README.md)\n",
    )
    assert "<!--" not in report
    (ROOT / "README.md").write_text(report)
    (ROOT / "index.html").write_text(page("Ranking das seis ideias — PPGCC/UFMG", report))

    full = [
        "# Painel completo: seis ideias de mestrado",
        "[Ler a recomendação consolidada](./) · [Método e limitações](methodology.md)",
        "Seis análises em contextos separados e trinta críticas cruzadas de reescritas. "
        "Nenhuma persona avaliou a própria versão. As identidades abaixo foram associadas às versões após as críticas.",
        "## Painel",
        "| Identificação | Especialidade | Lema | Estilo | Tipo |",
        "|---|---|---|---|---|",
    ]
    for person in panel:
        full.append("| " + " | ".join(person[key] for key in ("id", "specialty", "motto", "style", "agent_type")) + " |")

    full.append("\n## Análises integrais\n")
    rewrites = {}
    for person in panel:
        reviewer = person["id"]
        text = (ROOT / "analyses" / f"{reviewer}.md").read_text()
        analysis, rewrite = text.split("## REWRITE", 1)
        rewrites[reviewer] = rewrite
        full.extend([f"\n### Parecer {reviewer}\n", analysis.removeprefix("## ANALYSIS").strip()])

    full.append("\n## Reescritas integrais\n")
    for reviewer, rewrite in rewrites.items():
        full.extend([f"\n### Versão de {reviewer}\n", rewrite.strip()])

    full.extend([
        "\n## Matriz das 30 críticas cruzadas\n",
        "Linhas: revisores. Colunas: autores das reescritas. Os valores avaliam a qualidade dos textos "
        "e não devem ser confundidos com as notas das seis ideias. Pesos desta matriz: clareza 15%, solidez 35%, "
        "consistência 25%, estrutura 10%, originalidade 15%. São escolhas do painel, não da UFMG.",
        "| Revisor / versão | P1 | P2 | P3 | P4 | P5 | P6 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ])
    matrix = {(r["reviewer"], r["author"]): r["weighted"] for r in scores["cross_review_matrix"]}
    for person in panel:
        reviewer = person["id"]
        cells = ["—" if author["id"] == reviewer else number(matrix[reviewer, author["id"]], 2) for author in panel]
        full.append("| " + reviewer + " | " + " | ".join(cells) + " |")

    full.extend(["\n### Médias e variâncias por reescrita\n", "| Versão | Média ponderada | Variância | Pareceres |", "|---|---:|---:|---:|"])
    for row in scores["rewrites"]:
        full.append(f"| {row['author']} | {number(row['score']['mean'], 2)} | {number(row['score']['variance'], 4)} | {row['score']['n']} |")

    full.append("\n## Críticas integrais\n")
    for person in panel:
        reviewer = person["id"]
        identities = "; ".join(f"{version} = {author}" for version, author in mapping[reviewer].items())
        full.extend([
            f"\n### Revisão cruzada {reviewer}\n",
            "Correspondência revelada após a revisão: " + identities + ".\n",
            (ROOT / "cross-reviews" / f"{reviewer}.md").read_text().strip(),
        ])
    full.extend(["\n## Síntese\n", (ROOT / "synthesis.md").read_text().strip(), "\n## Documento final consolidado\n", report])
    full_text = "\n\n".join(full) + "\n"
    (ROOT / "panel-completo.md").write_text(full_text)
    (ROOT / "panel.html").write_text(page("Painel completo — avaliação das seis ideias", full_text))
    print("Rendered ranking, full panel, 30-review matrix and consolidated Markdown.")


if __name__ == "__main__":
    main()
