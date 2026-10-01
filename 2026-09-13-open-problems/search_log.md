# Registro da busca — 13/09/2026

Busca web dirigida, seguida de abertura de fontes primárias e leitura de trechos dos PDFs. Não é uma revisão sistemática nem um censo bibliográfico. Resultados de buscadores foram usados para descoberta; a fundamentação da seleção usa papers, documentação oficial e repositórios de autores. Notícias, agregadores e resumos automáticos não fundamentam as propostas.

## Consultas principais e decisões

| Família | Exemplos de consultas executadas | Consequência |
|---|---|---|
| Revogação | `"zk-creds" "revocation"`; `"anonymous credentials" "revocation" "2025"`; `"SNARK" "revocation" "2026" credentials` | Encontrados zk-creds, PRC e trabalhos recentes; revogação genérica descartada como novidade |
| Recuperação privada de witnesses | `cryptographic accumulators private delegation 2026 witness updates`; `"private" "Merkle" "PIR" witness update` | Encontrados ePrint 2026/832, TreePIR, Scaling Semaphore e implementação Zcash; combinação genérica Merkle+PIR não selecionada |
| Revogação autenticada | `"TAPIR" "Authenticated" "PIR"`; leitura de §4.1 e §5.3 do PRC | R2 formulada a partir da limitação contra corrupção ativa; composição com APIR permanece hipótese |
| Carteiras e mensagens | `"oblivious message" "2025" "2026"`; `"InstantOMR"`; `"Oblivious Signaling" paper`; `"UnifOMR"` | R3 passou a focar recuperação do histórico após overflow; UnifOMR acrescentado como baseline recente |
| Matching privado | `"Zswap" "zk-SNARK" matching future`; `"Indifferential Privacy" dark pool code`; `"Renegade" dark pool whitepaper MPC` | R4 delimitada à privacidade relaxada de volumes; descartada a alegação de que matching MPC+ZK seria novo |
| Delegação de provas | `"zkSaaS" private delegation proving 2025 2026` | Encontrados DFS, Siniel, coZK e trabalhos próximos; sem recorte suficientemente sustentado para a seleção principal |
| Provas de exploit | `"zkpoex" paper multi transaction limitations`; título exato do artigo; `"zero-knowledge proofs of exploits" recursive`; `"proof" "exploit" "multi-transaction" "zero"` | R1 formulada; distinguidos o código dos autores, outro projeto homônimo e a dissertação; pesquisa não estabelece ausência de solução equivalente |
| Segurança de circuitos | `"SNARK" vulnerabilities "smart contract" 2025 2026`; `"Circuzz" "SnarkProbe" "zkFuzz"`; título exato de Circuzz; `"zk" "circuit" "stateful" testing` | R5 delimitada à interface com contrato e estado, com alerta sobre trabalhos de context-binding |
| Reputação | `"zk-promises" anonymous credentials`; `"zk-promises" "private record certification"` | Paper lido para evitar reapresentar callbacks, bloqueio ou batching como inéditos; não selecionado como proposta principal |

Consultas compostas ou muito específicas retornaram, por vezes, resultados irrelevantes. Ausência de resultado útil não foi interpretada como prova de novidade. Também houve triagem inicial de light clients, shuffle, prova de passivos e zkTLS; sem um recorte melhor sustentado que os cinco escolhidos nesta rodada.

## Conferências relevantes

- PRC: limitação contra autoridades ativamente maliciosas conferida na página 8 do PDF; não confundida com sua propriedade de privacidade.
- Oblivious Signaling: FIFO com capacidade limitada, exclusões do modelo e comparação OMR conferidas na página 15 do PDF.
- Circuzz: passagem sobre ampliar oráculos de verificação encontrada na página 8 da cópia arXiv.
- Zswap: matching concreto deixado em aberto em §1.3, página 4 do PDF de PoPETs.
- Indifferential Privacy: adversário semi-honesto e informação pública/privada conferidos em §2, página 3 do PDF AAMAS.
- zkpoex: a limitação explícita de várias transações no README pertence a `zkoranges/zkPoEX`, distinto de `ziemen4/zkpoex`. A dissertação do autor descreve um trace EVM e propõe formalizar condições na página 96.
- TAPIR: ePrint registra ACNS 2026; README menciona ACNS'25. Registrada a divergência em vez de copiar o ano do código.
- UnifOMR: incluído após encontrar trabalho mais recente; a consulta a resumo/metadados não foi descrita como leitura integral.

