=== IDEIAS DE PROJETO — JEROEN VAN DE GRAAF ===
Arthur Abeilice | Julho 2026

Baseado em:
- Minha stack: Solidity, Go, Rust, Vue/Svelte, Tauri, Foundry, blockchain
- Pesquisa do Jeroen: e-voting, everlasting privacy, MPC/OT, DC-nets,
  RNG físico, SNARKs, criptografia teórica, blockchain

====================================================================
IDEIA 1 — Votação on-chain com privacidade eterna
====================================================================
O que é: Sistema de votação blockchain onde os votos são
publicamente verificáveis MAS a privacidade é incondicional (não
quebrável nem por quantum computer no futuro).
Como: Usar commitment schemes unconditionally hiding (como o
trabalho do Jeroen com Prêt-à-Voter + PunchScan) + blockchain como
public bulletin board.
Stack: Solidity + Foundry (smart contracts), Go/Vue (frontend),
conceitos de everlasting privacy.
Conexão com Jeroen: É o tema central da carreira dele. Ele tem
paper "Voting with Unconditional Privacy by Merging Prêt-à-Voter
and PunchScan" (2009, IEEE TIFS). A blockchain resolveria o
problema de public bulletin board de forma descentralizada.
Nível: Mais aplicado (código pesado) + teórico (criptografia).

====================================================================
IDEIA 2 — Implementação prática de MPC / OT em Go ou Rust
====================================================================
O que é: Implementar protocolos de Oblivious Transfer (OT) ou
Multi-Party Computation (MPC) do zero em Go ou Rust, com foco em
eficiência e usabilidade.
Exemplo: "Shared OT and Its Applications" (2024/2025) — implementar
OT compartilhado e aplicações como comparação de inteiros,
igualdade, bit-decomposition.
Stack: Go (minha stack principal) ou Rust + Tauri (app desktop)
ou CLI tool. Poderia virar lib open-source.
Conexão com Jeroen: Paper recente (2024-2025) "Shared OT". Ele tem
histórico em OT desde 1995 (CRYPTO). Projeto prático de
implementação criptográfica.
Nível: Médio — mais aplicado (implementar protocolo) mas exige
entender a teoria.

====================================================================
IDEIA 3 — DC-net (Dining Cryptographer Network) prática
====================================================================
O que é: Implementar uma rede de comunicação anônima baseada no
protocolo Dining Cryptographers, onde nenhum observador consegue
saber quem enviou qual mensagem.
Exemplo: Um app de chat anônimo ou sistema de broadcast anônimo.
Jeroen tem vários papers: "Beating the Birthday Paradox in Dining
Cryptographer Networks" (2014), "Anonymous One-Time Broadcast
Using Non-interactive Dining Cryptographer Nets" (2010).
Stack: Go (backend), Tauri + Rust (desktop), ou CLI.
Poderia incluir key distribution (One-Time Pad).
Conexão com Jeroen: Ele pesquisa DC-nets há anos. É um tema
"clássico" dele. Implementar NIDC (Non-Interactive DC) seria
um projeto bem interessante.
Nível: Médio — implementação prática com base teórica.

====================================================================
IDEIA 4 — Oracle de Aleatoriedade Verificável (Verifiable RNG)
====================================================================
O que é: Sistema que conecta um gerador físico de números
aleatórios (PhRNG) com a blockchain, permitindo que contratos
inteligentes usem aleatoriedade verdadeira (física) e verificável.
Ele tem um projeto de PhRNG baseado em diodo laser (2012-atual).
Stack: Solidity + Foundry (contratos), Go (oracle), hardware (RNG).
Conexão com Jeroen: Ele coordena projeto de PhRNG desde 2012.
Vc já tem experiência com Chainlink VRF (bicheiros2). Seria uma
evolução: RNG físico + blockchain.
Nível: Aplicado, multidisciplinar (hardware + software).

