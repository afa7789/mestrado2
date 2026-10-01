#!/usr/bin/env bash
#
# Converte .md -> .pdf usando o layout compacto compartilhado.
# Fica ao lado dos guias para que qualquer material novo herde a config.
#
#   ./build-pdf.sh guia.md              -> guia.pdf
#   ./build-pdf.sh guia.md saida.pdf    -> saida.pdf
#   ./build-pdf.sh *.md                 -> constrói todos
#
# Requer: pandoc + tectonic  (brew install pandoc tectonic)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULTS="$SCRIPT_DIR/pandoc-estudo.yaml"

[[ -f "$DEFAULTS" ]] || { echo "erro: defaults não encontrado em $DEFAULTS" >&2; exit 1; }
command -v pandoc   >/dev/null || { echo "erro: pandoc não instalado" >&2; exit 1; }
command -v tectonic >/dev/null || { echo "erro: tectonic não instalado (brew install tectonic)" >&2; exit 1; }

if [[ $# -eq 0 ]]; then
  set -- "$SCRIPT_DIR"/*.md
fi

status=0
for src in "$@"; do
  [[ -f "$src" ]] || { echo "pula: $src (não existe)" >&2; continue; }
  out="${2:-${src%.md}.pdf}"
  printf 'construindo %-34s -> %s\n' "$(basename "$src")" "$(basename "$out")"
  if pandoc --defaults="$DEFAULTS" "$src" -o "$out" 2>/tmp/pandoc-build.err; then
    pages=$(pdfinfo "$out" 2>/dev/null | awk '/^Pages/{print $2}' || echo '?')
    printf '  ok: %s páginas\n' "$pages"
  else
    printf '  FALHOU\n' >&2
    grep -E '^(error|! )' /tmp/pandoc-build.err >&2 | head -20 || tail -20 /tmp/pandoc-build.err >&2
    status=1
  fi
done

exit $status