## Limites e próximos testes de novidade

1. R1: obter a versão final SAC do artigo; comparar provas sequenciais com ferramentas atuais e com execução única segmentada pela zkVM. O download ACM respondeu HTTP 403; foi usada cópia pública da dissertação do autor, em URL fixada por commit.
2. R2: revisar ALLOSAUR e outras construções de revogação citadas pelo PRC; definir a autenticidade da raiz e a ameaça de conluio cliente-servidor. APIR verificado apenas pelo cliente não fecha esse problema.
3. R3: revisar implementações atuais de UnifOMR e alternativas de histórico/inbox; calcular custo completo de manter duas formas de recuperação e avaliar vazamento por retries.
4. R4: verificar composição das garantias de IDP com liquidação e definir se o operador segue sendo semi-honesto. Não equiparar essa garantia à do matching via MPC.
5. R5: verificar versões atuais de Circuzz, SNARKProbe e zkFuzz, e ler integralmente o preprint de context-binding. Delimitar o que uma análise conjunta detecta além das ferramentas existentes.

O pacote registra hipóteses para escolha e leitura. Não afirma ganhos de desempenho, descoberta de vulnerabilidades novas, prova formal concluída ou lacuna global confirmada.

---

# Registro da busca — 23/09/2026 (rodada "mais perguntas em aberto")

Rodada com o `BuscadorPaper` (`grafo_procura_schoolar/`, `research-graph 0.1.0`). Sementes: três PDFs localizados em `~/Downloads` e copiados para `papers/`: BSCI'25 (ZKP privacy-preserving transactions, `10.1145/3709016.3737794`), ZKVault (`10.2139/ssrn.6602198`) e a dissertação de Lehigh "Privacy-Preserving Compliance" (extração parcial — só leitura até a pág. 8). Config dedicada: `config.open-questions.yaml`; resultado parcial em `output-open-questions/`.

## Perguntas em aberto identificadas nas sementes

- **ZKVault (IEEE/SSRN 2026), §VII**:
  1. Integração de sistemas pós-quânticos (zk-STARKs) para eliminar o threat model quântico — ainda não endereçado.
  2. Recursão (Nova, Halo2) para agregar múltiplas provas de credenciais — sugerido, não implementado.
  3. Padronização de schemas de credencial (W3C VC, DIF Presentation Exchange) — lacuna de interoperabilidade.
  4. Avaliação empírica em pilotos com instituições reguladas — inexistente.
- **BSCI'25 (§5 conclusão)**: aceleração por hardware da geração de prova é citada como caminho, verificificação on-chain enxuta já demonstrada; sem comparação com STARKs pós-quânticos nem tratamento de setup confiável.
- **Lehigh thesis (sumário §7)**: DSL de restrições, inferência/otimização de provas, backends de provadores alternativos, transporte de prova de compliance por mixers, latência, aceitação industrial/regulatória. Conteúdo completo não lido (extração parcial).

## Resultado do programa (incompleto)

- `ingest` (OpenAlex + Semantic Scholar + Crossref + arXiv): 144 papers únicos; filtrados para 34 focados (≥2020, tópicos KYC/SSI/compliance/confidential transaction/recursão/pós-quântico/auditabilidade). Inclui ZKVault, BSCI'25, SwapCT, GENES, zkSSI e trabalhos de cross-border payments e sanctions em DeFi.
- `expand` (retrospectivamente: refs+citants via OpenAlex/S2/Crossref): não concluiu — processo terminou sem gravar; frontier de 6 seeds ainda gerou ~90 min de requisições. Otimização necessária: rate-limit ou frontier menor/max_hops=1.
- `download-pdfs`: rodou em background; cache `/openalex`, `/scihub`, `/annas`, `/unpaywall`, `/scidb` recebeu arquivos, mas `papers.json` final (164 entradas) ficou sem `pdf_path` — resultados não consolidados.
- Bugs corrigidos no BuscadorPaper: `source_provenance` tolera string vs lista (models/ingestion/dedupe/openalex_pdf); `_resolve_id` e coletores toleram `None`/exceções de providers que não implementam `get_references`.

