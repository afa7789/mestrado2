# Biblioteca de Papers — Intents Cross-Chain Trustless (Storage Proofs + Consensus Proofs + ZK)

Bibliografia para a pesquisa sobre um protocolo de **intents cross-chain trustless**, onde uma
chain (B) verifica, sem confiar num backend, que um evento (a liquidação de um intent) realmente
ocorreu noutra chain (A). A ideia central usa **duas provas complementares**, ambas verificadas
via **Zero-Knowledge**:

1. **Consensus Proof** → prova que o bloco pertence legitimamente à blockchain (foi produzido e finalizado corretamente).
2. **Storage Proof** → prova que determinado estado/valor realmente existe *naquele* bloco (dentro da Merkle Patricia Trie da EVM).

> Fluxo: `User → assina Intent → Chain A (contrato verifica assinatura, atualiza estado) → Storage Proof + Consensus Proof → ZK Proof → Chain B verifica → continua execução`.
> Sem o consensus proof, alguém poderia fabricar um storage proof de um estado inexistente.

Todos os PDFs foram verificados como arquivos reais (não páginas de erro HTML). Links verificados (HTTP 200) em 2026-07-14.

---

## 📖 Ordem de leitura recomendada

Vai do funcionamento interno da Ethereum até arquiteturas completas de intents cross-chain.

| # | Item | Arquivo |
|---|------|---------|
| 1 | Ethereum Yellow Paper (State Trie / MPT) | `00_Ethereum_Yellow_Paper.pdf` |
| 2 | EIP-1186 (`eth_getProof`) | `02_EIP-1186_eth_getProof.md` |
| 3 | Historical and Multichain Storage Proofs | `03_Historical_Multichain_Storage_Proofs_2411.00193.pdf` |
| 4 | Herodotus Docs (Storage Proofs + Block Hash Accumulator) | `04a_*.md`, `04b_*.md` |
| 5 | zkBridge | `01_zkBridge_2210.00264.pdf` |
| 6 | Zendoo | `06_Zendoo_2002.01847.pdf` |
| 7 | Consensus in the Age of Blockchains | `07_Consensus_Age_of_Blockchains_1711.03936.pdf` |

Complementos: Bankai (consensus proving), Daloc (protocolo de referência), Aztec e Miden (zkVMs / provas).

---

## 1. Fundamentos da Ethereum (State Trie & MPT)

### Ethereum Yellow Paper
- **Arquivo:** `00_Ethereum_Yellow_Paper.pdf` (42p) · **Link:** https://ethereum.github.io/yellowpaper/paper.pdf
- Especificação formal da EVM. Para esta pesquisa importa a estrutura de estado da Ethereum: a
  **State Trie**, a **Storage Trie** e a **Merkle Patricia Trie (MPT)** — a base sobre a qual todo
  storage proof é construído. É onde se entende *o que* exatamente uma prova de storage está provando.

### EIP-1186 (`eth_getProof`)
- **Arquivo:** `02_EIP-1186_eth_getProof.md` · **Link:** https://eips.ethereum.org/EIPS/eip-1186
- Especificação (não é paper) que formaliza o RPC `eth_getProof`, que retorna **account proofs** e
  **storage proofs** da Ethereum. É a interface concreta e padronizada para obter as provas de
  inclusão na MPT que os sistemas de storage proof consomem. Leitura curta e prática.

## 2. Storage Proofs

### Historical and Multichain Storage Proofs (vlayer Labs, 2024)
- **Arquivo:** `03_Historical_Multichain_Storage_Proofs_2411.00193.pdf` · **Link:** https://arxiv.org/abs/2411.00193
- O paper mais próximo do que a arquitetura descreve. Cobre Ethereum Storage Proofs, Merkle Patricia
  Trie, **MMR (Merkle Mountain Range)**, acesso a **estado histórico**, verificação **cross-chain** e
  o uso de **ZK**, comparando arquiteturas. Ponte direta entre os fundamentos e a aplicação cross-chain.

