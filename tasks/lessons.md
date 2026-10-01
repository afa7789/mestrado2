# Lessons

## 2026-09-24 — Obtendo PDFs binários de fontes bloqueadas (webfetch)
- webfetch **corrompe** downloads binários diretos (PDFs): os flate streams chegam danificados ("Bad FCHECK in flate stream") e `pdftotext` retorna 0 bytes.
- Caminho confiável: GitHub blob API (`api.github.com/repos/<org>/<repo>/git/blobs/<sha>`) retorna JSON com `content` em base64; o webfetch preserva o ASCII; decodificar localmente com `base64.b64decode`.
- Para achar o blob: `git/trees/<ref>?recursive=1` e procurar o caminho do PDF.
- Aplicado com sucesso a: Tornado Whitepaper v1.4 (`berkeley-defi/berkeley-defi.github.io`) e Privacy Pools whitepaper (`0xbow-io/privacy-pools-website/public/whitepaper.pdf`).
- Sites bloqueados para webfetch que já testei: SSRN `Delivery.cfm` (403), sciencedirect.com (403), tornado.cash (transport error), GitHub code search UI (requer login).
- IDs eprint fornecidos pelo usuário estavam errados (2019/1148, 2023/180): sempre verificar o repositório real (tornado.cash/audits, privacypools.com) em vez de confiar na numeração do eprint.