# Devcon & Devconnect — Referências ZK

> Biblioteca de referência para dissertação de mestrado (ZK / cross-chain / storage proofs / consensus proofs).
> Foco principal: trilhas e conteúdo de **Zero-Knowledge / criptografia aplicada** nos eventos da Ethereum Foundation.
> Todas as URLs foram verificadas (HTTP 200) em 2026-07-14.

---

## 1. O que são Devcon e Devconnect

**Devcon** é a conferência anual de referência da Ethereum Foundation, realizada desde 2014. Reúne uma vez por ano todo o ecossistema (pesquisadores, desenvolvedores e comunidades) para aprender, construir e se conectar em torno de tecnologia open-source. As edições são numeradas (Devcon 0 a 7). A edição mais recente realizada foi a **Devcon 7 (SEA)**, em Bangkok, Tailândia (novembro de 2024) — a maior até hoje, com ~6.000 participantes e ~350 palestrantes. A próxima é a **Devcon 8**, em Mumbai, Índia (3–6 de novembro de 2026).

**Devconnect** é um evento colaborativo de uma semana, formado por diversos eventos independentes co-localizados (não é uma conferência única de palco). O foco é construção colaborativa, workshops e coworking entre times do ecossistema. A edição mais recente foi a **Devconnect Argentina**, em Buenos Aires (17–22 de novembro de 2025) — apresentada como a "primeira Ethereum World's Fair", com mais de 14.000 participantes e distritos temáticos (DeFi, Privacy, Layer 2s, Hardware & Wallets, AI, etc.). Edições anteriores: Istambul (2023) e Amsterdã (2022).

---

## 2. Links oficiais

| Recurso | Descrição | URL |
|---|---|---|
| Devcon (home) | Site oficial; atualmente exibe a Devcon 8 (Mumbai, 2026) | https://devcon.org/en/ |
| Devcon Archive | Biblioteca de vídeos das palestras (Devcon 0–7 + Devconnect ARG), filtrável por evento e tags | https://archive.devcon.org/ |
| Devconnect (home) | Site oficial do Devconnect (edição Argentina 2025) | https://devconnect.org/ |
| Devcon Forum | Fórum oficial de discussão do Devcon (DIPs, Community Hubs, RFPs) | https://forum.devcon.org/ |
| Fellowship of Ethereum Magicians | Fórum técnico da comunidade Ethereum (EIPs, ERCs, RIPs) | https://ethereum-magicians.org/ |
| Ethereum Foundation Blog | Blog oficial da EF (anúncios, R&D, recaps de eventos) | https://blog.ethereum.org/ |
| Devcon no X (Twitter) | Conta oficial "@EFDevcon" (Deva the Devcon Unicorn) | https://x.com/EFDevcon |

---

## 3. Conteúdo ZK — FOCO PRINCIPAL

### 3.1. Devcon Archive filtrado por tags

O Devcon Archive permite filtrar as palestras por tag. Abaixo os filtros mais relevantes para ZK / criptografia / privacidade. As duas primeiras foram fornecidas pelo usuário; as demais usam nomes de tag reais existentes no arquivo.

| Tag / Filtro | O que traz | URL |
|---|---|---|
| Applied Cryptography | Palestras de criptografia aplicada (SNARKs/STARKs, MPC, FHE, primitivas), ordenadas por edição mais recente | https://archive.devcon.org/watch/?tags=Applied+Cryptography&sort=eventId&order=desc |
| Cypherpunk | Trilha Cypherpunk & Privacy (filosofia, privacidade, keynotes tipo "Glass Houses and Tornados") | https://archive.devcon.org/watch/?tags=Cypherpunk&sort=eventId&order=desc |
| Zero Knowledge | Palestras diretamente sobre provas de conhecimento zero (ELI5 ZK, ZK aplicado, etc.) | https://archive.devcon.org/watch/?tags=Zero+Knowledge&sort=eventId&order=desc |
| Privacy | Privacidade no Ethereum (anonimato, unlinkability, mixers, privacy-preserving apps) | https://archive.devcon.org/watch/?tags=Privacy&sort=eventId&order=desc |
| Layer 2 | Rollups (incl. ZK-rollups / validity proofs) e escalabilidade | https://archive.devcon.org/watch/?tags=Layer+2&sort=eventId&order=desc |