### Herodotus Docs — Storage Proofs
- **Arquivo:** `04a_Herodotus_Docs_StorageProofs.md` · **Link:** https://docs.herodotus.dev/herodotus-docs/developers/storage-proofs
- Documentação técnica (tratada como "paper" no contexto do projeto). Explica storage proofs como a
  combinação de **Inclusion Proofs** (dado existe na MPT) + **Proofs of Computation** + **ZK Proofs**,
  permitindo acesso on-chain a dados com a segurança da camada base.

### Herodotus Docs — Historical Block Hash Accumulator
- **Arquivo:** `04b_Herodotus_Docs_HistoricalBlockHashAccumulator.md` · **Link:** https://docs.herodotus.dev/herodotus-docs/protocol-design/historical-block-hash-accumulator
- Como a Herodotus prova hashes de blocos históricos: percorre a cadeia (parent hash → parent hash até
  o genesis) provando em **ZK-STARK/Cairo** e acumula os hashes válidos em dois **MMRs** (Keccak256 e
  Poseidon). Equivale a um "EIP-2935 sem mudanças de protocolo".

## 3. Cross-chain + ZK (bridges)

### zkBridge: Trustless Cross-chain Bridges Made Practical (2022)
- **Arquivo:** `01_zkBridge_2210.00264.pdf` (20p) · **Link:** https://arxiv.org/abs/2210.00264
- Autores incluem **Dan Boneh** e **Dawn Song** (Berkeley). Provavelmente o paper mais importante sobre
  comunicação cross-chain via ZK. Introduz uma bridge **trustless** baseada em provas sucintas e mostra
  como **provar que um bloco pertence à cadeia** e transportar mensagens entre blockchains — exatamente
  a combinação consensus proof + mensagem que a arquitetura precisa.

## 4. Sidechains usando ZK

### Zendoo: a zk-SNARK Verifiable Cross-Chain Transfer Protocol (2020)
- **Arquivo:** `06_Zendoo_2002.01847.pdf` (40p) · **Link:** https://arxiv.org/abs/2002.01847
- Propõe comunicação entre sidechains via **zk-SNARKs**, desacoplando a chain principal da lógica
  interna das sidechains. A chain principal verifica as sidechains só pelas provas, sem conhecer os
  detalhes internos — um modelo de referência de verificação trustless entre cadeias.

## 5. Consenso

### Consensus in the Age of Blockchains (2017)
- **Arquivo:** `07_Consensus_Age_of_Blockchains_1711.03936.pdf` (17p) · **Link:** https://arxiv.org/abs/1711.03936
- Survey sobre mecanismos de consenso. Não fala de ZK, mas explica com precisão o que significa "um
  bloco pertencer legitimamente a uma blockchain" — o conceito que o **consensus proof** formaliza
  criptograficamente.

---

## Consensus Proving na prática — Bankai

### Stateless Light Clients for PoS Blockchains (Paul Etscheit, Bankai)
- **Arquivo:** `bankai_research_paper.pdf` (18p) · **Fonte:** https://bankai.xyz/
- Core técnico de **consensus proving**: um **light client stateless** que roda off-chain. Em vez de um
  contrato on-chain com estado que exige atualização perpétua, comprime o histórico de validação da
  cadeia PoS em **provas STARK recursivas** de tamanho constante, passando o estado criptograficamente
  entre provas e seguindo o *finality gadget* da própria cadeia. Complementar à Herodotus: Bankai prova
  *qual header é canônico*; storage proofs provam *que estado esse header compromete*.
- Autor = o cofundador "Paul" citado (**Paul Etscheit**, `paul@bankai.xyz`, GitHub `petscheit`).
- **Detalhes de repos/links (Herodotus + Bankai):** ver `herodotus_bankai_REFERENCES.md`.

---

## Protocolo de referência (Prime Brokerage / Intents)

### Daloc: A Cross-Chain Prime Brokerage Protocol for Collateralized Credit (Herodotus)
- **Arquivo:** `05_Herodotus_DALOC_Whitepaper.pdf` (36p) · **Fonte:** https://github.com/HerodotusDev/daloc-whitepaper
- É o whitepaper do **Prime Brokerage Protocol** — protocolo DeFi baseado em **intents** que exige
  comunicação cross-chain e pretende migrar do backend tradicional (confiança num servidor) para uma
  arquitetura **trustless** usando exatamente storage proofs + consensus proofs + ZK. Serve como o caso
  de uso concreto que amarra toda a bibliografia.

