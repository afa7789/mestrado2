# YouTube ZK / Cross-chain / Rollup Talks — Referências

> Biblioteca de referências para a dissertação (ZK / cross-chain / storage proofs / consensus proofs).
> Coletado em 2026-07-14.

## Nota de método / limitações (IMPORTANTE)

O YouTube **bloqueou a extração** de descrições e de listas de vídeos via WebFetch: tanto as páginas de
playlist (`/playlist?list=...`) quanto as de vídeo (`/watch?v=...`) retornaram apenas o rodapé de
navegação (o conteúdo real é renderizado por JavaScript, que o WebFetch não executa). Portanto:

- **Não foi possível enumerar a lista completa de vídeos** de nenhuma das três playlists.
- **Não foi possível capturar a descrição verbatim** (com os links do autor) de nenhum dos vídeos.
- A **identidade de cada vídeo/playlist** (título, canal, edição do Devcon) foi obtida de forma confiável
  via a API pública **oEmbed** do YouTube (`/oembed?...&format=json`) e cruzada com o **Devcon Archive**.
- Os links listados abaixo em "Referências relacionadas" foram encontrados por **busca web pelo tema do
  talk**, e **não** extraídos da descrição do vídeo (que o YouTube não entregou). Isso está marcado
  explicitamente. Cada URL foi verificado por HTTP. Nada foi inventado.

Legenda da coluna "Resolve?": `200` = HTTP 200 OK; `403 (bot)` = a página existe mas bloqueia clientes
automatizados (curl) — acessível em navegador normal.

---

## Playlist 1 — "trustless:// interop.landscape" (canal: Account and Chain Abstraction / @ERC-4337)
URL: https://www.youtube.com/watch?v=EFiSyP-Zu7s&list=PLMf-2qLTukXoyHFmJr5D6XRTEyh_-9z17

Esta playlist **não é uma trilha oficial do Devcon**. Pertence ao canal **"Account and Chain Abstraction"**
(`@ERC-4337`, YouTube) e faz parte do ecossistema da conferência **trustless://** (interoperabilidade
trust-minimized entre rollups, ERC-4337, EIL/OIF). Tema: como construir um rollup Ethereum Stage 2 e
interop trustless entre L2s. Relevante para a parte de cross-chain / consensus proofs da tese.

Vídeos enumerados (YouTube bloqueou a lista completa da playlist):

