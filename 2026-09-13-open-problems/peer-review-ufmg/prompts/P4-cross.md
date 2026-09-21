You are P4, specialty: Security & Cryptography. Motto: "Flexibility > structure". Style: Interrogative/Socratic.

Below are 5 anonymized rewrites of the same original artifact, produced by
your peers. You did NOT write any of these — review them honestly.

ORIGINAL ARTIFACT (for reference):
<<<
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Ideias de pesquisa com papers e experimentos: Zswap com KZG, agregação de provas, empréstimos privados, acumuladores, revogação e carteiras.">
  <title>Ideias de pesquisa — ZK, swaps e empréstimos</title>
  <style>
    body { max-width: 76ch; margin: 0 auto; padding: 1rem; font-family: system-ui, sans-serif; line-height: 1.6; overflow-wrap: break-word; }
    h1, h2, h3 { line-height: 1.25; }
    section { margin-block: 3rem; }
    li { margin-block: .75rem; }
    summary { cursor: pointer; }
    footer { margin-top: 3rem; border-top: 1px solid; }
  </style>
</head>
<body>
  <header id="inicio">
    <h1>Ideias de pesquisa em ZK e Web3</h1>
    <p>ZK, criptografia e Web3 · Seleção atualizada em <time datetime="2026-09-14">14 de setembro de 2026</time></p>
    <p>Três novas candidatas sobre swaps e empréstimos privados, seguidas das propostas anteriores sobre KZG, revogação e carteiras. Cada ideia parte de um paper e muda uma peça específica.</p>
    <nav aria-label="Propostas atuais">
      <ul>
        <li><a href="#swap-kzg">Ideia 1 — Zswap: trocar Merkle por pertencimento privado com KZG</a></li>
        <li><a href="#swap-aggregation">Ideia 2 — Zswap: agregar as provas com SnarkPack</a></li>
        <li><a href="#loan-interval">Ideia 3 — Empréstimo: reutilizar a prova de garantia numa faixa de preços</a></li>
        <li><a href="#kzg">Ideia 4 — KZG: atualizar uma prova sem revelar o depósito</a></li>
        <li><a href="#revogacao">Ideia 5 — Revogação privada de credenciais</a></li>
        <li><a href="#carteira">Ideia 6 — Recuperar pagamentos depois de ficar offline</a></li>
      </ul>
    </nav>
    <p><strong>Por onde começar:</strong> <a href="#swap-aggregation">ideia 2</a> para combinar técnicas existentes; <a href="#loan-interval">ideia 3</a> para um primeiro circuito menor; <a href="#swap-kzg">ideia 1</a> se a preferência for trocar Merkle por KZG. A ideia 1 exige mais trabalho criptográfico. São candidatas à investigação, com novidade e vantagens ainda por demonstrar.</p>
  </header>
  <main>
    <section id="swap-kzg" aria-labelledby="titulo-swap-kzg">
      <h2 id="titulo-swap-kzg">Ideia 1 — Zswap: trocar Merkle por pertencimento privado com KZG</h2>
      <p>Num swap privado, você precisa provar que possui uma nota válida sem mostrar qual nota é sua. No paper Zswap, a prova de gasto inclui um caminho de Merkle.</p>
      <p><strong>A troca:</strong> pertencimento via Merkle → lookup privado baseado em KZG, como Caulk+.</p>
      <p><strong>Pergunta:</strong> em quais tamanhos de conjunto essa troca reduz o custo total de produzir uma prova de gasto, contando a manutenção dos dados auxiliares?</p>
      <h3>Papers para ler</h3>
      <ul>
        <li><a href="https://petsymposium.org/popets/2022/popets-2022-0120.pdf">Zswap: zk-SNARK Based Non-Interactive Multi-Asset Swaps</a> — PoPETs 2022. Ler a construção da prova de gasto, na <a href="papers/zswap-2022.pdf#page=13">página 13 do PDF local</a>, e a implementação, na página 15. <a href="https://github.com/felix-engelmann/zswap-code">Código do Zswap</a>.</li>
        <li><a href="https://eprint.iacr.org/2022/957">Caulk+: Table-independent lookup arguments</a> — 2022. Fornece a peça de pertencimento privado. <a href="accumulators/papers/caulk-plus-2022.pdf">PDF local de Caulk+</a> · <a href="https://github.com/geometryxyz/semacaulk">Implementação relacionada: Semacaulk</a>.</li>
      </ul>
      <p><strong>O que já existe:</strong> Semacaulk já aplica KZG a pertencimento privado. A contribuição candidata seria a composição com a prova de gasto e a avaliação no Zswap. A troca genérica Merkle → KZG, sozinha, não sustenta novidade.</p>
      <details>
        <summary>Experimento, dificuldade e diferença para a proposta anterior de KZG</summary>
        <p>Começar com dois ativos, quantidades limitadas e conjuntos de 2<sup>10</sup>, 2<sup>14</sup> e 2<sup>18</sup> notas, aumentando apenas se a memória permitir. Comparar a implementação Merkle original e a composição candidata sob a mesma segurança e o mesmo fluxo de gastos.</p>
        <p>Medir geração e verificação da prova completa, tamanho, memória, pré-processamento e atualização dos witnesses. Um witness menor não implica uma prova final mais barata: Merkle já fica escondido dentro do SNARK original.</p>
        <p>A prova de pertencimento precisa estar vinculada à mesma nota usada na autorização, no valor, no tipo de ativo e no nullifier, que impede gasto duplo. Uma abertura KZG pública revela a posição; duas provas independentes podem provar fatos sobre notas diferentes.</p>
        <p><strong>Dificuldade: média a alta.</strong> A composição entre Caulk+ e o circuito de gasto é o ponto central. Verificar pairings dentro do circuito pode eliminar a vantagem. É necessário preservar as propriedades de segurança exigidas pelo Zswap, incluindo extração sob simulação.</p>
        <p>A <a href="#kzg">proposta anterior de KZG</a> pergunta como atualizar witnesses com ajuda privada de um servidor. Esta pergunta como substituir e compor a prova de pertencimento no gasto de um swap. São experimentos distintos.</p>
      </details>
    </section>

    <section id="swap-aggregation" aria-labelledby="titulo-swap-aggregation">
      <h2 id="titulo-swap-aggregation">Ideia 2 — Zswap: agregar as provas com SnarkPack</h2>
      <p>O Zswap junta transações, mas mantém provas para cada entrada e saída. Um lote maior carrega mais provas para verificar.</p>
      <p><strong>A combinação:</strong> provas Groth16 do Zswap + agregação SnarkPack, feita depois que o lote estiver formado.</p>
      <p><strong>Pergunta:</strong> a partir de quantas provas a agregação compensa seu custo, comparada também à verificação em lote sem compressão?</p>
      <h3>Papers para ler</h3>
      <ul>
        <li><a href="papers/zswap-2022.pdf#page=13">Zswap — construção e junção de transações (PDF local)</a>. O <a href="https://github.com/felix-engelmann/zswap-code">repositório dos autores</a> já mede provas de gasto, provas de saída e junção de transações.</li>
        <li><a href="https://research.protocol.ai/publications/snarkpack-practical-snark-aggregation/">SnarkPack: Practical SNARK Aggregation</a> — Financial Cryptography 2022; preprint de 2021. Agrega provas Groth16. <a href="defi/papers/snarkpack-2021.pdf">PDF local de SnarkPack (29 páginas)</a> · <a href="https://github.com/filecoin-project/bellperson">Código em Bellperson</a>.</li>
      </ul>
      <p><strong>Primeiro experimento:</strong> comparar verificação individual, verificação em lote e SnarkPack com 4, 16, 64 e 256 provas. Medir tempo do agregador, tempo de verificação, bytes totais e espera para formar o lote.</p>
      <details>
        <summary>O que precisa funcionar para virar uma pesquisa</summary>
        <p>As provas agregadas pelo esquema precisam compartilhar a chave de verificação. Separar provas de gasto e de saída quando usarem chaves diferentes. Os participantes continuam gerando suas próprias provas; o agregador recebe as provas e os dados públicos.</p>
        <p>Preservar a associação entre provas e entradas públicas, a ordenação canônica, o balanço por ativo e a rejeição de nullifiers repetidos. O tamanho reduzido do agregado não elimina o custo de processar os dados públicos do lote.</p>
        <p>Guardar as provas originais até finalizar o lote. Não presumir que dois agregados possam ser combinados diretamente. Conferir a compatibilidade de curvas, formatos e parâmetros: Zswap usa Arkworks; Bellperson trabalha com BLS12-381. Os parâmetros adicionais de SnarkPack usam dois transcripts Powers of Tau.</p>
        <p><strong>Dificuldade: média, com integração a verificar.</strong> Começar medindo em Rust. Só declarar economia de gas depois de implementar e medir um verificador na rede escolhida.</p>
        <p><strong>Risco de novidade: alto.</strong> Agregar Groth16 já é conhecido. A pesquisa precisa explicar uma política de formação de lotes, uma composição justificada ou uma relação entre custo e latência que ainda não esteja estabelecida para esse protocolo. Uma chamada de biblioteca e um gráfico isolado seriam insuficientes.</p>
      </details>
    </section>

    <section id="loan-interval" aria-labelledby="titulo-loan-interval">
      <h2 id="titulo-loan-interval">Ideia 3 — Empréstimo: reutilizar a prova de garantia numa faixa de preços</h2>
      <p>Você prova que a garantia cobre a dívida sem revelar as quantidades. Se o preço público entrar como um valor exato no circuito, uma nova cotação pode exigir uma nova prova.</p>
      <p><strong>A mudança:</strong> prova para um preço exato → certificado válido para uma faixa pública de preços e um prazo curto, usando um SNARK convencional.</p>
      <p><strong>Exemplo:</strong> provar que a garantia cobre a dívida mesmo se o preço cair até R$ 90. O contrato pode reutilizar o certificado enquanto a cotação permanecer na faixa combinada, o prazo não vencer e a posição continuar no mesmo estado.</p>
      <h3>Paper para ler</h3>
      <p><a href="https://eprint.iacr.org/2025/1802">Zyga: Optimized Zero-Knowledge Proofs with Dynamic Public Inputs</a> — preprint de 2025, revisão de 22/12/2025. Ler <a href="defi/papers/zyga-2025.pdf#page=24">a seção 8.2 sobre empréstimos, na página 24</a>. <a href="defi/papers/zyga-2025.pdf">PDF completo de Zyga (31 páginas)</a>.</p>
      <p><strong>O que já existe:</strong> Zyga já propõe reutilização de provas com entradas públicas dinâmicas e cita empréstimos. O recorte aqui é investigar uma alternativa mais restrita com circuitos convencionais: quanto de reutilização se obtém ao certificar uma faixa conservadora, e quanta informação essa faixa revela?</p>
      <p><strong>Primeiro experimento:</strong> uma garantia, uma dívida e um limite de juros conhecido até o vencimento do certificado. Comparar uma nova prova por cotação com certificados de diferentes amplitudes. Medir provas evitadas, custo total e rejeições de posições que ainda seriam saudáveis no preço exato.</p>
      <details>
        <summary>O circuito, a privacidade e o limite do recorte</summary>
        <p>Com valores inteiros escalados, provar que <code>garantia × preço_mínimo ≥ razão_de_garantia × dívida_máxima_no_prazo</code>. Definir limites numéricos, arredondamento conservador e ausência de overflow. Provar também o vínculo com garantia efetivamente bloqueada e com o estado autorizado da posição.</p>
        <p>O contrato verifica cotação recente, faixa, prazo, política de juros e versão da posição. Alterar garantia ou dívida invalida o certificado. Isso é reutilizar uma checagem de saúde; o certificado não autoriza repetir um desembolso de empréstimo.</p>
        <p>Uma faixa escolhida individualmente pode revelar limites sobre a razão garantia/dívida. Comparar faixas comuns a todos com faixas personalizadas, incluindo o que sucessivas renovações revelam. Neste primeiro modelo, a posição é pública como um pseudônimo e os valores são privados; reutilizar o certificado permite correlacionar suas verificações.</p>
        <p><strong>Dificuldade: baixa a média para o protótipo; média para a análise.</strong> O desafio é caracterizar segurança, informação revelada e custo, além de procurar técnicas equivalentes na literatura. A ideia de certificado por faixa é uma hipótese desta busca, não um open problem declarado por Zyga.</p>
        <p>O escopo é a verificação privada da suficiência de garantia. Liquidar automaticamente uma posição privada exige mecanismos adicionais. Zyga entra como trabalho relacionado; seus números não serão usados como comparação direta sem reproduzir o artefato.</p>
      </details>
      <details>
        <summary>Mais leituras sobre empréstimos</summary>
        <p><a href="https://scholarworks.boisestate.edu/cs_facpubs/265/">ZeroLender: Trustless Peer-to-Peer Bitcoin Lending Platform</a> — CODASPY 2020. Usa ZK para desvincular credores e tomadores. Nesta busca foi consultado o resumo institucional; não há PDF local nem análise da construção.</p>
        <p><a href="https://scholarworks.sjsu.edu/faculty_rsca/5019/">Autonomous Lending Organization on Ethereum with Credit Scoring (ALOE)</a> — SVCC 2023. É uma base para estudar crédito, identidade e atualização de score; seu modelo associa contas a identidades por um notário e auditores. <a href="defi/papers/aloe-2023.pdf">PDF dos autores (8 páginas)</a> · <a href="https://github.com/taustin/cryptoCreditBureau/">Código do ALOE</a>.</p>
        <p>Provar apenas que um score supera um limite é um começo de implementação. Para virar proposta de pesquisa, ainda faltaria uma pergunta específica sobre atualização, omissão de dívidas ou privacidade.</p>
      </details>
      <p><a href="defi/README.md">Notas técnicas das três novas propostas</a> · <a href="defi/sources.json">Fontes, versões e limites da busca</a></p>
    </section>

    <section id="kzg" aria-labelledby="titulo-kzg">
      <h2 id="titulo-kzg">Ideia 4 — KZG: atualizar uma prova sem revelar o depósito</h2>
      <p>Você deposita num pool, fica offline e volta depois de milhares de novos depósitos. Quer atualizar o dado auxiliar da sua prova de saque, chamado <em>witness</em>, sem revelar ao servidor qual depósito é seu.</p>
      <p><strong>O que adaptar:</strong> técnicas de atualização privada de provas em acumuladores RSA/bilineares para um vector commitment KZG, com aplicação a um pool baseado em Caulk+/Semacaulk.</p>
      <p><strong>Pergunta:</strong> essa adaptação pode reduzir o trabalho da carteira sem revelar a posição consultada, mantendo a comunicação e o custo do servidor aceitáveis?</p>
      <p><strong>O que já existe:</strong> Tornado Cash usa Merkle; Semacaulk já faz a troca Merkle → KZG com pertencimento privado. O recorte proposto é a atualização privada do witness no compromisso vetorial. Uma abertura comum de KZG não esconde a posição do depósito.</p>
      <h3>Papers para ler</h3>
      <ul>
        <li>
          <a href="https://eprint.iacr.org/2026/832">Private Delegation of (Non-)Membership Proof Updates in Cryptographic Accumulators</a> — ePrint 2026/832.
          <p>Apresenta atualização privada de provas para RSA e acumuladores bilineares. Na página 30, os autores apontam vector commitments e polynomial commitments como direções para extensão.</p>
          <p><a href="accumulators/papers/private-delegation-2026.pdf#page=30">Abrir os trabalhos futuros (página 30)</a> · <a href="accumulators/papers/private-delegation-2026.pdf">Ler o paper completo (46 páginas)</a> · <a href="https://github.com/GlaszBoti/private-accumulator-proof-delegation">Código de delegação privada</a></p>
        </li>
        <li>
          <a href="https://eprint.iacr.org/2022/957">Caulk+: Table-independent lookup arguments</a> — ePrint 2022/957.
          <p>Prova pertencimento a uma tabela comprometida mantendo as posições ocultas. É uma das peças usadas no Semacaulk.</p>
          <p><a href="accumulators/papers/caulk-plus-2022.pdf">Ler Caulk+ (PDF, 11 páginas)</a> · <a href="https://github.com/geometryxyz/semacaulk">Código do Semacaulk</a></p>
        </li>
        <li>
          <a href="https://eprint.iacr.org/2023/1830">Vector Commitments with Efficient Updates</a> — cópia ePrint do trabalho da AFT 2023.
          <p>Explica a relação entre dados de atualização e trabalho do cliente. A seção 3.1 mostra como atualizar compromissos e aberturas KZG.</p>
          <p><a href="accumulators/papers/vector-updates-2023.pdf#page=11">Abrir a seção sobre atualização KZG (página 11)</a> · <a href="accumulators/papers/vector-updates-2023.pdf">Ler o paper completo (46 páginas)</a></p>
        </li>
      </ul>
      <p><a href="https://kohweijie.com/articles/23/semacaulk.html">A apresentação de Semacaulk pelos autores</a> é uma leitura inicial mais curta para entender a troca Merkle → KZG.</p>
      <details>
        <summary>Experimento, dificuldade e cuidados da proposta KZG</summary>
        <p>Começar com um vetor de capacidade fixa, uma nota por cliente e apenas inserções. Comparar a atualização local com a delegação candidata e com recuperação privada de witnesses pré-computados por PIR.</p>
        <p>Medir tempo e memória da carteira, bytes transferidos, processamento e armazenamento do servidor. O resultado precisa ser verificado contra o compromisso público aceito e funcionar numa prova real de pertencimento.</p>
        <p>O paper já cobre acumuladores bilineares baseados em polinômios. Um compromisso vetorial KZG representa os dados de outra forma; a adaptação para os witnesses usados pelo lookup precisa ser construída e justificada.</p>
        <p><strong>Escopo pequeno, com dificuldade criptográfica:</strong> a primeira etapa é reproduzir a atualização local. Delegação com posição oculta exige justificar correção, privacidade e rejeição de respostas falsas. Não há garantia de que a composição seja inédita ou mais eficiente.</p>
      </details>
      <p><a href="accumulators/">Ler a proposta KZG detalhada e os outros recortes com acumuladores</a></p>
    </section>

    <section id="revogacao" aria-labelledby="titulo-revogacao">
      <h2 id="titulo-revogacao">Ideia 5 — Revogação privada de credenciais</h2>
      <p>Provar que uma credencial continua válida sem revelar qual é ela, mesmo quando um servidor tenta fornecer uma resposta falsa.</p>
      <p><strong>O que combinar:</strong> consulta privada de revogação + recuperação autenticada + prova ZK vinculada à versão aceita da base de dados.</p>
      <p><strong>Pergunta:</strong> quanto custa impedir a aceitação de um registro falso ou antigo, preservando a privacidade da consulta?</p>
      <h3>Papers para ler</h3>
      <ul>
        <li>
          <a href="https://www.usenix.org/conference/usenixsecurity26/presentation/edalatnejad">Do You Need a Receipt? Anonymous Credential Revocation at Continental Scale via Private Record Certification</a> — USENIX Security 2026.
          <p>Combina consulta privada e computação entre servidores para certificar um registro. O modelo não impede a falsificação de certificados por autoridades de revogação ativamente maliciosas.</p>
          <p><a href="papers/prc-revocation-2026.pdf">Ler Do You Need a Receipt? (PDF, 21 páginas)</a> · <a href="https://zenodo.org/records/20433788">Artefato do PRC</a></p>
          <p>Começar pelo resumo e pela seção 4.1, na <a href="papers/prc-revocation-2026.pdf#page=8">página 8 do PDF de PRC</a>. A seção 5.3 explica por que assinaturas distribuídas, sozinhas, não resolvem a limitação.</p>
        </li>
        <li>
          <a href="https://eprint.iacr.org/2025/2177">TAPIR: A Two-Server Authenticated PIR Scheme with Preprocessing</a> — ACNS 2026; preprint de 2025.
          <p>Permite consultar dados privadamente e verificar a autenticidade da resposta, sob seu modelo de dois servidores. É uma possível peça para a combinação.</p>
          <p><a href="papers/tapir-2025.pdf">Ler TAPIR (PDF, 20 páginas)</a> · <a href="https://github.com/laurahetz/TAPIR">Código do TAPIR</a></p>
        </li>
      </ul>
      <details>
        <summary>Experimento, dificuldade e cuidados da ideia 5</summary>
        <p>Começar com dois servidores e credenciais sintéticas com dois estados: ativa ou revogada. Comparar o protocolo original, a composição proposta e uma solução simples com árvore de Merkle e ZK.</p>
        <p>Medir tempo, comunicação e custo das atualizações. Testar registros alterados e respostas de versões antigas da base.</p>
        <p>Não basta o cliente detectar uma resposta falsa: um cliente malicioso pode ignorar essa verificação. Quem recebe a prova também precisa verificar seu vínculo com a base aceita.</p>
        <p><strong>Dificuldade estimada:</strong> média a alta. Exige definir a segurança da composição e comparar com outras soluções de revogação, incluindo ALLOSAUR.</p>
      </details>
    </section>

    <section id="carteira" aria-labelledby="titulo-carteira">
      <h2 id="titulo-carteira">Ideia 6 — Recuperar pagamentos depois de ficar offline</h2>
      <p>Uma carteira privada precisa descobrir os pagamentos recebidos sem revelar ao servidor quais pertencem a ela. Isso fica mais difícil quando ela passa muito tempo offline.</p>
      <p><strong>O que combinar:</strong> uma caixa de entrada pequena para mensagens recentes + busca privada no histórico para recuperar as antigas.</p>
      <p><strong>Pergunta:</strong> essa combinação pode ser barata no uso diário e ainda recuperar todas as notificações após longos períodos offline?</p>
      <h3>Papers para ler</h3>
      <ul>
        <li>
          <a href="https://www.usenix.org/conference/usenixsecurity26/presentation/shuhan">Oblivious Signaling</a> — USENIX Security 2026.
          <p>Organiza a entrega para facilitar a consulta de uma caixa de entrada de tamanho fixo. Quando ela enche, as mensagens mais antigas são removidas.</p>
          <p><a href="papers/oblivious-signaling-2026.pdf">Ler Oblivious Signaling (PDF, 21 páginas)</a> · <a href="https://doi.org/10.5281/zenodo.20437084">Artefato de Oblivious Signaling</a></p>
          <p>A limitação de capacidade está na seção 7, na <a href="papers/oblivious-signaling-2026.pdf#page=15">página 15 do PDF de Oblivious Signaling</a>.</p>
        </li>
        <li>
          <a href="https://www.usenix.org/conference/usenixsecurity26/presentation/liang">InstantOMR: Oblivious Message Retrieval with Low Latency and Optimal Parallelizability</a> — USENIX Security 2026.
          <p>Recupera mensagens privadamente usando cálculos sobre dados criptografados. Pode servir como base para a camada de histórico.</p>
          <p><a href="papers/instant-omr-2026.pdf">Ler InstantOMR (PDF, 21 páginas)</a> · <a href="https://github.com/xiangxiecrypto/tfhe-omr">Código do InstantOMR</a></p>
        </li>
        <li>
          <a href="https://eprint.iacr.org/2026/910">UnifOMR: Oblivious Message Retrieval with Near-optimal Concrete Efficiency</a> — ePrint 2026/910.
          <p>Outra construção recente de recuperação privada, com escolhas diferentes de comunicação e interação. Deve entrar na comparação de desempenho.</p>
          <p><a href="papers/unif-omr-2026.pdf">Ler UnifOMR (PDF, 56 páginas)</a></p>
        </li>
      </ul>
      <details>
        <summary>Experimento, dificuldade e cuidados da ideia 6</summary>
        <p>Simular pagamentos e períodos offline. Comparar somente a caixa recente, somente a busca privada no histórico e a combinação. Medir tempo de recuperação, bytes e processamento por usuário.</p>
        <p>Contar o custo de manter as duas camadas. A própria decisão de buscar no histórico pode revelar informação; consultas em horários fixos e mensagens de preenchimento são possibilidades a avaliar.</p>
        <p>Recuperar uma notificação não prova que o pagamento está confirmado ou que o saldo pode ser gasto.</p>
        <p><strong>Dificuldade estimada:</strong> média a alta, por envolver FHE/PIR. A composição é uma hipótese de pesquisa; sua vantagem ainda precisa ser medida.</p>
      </details>
    </section>

  </main>
  <footer>
    <p>Os PDFs e descrições da seleção atual estão nesta página. A busca foi dirigida, com leitura de trechos relevantes; os protocolos ainda não foram implementados ou medidos nesta pesquisa.</p>
    <p><a href="history.html">Histórico das cinco ideias anteriores</a> · <a href="README.md">Notas da pesquisa (.md)</a> · <a href="sources.json">Fontes da primeira busca</a> · <a href="accumulators/sources.json">Fontes sobre acumuladores</a> · <a href="defi/sources.json">Fontes sobre swaps e empréstimos</a> · <a href="#inicio">Voltar ao início</a></p>
  </footer>
