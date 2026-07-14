# Materiais Futuros para Explorar — Bibliografia Estendida

Bibliografia de leitura futura para a tese sobre **intents cross-chain trustless** garantidos por ZK (storage proofs + consensus proofs verificados em zero-knowledge). Reúne materiais verificados (arXiv, IACR eprint, EIPs, specs e docs oficiais) **ainda não presentes** na biblioteca, organizados por tópico para as próximas iterações da pesquisa.

> Todas as URLs foram verificadas como reais. Ressalvas de acesso pontuais estão anotadas ao final de cada seção.

---

## 1. Merkle Patricia Trie / Estado Ethereum

| Item | Descrição (PT) | URL |
|---|---|---|
| Merkle Patricia Trie — Ethereum.org Developer Docs | Referência canônica e aprofundada da MPT (state/storage/tx/receipts tries) que fundamenta as storage proofs da tese. | https://ethereum.org/en/developers/docs/data-structures-and-encoding/patricia-merkle-trie/ |
| Verkle Trees — John Kuszmaul (MIT PRIMES, 2018) | Artigo original que introduz Verkle trees via vector commitments, base teórica de provas de tamanho constante. | https://math.mit.edu/research/highschool/primes/materials/2018/Kuszmaul.pdf |
| "Verkle trees" — Vitalik Buterin (2021) | Explicação didática de como Verkle trees reduzem witnesses e habilitam stateless clients, chave para provas leves cross-chain. | https://vitalik.eth.limo/general/2021/06/18/verkle.html |
| EIP-6800: Ethereum State Using a Unified Verkle Tree | Especificação oficial da árvore Verkle unificada do estado (Bandersnatch), reduzindo witnesses de ~KBs para ~200 bytes. | https://eips.ethereum.org/EIPS/eip-6800 |
| EIP-2935: Serve Historical Block Hashes from State | Torna 8.191 block hashes acessíveis via estado, essencial para consensus/storage proofs históricos em bridges trustless. | https://eips.ethereum.org/EIPS/eip-2935 |

---

## 2. Light Clients

| Item | Descrição (PT) | URL |
|---|---|---|
| Altair Light Client — Sync Protocol Spec (ethereum/consensus-specs) | Especificação oficial do protocolo de light client via sync committee, base dos consensus proofs de PoS na tese. | https://github.com/ethereum/consensus-specs/blob/dev/specs/altair/light-client/sync-protocol.md |
| Helios — a16z (GitHub) | Light client trustless em Rust que valida o consenso Ethereum localmente; referência prática de implementação. | https://github.com/a16z/helios |
| FlyClient: Super-Light Clients for Cryptocurrencies — Bünz, Kiffer, Luu, Zamani (IACR 2019/226) | Prova superlight com download logarítmico de headers, fundamento de verificação eficiente cross-chain. | https://eprint.iacr.org/2019/226 |
| Non-Interactive Proofs of Proof-of-Work (NIPoPoWs) — Kiayias, Miller, Zindros (IACR 2017/963) | Primitiva de provas sucintas de PoW com custo logarítmico, base de bridges cross-chain trustless. | https://eprint.iacr.org/2017/963 |
| Proofs of Proof-of-Stake with Sublinear Complexity (PoPoS) — Agrawal, Neu, Tas, Zindros (IACR 2022/1642) | Primeira definição formal de PoPoS sucinto, superlight client para PoS aplicável a bridges cross-chain. | https://eprint.iacr.org/2022/1642 |

---

## 3. Consensus Proofs / Proof of Consensus

| Item | Descrição (PT) | URL |
|---|---|---|
| Casper the Friendly Finality Gadget — Buterin & Griffith (2017) | Define o gadget de finalidade PoS do Ethereum, base teórica das provas de consenso da beacon chain. | https://arxiv.org/abs/1710.09437 |
| Combining GHOST and Casper ("Gasper") — Buterin et al. (2020) | Formaliza o Gasper (LMD-GHOST + Casper FFG), o mecanismo de finalidade que uma prova de consenso precisa atestar. | https://arxiv.org/abs/2003.03052 |
| zkBridge: Trustless Cross-chain Bridges Made Practical — Xie et al. (CCS 2022) | Usa zk-SNARKs sobre cabeçalhos de bloco para pontes cross-chain trustless, diretamente alinhado ao tema da tese. | https://arxiv.org/abs/2210.00264 |
| Succinct Telepathy — telepathy-contracts (Succinct Labs) | Implementa "Proof of Consensus": light client zk on-chain do protocolo de sync committee, referência prática. | https://github.com/succinctlabs/telepathy-contracts |
| Electron zkBridge 1.0 Mainnet Launch — Electron Labs | Documenta um zk light client em produção que comprime assinaturas de validadores via SNARK entre Ethereum e NEAR. | https://medium.com/electron-labs/electron-zkbridge-1-0-mainnet-launch-3cd1e1f8f37d |