---

## Projetos ZK relacionados

### Aztec — https://aztec.network (`aztec/`)
Rollup ZK focado em privacidade. O time do Aztec autorou sistemas de prova fundamentais usados
amplamente no ecossistema:

- **PLONK** — `aztec/Aztec_PLONK_eprint2019-953.pdf` (33p) · https://eprint.iacr.org/2019/953
  - Sistema de prova SNARK universal com *trusted setup* reutilizável. Base de grande parte dos ZK-rollups.
- **PLOOKUP** — `aztec/Aztec_PLOOKUP_eprint2020-315.pdf` (10p) · https://eprint.iacr.org/2020/315
  - Argumento de *lookup* que torna eficiente provar operações não-aritméticas (ex.: tabelas, XOR/bitwise) em circuitos PLONK.
- **Aztec Protocol Whitepaper** — `aztec/Aztec_Protocol_Whitepaper.pdf` (24p) · https://aztec.network
  - Arquitetura do protocolo Aztec (privacidade + ZK rollup).

### Miden — https://miden.xyz (`miden/`)
zkVM / rollup baseado em **STARKs**. O Miden **não publica um whitepaper de VM em PDF** — a spec
técnica autoritativa (design, constraints AIR, instruction set) vive só nas docs:
VM https://docs.miden.xyz/reference/miden-vm/ · Protocol https://docs.miden.xyz/reference/protocol.
Os PDFs abaixo são os papers técnicos de fato assinados pelo time Miden (via IACR eprint):

- **Adding ZK to STARKs** — `miden/Miden_Adding_ZK_to_STARKs_eprint2024-1037.pdf` (17p) · https://eprint.iacr.org/2024/1037
  - Como acrescentar zero-knowledge (privacidade) a provas STARK, que por padrão são apenas sucintas mas não ZK.
- **STARK-based Signatures / RPO** — `miden/Miden_STARK_Signatures_RPO_eprint2024-1553.pdf` (32p) · https://eprint.iacr.org/2024/1553
  - Esquema de assinaturas baseado em STARK usando a hash Rescue-Prime Optimized (RPO), relevante para intents assinados provados em ZK.
- **Arithmetization-Oriented Encryption** — `miden/Miden_Arithmetization_Oriented_Encryption_eprint2023-1668.pdf` (9p) · https://eprint.iacr.org/2023/1668
  - Cifra desenhada para ser barata dentro de circuitos/AIR (arithmetization-friendly).

_Referências completas de Miden e Aztec (incl. Aztec Yellow Paper e papers extras): ver `miden_aztec_LINKS.md`._

---

## Índice de arquivos

```
papers/
├── README.md                                             ← este arquivo
├── 00_Ethereum_Yellow_Paper.pdf                          (42p)
├── 01_zkBridge_2210.00264.pdf                            (20p)
├── 02_EIP-1186_eth_getProof.md
├── 03_Historical_Multichain_Storage_Proofs_2411.00193.pdf
├── 04a_Herodotus_Docs_StorageProofs.md
├── 04b_Herodotus_Docs_HistoricalBlockHashAccumulator.md
├── 05_Herodotus_DALOC_Whitepaper.pdf                     (36p) — Prime Brokerage
├── 06_Zendoo_2002.01847.pdf                              (40p)
├── 07_Consensus_Age_of_Blockchains_1711.03936.pdf        (17p)
├── bankai_research_paper.pdf                             (18p) — consensus proving
├── herodotus_bankai_REFERENCES.md                        — repos + links Herodotus/Bankai
├── miden_aztec_LINKS.md                                  — links Miden/Aztec
├── aztec/  (PLONK 33p, PLOOKUP 10p, Protocol Whitepaper 24p)
└── miden/  (Adding ZK to STARKs 17p, STARK Signatures/RPO 32p, AO Encryption 9p)
```