</body>
</html>

>>>

PEER REWRITES (anonymized as V1..V5):
<<<
V1:
As seis propostas abaixo são alternativas individuais para 24 meses, não um programa conjunto. **Escolha principal: 2. Reserva: 3.** Todas entregam especificação, artefato reproduzível e análise de limitações; ganhos são hipóteses.

**1 — Custo do pertencimento privado KZG na prova de gasto do Zswap**

**Pergunta testável:** em que frequência de inserções e tamanho do conjunto Caulk+ reduz o custo amortizado do gasto completo?

**Escopo mínimo:** dois ativos, valores limitados, capacidade fixa, apenas inserções; começar com 2¹⁰ notas. Vincular a mesma nota ao lookup e ao circuito de gasto, usando um compromisso comum e uma composição explicitamente justificada. Preservar os requisitos de segurança do Zswap.

**Contribuição:** integração delimitada e mapa dos custos que sobrevivem à manutenção dos witnesses. **Controles:** Merkle original com cache e atualização incremental, mesmo hardware, segurança e fluxo; medir prova inteira, pré-processamento, bytes e memória.

**Continuar/desistir:** até o mês 6, exigir vínculo correto e protótipo completo. Se depender de nova primitiva, encerrar esse recorte; ausência de ganho permite continuar como avaliação explicativa. **Primeiro passo:** reproduzir um gasto Merkle e listar cada relação que a substituição deve preservar.