---

## 4. zkVMs

| Item | Descrição (PT) | URL |
|---|---|---|
| RISC Zero zkVM — Proof System in Detail (whitepaper) | Descrição criptográfica do zkVM baseado em zk-STARK e RISC-V, candidato para provar storage/consensus proofs. | https://dev.risczero.com/proof-system-in-detail.pdf |
| SP1 — Succinct (repositório oficial) | zkVM RISC-V de alto desempenho para provar programas Rust, usado em light clients zk (ex.: SP1 Telepathy/Tendermint). | https://github.com/succinctlabs/sp1 |
| Cairo – a Turing-complete STARK-friendly CPU architecture — Goldberg, Papini, Riabzev (IACR 2021/1063) | Arquitetura de CPU STARK-friendly da StarkNet, pioneira do conceito de VM provável. | https://eprint.iacr.org/2021/1063 |
| Jolt — a16z crypto (repositório) | zkVM RISC-V baseado em lookups (Lasso) e sum-check, realizando a "lookup singularity"; simplicidade e velocidade. | https://github.com/a16z/jolt |
| Valida ISA Spec v1.0 — Lita / Delendum | ISA sem registradores, otimizada para provas sucintas de execução, alternativa ao RISC-V para zkVMs. | https://arxiv.org/abs/2505.08114 |
| Nexus zkVM 1.0 — Enabling Verifiable Computation (whitepaper) | zkVM modular baseado em folding/recursão voltado a computação verificável em escala. | https://whitepaper.nexus.xyz/ |

---

## 5. Intents & Interoperabilidade

| Item | Descrição (PT) | URL |
|---|---|---|
| ERC-7683: Cross Chain Intents | Padrão que define interface comum de ordens para protocolos de intents cross-chain, base direta para interoperabilidade trustless de intenções. | https://eips.ethereum.org/EIPS/eip-7683 |
| ERC-4337: Account Abstraction Using Alt Mempool | Abstração de contas via UserOperations e mempool alternativo, permitindo lógica de validação customizada para assinar/executar intents. | https://eips.ethereum.org/EIPS/eip-4337 |
| The Future of MEV is SUAVE — Flashbots Collective | Apresenta o SUAVE como camada de sequenciamento/leilão que agrega preferências (intents) e captura MEV cross-domain. | https://writings.flashbots.net/the-future-of-mev-is-suave |
| Anoma Whitepaper: A Unified Architecture for Full-Stack Decentralised Applications — Goes, Sun Yin, Brink (2022) | Formaliza intents como transações parciais resolvidas por solvers, fundamento teórico da arquitetura intent-centric. | https://github.com/anoma/whitepaper/blob/main/whitepaper.md |
| Intents Architecture in Across — Across Docs | Documenta arquitetura modular (RFQ, relayers, settlement) de uma bridge intent-centric, incluindo verificação agregada e ZK na V4. | https://docs.across.to/concepts/intents-architecture-in-across |
| UniswapX Whitepaper — Adams, Zinsmeister (2023) | Ordens off-chain assinadas com leilão holandês e fillers competitivos, com extensão para swaps cross-chain; design de intents. | https://app.uniswap.org/whitepaper-uniswapx.pdf |

---

## 6. IBC / Cross-chain Messaging