## Perguntas em aberto encontradas nos PDFs baixados

Dos 15 PDFs baixados para o cache, 12 tinham texto extraível; abaixo as perguntas em aberto localizadas nos relevantes ao tema do mestrado.

- **Zswap (PoPETs 2022), scihub/fa502c…, §8**: "An interesting open question is how to integrate Zswap with private smart contracts to support more elaborate private DeFi solutions" — primeiro passo seria estender um sistema de smart contracts público com políticas de minting para ativos privados (ex.: trading privado de NFTs).
- **"An Exploration of Constraint Systems in Verifiable Computation" (tese de doutorado, openalex/da5ac4…)**: comparações binárias são gargalo relevante em R1CS ("binary comparisons become a major performance bottleneck, especially for operations that occur frequently or on large bit-widths"); extensões expressivas do modelo AIR para reduzir o gap entre especificações de alto nível e representação algébrica em sistemas STARK; redução do tamanho de chaves/parâmetros é apontada como direção imediata. São perguntas em aberto alinhadas com a lacuna de aritmetização do tema.
- **"Cryptography for a Verifiable World" (tese UPM, openalex/2dfcc1…)**: vários problemas em aberto explícitos conceituados na área de compromissos funcionais e provas suculentas: (a) parâmetros públicos quadráticos na largura do circuito ("aiming for public parameters that are quadratic in the circuit width, which we believe is an interesting open question"); (b) esquema algébrico baseado em pairing onde |ck|·|π| = poly(λ)·o(s) ("a challenging open problem"); (c) provas algébricas BARG a partir de suposições de reticulado ("One notable open problem is to realize algebraic BARGs from lattice assumptions"); (d) instanciações competitivas para provas recursivas como pergunta em aberto.
- **"Byzantine-Tolerant Belief Aggregation over MerkleDAGs" (preprint 2026, openalex/3283b1…)**: limitações declaradas em §14 — correlação de fontes (desconto por informação mútua), redução de redutore por embeddings, prova mecanicizada (Coq/Lean) da convergência (verificação exaustiva bounded até N=6), suavidade de influência (escala quadrática de reputação), reticulação de identidade externa para operação permissionless. Relevância ao tema: revogação/convergência em identidade descentralizada.
- **Tese "Adaptive fund allocation for game-based verifiable computation outsourcing" (openalex/1b0857…)**: cap. 8 apresenta conclusões e trabalho futuro; o trecho não foi lido integralmente nesta rodada (registrado para leitura).
- **Informatica 49 (2025), openalex/a7a342… - transações privadas com aprendizado**: limitações declaradas — experimentos em ambiente simulado (sem robustez sob condições adversas reais), latência de ~5ms por transação do ajuste por aprendizado (impacta sistemas acima de ~10.000 TPS), overhead de 15% de storage para parâmetros dinâmicos; futuro: ambientes cross-chain e integração com criptografia homomórfica.

## Complemento — 24/09/2026: fim de TODOS os papers do conjunto focado (41)

Leitura sistemática da seção final (conclusion/future work) de cada paper do conjunto focado, cruzando com as perguntas em aberto já documentadas (R1–R5 no `README.md`). Fontes: PDFs locais, arXiv/ePrint, MDPI/Frontiers/IEEE-Access abertos, PDFs obtidos via web/scihub. Papers que continuam bloqueados por paywall estão marcados `[PAYWALL]`.

### 1) Papers com pergunta em aberto EXPLÍCITA na seção final