====================================================================
IDEIA 5 — ZK-proofs aplicado a votação ou identidade
====================================================================
O que é: Implementar um sistema usando SNARKs/STARKs para votação
privada ou identidade autossoberana. Jeroen ensinou SNARKs em
2023 e 2024.
Exemplo: Provas de elegibilidade sem revelar identidade. Ou um
sistema de "voto secreto verificável" usando zk-SNARKs.
Stack: Circom/Noir + Solidity (verificador on-chain) +
Vue/Svelte (frontend). Ou algo em Rust com arkworks.
Conexão com Jeroen: Ele ensina SNARKs. Projeto prático de ZK
aplicado a um domínio que ele domina (votação).
Nível: Desafiador — exige aprender ferramentas ZK + criptografia.

====================================================================
IDEIA 6 — Everlasting Privacy + Blockchain (híbrido)
====================================================================
O que é: Protocolo onde a blockchain provê verificação pública
mas a privacidade não depende de segurança computacional (quebra
com quantum). Usar commitment schemes que escondem informação
incondicionalmente + blockchain como âncora de integridade.
Stack: Solidity + Foundry + teoria de commitments unconditionally
hiding. Inspirado nos papers do Jeroen sobre everlasting privacy.
Conexão com Jeroen: É a interseção perfeita entre o tema central
dele (everlasting privacy) e sua stack (blockchain).
Nível: Teórico + implementação.

====================================================================
IDEIA 7 — Formal verification de protocolos criptográficos
====================================================================
O que é: Usar ferramentas de métodos formais (tipo EasyCrypt ou
ProVerif) para verificar propriedades de privacidade em protocolos
existentes ou novos. Mais teórico/matemático.
Stack: Ferramentas de verificação formal (EasyCrypt, ProVerif, etc).
Pouco código, muita lógica.
Conexão com Jeroen: O laboratório dele (InSCryP) trabalha com
métodos formais e quantificação de privacidade.
Nível: Teórico — mais perto de matemática que de código.

====================================================================
IDEIA 8 — Ferramenta de análise de privacidade em smart contracts
====================================================================
O que é: Ferramenta que analisa smart contracts em busca de
vazamento de informação. Mede quantos bits de informação são
revelados sobre as entradas privadas.
Stack: Rust (análise estática) + conceitos de information leakage.
Conexão com Jeroen: O lab dele pesquisa "quantificação de
vazamento de informação". Aplicar isso a smart contracts.
Nível: Médio-desafiador.

====================================================================
IDEIA 9 — App de autenticação por som ambiente (pesquisa ativa)
====================================================================
O que é: Dois smartphones gravam 5s de som ambiente e se autenticam
pela similaridade. Jeroen tem projeto ativo nisso no InSCryP.
Stack: Python/Rust (processamento áudio), mobile (Swift ou Kotlin),
ou Tauri desktop. Ou Go + processamento de sinal.
Conexão com Jeroen: É um projeto atual do laboratório dele.
Nível: Médio — processamento de sinal + app.

====================================================================
IDEIA 10 — Estudo + implementação de um paper dele
====================================================================
O que é: Pegar um paper específico do Jeroen, estudar a fundo, e
implementar uma demonstração funcional do protocolo descrito.
Opções:
- "Delphi: sharing assessments of cryptographic assumptions" (2024)
- "Shared OT and Its Applications" (2024-2025)
- "Unconditionally Secure, Universally Composable Privacy
   Preserving Linear Algebra" (2016)
Stack: Go, Rust, ou Python (depende do paper).
Conexão com Jeroen: Direta — vc implementa o paper dele.
Nível: Médio (implementar paper existente).

====================================================================
MEU PALPITE — O QUE EU FARIA
====================================================================
Se eu fosse você, consideraria forte a IDEIA 1 (votação on-chain
com everlasting privacy) ou a IDEIA 6 (everlasting privacy +
blockchain híbrido). Motivos:
1. É o tema central da carreira do Jeroen — ele vai ter muito a
   contribuir e se interessar.
2. Vc já tem domínio de Solidity/blockchain (bicheiros2, VRL, doiim).
3. É um projeto que une teoria (everlasting privacy) com prática
   (código em Solidity + frontend).
4. Tema quente: privacidade em blockchain é cada vez mais relevante.

A IDEIA 3 (DC-net) também é forte — Jeroen tem vários papers,
é um tema menos explorado que votação, e vc poderia fazer algo
único.

A IDEIA 10 (implementar paper) é a mais segura academicamente —
vc mostra que consegue ler, entender e implementar pesquisa.