| Item | Descrição (PT) | URL |
|---|---|---|
| Cosmos IBC — Interchain Standards (cosmos/ibc) | Especificação canônica do protocolo IBC (clients, TAO, ICS-20/27 etc.), messaging cross-chain baseado em verificação de estado. | https://github.com/cosmos/ibc |
| LayerZero V2 Whitepaper v2.1.1 — Zarick, Pellegrino, Zhang, Kim, Banister | Protocolo omnichain de mensagens com DVNs configuráveis e verificação/execução separadas, alternativa de messaging. | https://layerzero.network/publications/LayerZero_Whitepaper_V2.1.1.pdf |
| Hyperlane Documentation | Docs oficiais de mensageria interchain permissionless (message passing, Warp Routes) com módulos de segurança configuráveis (ISMs). | https://docs.hyperlane.xyz/ |
| Chainlink CCIP Documentation | Protocolo de interoperabilidade cross-chain com camadas Commit/Execution e defense-in-depth via redes de oráculos. | https://docs.chain.link/ccip |
| Chainlink 2.0: Next Steps in the Evolution of Decentralized Oracle Networks — Juels, Breidenbach, Cachin et al. | Redefine DONs como camada de abstração blockchain para computação off-chain e contratos híbridos, base de confiança do CCIP. | https://research.chain.link/whitepaper-v2.pdf |

---

## 7. Fundamentos de SNARKs / STARKs

| Item | Descrição (PT) | URL |
|---|---|---|
| Groth16 — On the Size of Pairing-based Non-interactive Arguments (Jens Groth, EUROCRYPT 2016) | zk-SNARK de prova mais compacta (3 elementos) e verificação O(1), base de verificadores on-chain baratos. | https://eprint.iacr.org/2016/260 |
| Marlin — Preprocessing zkSNARKs with Universal and Updatable SRS (Chiesa et al., 2019) | SNARK com SRS universal e atualizável, evitando trusted setup por circuito — verificadores de intents reutilizáveis. | https://eprint.iacr.org/2019/1047 |
| Halo — Recursive Proof Composition without a Trusted Setup (Bowe, Grigg, Hopwood, 2019) | Composição recursiva de provas sem trusted setup, fundamento para agregar provas cross-chain de forma escalável. | https://eprint.iacr.org/2019/1021 |
| The halo2 Book — Zcash / ECC | Documentação de referência do halo2 (PLONKish + acumulação), stack usado em sistemas de prova para verificação de estado. | https://zcash.github.io/halo2/ |
| STARKs — Scalable, Transparent, and Post-Quantum Secure Computational Integrity (Ben-Sasson et al., 2018) | STARKs transparentes (sem trusted setup) e pós-quânticos, base de provas de integridade para consensus/storage proofs. | https://eprint.iacr.org/2018/046 |
| FRI — Fast Reed-Solomon Interactive Oracle Proofs of Proximity (Ben-Sasson et al., ICALP 2018) | Protocolo de proximidade que dá aos STARKs prova linear e verificação logarítmica — núcleo de commitments sem pairing. | https://eccc.weizmann.ac.il/report/2017/134/ |
| KZG — Constant-Size Commitments to Polynomials and Their Applications (Kate, Zaverucha, Goldberg, ASIACRYPT 2010) | Compromissos polinomiais de tamanho constante, base de PLONK/Marlin e de provas de estado eficientes on-chain. | https://www.iacr.org/archive/asiacrypt2010/6477178/6477178.pdf |
| Plonky2 Whitepaper — Polygon Zero | Sistema recursivo FRI+PLONK sobre o campo Goldilocks, otimizado para recursão rápida — provas cross-chain agregadas. | https://github.com/0xPolygonZero/plonky2/blob/main/plonky2/plonky2.pdf |
| Plonky3 — Polygon Zero (repositório) | Toolkit modular de PIOPs (campos, PCS FRI, STARKs) que hoje sustenta zkVMs — infraestrutura para provadores de intents. | https://github.com/Plonky3/Plonky3 |
| Nova — Recursive Zero-Knowledge Arguments from Folding Schemes (Kothapalli, Setty, Tzialla, 2021) | Introduz folding schemes para recursão incremental (IVC) de baixo custo — dobrar múltiplas provas de blocos/estados. | https://eprint.iacr.org/2021/370 |

---

## 8. Ecossistema de Storage Proofs