| Paper (ano) | Seção final — pergunta em aberto | Cruzamento com R1–R5 |
|---|---|---|
| **ZKVault** (SSRN 2026, semente) §VII | pós-quântico (zk-STARKs); recursão Nova/Halo2 para agregar provas de credenciais; schemas W3C VC/DIF PE; pilotos com instituições reguladas | reforça R2 (revogação/credenciais) e a ideia 4 (witness KZG); recursão = base de custo |
| **BSCI'25** (ACM 2025, semente) §5 | aceleração por hardware da geração de prova; verificação on-chain já enxuta; sem comparação com STARKs pós-quânticos nem tratamento de trusted setup | base para R4 (custo de primitivas) e R5 (integração circuito-contrato) |
| **GENES** (MDPI Electronics 2025) §6 | tamanho de prova; rastrear transações armazenadas como commitments; aplicação novel em blockchain | recursão e proof size — alimenta R1/R5 |
| **SwapCT** (PoPETs 2021) | (família Zswap) — trocas multi-token privadas não-interativas | R4 (matching privado verificável) — mesmo grupo dos autores de Zswap |
| **SSI vazinação** (arXiv 2202.09207) §7 | "no single solution will be universally appropriate" — customização por uso (wallet/blockchain/agentes) | baixo; contexto alternativo ao R2 |
| **Sybil-Resistant SSI** (IEEE Access 2025) §VIII.B | generalizar de fonte única de identidades para "existência de qualquer pessoa natural"; protótipo em Ethereum 2.0; reavaliar sob composição universal (UC) | direto para R2 (autenticidade contra servidor malicioso) |
| **National ID + VWR** (ESI Preprints 2025) §7 | mensuração de linkability na telemetria de auditoria (calibrar lifetimes de tokens, rotação de pseudônimos); proporcionalidade em overrides legais (time-boxing, aprovação dupla) | fortalece R1 (evitar estados intermediários reveladores) |
| **ESJ 2026** (versão condensada do anterior) | nenhuma explícita (só síntese) | — |
| **SSI IEEE Access 2023** Σ§VII | "once implemented" — lacuna implícita de validação prática | R2/R5 |
| **Proof-of-Assets Bitcoin** (arXiv 2208.01263 / IEEE COMSNETS 2023) §VI | estender a P2PKH (prova de conhecimento do preimage de hash) e combinar com proof of liabilities via set-membership proofs | nova; vizinha de R4 (solvência verificável) |
| **AURA** (Research Square 2026) §8.6 | 4 frentes: (1) latência de geração de prova/hardware (GPU, ARM SoC); (2) descentralizar o sequencer; (3) privacidade cross-chain; (4) migração pós-quântica (BN254→lattice, híbrida) | R4 (custo) + pós-quântico |
| **EduRangeProof** (CSEDU 2026) §5 | eliminar trusted setup (RSA→curvas/lattices); agregação de provas/verificação em lote; multi-atributos com composição lógica | R5 (integração) + custo |
| **Cross-border payments ZK** (EMSJ 2025) §5 | escalar ZKPs (overhead limita throughput); interoperar cadeias heterogêneas; FHE/SMPC; governança cross-jurisdicional; pós-quântico | R4 (custo de matching/liquidação) |
| **Zident KYC** (IJASRET 2025) §VI-VII | interoperabilidade cross-chain; W3C DIDs/VCs; trust scoring com zkML; pós-quântico (zk-STARKs) | R2 direto |
| **Agentic AI/SSI** (IJCMI 2025) §conclusão | performance do registro DID e propagação eficiente de revogações em escala massiva M2M | R2 (revogação privada) |
| **FairAI** (MDPI FI 2026) §8 | governança de proofs p/ derivação verificável de métricas; fortalecer privacidade (secure aggregation/DP); avaliar multi-instituição | R4/R5 |
| **Industrial SSI/Hyperledger Identus** (TechRxiv 2025) | avaliar eficiência/desempenho com evolução dos padrões; integração com 6G, Web3, quântico | R2 |
| **PQC Confidential Clouds** (IJAIRI 2025) §5.4-6 | validação empírica em escala; automação de raciocínio sobre evidências para provas de conformidade regulatória | R5 |
| **Defi/sanctions mixers** (Politics&Security 2025) §5 | como sancionar código autônomo quando intermediários não são o alvo — portfólio em camadas (entrada/saída, infra, design de protocolo) | motiva R4/R5 em compliance verificável |
| **Invisible Author/GAI** (SSRN 2026) | compatibilidade auditabilidade × desempenho em logs de interação com IA (privacidade, robustez a ruído, grounding semântico) | R5 |
| **Voting agregado ZK** (CFS 2025) §8 | votação ponderada em eleições de larga escala (próxima direção) | baixo |
| **Voting SciRep** (2026) | (conclusão descritiva; sem futuro explícito) | baixo |
| **Informatica 49 DA-ZKP** (2025) | cross-chain + integração com homomorphic encryption | R4 |