====================================================================
IDEIA 11 — Entangled Rollup / Cross-chain sem bridge
====================================================================
O que é: Implementar um protótipo do conceito de Entangled Rollup
que o Jeroen inventou na ZKM — uma L2 compartilhada por duas L1s
que permite transferência trustless de ativos sem bridge.
Jeroen escreveu a série "Cross-chain Asset Transfer Without a Bridge"
(2024) e o litepaper do Entangled Rollup (2024). Ele é Senior
Cryptographer na ZKM.
Stack: Solidity + Foundry (contracts L1), zkVM / zkMIPS (provas),
Go ou TypeScript (sequencer/relayer). Vc já tem experiência com
Arbitrum Orbit no projeto doiim/rollup/.
Conexão com Jeroen: Direta — é A pesquisa atual dele na ZKM.
Ele tem artigos, litepaper, e palestras sobre o tema.
Nível: Pesado — exige entender ZK, rollup mechanics, bridge security.
Mas vc já tem metade do caminho com a exp em Orbit.

====================================================================
IDEIA 12 — ZK-Private VRL (stablecoin privado)
====================================================================
O que é: Adicionar privacidade ZK ao seu protocolo VRL.FINANCE.
Transações do stablecoin DBRL seriam criptografadas, com provas ZK
de validade (saldo suficiente, não-double-spend) sem revelar
valores ou contrapartes. Similar ao Zcash mas para real brasileiro.
Stack: VRL existente (Solidity, Foundry) + Circom/Noir (circuits) +
verificador on-chain. Frontend SvelteKit com provedor ZK.
Conexão com Jeroen: Verifiable computation + ZK, que ele pesquisa
e ensina. Além disso, Jeroen é consultor na ZKM que constrói zkVM.
Nível: Médio-alto — vc já tem o protocolo VRL pronto, é adicionar
a camada ZK. Mais focado em ferramentas ZK atuais (Noir/Circom).

====================================================================
IDEIA 13 — ZK-KYC / Prova de elegibilidade para fintech
====================================================================
O que é: Sistema onde o usuário prova que é elegível (maior de
idade, não-sancionado, etc.) sem revelar dados pessoais.
Aplicação direta na BRAZA (tokenização, crowdloaning CVM 88).
Um issuer verifica os docs uma vez, emite um "attestation" ZK,
e o usuário reusa pra provar elegibilidade em múltiplos protocols.
Stack: Noir (circuitos ZK) + Solidity (verificador) + TypeScript
(off-chain prover). Integração com a stack BRAZA.
Conexão com Jeroen: Ele trabalha com privacy-preserving tech,
e é pesquisador na área de identidade. Tema prático e atual.
Nível: Médio — ZK aplicado de forma pragmática. Muita demanda real.

====================================================================
IDEIA 14 — Proof of Reserves ZK para exchange
====================================================================
O que é: Exchange (ou stablecoin VRL) prova que tem lastro sem
revelar posições individuais. Usa ZK pra mostrar que "soma dos
passivos ≤ soma dos ativos" com privacidade.
Stack: Go (backend), Rust ou Noir (circuits), Solidity (se for
on-chain), ou app web standalone.
Conexão com Jeroen: Verifiable computation clássico — exatamente
o que ele descreve na talk "algebra of polynomials over finite
fields causing a gold rush in blockchain".
Nível: Médio — proof of reserves já é um padrão conhecido, aplicar
ZK é uma evolução natural.

====================================================================
IDEIA 15 — Leilão selado / DEX privada com ZK
====================================================================
O que é: DEX (DEX privada estilo leilão de Vickrey) onde as ordens
são submetidas criptografadas e apenas o resultado final é revelado.
Usa ZK pra provar que o leilão foi executado corretamente.
Stack: Solidity + Foundry + Noir/Circom + frontend Vue/Svelte.
Conexão com Jeroen: Aplicação de MPC + ZK em DeFi. Ele tem paper
sobre "Unconditionally Secure, Universally Composable Privacy
Preserving Linear Algebra" (2016) que é exatamente a matemática
por trás de leilões privados.
Nível: Médio-alto — combina DeFi + criptografia.