| Item | Descrição (PT) | URL |
|---|---|---|
| Axiom — Documentação (Proving API / OpenVM) | Coprocessador ZK que prova consultas sobre dados históricos do Ethereum on-chain; API de prova para estado verificável. | https://docs.axiom.xyz/ |
| Lagrange — ZK Coprocessor Overview (Docs) | Coprocessador ZK que prova consultas SQL sobre dados on-chain; inclui State Committees (light client ZK) para interop. | https://docs.lagrange.dev/zk-coprocessor/overview |
| Brevis — zkCoprocessor Docs | Coprocessador ZK que permite a contratos ler todo o histórico on-chain de várias chains e computar de forma trustless. | https://coprocessor-docs.brevis.network/ |
| Relic Protocol — Intro / Litepaper (Docs) | Acesso trustless a todo o estado histórico do Ethereum via acumulação de block hashes e provas Merkle-Patricia. | https://docs.relicprotocol.com/overview/intro-to-relic-protocol/ |
| Herodotus HDP — Data Processor (Docs) | Herodotus Data Processor: verifica storage proofs em zkVM e delega computação sobre dados on-chain autenticados. | https://docs.herodotus.dev/herodotus-docs/developers/data-processor |

---

## 9. Grupos de Pesquisa e Eventos — Blockchain

| Item | Descrição (PT) | URL |
|---|---|---|
| IC3 — Initiative for Cryptocurrencies and Contracts | Consórcio acadêmico de 13 universidades com pesquisa fundacional em blockchain (criptografia aplicada, consenso, PLs, mechanism design). Publica papers relevantes para storage proofs, consensus proofs e intents. | https://ic3research.org/ |
| IC3 — Publications | Index de publicações dos membros IC3; inclui papers sobre light clients, bridges, zk-SNARKs e consenso. | https://ic3research.wordpress.com/publications/ |
| IC3 — Projects | Projetos de pesquisa ativos: inclui trabalhos sobre verificabilidade, privacidade e infraestrutura blockchain. | https://ic3research.wordpress.com/projects/ |
| IC3 — YouTube | Canal com palestras e talks do IC3 Blockchain Camp e eventos. | https://www.youtube.com/channel/UCz-eTbD4kHkYxGhUfXawHow |
| Crypto x AI Survey (IC3, 2026) | Survey sobre intersecção crypto×IA, sistematiza trabalho existente e identifica open questions relevantes. | https://aic3.io/ |
| IC3 Blockchain Camp 2026 | Evento anual (Princeton, Jun 2026) com talks técnicas e hackathons — boa fonte de papers e apresentações. | https://ic3research.org/ic3-blockchain-camp-2026/ |
| IC3 Winter Retreat 2026 | Retreat técnico (Engelberg, Jan 2026) — formato íntimo com discussão de pesquisa avançada. | https://ic3research.org/ic3-winter-retreat-2026/ |

> **Nota:** IC3 é particularmente relevante para a tese porque seus membros publicaram papers fundamentais sobre light clients, consensus proofs e bridges trustless (ex.: NIPoPoWs, FlyClient, etc. — já referenciados na Seção 2). O grupo também organiza eventos onde a galera apresenta papers de blockchain com foco acadêmico rigoroso.

---

## Notas de verificação e ressalvas

- **Relic Protocol** (Tópico 8): página indexada com conteúdo ativo, mas `docs.relicprotocol.com` falhou na resolução de DNS via fetch neste ambiente; verificado apenas por indexação de busca. Alternativa fetchável relacionada: *Historical and Multichain Storage Proofs* (arXiv 2411.00193) — já presente na biblioteca.
- **Lagrange overview** (Tópico 8): URL real e indexada; o fetch retornou HTTP 403 (Cloudflare), não inexistência — a página existe.
- **Plonky2** (Tópico 7): o whitepaper migrou de `mir-protocol/plonky2` para `0xPolygonZero/plonky2`; usada a URL atual do PDF.
- **Altair sync-protocol.md** (Tópico 2): existência confirmada na branch `dev` via GitHub Contents API (fetch direto retornou 404 transitório).

### Fontes complementares canônicas (alternativas para citação)
- Cairo em PDF IACR: https://eprint.iacr.org/2021/1063.pdf
- Jolt — artigo formal "SNARKs for Virtual Machines via Lookups" (IACR 2023/1217): https://eprint.iacr.org/2023/1217 · docs: https://jolt.a16zcrypto.com/
- Nexus zkVM — repositório: https://github.com/nexus-xyz/nexus-zkvm · docs: https://docs.nexus.xyz/zkvm
- SP1 — docs oficiais: https://docs.succinct.xyz/docs/sp1/introduction
- zkBridge na ACM DL: https://dl.acm.org/doi/10.1145/3548606.3560652