### 2) Papers sem pergunta explicitada na seção final

| Paper (ano) | Última frase relevante / observação |
|---|---|
| **SSI Canada** (Frontiers 2021) §conclusão | desafios de adoção e ausência de restrições regulatórias |
| **SSI eIDAS/GDPR** (IEEE Access 2023) | "once implemented..." (validação prática pendente) |
| **ETH ZK-PPIdM** (IEEE Access 2023) | conclui demonstrando eficiência; sem future work |
| **Multi-chain hash calendar** (IEEE CCSB 2022) | simulação mostra expansão de storage; sem pergunta futura explícita |
| **ZeroMedChain** (IndiaCom 2024) | melhora 34% tempo vs PoW; sem future work |
| **KYC IEEE ICSEDIS 2026 (PRISM)** | `[PAYWALL]` — sem conclusão acessível |
| **Digital ID OCIT 2023** | `[PAYWALL]` — sem conclusão acessível |
| **zkSSI (IEEE Blockchain 2024)** | `[PAYWALL]` — recursão/composição de provas citadas no abstract |
| **ZKP W3C mobile auth (ACM 2026)** | `[PAYWALL]` — Schnorr/sigma-protocol, <10ms assinatura, <15ms verificação |
| **ZK Interop Payments (ACM TWEB 2026)** | `[PAYWALL]` — KYC + SSI + cross-chain interoperable payments |
| **Korea DID/universidade** | `[PAYWALL]` — KoreaScience/earticle inalcançáveis |
| **Enhancing Digital KYC (ICDLT 2025)** | `[PAYWALL]` — mesmo autor do zkSSI |
| **QKD+ZKP** (OptCom 2025); **ICV+ZKP** (SPIE 2025); **PQ-ZKP info quântica** (Springer 2022); **BHDA smart grid** (2021); **credential model** (CRC 2022); **HW/SW Halo FPGA** (Springer 2021); **L2 aggregation** (ICBDS 2025); **ZK voting CAIBDA** (2025); **quantum NIZK** (Springer 2024); **RBH healthcare** (Cluster 2026) | `[PAYWALL]` ou fora de escopo aplicado — fins não verificados |

### 3) Síntese — onde o conjunto cruza com as ideias já existentes

- **R2 (revogação privada + autenticidade):** campeão de convergência — Sybil-resistant SSI (UC), ZKVault (schemas W3C), Zident (DID/VC), Agentic AI (revogação M2M), Industrial SSI (Identus), zkSSI/ICDLT (mesmo autor).
- **R4 (custo de privacidade verificável):** Zswap/SwapCT (matching), Proof-of-Assets (solvência), AURA (latência/GPUs), cross-border ZK (throughput), Informatica (5ms/tx), EduRangeProof (agregação).
- **R1/R5 (composição de provas e integração circuito-contrato):** GENES (recursão), BSCI (hardware), PQC Confidential Clouds (audit trail), Invisible Author (auditabilidade), FairAI.
- **Pós-quântico: direção transversal em ~8 papers do conjunto** (ZKVault, AURA, cross-border, Zident, QKD, PQ-ZKP, quantum-NIZK, SSI IEEE Access) — nenhum dos R1–R5 o trata como eixo principal, apenas nota de leitura (R2 §70).

> Acesso institucional IEEE/ACM/Springer destravaria a leitura dos fins dos ~15 papers paywalled restantes.