**2 — Formação de lotes para agregação Groth16 no Zswap**

**Pergunta testável:** como tamanho máximo e prazo de fechamento alteram bytes totais, trabalho do agregador e latência de validação frente ao batching?

**Escopo mínimo:** execução Rust, duas classes de chave de verificação, lotes de 4–256 provas e chegadas sintéticas uniformes e em rajadas. Agregar somente após fechar o lote; manter provas originais até sua finalização.

**Contribuição:** fronteira custo–latência explicada por um modelo e validada por medições. **Controles:** verificação individual, batching aleatorizado correto e SnarkPack com política fixa. Contabilizar entradas públicas, serialização e espera; testar provas inválidas, permutações e nullifiers repetidos. Preservar balanço e ordenação do protocolo.

**Continuar/desistir:** até o mês 3, demonstrar compatibilidade de uma prova real; até o 6, comparação completa. Interromper a integração se exigir migração criptográfica extensa; resultados desfavoráveis continuam válidos. **Primeiro passo:** inventariar curva, chaves, formatos e garantias usadas pelo artefato Zswap.

**3 — Certificados conservadores de garantia com reutilização verificável**

**Pergunta testável:** quanto custo de prova se evita, para diferentes faixas e vencimentos, em troca de rejeições conservadoras e informação sobre garantia/dívida?

