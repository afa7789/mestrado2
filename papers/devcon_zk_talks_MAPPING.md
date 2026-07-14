# Devcon 6 (Bogotá 2022) — Trilha ZKP: Mapeamento Palestra → Paper/Spec

> Biblioteca de referência para dissertação de mestrado (ZK / cross-chain / storage proofs).
> Para cada uma das 50 palestras da trilha ZKP, buscou-se o paper acadêmico (arXiv / IACR eprint) ou a spec/whitepaper canônica subjacente.
> URLs verificadas em 2026-07-14. PDFs genuínos (arXiv / IACR) foram baixados para `devcon_zk_talks/`. IACR eprint foi obtido via Wayback Machine (Cloudflare bloqueia curl direto).

## Resumo auditado

- **8 palestras** têm vínculo direto ou fundacional forte com **paper acadêmico contemporâneo** (arXiv/IACR); **2 outras** (#20 e #47) têm somente leitura acadêmica relacionada e foram rebaixadas na auditoria. Há **7 PDFs acadêmicos únicos** em `devcon_zk_talks/`; 7/25/41 compartilham WAKU-RLN, #27 (Vampire) já está em `../Vampire_zkSNARK_eprint2022-406.pdf`, e #44 aponta para trabalho posterior (2026), não para um paper apresentado em 2022.
- **14 palestras** mapeiam para **spec/whitepaper** (link apenas — não é PDF arXiv/IACR, fora da regra de download).
- **26 palestras** são **talk-only** (sem paper ou spec formal subjacente — libraries, apps, painéis, relatos de experiência).
- **9 PDFs locais verificados** estão na pasta: os 7 acadêmicos anteriores mais o whitepaper Semaphore (#24) e o relatório PSE UniRep (#46). Todos abrem como PDF e tiveram a contagem de páginas conferida com `pdfinfo`.

### Critério de evidência e confiança

- **Alta** — título/autoria/conteúdo da página oficial da palestra coincide diretamente com o paper/spec, ou o próprio projeto mantém o documento canônico.
- **Média** — paper é fundamento técnico explícito do sistema apresentado, mas a palestra não afirma ser apresentação daquele paper.
- **Baixa / leitura relacionada** — tema próximo, sem evidência de que o documento seja base da palestra. Não deve ser citado como “paper subjacente”.
- As páginas do **Devcon Archive** são a evidência primária para título, palestrante, data e resumo. URLs de IACR/arXiv, documentação oficial e repositórios das organizações são a evidência primária dos documentos.

---

## Papers baixados (PDFs genuínos arXiv / IACR)

| # | Palestra | Tipo | Paper | URL | Baixado (arquivo, páginas) |
|---|----------|------|-------|-----|----------------------------|
| 2 | Little Things I've Learned in Developing Halo2 Circuits — Chih-Cheng Liang | paper | Halo: Recursive Proof Composition without a Trusted Setup (Bowe, Grigg, Hopwood) | https://eprint.iacr.org/2019/1021 | `devcon_zk_talks/02_Halo_Recursive_Proof_Composition.pdf` — 31 pág. |
| 7 | Building Privacy-Protecting Infrastructure — Oskar Thorén | paper | WAKU-RLN-RELAY: Privacy-Preserving Peer-to-Peer Economic Spam Protection | https://arxiv.org/abs/2207.00117 | `devcon_zk_talks/07_25_41_WAKU_RLN_Relay_arXiv_2207.00117.pdf` — 7 pág. |
| 20 | Are Your Zero-Knowledge Proofs Correct? — Jon Stephens (Veridise) | leitura relacionada (baixa) | Automated Detection of Under-Constrained Circuits in Zero-Knowledge Proofs | https://eprint.iacr.org/2023/512 | `devcon_zk_talks/20_Veridise_Underconstrained_Circuits_ZKP.pdf` — 25 pág.; **posterior à palestra (2023), não pode ser paper subjacente** |
| 21 | Non-interactive, Unique Nullifiers (PLUME) — Aayush Gupta | paper | PLUME: An ECDSA Nullifier Scheme for Unique Pseudonymity within ZKPs (ERC-7524) | https://eprint.iacr.org/2022/1255 | `devcon_zk_talks/21_PLUME_ECDSA_Nullifier_eprint2022-1255.pdf` — 26 pág. |
| 25 | Rate Limiting Nullifier (RLN) — AtHeartEngineer | paper | WAKU-RLN-RELAY (mesmo paper da #7) | https://arxiv.org/abs/2207.00117 | (compartilha `07_25_41_WAKU_RLN_Relay_arXiv_2207.00117.pdf` — 7 pág.) |
| 27 | Vampire, a Novel, Cheap to Verify, zkSNARK — Michal Zajac | paper | Vampire zkSNARK | https://eprint.iacr.org/2022/406 | `../Vampire_zkSNARK_eprint2022-406.pdf` (já na biblioteca) |
| 40 | Scaling up Trustless Neural Network Inference with ZKPs | paper | Scaling up Trustless DNN Inference with Zero-Knowledge Proofs (Kang, Hashimoto, Stoica, Sun) | https://arxiv.org/abs/2210.08674 | `devcon_zk_talks/40_Trustless_NN_Inference_2210.08674.pdf` — 12 pág. |
| 41 | Using ZKP for better p2p messaging with Waku | paper | WAKU-RLN-RELAY (mesmo paper da #7) | https://arxiv.org/abs/2207.00117 | (compartilha `07_25_41_WAKU_RLN_Relay_arXiv_2207.00117.pdf` — 7 pág.) |
| 47 | SNARK Light Clients — Uma Roy (Succinct) | leitura relacionada (baixa) | SoK: Blockchain Light Clients | https://eprint.iacr.org/2021/1657 | `devcon_zk_talks/47_SNARK_Light_Clients_SoK_eprint_2021-1657.pdf` — 28 pág.; **não há evidência reunida de autoria/vínculo direto com a palestra** |
| 49 | The Future of PlonK ish System | paper | PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge | https://eprint.iacr.org/2019/953 | `devcon_zk_talks/49_PlonK_eprint_2019-953.pdf` — 34 pág. |

**Descrições (PT):**
- **#2 Halo** — Fundamento teórico do Halo2: composição recursiva de provas sem setup confiável via esquema de acumulação.
- **#7 WAKU-RLN-RELAY** — Proteção anti-spam econômica preservando privacidade em rede p2p (Waku) via Rate-Limiting Nullifier (zkSNARK).
- **#20 Veridise** — Detecção automática de circuitos sub-restringidos (underconstrained) em Circom que permitiriam testemunhas maliciosas; base do Picus.
- **#21 PLUME** — Esquema de nullifier determinístico sobre ECDSA garantindo pseudonímia única em provas ZK.
- **#25 RLN** — Mesmo paper da #7; gadget ZK que limita taxa de mensagens por época e revela o segredo do infrator em caso de spam.
- **#27 Vampire** — zkSNARK novo, barato de verificar (já baixado anteriormente).
- **#40 Trustless NN Inference** — Primeiro método prático em escala ImageNet para verificar inferência de redes neurais de forma não-interativa via ZK-SNARKs.
- **#41 Waku** — Mesmo paper da #7; mensageria p2p do Waku usando RLN/Semaphore para proteção anti-spam anônima.
- **#47 SNARK Light Clients** — SoK acadêmico sobre light clients de blockchain, incluindo abordagens baseadas em SNARK (referência canônica do tema).
- **#49 PlonK** — Paper original do PlonK, SNARK universal com setup atualizável que fundamenta os sistemas "PlonK-ish".

---

## Specs / whitepapers (link apenas)

| # | Palestra | Tipo | Spec/Whitepaper | URL | Baixado? |
|---|----------|------|-----------------|-----|----------|
| 1 | A ZoKrates Update — Thibaut Schaeffer | spec | ZoKrates (docs). Paper subjacente: Eberhardt & Tai, IEEE iThings 2018 (paywall) | https://zokrates.github.io/ | Não (paper IEEE pago; sem arXiv/IACR) |
| 4 | Designing Public Goods Using ZKPs — Rachel | spec | MACI — Minimal Anti-Collusion Infrastructure | https://maci.pse.dev/ | Não (spec de protocolo) |
| 8 | Penumbra: Private DEX with ZKPs & Threshold Crypto — Henry de Valence | spec | The Penumbra Protocol Specification (Groth16 s/ BLS12-377, flow encryption) | https://protocol.penumbra.zone/main/index.html | Não (spec em site) |
| 9 | Interep: Identity Bridge Web2→Web3 — Geoff Lamperd | spec | Semaphore (base do Interep) | https://docs.semaphore.pse.dev/ | Não (spec/proposta) |
| 12 | Scaling Privacy with Starlight (EY) | spec | Starlight ZKP compiler (docs/repo) | https://github.com/EYBlockchain/starlight | Não (docs de projeto) |
| 13 | ZK Badges — dhadrien (Sismo) | spec | Sismo attestation protocol / sismo-badges | https://github.com/sismo-core/sismo-badges | Não (whitepaper/docs) |
| 17 | Public Goods and Experiments, the journey of Zkopru — Wanseob Lim | spec | Zkopru: ZK Optimistic Rollup (post fundador) | https://ethresear.ch/t/zkopru-zk-optimistic-rollup-for-private-transactions/7717 | Não (spec em ethresear.ch) |
| 18 | Building a Unirep ecosystem — Chance Hudson | spec | UniRep protocol (docs) | https://developer.unirep.io/ | Não (spec/docs) |
| 24 | Anonymous Signalling on Ethereum — Cedoor (Semaphore) | whitepaper (alta) | Semaphore: Zero-Knowledge Signaling on Ethereum | https://semaphore.pse.dev/whitepaper-v1.pdf | `devcon_zk_talks/24_Semaphore_whitepaper_v1.pdf` — 16 pág. |
| 28 | Shielded Voting Using Threshold Encryption (Shutter) | spec | Shutter — shielded voting via threshold/homomorphic encryption (blog técnico) | https://blog.shutter.network/coming-soon-to-daos-permanent-shielded-voting-via-homomorphic-encryption/ | Não (blog/spec) |
| 32 | A New DeFi Primitive - Private DCA Trading with Aztec Connect | spec | Aztec Connect — private DeFi bridge (docs/blog) | https://aztec.network/blog/private-defi-with-the-aztec-connect-bridge | Não (spec/blog) |
| 42 | Worldcoin | spec | Worldcoin: Private by Design (World ID whitepaper) | https://worldcoin-company-website.cdn.prismic.io/worldcoin-company-website/Zuvl4bVsGrYSvlIU_WorldcoinPrivateByDesign.pdf | Não (whitepaper corporativo) |
| 44 | zkemail: Decentralized ID Verification on Chain — Aayush Gupta | paper posterior (baixa para a palestra) | ZK Proofs of Generalized Regex Matching for Anonymized Email Verification (ZK Email) | https://eprint.iacr.org/2026/1284 | Não; publicado em 2026, portanto é evolução posterior, não paper subjacente à palestra de 2022 |
| 46 | Unirep Social: A demo application of Unirep protocol | relatório técnico (alta) | UniRep: A Protocol for Sharing Credibility Across Anonymous Accounts (PSE) | https://reports.pse.dev/reports/Applied_ZKP_Primitives/UniRep/UniRep.pdf | `devcon_zk_talks/46_UniRep_PSE_report.pdf` — 7 pág. |

**Descrições (PT):**
- **#1 ZoKrates** — Toolbox para gerar/verificar zkSNARKs em Solidity a partir de linguagem de alto nível.
- **#4 MACI** — ZKPs para votação privada e financiamento de bens públicos resistente a suborno.
- **#8 Penumbra** — DEX privada (Cosmos) combinando ZKPs e criptografia de limiar (flow encryption) para swaps confidenciais.
- **#9 Interep** — Ponte de identidade que traz reputação de contas Web2 para identidades anônimas on-chain via Semaphore.
- **#12 Starlight** — Compilador da EY que marca variáveis privadas em Solidity e gera circuitos ZKP automaticamente.
- **#13 Sismo ZK Badges** — Badges ZK (ERC1155 não-transferíveis) que atestam fatos sobre contas web2/web3 preservando privacidade.
- **#17 Zkopru** — Rollup L2 que combina zk-SNARK e optimistic rollup para transações privadas.
- **#18 UniRep** — Protocolo ZK de reputação universal e não-repudiável via epoch keys anônimas.
- **#24 Semaphore** — Protocolo de sinalização anônima via zk-SNARK e árvore de Merkle de compromissos de identidade.
- **#28 Shutter** — Voto secreto via encriptação de limiar (DKG + Keypers); votos só decriptados após o encerramento.
- **#32 Aztec Connect** — Primitiva de DeFi para DCA privado sobre a ponte Aztec Connect.
- **#42 Worldcoin** — Prova de personhood via biometria (Orb) e ZKPs; whitepaper de privacidade do World ID.
- **#44 zkEmail** — Verifica assinaturas DKIM e faz matching de regex em ZK para provar propriedades de e-mails on-chain sem servidores. Paper canônico existe (IACR 2026/1284) mas não pôde ser baixado.
- **#46 Unirep Social** — App demo do protocolo UniRep (reputação anônima e não-repudiável).

---

## Talk-only (sem paper/spec formal subjacente)

| # | Palestra | Tipo | Observação | URL |
|---|----------|------|-----------|-----|
| 3 | What to know about Zero Knowledge | talk-only | Panorama educacional | https://archive.devcon.org/archive/watch/6/what-to-know-about-zero-knowledge/ |
| 5 | A SNARKs Tale: Building SNARK Solutions on Mainnet | talk-only | Relato de experiência | https://archive.devcon.org/archive/watch/6/a-snarks-tale-a-story-of-building-snark-solutions-on-mainnet/ |
| 6 | ELI5: Zero Knowledge — Wanseob Lim | talk-only | Didática, ligada ao Zkopru | https://archive.devcon.org/devcon-6/eli5-zero-knowledge/ |
| 10 | Recursive ZK Applications and Affordances | talk-only | Panorama (refs: Halo 2019/1021, Nova 2021/370) | https://archive.devcon.org/archive/watch/6/recursive-zk-applications-and-affordances/ |
| 11 | Scalability is Boring, Privacy is Dead — Ian Miers | talk-only | Reflexão de opinião (ref: Zerocash, eprint 2014/349) | https://eprint.iacr.org/2014/349 |
| 14 | Towards a Feature-Complete...Privacy Layer for Ethereum | talk-only | Visão/design da PSE | https://archive.devcon.org/archive/watch/6/towards-a-feature-complete-and-backwards-compatible-privacy-layer-for-ethereum/ |
| 15 | ZKPs and "Programmable Cryptography" — gubsheep | talk-only | Ensaio/blog (0xPARC) | https://notes.0xparc.org |
| 16 | Private Exchange on ZKOPRU — Takamichi Tsutsumi | talk-only | App experimental sobre Zkopru | https://archive.devcon.org/archive/watch/6/private-exchange-on-zkopru/ |
| 19 | ZK Proof Performance and Security Characteristics — Brian Wilkes | talk-only | Apenas slide-deck (não é paper) | https://archive.devcon.org/resources/6/zk-proof-performance-and-security-characteristics.pdf |
| 22 | Private Value Transfer in 10 Lines — Maxim Vezenov | talk-only | Demo do Aztec Noir | https://archive.devcon.org/archive/watch/6/private-value-transfer-in-10-lines/ |
| 23 | ZK Application Design Patterns — Yi Sun & Lakshman Sankar (Axiom) | talk-only | Padrões de design | https://archive.devcon.org/archive/watch/6/zk-application-design-patterns/ |
| 26 | Why We Need Threshold FHE for Blockchains — Wei Dai | talk-only | Conceito MOCCAs (ref: smartFHE eprint 2021/133) | https://archive.devcon.org/archive/watch/6/why-we-need-threshold-fhe-for-blockchains/ |
| 29 | Improving Performance of Provable Computations Using Rust | talk-only | Cairo VM em Rust | https://archive.devcon.org/archive/watch/6/improving-performance-of-provable-computations-using-rust/ |
| 30 | Public-Private Composability — Mike Connor (Aztec) | talk-only | Arquitetura do Aztec | https://archive.devcon.org/archive/watch/6/public-private-composability/ |
| 31 | Lessons from the Field: Threat Modeling for Digital Currency | talk-only | Talk prática (CBDC threat modeling) | https://archive.devcon.org/archive/watch/6/ |
| 33 | Optimizing Cryptographic Algorithms used in Gnark | talk-only | Library (gnark/gnark-crypto) | https://archive.devcon.org/devcon-6/optimizing-cryptographic-algorithms-used-in-gnark/ |
| 34 | Next Generation DSLs and IRs - Panel | talk-only | Painel (DSLs/IRs para circuitos ZK) | https://archive.devcon.org/archive/watch/6/next-generation-dsls-and-irs/ |
| 35 | STARKs in SNARKs — Jordi Baylina | talk-only | Recursão STARK→FFLONK (Polygon zkEVM, blog) | https://polygon.technology/blog/the-go-fast-machine-adding-recursion-to-polygon-zkevm |
| 36 | ZK Circuits for Elliptic Curve Operations in Halo2 | talk-only | Library (halo2-ecc, Axiom) | https://archive.devcon.org/archive/watch/6/zk-circuits-for-elliptic-curve-operations-in-halo2/ |
| 37 | Crypt Keeper ZK Identity Wallet | talk-only | App (extensão de navegador) | https://archive.devcon.org/archive/watch/6/crypt-keeper-zk-identity-wallet/ |
| 38 | heyanon.xyz | talk-only | App (Personae Labs) | https://archive.devcon.org/archive/watch/6/heyanonxyz/ |
| 39 | Proof Systems for zkRollups | talk-only | Panorama de sistemas de prova | https://archive.devcon.org/archive/watch/6/ |
| 43 | Zero Knowledge Machine Learning | talk-only | Introdução genérica (ref próxima: arXiv 2210.08674, já baixado como #40) | https://archive.devcon.org/archive/watch/6/ |
| 45 | Zkitter - Anonymous Social Network | talk-only | App sobre Semaphore/RLN | https://pse.dev/en/projects/zkitter |
| 48 | Auditing Strategy for zkEVM | talk-only | Estratégia de auditoria (sem paper contemporâneo) | https://archive.devcon.org/archive/watch/6/ |
| 50 | Maze - Aggregation Tool for Circom PLONK Proofs | talk-only | CLI open-source (agrega provas PLONK) | https://github.com/privacy-ethereum/maze |

---

## Arquivos em `devcon_zk_talks/`

```
02_Halo_Recursive_Proof_Composition.pdf              31 pág.  (IACR 2019/1021)
07_25_41_WAKU_RLN_Relay_arXiv_2207.00117.pdf          7 pág.  (arXiv 2207.00117 — talks 7, 25, 41)
20_Veridise_Underconstrained_Circuits_ZKP.pdf        25 pág.  (IACR 2023/512)
21_PLUME_ECDSA_Nullifier_eprint2022-1255.pdf         26 pág.  (IACR 2022/1255)
24_Semaphore_whitepaper_v1.pdf                       16 pág.  (whitepaper oficial)
40_Trustless_NN_Inference_2210.08674.pdf             12 pág.  (arXiv 2210.08674)
46_UniRep_PSE_report.pdf                              7 pág.  (relatório PSE)
47_SNARK_Light_Clients_SoK_eprint_2021-1657.pdf      28 pág.  (IACR 2021/1657)
49_PlonK_eprint_2019-953.pdf                         34 pág.  (IACR 2019/953)
```

Total verificado na pasta: **9 PDFs** (7 acadêmicos + 2 técnicos). Palestra 27 (Vampire, IACR 2022/406) já estava em `../Vampire_zkSNARK_eprint2022-406.pdf`.

## Lacunas não resolvidas

- **#26 Threshold FHE:** o paper contemporâneo e diretamente relevante é *PESCA: A Privacy-Enhancing Smart-Contract Architecture* (Wei Dai, IACR 2022/1119), que usa threshold FHE. Evidência: https://eprint.iacr.org/2022/1119 e cópia oficial do autor em https://wdai.us/files/2022/PESCA.pdf. O download IACR retornou HTTP 403 e a tentativa pela cópia do autor foi interrompida; por isso nenhum arquivo parcial foi mantido. Confiança **alta** como paper relacionado à fala/autoria, mas não foi possível confirmar pelo texto arquivado da palestra que ela apresentava formalmente o PESCA.
- **#20:** a página oficial confirma que Jon Stephens apresentou pesquisa e ferramentas Veridise, mas o PDF disponível é de 2023. Falta localizar uma publicação contemporânea específica; classificação final: **leitura posterior**, não paper subjacente.
- **#47:** a página/podcast contemporâneo confirma o projeto Succinct de light clients por SNARK, mas não vincula o SoK 2021/1657 à palestra. Falta um paper autoral específico; classificação final: **leitura de contexto**.
- Os demais itens `talk-only` permanecem sem paper/spec formal identificado. Isso é uma conclusão conservadora, não prova de inexistência.