====================================================================
IDEIA 16 — Especificação formal de rollup (segurança)
====================================================================
O que é: Analisar formalmente as propriedades de segurança de um
rollup existente (Arbitrum, Optimism, ZKsync) usando métodos
formais. Identificar pressupostos de confiança, gaps de segurança,
ou propor melhorias. Mais análise que implementação.
Stack: ProVerif, EasyCrypt, ou até papel e caneta. Conhecimento de
rollup architecture (que vc já tem pelo projeto Orbit).
Conexão com Jeroen: O InSCryP trabalha com métodos formais e
quantificação de segurança. Jeroen escreveu o artigo "Reflections
on Terminology for Rollups". Ele adora discussão conceitual.
Nível: Mais teórico — adequado se vc quiser algo menos de código.

====================================================================
IDEIA 17 — zkOracle: bridge + oracle descentralizado via ZK
====================================================================
O que é: Oracle que prova ZK sobre dados off-chain. Combina o
conceito de Entangled Rollup (Jeroen) com Chainlink (sua exp).
Exemplo: provar que um evento ocorreu em outra chain usando ZK,
sem confiar em validadores. Útil pra fintech multi-chain.
Stack: Solidity + Foundry + Go (relayer) + zkVM.
Conexão com Jeroen: Entangled Rollup + verifiable computation.
Vc já usou Chainlink VRF, entende o problema de confiança em oracle.
Nível: Médio-alto — próxima geração de oracles.

====================================================================
IDEIA 18 — zk- aplicado a pagamentos P2P (P2Pix + ZK)
====================================================================
O que é: Adicionar privacidade ZK ao P2Pix (projeto do doiim).
Pagamentos P2P na blockchain são públicos por padrão. Com ZK,
vc prova que "pagou o valor correto pra pessoa certa" sem revelar
o valor ou pra quem. Transações tipo cash digital.
Stack: Solidity + Foundry + Noir/Circom + Vue 3 (frontend).
Vc já conhece o código do P2Pix.
Conexão com Jeroen: Privacy-preserving fintech. Ele pesquisa
privacy + blockchain. É um fork natural do P2Pix.
Nível: Médio — vc já tem o P2Pix rodando, é adicionar ZK.

====================================================================
RESUMO — NOVAS IDEIAS (ROLLUP + ZK + FINTECH)
====================================================================
ID  | Projeto                        | Stack principal        | Nível
----|--------------------------------|------------------------|-------
11  | Entangled Rollup protótipo     | Solidity, Go, zkVM     | Pesado
12  | ZK-Private VRL                 | Solidity, Noir, VRL    | Médio+
13  | ZK-KYC para fintech            | Noir, Solidity, TS     | Médio
14  | Proof of Reserves ZK           | Go, Rust, Noir         | Médio
15  | Leilão selado / DEX privada    | Solidity, Foundry, Noir| Médio+
16  | Especificação formal rollup    | ProVerif, papel        | Teórico
17  | zkOracle                       | Solidity, Go, zkVM     | Médio+
18  | P2Pix + ZK (pagamentos)        | Solidity, Noir, Vue    | Médio

JEROEN NA ZKM (contexto importante):
- Senior Cryptographer na ZKM (desde 2022)
- Criador do conceito de Entangled Rollup
- Escreveu "Cross-chain Asset Transfer Without a Bridge" (série 2024)
- Pesquisa: zkRollup, zkMIPS, verifiable computation
- Palestra: "Why the algebra of polynomials over finite fields
  is causing a gold rush in the blockchain world"
- Professor de SNARKs na UFMG (2023, 2024)

MEU PALPITE ATUALIZADO:
A IDEIA 11 (Entangled Rollup) é a mais alinhada com a pesquisa
ATUAL dele — é o que ele vive fazendo na ZKM. Vc já tem exp em
Orbit. Seria um projeto de peso.

A IDEIA 12 (ZK-Private VRL) é forte se vc quiser algo mais
"seu" — melhorar seu próprio protocolo com a pesquisa dele.

A IDEIA 18 (P2Pix + ZK) é a mais prática — vc já tem o código,
Jeroen gosta de privacy, e é um projeto concreto.

====================================================================