**Escopo mínimo:** uma garantia de quantidade não negativa, dívida em unidade fixa e juros limitados até o vencimento. Provar `garantia × preço_mínimo ≥ razão × dívida_máxima`, com escalas, arredondamento e limites inteiros definidos. Vincular garantia bloqueada, posição, versão, domínio e prazo; validar oráculo recente. Alteração de posição invalida o certificado; não há desembolso reutilizável.

**Contribuição:** fronteira entre reutilização, conservadorismo e redução do conjunto de razões compatíveis com sucessivas apresentações. **Controles:** prova por cotação, renovação apenas quando necessária, faixas globais e personalizadas. Zyga será comparação conceitual até reprodução compatível.

**Continuar/desistir:** até o mês 6, exigir invariantes verificáveis e métrica explícita de vazamento. Se restar apenas demonstrar a desigualdade, desistir; ausência de economia não encerra análise informativa. **Primeiro passo:** construir simulador determinístico das renovações antes do circuito.

**4 — Delegação privada de atualização de witnesses KZG com inserções**

**Pergunta testável:** a adaptação das técnicas de delegação reduz trabalho do cliente para k inserções, mantendo índice oculto e resposta verificável?

**Escopo mínimo:** vetor fixo, uma nota por cliente, servidor não confiável e compromisso público aceito. Identificar todos os dados auxiliares exigidos pelo lookup, não apenas uma abertura KZG. Excluir remoções e crescimento de capacidade.