1. [trustless://interop.landscape] Workshop - How to build a Stage 2 Ethereum Rollup  *(vídeo atual da lista)*

**Descrição do vídeo:** não recuperável (YouTube bloqueou). Os links abaixo foram encontrados por busca
pelo tema do workshop (interop trustless + rollup Stage 2), NÃO confirmados como estando na descrição:

| Item | Tipo | URL | Resolve? |
|---|---|---|---|
| trustless:// (conferência) | Site / evento | https://trustlessconference.com/ | 200 |
| Trustless Interoperability between Rollups: Landscape, Constructions, and Challenges (1kx) | Artigo/paper | https://1kx.network/writing/trustless-interoperability-between-rollups-landscape-constructions-and-challenges | 200 |
| Mesmo artigo (mirror Medium) | Blog | https://medium.com/1kxnetwork/trustless-interoperability-between-rollups-landscape-constructions-and-challenges-8ff195ea92cc | 403 (bot) |
| EIL: Trust-minimized cross-L2 interop | Ethereum Research | https://ethresear.ch/t/eil-trust-minimized-cross-l2-interop/23437 | 200 |
| Making Ethereum Feel Like One Chain Again (EIL) | Blog EF | https://blog.ethereum.org/2025/11/18/eil | 200 |
| L2 Interop Working Group — Call #2 | Notas/spec | https://notes.ethereum.org/@rudolf/interop-call2 | 200 |
| Introducing Stages — framework de maturidade de rollups (L2BEAT) | Blog | https://medium.com/l2beat/introducing-stages-a-framework-to-evaluate-rollups-maturity-d290bb22befe | 403 (bot) |
| L2BEAT Stages (Stage 0/1/2) | Referência | https://l2beat.com/stages | 200 |

---

## Playlist 2 — Devcon SEA (Devcon 7, Bangkok, nov/2024) — canal: Ethereum Foundation
URL: https://www.youtube.com/watch?v=haxfI3A-E4g&list=PLaM7G4Llrb7wzshzdWkwmddVJYagkkEgz

Playlist do canal oficial **Ethereum Foundation**, edição **Devcon SEA (Devcon 7)**, Bangkok, novembro de
2024. O vídeo atual é uma keynote de política/privacidade (caso Tornado Cash), não um talk técnico de ZK,
mas está na coleção. YouTube bloqueou a enumeração completa da playlist.

Vídeos enumerados:

1. Keynote: Glass Houses and Tornados — Peter Van Valkenburgh (Coin Center) | Devcon SEA  *(vídeo atual da lista)*

**Descrição do vídeo:** não recuperável no YouTube. Abstract confirmado no Devcon Archive: aborda como as
sanções e processos criminais contra o Tornado Cash desafiaram suposições sobre licenciamento de
transmissão de dinheiro, leis anti-lavagem e sanções, e a suposição de que blockchains devem permanecer
transparentes.

| Item | Tipo | URL | Resolve? |
|---|---|---|---|
| Devcon Archive — Keynote: Glass Houses and Tornados | Página do talk (abstract) | https://archive.devcon.org/devcon-7/keynote-glass-houses-and-tornados/ | 200 |
| Coin Center — Glass Houses and Tornados (texto da keynote) | Blog/artigo | https://www.coincenter.org/glass-houses-and-tornados-keynote-at-devcon-sea/ | 200 |

---

## Playlist 3 — Devcon Bogotá (Devcon 6, out/2022) — canal: Ethereum Foundation
URL: https://www.youtube.com/watch?v=umLmjsi_GbY&list=PLaM7G4Llrb7x5JgkfCN9kf7IB6QtomyCu

Playlist do canal oficial **Ethereum Foundation**, edição **Devcon Bogotá (Devcon 6)**, outubro de 2022.
O vídeo atual é um talk técnico de ZK (ferramentaria zkSNARK). YouTube bloqueou a enumeração completa.

Vídeos enumerados:

1. A ZoKrates Update — Thibaut Schaeffer | Devcon Bogotá  *(vídeo atual da lista)*

**Descrição / abstract (confirmado no Devcon Archive):** "zkSNARKs estão se tornando um pilar das
tecnologias descentralizadas" mas ainda são difíceis para iniciantes. O talk apresenta atualizações do
**ZoKrates**, um toolbox que simplifica a criação de aplicações de zero-knowledge proof por meio de uma
linguagem de alto nível em vez de projeto manual de circuitos. Duração 24:14. Tags: Privacy, Language,
zkSNARK, ZoKrates. A página do Archive **não listou** links externos/papers.

| Item | Tipo | URL | Resolve? |
|---|---|---|---|
| Devcon Archive — A ZoKrates Update | Página do talk (abstract) | https://archive.devcon.org/devcon-6/a-zokrates-update/ | 200 |
| ZoKrates — repositório | GitHub | https://github.com/Zokrates/ZoKrates | 200 |
| ZoKrates — documentação | Docs/site | https://zokrates.github.io/ | 200 |

---

## Papers / specs / recursos mais relevantes para a biblioteca

Selecionados dos itens extraídos acima, com foco em cross-chain / rollups / ZK tooling:

- **Trustless Interoperability between Rollups: Landscape, Constructions, and Challenges** (1kx) — panorama
  de interop trust-minimized entre rollups. https://1kx.network/writing/trustless-interoperability-between-rollups-landscape-constructions-and-challenges
- **EIL: Trust-minimized cross-L2 interop** (Ethereum Research) — construção de interop cross-L2 minimizando
  confiança. https://ethresear.ch/t/eil-trust-minimized-cross-l2-interop/23437
- **Making Ethereum Feel Like One Chain Again (EIL)** (EF Blog) — visão de UX/arquitetura de interop.
  https://blog.ethereum.org/2025/11/18/eil
- **L2BEAT Stages** — framework de maturidade/descentralização de rollups (Stage 0/1/2), base do "Stage 2".
  https://l2beat.com/stages
- **ZoKrates** — toolbox/linguagem de alto nível para zkSNARKs em Ethereum (repo + docs).
  https://github.com/Zokrates/ZoKrates · https://zokrates.github.io/
- **Coin Center — Glass Houses and Tornados** — referência de política/privacidade (Tornado Cash, sanções),
  útil para contexto regulatório de privacy/ZK. https://www.coincenter.org/glass-houses-and-tornados-keynote-at-devcon-sea/

> Observação: para papers formais (arXiv/eprint) e specs (EIPs) referenciados NAS descrições dos vídeos,
> seria necessário abrir cada vídeo em um navegador (o YouTube bloqueou a extração automatizada da
> descrição). Nenhum link de arXiv/eprint/EIP foi confirmado a partir das descrições nesta coleta.