> Nota: o Archive é uma SPA — todos os links de tag retornam HTTP 200 e a filtragem ocorre no navegador. As tags acima foram confirmadas como reais a partir do conteúdo do arquivo.

### 3.2. Playlists no YouTube

Títulos, canais e contagem de vídeos verificados diretamente nos metadados de cada playlist.

| Playlist | Canal | Vídeos | Conteúdo | URL |
|---|---|---|---|---|
| **trustless://** | @ERC-4337 | ~35 | Série técnica sobre sistemas trustless / rollups / account abstraction. Vídeo de entrada: *"Workshop - How to build a Stage 2 Ethereum Rollup"*. Relevante para validity/ZK proofs em rollups Stage 2. | https://www.youtube.com/watch?v=EFiSyP-Zu7s&list=PLMf-2qLTukXoyHFmJr5D6XRTEyh_-9z17 |
| **Why decentralization matters** | @EthereumFoundation | ~19 | Playlist curada pela Ethereum Foundation sobre descentralização/privacidade. Vídeo de entrada: *"Glass Houses and Tornados"* (keynote de Peter Van Valkenburgh na Devcon SEA — trilha Cypherpunk & Privacy). | https://www.youtube.com/watch?v=haxfI3A-E4g&list=PLaM7G4Llrb7wzshzdWkwmddVJYagkkEgz |
| **DevCon 6 - ZKPs: Privacy, Identity, Infrastructure & More Track** | @EthereumFoundation | (trilha completa) | Trilha oficial de ZKPs da Devcon 6 (Bogotá, 2022): privacidade, identidade e infraestrutura ZK. Vídeo de entrada: *"A ZoKrates Update" (Thibaut Schaeffer)*. **A playlist mais diretamente sobre ZK.** | https://www.youtube.com/watch?v=umLmjsi_GbY&list=PLaM7G4Llrb7x5JgkfCN9kf7IB6QtomyCu |

---

## 4. IC3 — Initiative for Cryptocurrencies and Contracts

**IC3** é um consórcio acadêmico de 13 universidades (Cornell, Princeton, UC Berkeley, etc.) focado em pesquisa fundacional em blockchain. Diferente dos eventos da EF (Devcon/Devconnect), IC3 é primariamente um **grupo de pesquisa acadêmico** que também organiza eventos onde papers são apresentados — incluindo o **IC3 Blockchain Camp** e o **Winter Retreat**.

| Recurso | Descrição | URL |
|---|---|---|
| IC3 (home) | Site oficial do consórcio | https://ic3research.org/ |
| Publications | Index de papers dos membros IC3 | https://ic3research.wordpress.com/publications/ |
| Projects | Projetos de pesquisa ativos | https://ic3research.wordpress.com/projects/ |
| YouTube | Canal com talks e palestras | https://www.youtube.com/channel/UCz-eTbD4kHkYxGhUfXawHow |
| Crypto x AI Survey (2026) | Survey recente crypto×IA | https://aic3.io/ |

> **Relevância para a tese:** Membros do IC3 publicaram papers fundamentais sobre light clients e bridges trustless que já estão na biblioteca (NIPoPoWs, FlyClient, PoPoS — ver Seção 2 de `FUTURE_materials_to_explore.md`). O IC3 Blockchain Camp (Princeton, anual) é um evento onde a galera apresenta papers de blockchain com foco acadêmico rigoroso.

---

## Resumo das 3 playlists

1. **`trustless://`** (canal @ERC-4337, ~35 vídeos) — série sobre rollups/trustless/account abstraction; abre com o workshop *"How to build a Stage 2 Ethereum Rollup"*.
2. **`Why decentralization matters`** (canal @EthereumFoundation, ~19 vídeos) — playlist curada pela EF; abre com o keynote Cypherpunk *"Glass Houses and Tornados"* (Peter Van Valkenburgh, Devcon SEA).
3. **`DevCon 6 - ZKPs: Privacy, Identity, Infrastructure & More Track`** (canal @EthereumFoundation) — trilha oficial de ZKPs da Devcon 6 (Bogotá, 2022); a mais focada em Zero-Knowledge.