**Contribuição:** adaptação fundamentada para esse caso ou caracterização precisa do obstáculo algébrico. **Controles:** atualização local incremental, recomputação e PIR de witnesses pré-computados, incluindo manutenção e armazenamento do servidor. Testar respostas falsas e versões erradas.

**Continuar/desistir:** até o mês 4, exigir equações de atualização e argumento de privacidade; até o 6, uso numa prova real. Se a adaptação demandar primitiva inédita, abandonar como projeto principal. **Primeiro passo:** reproduzir as fórmulas locais e mapear o witness de Caulk+ para elas.

**5 — Prova privada de não revogação vinculada a uma base aceita**

**Pergunta testável:** qual custo adicional permite ao verificador rejeitar registro falso ou antigo mesmo quando cliente e um servidor cooperam?

**Escopo mínimo:** duas réplicas, pelo menos uma honesta, estados ativa/revogada e raiz por época publicada por mecanismo confiável explicitado. Compor consulta autenticada com prova ZK de posse da credencial e de seu estado sob essa raiz. Não prometer corrigir revogações fraudulentas autorizadas pelo publicador.

**Contribuição:** composição com garantia transferida ao verificador, delimitando se privacidade da base é preservada. **Controles:** PRC no modelo original, Merkle+ZK e ALLOSAUR sob hipóteses comparáveis; medir atualizações, prova e consultas, incluindo adulteração, replay e falha seletiva.

**Continuar/desistir:** até o mês 6, exigir que o verificador detecte falsificações e que os modelos de confiança sejam compatíveis. Se a checagem permanecer só no cliente, desistir. **Primeiro passo:** escrever a relação pública/privada e executar um caso adversarial mínimo.

**6 — Recuperação privada de notificações com caixa recente e histórico**

**Pergunta testável:** sob quais padrões de recebimento e tempo offline a combinação recupera todas as notificações com menor custo total ou menor latência de retorno?

**Escopo mínimo:** histórico retido, identificadores estáveis, épocas públicas e cursor local confirmado. Usar caixa recente e um backend OMR; definir sobreposição entre épocas para evitar lacunas e remover duplicatas. Garantia de completude condicionada ao histórico disponível e às hipóteses do backend.

**Contribuição:** protocolo de retomada com invariantes e modelo de custo das duas camadas. **Controles:** caixa isolada, histórico isolado, combinação e download integral; incluir InstantOMR e UnifOMR quando reproduzíveis. Medir perdas, duplicatas, bytes, tempo e processamento na entrega e recuperação; comparar consultas sob demanda com calendário fixo.

**Continuar/desistir:** até o mês 6, demonstrar retomada após exceder a capacidade e explicitar vazamentos do acionamento do histórico. Sem cobertura completa, interromper; desempenho negativo com explicação permanece resultado. **Primeiro passo:** simular mensagens e interrupções, validando cursores antes de integrar FHE.

V2:
As seis propostas abaixo são alternativas. Para a escolhida: meses 1–3, revisão e reprodução; 4–6, modelo e protótipo mínimo; 7–15, implementação e experimentos; 16–20, análise; 21–24, escrita e reprodução independente. Os marcos delimitam trabalho, sem presumir disponibilidade pessoal.

**1 — Custo completo de pertencimento privado KZG no Zswap.**

**Pergunta:** em que combinação de notas e atualizações Caulk+ altera o custo do gasto completo? **Escopo mínimo:** dois ativos, quantidades limitadas e conjuntos de 2¹⁰ e 2¹⁴ notas; 2¹⁸ somente depois. **Contribuição:** composição explicitamente vinculada à nota e mapa de custos, preservando a segurança exigida pelo Zswap. **Controles:** Merkle original com mesma carga, segurança e recursos; medir prova completa, memória, pré-computação e manutenção. Trocar nota, ativo, nullifier e compromisso deve produzir rejeição; comparar decisões com um modelo simples do gasto. **Continuar/desistir:** continuar com relação e argumentos de composição fechados até o mês 6; abandonar se isso exigir uma primitiva nova sem plano viável. Ausência de ganho não encerra o estudo. **Primeiro passo:** reproduzir um gasto Merkle e inventariar suas entradas públicas e privadas.

**2 — Agregação no Zswap sob um limite de espera.**

**Pergunta:** como tamanho máximo do lote e prazo de fechamento alteram bytes, CPU e latência por transação? **Escopo mínimo:** Rust, uma curva, lotes de 4–256 provas, gasto e saída separados por chave. **Contribuição:** fronteira reproduzível de custo/latência específica do protocolo. **Controles:** verificação individual e em lote; políticas por tamanho e por prazo, com mesmas chegadas sintéticas e públicos. Contar preparação, agregação e fila. Alterar públicos, duplicar nullifiers, misturar chaves e corromper uma prova deve levar à rejeição correta. Preservar também os vínculos da construção original. **Continuar/desistir:** seguir após compatibilidade demonstrada e pergunta adicional ao benchmark publicado; abandonar se restar apenas repetir esse gráfico. **Primeiro passo:** verificar diferencialmente um lote válido e outro com uma prova inválida, conservando as originais.

**3 — Certificados conservadores de garantia por faixa.**

**Pergunta:** qual reutilização é obtida para cada nível de rejeição conservadora e informação revelada? **Escopo mínimo:** uma garantia, dívida com juros limitados até o vencimento, pseudônimo público e quantidades privadas; somente checagem de saúde. **Contribuição:** caracterização conjunta de custo, utilidade e inferência sucessiva. **Controles:** prova por preço exato, faixas comuns e personalizadas; traços sintéticos estáveis, voláteis e com mudanças de posição. Comparar circuito com aritmética inteira de precisão arbitrária; testar arredondamento, fronteiras, expiração, cotação antiga e versão alterada. Definir publicamente o que a sequência de faixas permite inferir. **Continuar/desistir:** continuar se houver distinção demonstrável da literatura e análise informativa; abandonar se todo o resultado já estiver estabelecido. **Primeiro passo:** especificar a relação e a máquina de estados que impede usar certificado antigo após retirada ou nova dívida.

**4 — Delegação privada de atualização dos witnesses KZG de lookup.**

**Pergunta:** quanto trabalho da carteira pode ser delegado sem revelar o índice, contabilizando servidor e comunicação? **Escopo mínimo:** vetor fixo, inserções, uma nota por cliente e um servidor sob modelo explícito. **Contribuição:** adaptação justificada aos witnesses efetivamente consumidos por Caulk+. **Controles:** atualização local e PIR de witnesses pré-computados, incluindo manutenção de todos eles; comparar resultados com recomputação integral em instâncias pequenas. Testar resposta falsa, época antiga e índice incorreto. **Continuar/desistir:** avançar somente se, até o mês 6, houver algoritmo e argumento de privacidade/correção plausíveis; abandonar se a transferência algébrica não fechar. **Primeiro passo:** reproduzir as fórmulas locais e documentar exatamente a diferença entre o polinômio do acumulador bilinear e o vetor interpolado.

**5 — Revogação privada vinculada a uma época aceita.**

**Pergunta:** qual custo adicional impede o verificador de aceitar estado falso ou antigo quando cliente e um servidor desviam do protocolo? **Escopo mínimo:** dois servidores, um honesto, estados ativa/revogada e publicação autenticada de compromissos por época. **Contribuição:** composição com vínculo verificável entre credencial, registro e época. **Controles:** PRC para custo contextual e Merkle+ZK com segurança comparável; situar ALLOSAUR pela diferença de hipóteses. Testar cliente que ignora TAPIR, registro trocado, rollback e falhas seletivas. Compromisso autêntico não garante que a autoridade decidiu revogar corretamente: explicitar essa confiança. **Continuar/desistir:** seguir com apresentação verificável e modelo coerente; abandonar se a proteção existir apenas no cliente honesto. **Primeiro passo:** escrever o predicado aceito pelo verificador e construir um caso revogado contra ele.

**6 — Recuperação completa de notificações entre caixa recente e histórico.**

**Pergunta:** quando a combinação reduz custo mantendo recuperação até uma época pública após períodos offline? **Escopo mínimo:** histórico retido, mensagens com identificadores, operações honestas do servidor e primitivas existentes. **Contribuição:** política de recuperação com completude especificada e custo de suas consultas observáveis. **Controles:** caixa isolada, OMR isolado e combinação; caixa isolada é controle de perda, não equivalente funcional. Usar varredura local como oráculo e variar rajadas, duração offline, capacidade e anonimato. Contar entrega, duplicação, armazenamento, recuperação e preenchimento; comparar InstantOMR e, quando reproduzível, UnifOMR. **Continuar/desistir:** seguir se fronteiras entre épocas preservarem recuperação e vazamento declarado; abandonar se não houver pergunta distinta da comparação existente. **Primeiro passo:** simular esvaziamento, transbordamento e retorno offline, garantindo que cada notificação pertinente seja recuperada e deduplicada.

V3:
Convenção experimental comum: primeiros três meses para literatura e reprodução; até o sexto, confirmar o mecanismo mínimo; meses 7–15 para implementação e coleta; 16–24 para análise, artefato e dissertação. Este é um plano de escopo, condicionado à preparação e aos recursos disponíveis. Todas as propostas admitem demonstrar ausência de vantagem.

**1 — Custo completo do pertencimento privado KZG no Zswap.**

**Pergunta:** para quais capacidades e taxas de inserção Caulk+ reduz o custo da prova completa de gasto? **Escopo mínimo:** dois ativos, formato fixo de transação, conjuntos de 2¹⁰, 2¹⁴ e 2¹⁸ notas; primeiro uma ligação explícita à mesma nota e ao nullifier. **Contribuição:** composição justificada e mapa de custo incluindo manutenção. **Controles:** Merkle original, mesmo nível de segurança, mesma capacidade e fluxo; separar ocupação de profundidade da árvore. **Continuar/desistir:** continuar com relação verificável e experimento reproduzível, mesmo sem ganho; abandonar o recorte se preservar a segurança exigir uma construção sem caminho concreto até o sexto mês. **Primeiro passo:** reproduzir e decompor o custo de uma prova de gasto original.

**2 — Lotes de provas Zswap sob limite de espera.**

**Pergunta:** como tamanho máximo e prazo de fechamento alteram CPU total, comunicação e latência quando se usa SnarkPack? **Escopo mínimo:** Rust, curvas e formatos compatíveis, agregação separada por chave; lotes de 4, 16, 64 e 256 provas reais. **Contribuição:** fronteiras entre custo e latência, com política simples de lote e validação da composição. **Controles:** verificação individual e em lote; mesmas chegadas e prazos; contar entradas públicas, validação de nullifiers e número de verificadores. **Continuar/desistir:** continuar se houver comparação correta e pergunta ainda aberta; abandonar se restar apenas repetir números conhecidos ou reescrever uma infraestrutura inteira. **Primeiro passo:** verificar uma prova original e testar sua interoperabilidade antes de agregar.

**3 — Certificados conservadores de garantia e sua reutilização efetiva.**

**Pergunta:** quanto trabalho se evita por diferentes faixas e prazos, para a mesma demanda de checagens, e quais limites sobre garantia/dívida se revelam? **Escopo mínimo:** uma garantia, uma dívida, juros limitados e posição pseudônima versionada; circuito inteiro para `C × p_min ≥ r × D_max`, com limites e arredondamento conservador. **Contribuição:** caracterização de custo, rejeição conservadora e informação acumulada. **Controles:** prova exata nos mesmos eventos, faixas comuns/personalizadas e limite inferior com prazo; renovação por teto de preço deve ter justificativa. **Continuar/desistir:** continuar com vínculo ao estado bloqueado e métrica de divulgação; abandonar se literatura cobrir integralmente o recorte. **Primeiro passo:** especificar eventos de checagem e invalidação, incluindo mudança da política de juros e rejeição de estado antigo.

**4 — Atualização privada de witnesses KZG após inserções.**

**Pergunta:** delegar a atualização reduz trabalho da carteira por qual custo adicional no servidor e na rede? **Escopo mínimo:** vetor de capacidade fixa, inserções, uma nota e um servidor; preservar as hipóteses do mecanismo escolhido. **Contribuição:** adaptação delimitada ou identificação formal/experimental dos obstáculos. **Controles:** atualização local e PIR de witnesses pré-computados, explicitando diferenças de confiança; contabilizar construção, armazenamento e atualização das tabelas. **Continuar/desistir:** continuar após explicitar correção, índice oculto e validação no compromisso aceito; encerrar a tentativa de adaptação se esses vínculos permanecerem sem construção até o sexto mês. **Primeiro passo:** atualizar localmente um witness e consumi-lo numa prova Caulk+ real.

**5 — Custo de revogação privada autenticada por versão.**

**Pergunta:** qual sobrecusto torna uma apresentação inválida diante de registro adulterado ou versão rejeitada? **Escopo mínimo:** dois servidores, um honesto e sem conluio, registros binários e raiz/época aceita pelo verificador; cliente potencialmente malicioso. **Contribuição:** composição explícita entre consulta, credencial e apresentação ZK, com custo de atualização. **Controles:** PRC no seu modelo declarado e Merkle+ZK com download periódico da base; distinguir garantias ao comparar tempos. **Continuar/desistir:** continuar se a prova final vincular credencial, registro e versão; abandonar a composição se exigir mudar silenciosamente o adversário ou não permitir esse vínculo. **Primeiro passo:** escrever a relação verificada e os casos de falsificação, repetição e indisponibilidade; autenticidade não garante disponibilidade.

**6 — Caixa recente e histórico privado sob períodos offline.**

**Pergunta:** em quais cargas a combinação reduz custo total mantendo recuperação dentro do histórico retido? **Escopo mínimo:** mensagens sintéticas, caixa FIFO fixa, arquivo por épocas e um backend OMR; definir formatos comuns, deduplicação e probabilidades de falha. **Contribuição:** política reproduzível de recuperação e regiões de benefício ou desperdício. **Controles:** caixa isolada com perdas contabilizadas, histórico isolado sob consulta periódica e processamento contínuo, composição; incluir entrega, armazenamento, preenchimento e recuperação. Documentar também UnifOMR sob suas hipóteses. **Continuar/desistir:** continuar com recuperação correta e divulgação de metadados delimitada; abandonar a integração se formatos exigirem refazer a criptografia. **Primeiro passo:** reproduzir caixa e histórico separadamente e instrumentar custo por mensagem enviada e recuperada.

V4:
Para a alternativa escolhida: meses 1–3 para literatura, especificação e reprodução; 4–8 para composição mínima; 9–16 para experimentos e análise; 17–24 para consolidação, escrita e margem. Fixar hardware, versões, segurança e repetições; registrar dispersão. Usar dados sintéticos, explicitar metadados observáveis e reter registros necessários à reprodução.

**1 — Pertencimento privado KZG na prova de gasto do Zswap**

**Pergunta:** em quais tamanhos de conjunto KZG/Caulk+ altera o custo completo do gasto, incluindo manutenção, preservando o vínculo e as garantias do Zswap?

**Escopo mínimo:** dois ativos, quantidades limitadas e conjuntos de 2¹⁰, 2¹⁴ e 2¹⁸ notas. Construir uma relação que vincule pertencimento, nota, valor, ativo, autorização e nullifier; listar hipóteses e propriedades de extração necessárias.

**Contribuição:** composição delimitada e mapa de custos, inclusive regimes desfavoráveis. **Controles:** Merkle original com segurança equivalente e mesma carga; medir pré-processamento, atualização, prova completa, verificação, bytes e memória. Testar troca de nota, compromisso e nullifier.

**Continuar/desistir:** continuar se até o mês 4 houver composição justificada; abandonar esta candidata se depender de propriedade não obtida pelos componentes e exigir nova primitiva. Ausência de ganho não determina abandono. **Primeiro passo:** reproduzir um gasto Merkle e escrever a relação candidata antes da integração.

**2 — Agregação das provas do Zswap com latência limitada**

**Pergunta:** qual combinação de tamanho e prazo de fechamento do lote minimiza custo total para limites declarados de latência?

**Escopo mínimo:** agregação após formação do lote; separar gasto e saída por chave. Comparar 4, 16, 64 e 256 provas, com ordem canônica e dados públicos associados. O agregador recebe provas e entradas públicas; explicitar o vazamento da chegada e da composição prévia das transações.

**Contribuição:** caracterização reproduzível de custo/latência e regras de montagem. **Controles:** verificação individual, em lote e SnarkPack; medir bytes totais, agregação, verificação, memória e espera. Rejeitar entradas trocadas, nullifiers repetidos e balanços inválidos; preservar provas originais até finalizar.

**Continuar/desistir:** continuar após demonstrar compatibilidade e identificar questão não resolvida pelos benchmarks existentes; abandonar se restar apenas duplicação experimental sem pergunta adicional. **Primeiro passo:** agregar provas reais de uma chave do Zswap e conferir o conjunto de entradas aceito.

**3 — Certificados conservadores de garantia: reutilização e informação revelada**

**Pergunta:** como amplitude e prazo afetam provas evitadas, rejeições conservadoras e informação acumulada sobre garantia/dívida?

**Escopo mínimo:** uma garantia, dívida denominada na unidade de conta, preço público, juros limitados e posição pseudônima versionada. Provar `garantia × preço_mínimo ≥ razão × dívida_máxima`, com inteiros limitados e arredondamento conservador. Vincular garantia bloqueada, estado e vencimento. Mudanças na posição invalidam o certificado; a reutilização é somente da checagem de saúde.

**Contribuição:** fronteira entre custo, utilidade e vazamento. **Controles:** prova por cotação, faixas comuns e personalizadas; preços sintéticos estáveis, voláteis e com saltos. Medir intervalos possíveis para a razão privada após sucessivas renovações, sem pressupor distribuição probabilística.

**Continuar/desistir:** continuar com invariantes demonstrados e comparação diferenciada da literatura; abandonar se não houver pergunta além da desigualdade conhecida. **Primeiro passo:** implementar aritmética exata de referência, transições de estado e casos de fronteira antes do SNARK.

**4 — Delegação privada de atualização do witness KZG**

**Pergunta:** a delegação reduz trabalho da carteira sob custos totais explícitos e privacidade de consultas repetidas?

**Escopo mínimo:** vetor de capacidade fixa, inserções, uma nota por cliente e um servidor. Especificar atualização entre dois compromissos públicos aceitos e exatamente quais auxiliares Caulk+ consome. Definir adversário, vazamento permitido e rejeição de respostas falsas.

**Contribuição:** adaptação restrita e análise de segurança/custos. **Controles:** atualização local e PIR de witnesses pré-computados, contabilizando armazenamento e atualização do servidor, comunicação e verificação pelo cliente. Testar respostas antigas e alterações; validar o witness numa prova de pertencimento.

**Continuar/desistir:** continuar apenas se houver construção justificada até o mês 4; interromper se ocultação e verificabilidade exigirem desenvolver nova primitiva. Resultado negativo de desempenho pode sustentar contribuição delimitada. **Primeiro passo:** reproduzir a atualização local e identificar quais dados dependem secretamente da posição.

**5 — Revogação privada vinculada a uma versão aceita**

**Pergunta:** qual sobrecusto permite ao verificador rejeitar registro falso ou antigo quando um servidor e o cliente podem ser maliciosos?

**Escopo mínimo:** dois servidores, um semi-honesto sem conluio, estados ativa/revogada e compromisso por época aceito pelo verificador. A composição candidata usa PRC/TAPIR e prova ZK vinculando credencial, índice oculto, registro e época. A autoridade que determina a base correta fica explícita no modelo.

**Contribuição:** especificação da composição e custo da garantia adicional. **Controles:** PRC no seu modelo original, Merkle+ZK e ALLOSAUR sob hipóteses comparáveis; medir consulta, atualização e apresentação. Testar cliente que ignora checagens, resposta antiga, base divergente e falha seletiva.

**Continuar/desistir:** continuar se até o mês 4 existir evidência autenticada incorporável à apresentação ZK; interromper a composição se exigir novo APIR. **Primeiro passo:** escrever a relação verificada por terceiros e demonstrar a rejeição de um registro falso num exemplo mínimo.

**6 — Recuperação privada com caixa recente e histórico retido**

**Pergunta:** quando duas camadas reduzem custo total mantendo recuperação de todas as notificações dentro de uma retenção declarada?

**Escopo mínimo:** inbox fixa e arquivo por épocas, com retenção H; simular desconexões menores e maiores que H. Garantir completude somente dentro de H, com arquivo disponível e atualizações corretas. Deduplicar localmente. Separar notificação recuperada de pagamento confirmado.

**Contribuição:** política de recuperação e caracterização de custo/vazamento. **Controles:** caixa isolada, histórico isolado e composição; comparar InstantOMR e UnifOMR nas condições reproduzíveis. Medir perdas, duplicatas, entrega, recuperação, armazenamento e bytes. Comparar consulta ao histórico sob demanda com calendário fixo e preenchimento, contando o custo de ambos.

**Continuar/desistir:** continuar se a política preservar a garantia delimitada e gerar comparação reprodutível; abandonar promessa de completude se houver apagamento fora do modelo ou arquivo insuficiente. **Primeiro passo:** simular FIFO, retenção e períodos offline antes de integrar FHE/OMR.

V5:
Seis alternativas independentes para um mestrado de 24 meses. Escolher uma após a etapa inicial de viabilidade. Em todos os experimentos, registrar versões, parâmetros de segurança, hardware, memória máxima, sementes, repetições, dispersão dos tempos e falhas. Publicar também resultados desfavoráveis.

**1 — Custo completo do pertencimento privado KZG no Zswap.**

**Pergunta:** como tamanho do conjunto e frequência de inserções alteram o custo total do gasto ao substituir Merkle por Caulk+? **Escopo mínimo:** dois ativos, uma entrada por participante, capacidade fixa inicial de 2¹⁰ notas; crescer depois. **Contribuição:** composição explicitada e explicação dos custos dominantes. **Controles:** Zswap original e medição isolada de pertencimento; comparar provas completas sob segurança equivalente, incluindo manutenção e memória. Vincular pertencimento, autorização, valores e nullifier à mesma nota. **Continuar/desistir:** continuar com ligação justificada e protótipo completo; abandonar este recorte se exigir nova construção central além do orçamento inicial. Desempenho inferior permanece resultado válido. **Primeiro passo:** desenhar a relação completa e tentar combinar pertencimento de uma nota com autorização de outra antes de otimizar.

**2 — Agregação no Zswap sob limite de espera.**

**Pergunta:** quando SnarkPack reduz bytes ou custo de verificação sob uma espera máxima definida para finalizar o lote? **Escopo mínimo:** avaliador Rust, provas de gasto e saída separadas por chave, lotes de 4 a 256 provas. **Contribuição:** mapa reproduzível entre chegada de transações, composição dos lotes, custo e latência. **Controles:** verificação individual, batching e agregação, contando dados públicos, geração do agregado e espera. Testar adulteração de entradas públicas, nullifiers repetidos e composição com as garantias exigidas pelo Zswap. **Continuar/desistir:** continuar se existir caminho de integração limitado e pergunta ainda não respondida; encerrar a candidatura se reproduzir apenas curvas já conhecidas sem consequência específica. Ausência de ganho não encerra automaticamente. **Primeiro passo:** verificar um agregado de quatro provas reais e compatíveis.

**3 — Certificados conservadores de garantia com estado versionado.**

**Pergunta:** qual relação entre provas evitadas, recusas conservadoras e informação revelada surge ao variar faixa e prazo? **Escopo mínimo:** uma garantia, uma dívida, razão de garantia fixa, juros limitados e posição pseudônima versionada. Provar `garantia × preço_mínimo ≥ razão × dívida_máxima`, com limites inteiros e arredondamento conservador. **Contribuição:** caracterização experimental dessa relação usando SNARK convencional. **Controles:** prova por cotação, faixas comuns e personalizadas; variar preços e frequência de alterações da posição. Medir limites inferíveis sobre garantia/dívida após renovações. **Continuar/desistir:** continuar se houver pergunta distinta da literatura e estado seguro; desistir se o recorte estiver integralmente resolvido. **Primeiro passo:** implementar a máquina de estados e casos de vencimento, preço limítrofe, overflow e alteração de dívida. O certificado apenas atesta saúde; não permite novos desembolsos.

**4 — Delegação privada de atualizações KZG em vetor fixo.**

**Pergunta:** uma adaptação de técnicas existentes reduz trabalho da carteira com consulta oculta, considerando comunicação e servidor? **Escopo mínimo:** inserções, uma posição por carteira e atualização entre duas épocas; identificar exatamente os witnesses consumidos pelo lookup. **Contribuição:** adaptação limitada, argumento de segurança e comparação com recuperação privada pré-computada. **Controles:** atualização local, recuperação PIR e delegação candidata; contabilizar preparação, armazenamento e amortização por clientes. **Continuar/desistir:** até o mês 3, exigir candidato algébrico explícito e justificativa de privacidade; abandonar se depender de inventar uma primitiva. Não exigir vantagem positiva. **Primeiro passo:** atualizar localmente todos os dados auxiliares e produzir uma prova Caulk+ válida contra o compromisso novo, rejeitando respostas antigas ou alteradas.

**5 — Revogação privada vinculada à versão aceita.**

**Pergunta:** qual custo adicional permite ao verificador rejeitar apresentações baseadas em registros falsos ou versões vencidas? **Escopo mínimo:** dois servidores, base binária sintética, autoridade que publica compromisso e época aceitos; declarar hipóteses separadas para autoridade, servidores e cliente. **Contribuição:** composição e avaliação da garantia adicional, sem prometer corrigir decisões fraudulentas da autoridade da base. **Controles:** PRC original, TAPIR com prova ZK e Merkle com ZK; ALLOSAUR como comparação de garantias, e de desempenho somente se reproduzido. **Continuar/desistir:** continuar quando o vínculo ao compromisso aceito for verificável por terceiros; abandonar se depender da honestidade do cliente. **Primeiro passo:** tentar apresentar uma credencial revogada com cliente conivente, resposta alterada e época antiga; examinar também vazamento por abortos seletivos.

**6 — Caixa recente com recuperação privada de histórico.**

**Pergunta:** sob quais durações offline e cargas a composição reduz custo mantendo recuperação de todas as notificações retidas? **Escopo mínimo:** caixa FIFO e histórico em épocas fixas, servidor seguindo as atualizações, retenção declarada e sobreposição para evitar lacunas na transição. **Contribuição:** política de recuperação, invariantes de completude e avaliação do custo total. **Controles:** caixa isolada, histórico isolado e combinação; incluir UnifOMR conforme possibilidade de reprodução, distinguindo comparação analítica. Medir custos de envio, armazenamento, consultas, preenchimento e recuperação. **Continuar/desistir:** continuar com recuperação completa nas cargas declaradas e política de vazamento explícita; abandonar se a solução depender de nova primitiva. Perder em desempenho ainda pode explicar limites úteis. **Primeiro passo:** testar offline maior que a capacidade, mensagens na fronteira das épocas, duplicatas e retomada interrompida antes de integrar FHE.
>>>

For EACH version, score 0–10 on:
- Clarity (ease of understanding)
- Quality (technical/argumentative soundness)
- Consistency (holds up under scrutiny)
- Structure (flow and hierarchy)
- Originality (beyond the obvious)

Then write 2–4 lines of specific critique per version. No generic praise. No
empty criticism. Genuine disagreement is rewarded.

Return:

## SCORES
| Version | Clarity | Quality | Consistency | Structure | Originality |
|---------|---------|---------|-------------|-----------|-------------|
| V1      | ...     | ...     | ...         | ...       | ...         |
...

## CRITIQUES
### V1
{2–4 lines}
### V2
{2–4 lines}
...

Contrato de entrega: escreva em português. Avalie o mérito dos cinco textos
fornecidos como reformulações de propostas de mestrado, não como protocolos
implementados. Escala de mérito não é probabilidade de ingresso. A rubrica das
IDEIAS foi 35% relevância, 35% originalidade/coerência e 30% viabilidade; os CINCO
eixos desta revisão cruzada medem a qualidade das REESCRITAS e são distintos.
Não atribua autoria às versões nem tente descobri-la. Não leia outros arquivos
de pareceres, panel.json ou anonymization.json. Não crie subagentes.
Preserve críticas técnicas concretas: contribuição pode ser incremental,
resultado negativo pode ser útil, teste não substitui argumento de segurança.
Não use sua nota para fingir avaliação por um professor real da UFMG.

Grave o texto integral, com SCORES e CRITIQUES, em /Users/afa/Developer/mestrado2/grafo_procura_schoolar/research/2026-09-13-open-problems/peer-review-ufmg/cross-reviews/P4.md.
Grave também /Users/afa/Developer/mestrado2/grafo_procura_schoolar/research/2026-09-13-open-problems/peer-review-ufmg/cross-reviews/P4.json, no formato:
{"reviewer":"P4","versions":[{"version":"V1","clarity":0,
"quality":0,"consistency":0,"structure":0,"originality":0,
"critique":"crítica específica em 2–4 linhas"}, ...V2 até V5]}.
Só escreva esses dois arquivos. Na resposta final, informe os caminhos e a
principal tensão encontrada. Não reescreva mais uma vez as seis ideias.
