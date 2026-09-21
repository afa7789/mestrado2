# Painel completo: seis ideias de mestrado

[Ler a recomendação consolidada](./) · [Método e limitações](methodology.md)

Seis análises em contextos separados e trinta críticas cruzadas de reescritas. Nenhuma persona avaliou a própria versão. As identidades abaixo foram associadas às versões após as críticas.

## Painel

| Identificação | Especialidade | Lema | Estilo | Tipo |

|---|---|---|---|---|

| P1 | Blockchain | Boring technology | Optimistic/possibility-focused | general-purpose |

| P2 | Testing Strategy | Clean abstractions | Casual/pragmatic | general-purpose |

| P3 | Performance Optimization | Convention over configuration | Formal/rigid | general-purpose |

| P4 | Security & Cryptography | Flexibility > structure | Interrogative/Socratic | general-purpose |

| P5 | Compliance & Privacy | Maintainability | Conservative/cautious | general-purpose |

| P6 | Prototyping | Fail fast, fail loud | Vertical/depth-first | general-purpose |


## Análises integrais



### Parecer P1


**Perspectiva: Blockchain; lema: “Boring technology”.** Recomendo a **ideia 2**, com a **ideia 3 como reserva**. Favoreço componentes conhecidos, invariantes explícitos e resultados reproduzíveis. Uma dissertação pode contribuir explicando quando uma combinação deixa de compensar; não precisa inventar uma primitiva nem demonstrar ganho positivo.

Avalio as ideias originais, sem atribuir às notas os aperfeiçoamentos abaixo. Uso R = relevância/problema/objetivos/aderência, O = originalidade/coerência/trabalhos existentes/resultados e E = exequibilidade/metodologia, com **0,35R + 0,35O + 0,30E**, conforme o [edital regular PPGCC 2026, Anexo V, tabela 8](https://ppgcc.dcc.ufmg.br/wp-content/uploads/2025/10/Edital-Regular_Ciencia-da-Computacao_MD_2026.pdf). O edital exige NPP ≥ 70/100 e atribui peso de 20% ao pré-projeto no ingresso; estas notas de ideias não equivalem à NPP nem estimam admissão. Os 24 meses são horizonte de planejamento; preparo matemático, currículo, orientação e disponibilidade pessoal permanecem desconhecidos. A [página oficial de docentes](https://ppgcc.dcc.ufmg.br/docentes/) sustenta aderência à criptografia e segurança, sem demonstrar disponibilidade de orientação.

| Ideia original | R | O | E | Nota | Posição |
|---|---:|---:|---:|---:|---:|
| 1 — Pertencimento KZG no Zswap | 8,1 | 6,5 | 5,7 | **6,8** | 6ª |
| 2 — SnarkPack no Zswap | 8,8 | 6,9 | 8,5 | **8,0** | 1ª |
| 3 — Garantia por faixa | 8,3 | 6,9 | 8,2 | **7,8** | 2ª |
| 4 — Atualização privada KZG | 8,2 | 7,7 | 4,8 | **7,0** | 5ª |
| 5 — Revogação autenticada | 8,5 | 7,3 | 6,4 | **7,5** | 4ª |
| 6 — Recuperação após período offline | 8,7 | 7,2 | 6,8 | **7,6** | 3ª |

**Strengths — o que preservar.** As seis já reconhecem anterioridade, indicam artefatos e propõem medições. A ideia 2 preserva a geração independente das provas; a 3 limita a função do certificado; a 4 inclui PIR como controle; a 5 exige verificação pelo destinatário; a 6 contabiliza ambas as camadas. Isso aproxima as perguntas de sistemas utilizáveis.

**Weaknesses — objeção, novidade, viabilidade e evidência por ideia.**

**1.** Principal objeção: o vínculo entre pertencimento, autorização e nullifier continua sem construção. O [Zswap, construção e implementação](https://petsymposium.org/popets/2022/popets-2022-0120.pdf) exige mais que pertencimento isolado; [Caulk+](https://eprint.iacr.org/2022/957) fornece posição oculta, mas não estabelece automaticamente essa composição. A anterioridade de [Semacaulk](https://kohweijie.com/articles/23/semacaulk.html) é constatada; eventual vantagem no gasto completo é incógnita. Risco de novidade alto, viabilidade média-baixa. A composição ainda indefinida explica E inferior à ideia 2.

**2.** Principal objeção: repetir o gráfico de agregação versus batching já presente em [SnarkPack](https://research.protocol.ai/publications/snarkpack-practical-snark-aggregation/) seria contribuição fraca. A incógnita interessante é o custo completo em lotes efetivamente formados no Zswap, com gasto/saída separados e espera limitada. A disponibilidade de [código do Zswap](https://github.com/felix-engelmann/zswap-code) torna o começo concreto; compatibilidade de curvas, formatos e garantias permanece por verificar. Risco de novidade alto, viabilidade alta relativa. Recebe a maior nota pela pergunta operacional delimitada, sem pressupor integração trivial.

**3.** Principal objeção: uma desigualdade conservadora, sozinha, não estabelece contribuição científica. [Zyga, §8.2](https://eprint.iacr.org/2025/1802) já aplica reutilização a empréstimos; a original distingue uma alternativa restrita, mas ainda não quantifica a informação revelada. Viabilidade alta para o circuito, média para a avaliação longitudinal. Risco de novidade alto. Fica próxima da 2 porque a matemática simples favorece execução, embora faltem baselines que reutilizem certificados após alterações de preço já cobertas.

**4.** Principal objeção: “adaptar” pode exigir justamente o protocolo novo que o usuário pretende evitar. Há uma direção explicitamente aberta em [Private Delegation, §8](https://eprint.iacr.org/2026/832), e fórmulas locais conhecidas em [Vector Commitments with Efficient Updates, §3.1](https://eprint.iacr.org/2023/1830). Isso sustenta O relativamente alto; não demonstra ocultação da posição para os witnesses de Caulk+. Risco de novidade médio-alto e viabilidade baixa sem uma identidade algébrica concreta. A nota supera a 1 pela lacuna mais precisamente documentada, apesar de maior risco de execução.

**5.** Principal objeção: autenticar a resposta para um cliente honesto não impede um cliente malicioso de apresentar outro estado. A limitação do [PRC, §§4–5](https://www.usenix.org/conference/usenixsecurity26/presentation/edalatnejad) é constatada. [TAPIR](https://eprint.iacr.org/2025/2177) protege consultas sob suas hipóteses; não decide qual raiz é atual ou legítima. Risco de novidade médio-alto diante de [ALLOSAUR](https://eprint.iacr.org/2022/1362), cuja segurança cobre adversários maliciosos em seu modelo. Viabilidade média: composição, governança da raiz e privacidade da base precisam caber no mesmo recorte.

**6.** Principal objeção: falta explicar como detectar lacunas e recuperar exatamente o intervalo perdido. A expulsão FIFO em [Oblivious Signaling, §7](https://www.usenix.org/conference/usenixsecurity26/presentation/shuhan) é uma limitação constatada; a existência de [InstantOMR](https://www.usenix.org/conference/usenixsecurity26/presentation/liang) e [UnifOMR](https://eprint.iacr.org/2026/910) oferece componentes, não garante vantagem conjunta. Risco de novidade médio-alto; viabilidade média se tratados como bibliotecas. Supera a 5 porque continuidade de recuperação admite experimento incremental sem primeiro resolver certificação adversarial.

**Gaps — ausências.** Faltam critérios de parada, orçamento de hardware, contratos de interface e cronograma com reserva para reprodução. A busca dirigida em fontes primárias e a leitura de trechos locais não confirmam ineditismo nem validam provas formais integralmente. Nas seis, “privado” precisa especificar observador, vazamento permitido e hipóteses de confiança.

**Improvements — propostas concretas.** Fixar versões dos artefatos; separar custo inicial e recorrente; medir memória, comunicação e latência de cauda; comparar o mesmo nível de segurança. Reservar meses 1–3 para reprodução, 4–6 para decisão de continuidade, 7–15 para implementação, 16–20 para avaliação e 21–24 para escrita.

**Risks — armadilhas.** Prova válida sobre estado antigo, metadados entre consultas e mudança implícita de modelo podem invalidar conclusões. Um benchmark negativo permanece contribuição quando identifica limites generalizáveis; integração incompleta ou parâmetros incompatíveis não sustentam comparação de desempenho.


### Parecer P2


**Strengths — preservar.** A seleção reconhece anterioridade, evita prometer ganhos e inclui custos frequentemente esquecidos. Meu critério de estratégia de testes é “Clean abstractions”: cada proposta deve separar a propriedade garantida, o mecanismo que a implementa e o experimento que pode refutá-la. Isso favorece perguntas delimitadas, mesmo com resultado negativo.

Avalio o mérito das **ideias originais**, sem crédito pelas melhorias abaixo. Uso R para relevância/problema/objetivos/aderência, O para originalidade/coerência/trabalhos/resultados e E para exequibilidade/metodologia/contribuição. A nota é 0,35R + 0,35O + 0,30E, conforme [Anexo V, tabela 8 do edital regular 2026](https://ppgcc.dcc.ufmg.br/wp-content/uploads/2025/10/Edital-Regular_Ciencia-da-Computacao_MD_2026.pdf). O piso oficial é NPP 70/100; o pré-projeto pesa 20% no ingresso. Estas notas exploratórias não são NPP nem probabilidade de admissão.

| Ordem | Ideia original | R | O | E | Nota |
|---|---|---:|---:|---:|---:|
| 1 | 3 — Garantia por faixa | 8,0 | 7,0 | 8,5 | **7,8** |
| 2 | 2 — Zswap + SnarkPack | 7,5 | 6,5 | 8,0 | **7,3** |
| 3 | 6 — Carteira offline | 8,0 | 7,0 | 6,5 | **7,2** |
| 4 | 5 — Revogação privada | 8,0 | 7,5 | 5,5 | **7,1** |
| 5 | 4 — Atualização privada KZG | 8,0 | 7,5 | 4,5 | **6,8** |
| 6 | 1 — Pertencimento KZG no Zswap | 7,5 | 6,5 | 5,5 | **6,6** |

A ideia 3 lidera pela possibilidade de testar segurança e utilidade com uma relação aritmética pequena. A 2 tem menor originalidade, mas componentes e controles mais definidos. A 6 oferece uma pergunta operacional relevante; a 5 precisa fechar uma fronteira de confiança mais difícil. A 4 tem uma direção científica mais explícita que a 1, porém sua entrega central depende de construção criptográfica incerta. Diferenças pequenas, especialmente entre 2, 6 e 5, não sustentam uma hierarquia categórica.

Há aderência temática: a [página oficial de docentes](https://ppgcc.dcc.ufmg.br/docentes/) relaciona Jeroen van de Graaf a criptografia teórica/aplicada e Leonardo Barbosa e Oliveira a segurança de sistemas distribuídos/criptografia aplicada. Isso não indica disponibilidade ou aceite. Considero 24 meses somente como horizonte de escopo; formação, currículo, orientação e dedicação permanecem desconhecidos.

**Weaknesses — objeções, novidade e viabilidade por ideia.**

**1.** A principal objeção é que a operação substituída está dentro de uma prova maior. Constatado: [Zswap, construção e implementação](https://petsymposium.org/popets/2022/popets-2022-0120.pdf) vincula gasto, nota e nullifier; [Caulk+](https://eprint.iacr.org/2022/957) acrescenta ocultação de posição e pré-computação. [Semacaulk](https://kohweijie.com/articles/23/semacaulk.html) já explora essa família de substituições. Risco de novidade alto. Incógnitas: composição que preserve as garantias do gasto e vantagem após manutenção. Viabilidade média a baixa; testar pertencimento isolado não resolve a proposta.

**2.** O principal risco é repetir um resultado experimental conhecido. Constatado: [SnarkPack, §7](https://eprint.iacr.org/2021/529) já compara agregação e verificação em lote e discute pontos de equilíbrio. O próprio esquema exige chave de verificação comum. Risco de novidade alto. Incógnitas: efeito do fluxo real de Zswap, heterogeneidade gasto/saída e espera. Viabilidade relativamente alta porque é possível começar com verificação diferencial e restringir a contribuição a custo versus latência; compatibilidade das implementações continua pendente.

**3.** A objeção é científica: certificar o pior preço de uma faixa monotônica é simples. Constatado: [Zyga, §8.2](https://eprint.iacr.org/2025/1802) já apresenta empréstimos com preços dinâmicos. Portanto, reutilização genérica não é novidade; o recorte por faixa não foi demonstrado equivalente a um trabalho anterior nesta busca. Risco de novidade médio a alto. Incógnita central: utilidade restante após juros, mudanças de estado, rejeições conservadoras e inferência das faixas. Viabilidade alta para um protótipo; a análise desses compromissos deve carregar a contribuição.

**4.** A objeção principal é chamar de adaptação pequena uma interface criptográfica ainda ausente. Constatado: [delegação privada, p. 30](https://eprint.iacr.org/2026/832) sugere VCs/PCS como extensão, mas já emprega KZG no acumulador bilinear. [Vector Commitments with Efficient Updates, §3.1](https://eprint.iacr.org/2023/1830) fornece atualização local, sem resolver automaticamente delegação com posição oculta. Risco de novidade médio, não inexistente. Incógnita: atualização dos witnesses concretos do lookup com segurança e custo aceitáveis. Viabilidade baixa para o perfil desejado, pois o caminho crítico pode exigir um protocolo novo.

**5.** A principal objeção é a distância entre autenticar uma resposta para o cliente e convencer um verificador perante cliente e servidor maliciosos. Constatado: [PRC, §§4.2–4.3 e 5.3](https://www.usenix.org/conference/usenixsecurity26/presentation/edalatnejad) limita resistência à falsificação por autoridades ativas; [TAPIR, §3.1](https://eprint.iacr.org/2025/2177) exige um servidor honesto no modelo de dois servidores. Autenticidade também não define qual versão deve ser aceita. Risco de novidade médio: [ALLOSAUR](https://eprint.iacr.org/2022/1362) já considera gestores maliciosos e atualizações anônimas. Incógnitas: composição, publicação do estado e custo da apresentação ZK. Viabilidade média a baixa.

**6.** A principal objeção é faltar um contrato preciso de recuperação: até qual época, com qual retenção e sob quais falhas? Constatado: [Oblivious Signaling, §7](https://www.usenix.org/conference/usenixsecurity26/presentation/shuhan) descarta mensagens antigas quando a caixa enche, já compara custos com OMR e deixa corrupção maliciosa do estado fora da garantia de correção. Risco de novidade médio a alto: duas camadas, sozinhas, são uma composição natural. Incógnitas: completude da transição e vazamento da política de busca. Viabilidade média, usando [InstantOMR](https://www.usenix.org/conference/usenixsecurity26/presentation/liang) existente e incluindo [UnifOMR](https://eprint.iacr.org/2026/910) na comparação pertinente.

**Gaps — ausências.** Faltam critérios prévios de encerramento, orçamento de memória/hardware, cargas justificadas e um modelo de referência executável. A busca dirigida em fontes primárias e os trechos locais consultados não estabelecem ineditismo; nenhum artefato foi executado neste parecer. Também faltam argumentos que conectem cada subprotocolo à propriedade final.

**Improvements — propostas concretas.** Separar testes de correção, casos adversariais e avaliação de custo. Fixar versões, segurança, hardware e sementes; registrar repetições, dispersão e custos amortizados sob taxas de atualização distintas. Usar ablações apenas quando isolarem uma hipótese. Testes encontram violações; não substituem argumentos de segurança. Recomendo **3 como principal e 2 como reserva**, pela menor dependência de inventar mecanismos criptográficos.

**Risks — armadilhas.** Comparar funcionalidades diferentes, esconder pré-processamento ou declarar privacidade a partir de ausência de falhas invalida conclusões. Um resultado sem ganho pode sustentar uma dissertação se explicar uma fronteira de aplicabilidade ainda não estabelecida. Desistir deve significar abandonar uma pergunta duplicada ou inexequível, não descartar resultados desfavoráveis.


### Parecer P3


**Perspectiva.** Aplico “Convention over configuration” à otimização de desempenho: reutilizar construções estabelecidas, reduzir parâmetros livres e medir o caminho completo. Favoreço projetos que produzam conhecimento verificável sem depender da invenção de uma primitiva. Um resultado negativo pode ser uma contribuição de mestrado se explicar limites e permitir reprodução.

As notas avaliam **as seis ideias originais**, sem crédito pelas reescritas. Uso R = problema, objetivos e aderência; O = originalidade, coerência, literatura e resultados; E = metodologia e exequibilidade. A fórmula é **0,35R + 0,35O + 0,30E**, conforme o [Anexo V, tabela 8, do edital regular 2026](https://ppgcc.dcc.ufmg.br/wp-content/uploads/2025/10/Edital-Regular_Ciencia-da-Computacao_MD_2026.pdf). O piso oficial NPP é 70/100 e seu peso final é 20%; estas notas de ideias não equivalem à NPP de uma submissão completa nem estimam admissão. Adoto 24 meses para delimitar escopo; preparação, disponibilidade pessoal e orientação permanecem desconhecidas.

| Posição | Ideia original | R | O | E | Nota |
|---|---|---:|---:|---:|---:|
| 1 | 2 — Agregação no Zswap | 8,5 | 6,8 | 8,3 | **7,8** |
| 2 | 3 — Garantia por faixa | 8,2 | 6,5 | 8,4 | **7,7** |
| 3 | 6 — Recuperação após período offline | 8,6 | 7,2 | 6,4 | **7,5** |
| 4 | 5 — Revogação privada | 8,6 | 7,3 | 5,9 | **7,3** |
| 5 | 4 — Atualização privada KZG | 8,2 | 7,4 | 4,5 | **6,8** |
| 6 | 1 — Pertencimento KZG no Zswap | 8,0 | 6,3 | 5,4 | **6,6** |

**Strengths — preservar.** O original distingue hipótese de novidade comprovada, inclui baselines e reconhece custos auxiliares. As ideias 2 e 3 já delimitam experimentos pequenos. A [página oficial de docentes](https://ppgcc.dcc.ufmg.br/docentes/) registra criptografia teórica/aplicada para Jeroen van de Graaf e segurança distribuída/criptografia aplicada para Leonardo Barbosa e Oliveira. Isso sustenta aderência temática das seis ideias; não demonstra disponibilidade ou interesse específico em orientá-las.

**Weaknesses — avaliação individual.**

**1. Pertencimento KZG.** Principal objeção: a otimização depende de uma composição ainda ausente. É constatado que [Caulk+](https://eprint.iacr.org/2022/957) obtém eficiência mediante pré-computação e argumentos de posição oculta; o [Zswap](https://petsymposium.org/popets/2022/popets-2022-0120.pdf) exige vínculo entre pertencimento, nota, autorização e nullifier. O custo dessa ligação é incógnita. **Novidade: risco alto**, pois [Semacaulk](https://github.com/geometryxyz/semacaulk) já cobre pertencimento privado KZG. **Viabilidade: baixa a média**: medir apenas lookup seria insuficiente, mas implementar uma composição segura pode dominar o calendário. Recebe menos O que 4 porque a extensão motivadora está menos fundamentada.

**2. Agregação.** Principal objeção: o limiar genérico já é parte da avaliação de [SnarkPack](https://research.protocol.ai/publications/snarkpack-practical-snark-aggregation/); aplicar a biblioteca não estabelece a contribuição. **Novidade: risco alto**, mitigado pela pergunta sobre latência e dados públicos específicos do Zswap. A exigência de mesma chave está constatada em §3.1 do PDF; integração entre os artefatos continua incógnita. **Viabilidade: alta relativa**: três baselines claros e provas existentes permitem resultados graduais. A nota superior vem dessa metodologia, não de uma suposta novidade criptográfica. O custo de agregação pode compensar com muitos verificadores e perder com apenas um.

**3. Garantia por faixa.** Principal objeção: “uma prova por cotação” pode superestimar trabalho realmente necessário; falta demonstrar quando o sistema exige nova checagem. [Zyga, §8.2](https://eprint.iacr.org/2025/1802), já contempla preços variáveis e empréstimos: anterioridade constatada. A existência de certificados equivalentes por faixa permanece incógnita após busca dirigida. **Novidade: risco alto**; a desigualdade conservadora sozinha é elementar. **Viabilidade: alta relativa**, com contribuição possível na caracterização de reutilização, rejeições conservadoras e divulgação acumulada. Fica próxima de 2 pela simplicidade do circuito, mas abaixo porque o baseline de demanda está menos estabelecido.

**4. Atualização privada KZG.** Principal objeção: o núcleo do trabalho ainda é construir o algoritmo com índice oculto. A [delegação privada de acumuladores, p. 30](https://eprint.iacr.org/2026/832), indica VC/PCS como direção futura; isso fortalece O, sem fornecer a adaptação. [Vector Commitments with Efficient Updates, §3.1](https://eprint.iacr.org/2023/1830), descreve atualização KZG dependente de dados auxiliares. **Novidade: risco médio**, ainda não confirmada para Caulk+. **Viabilidade: baixa** para quem quer evitar criar uma construção criptográfica: tradução de representações, privacidade de acessos e validação podem exigir trabalho fundamental. Essa dependência justifica o menor E.

**5. Revogação.** Principal objeção: autenticação da resposta ao cliente não produz automaticamente uma apresentação segura para outro verificador. A limitação de servidores ativos maliciosos é explícita em [PRC, §5.3](https://www.usenix.org/conference/usenixsecurity26/presentation/edalatnejad). [TAPIR](https://eprint.iacr.org/2025/2177) trata autenticidade e privacidade sob hipóteses próprias de servidores; não resolve sozinho a publicação da versão aceita. **Novidade: risco médio a alto**: [ALLOSAUR](https://eprint.iacr.org/2022/1362) já trata comportamento malicioso de participantes sob outro limiar de confiança. **Viabilidade: média a baixa**: composição e controle de versões pesam mais que a recuperação binária. A questão é relevante, mas o mecanismo completo permanece incógnita.

**6. Recuperação offline.** Principal objeção: a camada recente cobra trabalho mesmo quando ninguém consulta. A expulsão FIFO está constatada em [Oblivious Signaling, §7](https://www.usenix.org/conference/usenixsecurity26/presentation/shuhan), cuja arquitetura desloca custo para entrega. [InstantOMR](https://www.usenix.org/conference/usenixsecurity26/presentation/liang) já discute processamento contínuo; comparar só recuperação tardia produziria um baseline incompleto. **Novidade: risco médio a alto**; a vantagem da combinação continua incógnita. **Viabilidade: média**: duas implementações FHE e formatos compatíveis dificultam reprodução, mas um estudo de carga preserva valor sem nova primitiva. [UnifOMR](https://eprint.iacr.org/2026/910) precisa entrar como comparação documentada, respeitando comunicação e interação distintas.

**Gaps — ausências.** Faltam, transversalmente, carga justificável, orçamento de memória, versões fixadas, política de amortização e critérios de encerramento. A busca consultou trechos locais relevantes e fontes primárias; não certifica ausência de anterioridade nem segurança integral dos protocolos.

**Improvements — propostas concretas.** Fixar uma configuração inicial, um modelo de confiança e um responsável por cada custo. Reportar CPU total, tempo observado, memória máxima, bytes e pré-processamento separadamente. Variar taxas de atualização/consulta antes de multiplicar curvas ou bibliotecas. Medir distribuições e repetições, não apenas a melhor execução.

**Risks — falhas latentes.** Ganhos obtidos mudando segurança, hardware, estado aceito ou frequência de consultas não sustentam comparação. Falta de ganho não é critério suficiente para abandonar; impossibilidade de testar a pergunta ou contribuição já integralmente coberta são razões melhores. **Recomendo 2 como principal e 3 como reserva**; a diferença pequena exige confirmar artefatos e literatura antes da escolha definitiva.


### Parecer P4


**Strengths — O que preservar.** Recomendo a **ideia 3**, com a **ideia 5 como reserva**. Pela perspectiva de segurança e criptografia, “Flexibility > structure” significa preservar uma pergunta útil mesmo quando a combinação inicialmente escolhida fracassa. O original já identifica vínculos entre provas, custos de manutenção e limites de privacidade. Também distingue hipóteses próprias de resultados publicados: isso merece preservação.

Avalio as ideias originais como pontos de partida, sem conceder crédito retroativo às reescritas. Uso R = relevância/problema/aderência, O = originalidade/coerência/trabalhos existentes e E = exequibilidade/metodologia, com **0,35R + 0,35O + 0,30E**, seguindo o Anexo V, tabela 8. O piso oficial NPP é 70/100 e seu peso no ingresso é 20%; estas notas de ideias não são NPP nem probabilidades de admissão. [Edital regular 2026](https://ppgcc.dcc.ufmg.br/wp-content/uploads/2025/10/Edital-Regular_Ciencia-da-Computacao_MD_2026.pdf).

| Ordem | Ideia original | R | O | E | Nota |
|---|---|---:|---:|---:|---:|
| 1 | 3 — Garantia por faixa | 8,4 | 6,9 | 8,1 | **7,8** |
| 2 | 5 — Revogação privada | 8,8 | 7,8 | 5,6 | **7,5** |
| 3 | 6 — Recuperação offline | 8,2 | 7,0 | 5,9 | **7,1** |
| 4 | 2 — Agregação Zswap | 7,6 | 5,9 | 7,4 | **6,9** |
| 5 | 4 — Atualização privada KZG | 8,0 | 7,4 | 4,5 | **6,7** |
| 6 | 1 — Pertencimento KZG no Zswap | 7,7 | 6,2 | 4,8 | **6,3** |

A aderência temática encontra apoio nas áreas declaradas de Jeroen van de Graaf e Leonardo Barbosa e Oliveira; isso não indica disponibilidade ou aceite de orientação. [Docentes do PPGCC](https://ppgcc.dcc.ufmg.br/docentes/). Os 24 meses delimitam escopo, sem pressupor formação matemática, currículo ou dedicação conhecidos.

**Weaknesses — Objeções, novidade e viabilidade.**

**1. Qual garantia autoriza compor essas duas provas?** A objeção principal é preservar autorização e extração sob simulação, além de provar pertencimento. O teorema antirroubo de [Zswap, §6](https://petsymposium.org/popets/2022/popets-2022-0120.pdf) depende dessa extração; [Caulk+, §2.7](https://eprint.iacr.org/2022/957) apresenta outra caracterização de segurança. Essa diferença de requisitos é constatada; uma incompatibilidade inevitável não foi demonstrada. [Semacaulk](https://kohweijie.com/articles/23/semacaulk.html) já faz pertencimento privado KZG. Risco de novidade alto e viabilidade baixa a média: a integração pode exigir mais criptografia que o usuário deseja. Por isso fica abaixo da ideia 4, cuja lacuna é mais explícita.

**2. O que o novo gráfico explicará além do artigo original?** [SnarkPack, §7](https://eprint.iacr.org/2021/529) já compara agregação e verificação em lote, mostrando mudança de vantagem conforme o tamanho. A anterioridade é constatada, tornando alto o risco de novidade. Aplicar ao Zswap continua viável, mas um limiar específico precisa explicar características do protocolo, latência ou falhas. A associação entre entradas públicas, provas e chaves também precisa sobreviver a um agregador malicioso. A compatibilidade dos artefatos permanece incógnita. Sua exequibilidade supera a da ideia 5; seu problema científico está menos definido.

**3. Quem realmente precisa de uma prova a cada cotação?** O controle proposto pode superestimar economia se houver poucas verificações solicitadas. Essa fragilidade metodológica está no texto, não é um ataque demonstrado ao certificado. [Zyga, §8.2](https://eprint.iacr.org/2025/1802) já discute empréstimos com preços variáveis; a novidade da faixa conservadora permanece incerta, com risco alto de anterioridade conceitual. A viabilidade é a melhor: circuito convencional, estado pequeno e análise de vazamento podem produzir contribuição sem nova primitiva. A diferença para as demais é conseguir separar correção, utilidade e privacidade em experimentos pequenos.

**4. Qual witness está sendo delegado e o que o servidor aprende nas falhas?** A direção VC/PCS é explícita em [Private Delegation, p. 30](https://eprint.iacr.org/2026/832), mas isso não fornece a adaptação pronta. [Vector Commitments with Efficient Updates, §3.1](https://eprint.iacr.org/2023/1830) explica atualização KZG; Caulk+ exige material auxiliar específico. A falta de uma construção é constatada; seu custo e originalidade exata são incógnitas. Risco de novidade médio, viabilidade baixa no perfil solicitado: demonstrar privacidade contra consultas repetidas e falhas seletivas pode virar o trabalho inteiro. Escopo operacional pequeno não implica prova de segurança pequena.

**5. Autenticidade para quem, contra qual autoridade?** [PRC, §4.1](https://www.usenix.org/conference/usenixsecurity26/presentation/edalatnejad) admite falsificação de tokens com uma autoridade ativamente maliciosa. A lacuna é real. Entretanto, [TAPIR, §3.1](https://eprint.iacr.org/2025/2177) pressupõe ao menos um servidor sem conluio que segue o protocolo; não resolve sozinho a aceitação por um verificador diante de cliente malicioso. Autenticar uma base também não demonstra que a autoridade publicou o estado legítimo. [ALLOSAUR](https://eprint.iacr.org/2022/1362) já aborda atualizações anônimas sob comportamento malicioso. Risco de novidade médio a alto; viabilidade média a baixa, mas a propriedade a investigar é mais substantiva que uma compressão já conhecida. Isso justifica a reserva.

**6. Recuperar tudo significa resistir a omissão deliberada?** [Oblivious Signaling, §7](https://www.usenix.org/conference/usenixsecurity26/presentation/shuhan) limita a correção a atualizações que seguem o protocolo e confirma expulsão FIFO. A proposta não define claramente esse limite para sua promessa de recuperação. É uma lacuna constatada; não concluo que a composição seja insegura. [InstantOMR](https://www.usenix.org/conference/usenixsecurity26/presentation/liang) já oferece processamento contínuo, e [UnifOMR](https://eprint.iacr.org/2026/910) acrescenta alternativas com comunicação e interação diferentes. Novidade média a incerta; viabilidade média a baixa pelas interfaces e custos de duas camadas. Tem mais espaço de pesquisa que a ideia 2, mas menor previsibilidade.

**Gaps — O que falta.** Nenhuma proposta possui artefato reproduzido nesta pesquisa. Faltam adversários e vazamentos definidos como parte da pergunta, não apenas como cuidados finais. Também faltam demanda de verificações na ideia 3 e política de retenção na 6. A busca dirigida em fontes primárias não demonstra ausência de anterioridade; as leituras locais foram de trechos pertinentes, sem auditoria integral das provas.

**Improvements — Mudanças concretas.** Fixar primeiro interfaces, entradas públicas, versão aceita e adversário. Depois reproduzir um controle pequeno. Na ideia 3, privilegiar uma análise de custo e informação; na 5, verificar o registro contra um compromisso aceito pelo destinatário da prova. Uma comparação rigorosa com resultado negativo pode sustentar contribuição de mestrado.

**Risks — Armadilhas.** Bibliotecas disponíveis não garantem hipóteses compatíveis. Respostas antigas podem ser autênticas; rejeições observáveis podem revelar a consulta. A reserva 5 exige interromper cedo se depender de inventar uma primitiva. Essa flexibilidade protege o prazo sem exigir novidade de doutorado.


### Parecer P5


**Forças — o que preservar (Strengths).** A seleção distingue hipótese de novidade, identifica artefatos e contabiliza manutenção, dados públicos e latência. Sob a perspectiva de **Compliance & Privacy**, manutenção significa preservar garantias quando estados, versões e componentes mudam. ZK não demonstra conformidade regulatória.

Avalio as **ideias originais**, sem crédito pelas melhorias abaixo, por `0,35R + 0,35O + 0,30E`: relevância/objetivos/aderência, originalidade/coerência/trabalhos existentes e exequibilidade/metodologia. São os eixos da tabela 8 do [edital regular PPGCC 2026](https://ppgcc.dcc.ufmg.br/wp-content/uploads/2025/10/Edital-Regular_Ciencia-da-Computacao_MD_2026.pdf). O piso oficial NPP é 70/100 e o pré-projeto pesa 20% na nota final; estas avaliações de ideias não são NPP nem estimativas de admissão. Não penalizo o formato HTML. A [página de editais](https://ppgcc.dcc.ufmg.br/editais/) foi conferida em 14/09/2026; não presumo regras de 2027.

| Ordem | Ideia original | R | O | E | Ponderada |
|---|---|---:|---:|---:|---:|
| 1 | 3 — Garantia por faixa | 8,4 | 7,1 | 8,7 | **8,0** |
| 2 | 5 — Revogação privada | 9,0 | 7,8 | 6,2 | **7,7** |
| 3 | 2 — Agregação no Zswap | 8,0 | 6,0 | 8,0 | **7,3** |
| 4 | 6 — Recuperação offline | 8,4 | 6,9 | 5,6 | **7,0** |
| 5 | 4 — Atualização privada KZG | 8,0 | 7,7 | 4,8 | **6,9** |
| 6 | 1 — Pertencimento KZG no Zswap | 8,0 | 5,7 | 5,9 | **6,6** |

A aderência temática é sustentada pelas áreas de criptografia de Jeroen van de Graaf e segurança distribuída/criptografia aplicada de Leonardo Barbosa e Oliveira no [quadro docente oficial](https://ppgcc.dcc.ufmg.br/docentes/). Isso não estabelece disponibilidade ou aceite. Os 24 meses delimitam planejamento; formação, currículo e dedicação permanecem desconhecidos.

**Fragilidades — diferenças entre as notas (Weaknesses).**

**1.** A objeção é vincular a mesma nota a pertencimento, autorização e nullifier sem deslocar custos para outra prova. A anterioridade genérica está constatada: [Semacaulk](https://kohweijie.com/articles/23/semacaulk.html) já utiliza KZG e Caulk+. O [Zswap, pp. 13–15](https://petsymposium.org/popets/2022/popets-2022-0120.pdf), exige relações vinculadas e extração sob simulação. A segurança da composição é incógnita, não falha demonstrada. Risco de novidade **alto**; viabilidade **média-baixa**, com dois sistemas criptográficos para manter. Por isso perde para a ideia 4 em originalidade, apesar de ter aplicação mais concreta.

**2.** A objeção é haver uma pergunta científica além da integração. [SnarkPack, §3.1](https://eprint.iacr.org/2021/529), já agrega Groth16 sob a mesma chave; o [artefato Zswap](https://github.com/felix-engelmann/zswap-code) já mede junção e provas. Anterioridade constatada; compatibilidade de parâmetros e propriedades adicionais do Zswap são incógnitas. Risco de novidade **alto**, viabilidade **alta relativa**: participantes preservam seus provadores. Falta analisar o que o agregador aprende ao receber transações antes da junção. Compressão não concede anonimato adicional automaticamente.

**3.** A objeção é transformar a faixa em contribuição mensurável, pois a desigualdade conservadora isolada é simples. [Zyga, §8.2](https://eprint.iacr.org/2025/1802), já apresenta empréstimos com preços dinâmicos; não demonstra a novidade deste recorte por faixas. Risco **médio-alto**, viabilidade **alta relativa**, graças a um circuito convencional e estado delimitado. A exposição do pseudônimo e a correlação das verificações são limitações reconhecidas; quanto as renovações revelam sobre a razão garantia/dívida permanece incógnito. Sua liderança resulta de exequibilidade e hipótese de privacidade testável, sem exigir uma primitiva nova.

**4.** A objeção é o protocolo de delegação ainda não estar construído. A [delegação privada de acumuladores, p. 30](https://eprint.iacr.org/2026/832), aponta VC/PCS como extensão; [atualizações vetoriais, §3.1](https://eprint.iacr.org/2023/1830), fornece atualização KZG local. Isso evidencia uma direção aberta, não uma adaptação pronta para os witnesses do lookup. Risco de novidade **médio**, viabilidade **baixa relativa**: ocultar a posição, verificar a resposta e lidar com consultas repetidas podem exigir trabalho criptográfico substancial. Essa incógnita reduz a exequibilidade.

**5.** A objeção é definir quem estabelece a base aceita: autenticação comprova correspondência ao estado autorizado, não a veracidade das decisões da autoridade. O [PRC, §4.1](https://www.usenix.org/conference/usenixsecurity26/presentation/edalatnejad), explicitamente admite falsificação com autoridade ativamente maliciosa. [TAPIR, §3.1](https://eprint.iacr.org/2025/2177), assume pelo menos um servidor semi-honesto sem conluio; sua garantia ao cliente não constitui automaticamente prova para terceiros. Limitação original constatada; composição segura incerta. Risco de novidade **médio**, viabilidade **média**. [ALLOSAUR](https://eprint.iacr.org/2022/1362) já trata adversários maliciosos sob outro modelo, impedindo vender revogação robusta genericamente como nova.

**6.** A objeção é prometer recuperação completa sem fixar retenção, disponibilidade e comportamento do servidor. [Oblivious Signaling, §7](https://www.usenix.org/conference/usenixsecurity26/presentation/shuhan), confirma expulsão FIFO e assume atualizações corretas para correção; não garante resistência à corrupção do estado. Benefício da composição incógnito. Risco de novidade **médio-alto**, viabilidade **média-baixa**, pela manutenção simultânea de duas camadas. [InstantOMR](https://www.usenix.org/conference/usenixsecurity26/presentation/liang) e [UnifOMR](https://eprint.iacr.org/2026/910) exigem controles atuais; o segundo explicita custos de interação e comunicação que precisam entrar na comparação.

**Lacunas (Gaps).** Faltam vazamento formalizado, ciclo de vida dos estados e critérios de interrupção. Li os trechos locais indicados e fiz buscas dirigidas sobre agregação Zswap, intervalos de garantia, delegação KZG e revogação/OMR; não estabeleci ineditismo nem auditei provas integrais. Artefatos não executados. Confiança média: gargalos documentados, custos locais desconhecidos.

**Melhorias (Improvements).** Recomendo **3 como principal e 5 como reserva**. A reserva tem problema adversarial melhor fundamentado que a agregação, mas exige verificação inicial rigorosa. Produzir relação formal pequena, implementação versionada, cargas sintéticas reproduzíveis e comparação sob garantias equivalentes. Resultado sem ganho positivo tem valor se responder à pergunta e explicar custos.

**Riscos (Risks).** Correlacionar falhas, horários, versões ou renovações pode desfazer a privacidade da consulta. TAPIR trata falhas seletivas; a composição precisa conservar essa proteção. Crescimento de estado auxiliar e dependências incompatíveis ameaçam manutenção. Pseudonimização não equivale a anonimato integral.


### Parecer P6


**Pontos fortes — o que preservar.** A seleção reconhece anterioridades e propõe controles relevantes. Pela perspectiva de prototipagem — *“Fail fast, fail loud”* — valorizo especialmente ideias cujo primeiro experimento pode revelar cedo uma hipótese falsa. A ideia 3 permite isso com aritmética pequena; a 2, com provas existentes. Dificuldade criptográfica, por si só, não torna uma proposta melhor.

Avalio as **ideias originais**, sem crédito antecipado pela reescrita. R representa relevância, objetivos e aderência; O, originalidade, coerência e trabalhos existentes; E, exequibilidade e metodologia. Uso **0,35R + 0,35O + 0,30E**, conforme o Anexo V, tabela 8 do [edital PPGCC 2026](https://ppgcc.dcc.ufmg.br/wp-content/uploads/2025/10/Edital-Regular_Ciencia-da-Computacao_MD_2026.pdf). O piso oficial de NPP é 70/100 e seu peso final é 20%; estas notas de ideias não são NPP nem probabilidades de ingresso. Formação, currículo, orientação e dedicação pessoal são desconhecidos. Os 24 meses apenas delimitam o planejamento.

| Ideia original | R | O | E | Nota ponderada | Posição |
|---|---:|---:|---:|---:|---:|
| 1 — Zswap com KZG | 7,6 | 6,5 | 5,2 | **6,5** | 5 |
| 2 — Agregação no Zswap | 8,0 | 6,2 | 8,2 | **7,4** | 2 |
| 3 — Garantia por faixa | 8,1 | 6,7 | 8,7 | **7,8** | 1 |
| 4 — Atualização privada KZG | 7,6 | 7,0 | 4,2 | **6,4** | 6 |
| 5 — Revogação autenticada | 8,5 | 7,0 | 5,4 | **7,0** | 4 |
| 6 — Carteira após período offline | 8,1 | 7,0 | 6,3 | **7,2** | 3 |

A [página oficial de docentes](https://ppgcc.dcc.ufmg.br/docentes/) registra criptografia teórica/aplicada para Jeroen van de Graaf e segurança distribuída/criptografia aplicada para Leonardo Barbosa e Oliveira. Isso sustenta aderência temática geral, sem demonstrar disponibilidade ou interesse específico. A [página de editais](https://ppgcc.dcc.ufmg.br/editais/) foi consultada em 14/09/2026; não extrapolo regras para 2027.

**Fragilidades — avaliação por ideia.**

**1. Zswap com KZG.** A principal objeção é a dependência de uma composição segura antes de descobrir se existe benefício. Está constatado que [Semacaulk](https://kohweijie.com/articles/23/semacaulk.html) já faz pertencimento privado com KZG/Caulk+; portanto, a troca genérica tem alto risco de novidade insuficiente. O [Zswap](https://petsymposium.org/popets/2022/popets-2022-0120.pdf), construção e implementação, exige mais que pertencimento: a nota participa da autorização, do nullifier e do balanço. É incógnita se a composição preservará essas relações e extração sob simulação com custo aceitável. A viabilidade cai porque um microbenchmark de lookup pode funcionar enquanto a prova completa fracassa. Seu experimento é mais concreto que o da ideia 4.

**2. Agregação.** A principal objeção é que a pergunta do ponto de equilíbrio já aparece parcialmente no [SnarkPack](https://eprint.iacr.org/2021/529), §7: o artigo compara agregação e batching e explicita o processamento linear das entradas públicas. Isso constata anterioridade, não demonstra que o comportamento no Zswap esteja resolvido. Novidade de risco alto; uma análise de chegadas, espera e mistura de provas pode constituir contribuição suficiente de mestrado. A [implementação do Zswap](https://github.com/felix-engelmann/zswap-code) oferece uma base concreta, justificando E alto. Compatibilidade e preservação da segurança permanecem incógnitas: a integração não foi executada.

**3. Garantia por faixa.** A principal objeção é transformar uma desigualdade conservadora simples em pergunta científica suficientemente distinta. [Zyga](https://eprint.iacr.org/2025/1802), §8.2, já aplica entradas dinâmicas a empréstimos; isso está constatado. A anterioridade exata de certificados convencionais por faixa permanece incógnita, com risco alto. A viabilidade é a maior porque estado, prazo, juros limitados e aritmética permitem um protótipo pequeno e testes de fronteira. A análise de informação revelada e recusas conservadoras pode sustentar uma contribuição modesta. Falta demonstrar em qual fluxo de verificações a reutilização traz utilidade, contando mudanças da própria posição.

**4. Atualização privada KZG.** A principal objeção é chamar de adaptação uma tarefa que pode exigir conceber um protocolo criptográfico. A extensão a compromissos vetoriais/polinomiais é direção explícita de [Private Delegation](https://eprint.iacr.org/2026/832), §8; já existem fórmulas de atualização local em [Vector Commitments with Efficient Updates](https://eprint.iacr.org/2023/1830), §3.1. Isso não fornece a delegação de todos os dados auxiliares necessários ao [Caulk+](https://eprint.iacr.org/2022/957). O risco de anterioridade é médio; a incógnita dominante é de construção e prova de privacidade. Recebe a menor viabilidade por contrariar a preferência de evitar novas primitivas.

**5. Revogação.** A principal objeção é que autenticar a resposta ao cliente não autentica automaticamente a apresentação a terceiros. O [PRC](https://www.usenix.org/system/files/usenixsecurity26-edalatnejad.pdf), §§4.2 e 5.3, explicita a limitação contra autoridades ativamente maliciosas; o [TAPIR](https://eprint.iacr.org/2025/2177) fornece recuperação autenticada sob seu próprio modelo. A passagem entre esses modelos é incógnita e reduz a viabilidade. Risco de novidade médio/alto: [ALLOSAUR](https://eprint.iacr.org/2022/1362) já trata revogação privada com adversários maliciosos sob outras hipóteses de confiança. A relevância é a maior, mas falta fixar quem determina a base aceita e o que acontece se essa autoridade também mente.

**6. Recuperação offline.** A principal objeção é prometer recuperação completa sem delimitar retenção, falhas e fronteira entre as duas camadas. A expulsão FIFO e a correção condicionada a atualizações honestas estão constatadas em [Oblivious Signaling](https://www.usenix.org/system/files/usenixsecurity26-shuhan.pdf), §7. A composição com [InstantOMR](https://www.usenix.org/system/files/usenixsecurity26-liang.pdf) é incógnita; [UnifOMR](https://eprint.iacr.org/2026/910) amplia a comparação necessária. Novidade de risco médio/alto. Supera 5 em viabilidade: pode-se refutar a hipótese sem inventar uma primitiva; integração, armazenamento duplicado e vazamento ainda dificultam o trabalho.

**Lacunas.** Nenhuma implementação foi compilada ou medida nesta avaliação. Consultei textos locais das seções citadas e fontes primárias na web. A busca dirigida não estabelece ineditismo. Faltam versões fixadas dos artefatos, orçamento de memória, cargas justificadas, plano estatístico e critérios de encerramento.

**Melhorias.** Recomendo **3 como principal e 2 como reserva**. Nos primeiros três meses, reproduzir a menor execução completa e verificar a anterioridade; até o mês 6, fechar o recorte e sua análise de segurança; meses 7–15, experimentos; 16–20, robustez e interpretação; 21–24, dissertação. Esses marcos são limites de escopo, não estimativas pessoais. Um resultado negativo reproduzível pode ser uma boa contribuição se explicar uma decisão real e os limites de generalização.

**Riscos.** Não confundir teste adversarial aprovado com demonstração criptográfica; bytes de prova com bytes totais; custo transferido ao servidor com economia global; autenticidade com atualidade; ou ausência de um artigo na busca com novidade. Não exigiria vitória sobre todo baseline nem novidade de doutorado; exigiria uma resposta útil mesmo com hipótese otimista refutada.


## Reescritas integrais



### Versão de P1


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


### Versão de P2


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


### Versão de P3


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


### Versão de P4


As seis propostas abaixo preservam suas combinações originais. Para qualquer escolha: meses 1–3 para anterioridade e modelo; 4–6 para controle e decisão de continuidade; 7–14 para composição; 15–20 para avaliação; 21–24 para redação. O plano será ajustado às condições pessoais e à orientação.

**1 — Pertencimento KZG vinculado ao gasto do Zswap**

**Pergunta:** em quais tamanhos e taxas de inserção Caulk+ altera o custo total do gasto mantendo as propriedades exigidas pelo Zswap? **Escopo mínimo:** dois ativos, capacidade fixa, uma entrada por prova, começando com 2¹⁰ notas. **Contribuição:** relação composta com vínculo da mesma nota à autorização, valor, ativo e nullifier, acompanhada de avaliação reproduzível. **Controles:** Merkle original; capacidades 2¹⁴ e 2¹⁸ apenas se couberem; medir preparação, atualização, prova completa, memória e bytes sob parâmetros comparáveis. Testar substituição de nota e reutilização indevida. **Continuar/desistir:** continuar com argumento de segurança delimitado; interromper se exigir novo sistema de provas. Desempenho inferior é resultado admissível. **Primeiro passo:** escrever as relações e identificar onde a extração sob simulação é necessária.

**2 — Agregação final do Zswap com limite de espera**

**Pergunta:** qual política de tamanho e prazo minimiza custo sob uma latência máxima, contando lotes rejeitados? **Escopo mínimo:** Rust, provas reais de gasto e saída agrupadas por chave; 4, 16, 64 e 256 provas. **Contribuição:** caracterização da formação de lotes específica ao fluxo Zswap, distinguindo compressão, processamento público e recuperação após falha. **Controles:** verificação individual, lote sem compressão e SnarkPack; mesmas provas, chegadas esparsas e rajadas, com entradas inválidas e nullifiers repetidos. **Continuar/desistir:** continuar se a análise responder algo além do limiar já publicado; encerrar a integração se a diferença for apenas repetir aquele experimento. **Primeiro passo:** verificar compatibilidade de curvas, chaves e formatos, preservando as provas originais até finalizar cada lote.

**3 — Certificados conservadores para saúde de empréstimos privados**

**Pergunta:** quanto custa reutilizar certificados por faixa, considerando verificações efetivamente solicitadas, rejeições conservadoras e informação revelada? **Escopo mínimo:** uma garantia não negativa, uma dívida, juros máximos conhecidos e posição pseudônima versionada. Provar `C × p_min ≥ r × D_max`, com inteiros limitados e arredondamento conservador; `p_max` apenas delimita a política. **Contribuição:** análise conjunta de segurança temporal, custo e inferência sobre C/D. **Controles:** prova exata sob demanda, faixas comuns e personalizadas; cache de verificação quando aplicável, mesmos preços e solicitações. Testar mudanças de estado, cotação vencida, overflow e renovações correlacionadas. **Continuar/desistir:** continuar se restar pergunta empírica ou formal após anterioridade; desistir se tudo estiver coberto. **Primeiro passo:** definir o verificador de estado e prazo. O certificado atesta saúde, sem autorizar novos desembolsos ou implementar liquidação.

**4 — Delegação privada de atualização do witness KZG**

**Pergunta:** pode-se reduzir trabalho da carteira preservando o índice consultado, com resultado verificável no compromisso atual? **Escopo mínimo:** vetor fixo, inserções, uma nota por carteira e um servidor; identificar o material auxiliar efetivamente consumido por Caulk+. **Contribuição:** adaptação delimitada e análise de consultas repetidas, respostas falsas e vazamentos por falha. **Controles:** atualização local e PIR de witnesses pré-computados; contabilizar memória e pré-processamento de ambas as pontas, comunicação e prova final de pertencimento. **Continuar/desistir:** continuar se uma adaptação de técnicas existentes preservar o modelo; interromper antes da implementação extensa se exigir nova primitiva. **Primeiro passo:** reproduzir a atualização local e demonstrar que seu resultado alimenta Caulk+; depois escrever a interface de delegação.

**5 — Revogação privada verificável contra uma base aceita**

**Pergunta:** qual sobrecusto impede aceitar estado falso ou antigo quando cliente e um servidor podem ser maliciosos? **Escopo mínimo:** dois servidores, registros binários sintéticos, épocas e compromisso da base aceito pelo verificador. Manter explícita a hipótese sobre quem publica esse compromisso. **Contribuição:** composição de consulta privada, autenticação e prova ZK que vincule credencial, registro e época. **Controles:** PRC original, Merkle com ZK e comparação com ALLOSAUR sob diferenças de confiança declaradas; medir consultas, atualização e apresentação. **Continuar/desistir:** continuar se o verificador rejeitar falsificações sem confiar na honestidade do cliente; interromper se a solução apenas deslocar essa confiança. **Primeiro passo:** modelar falsificação e replay; avaliar TAPIR com autenticação Merkle como componente, sem atribuir-lhe uma garantia pública ainda não demonstrada.

**6 — Recuperação privada com caixa recente e histórico**

**Pergunta:** para quais distribuições de atividade e ausência a combinação reduz custo mantendo recuperação e vazamento explicitamente delimitados? **Escopo mínimo:** notificações sintéticas, retenção histórica definida e servidor que segue o protocolo para correção; estudar privacidade no adversário permitido por cada componente. **Contribuição:** composição com cobertura de épocas, deduplicação e contabilização do vazamento ao ativar o histórico. **Controles:** somente caixa recente, InstantOMR histórico/contínuo, combinação e UnifOMR quando reproduzível; mesmas mensagens e orçamento computacional. Medir custo de entrega e recuperação, armazenamento, preenchimento e notificações perdidas. **Continuar/desistir:** continuar se interfaces e limites permitirem uma comparação informativa; interromper se a recuperação completa depender de garantias ausentes. **Primeiro passo:** demonstrar cobertura e transição entre camadas numa simulação sem FHE, antes da integração criptográfica.


### Versão de P5


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


### Versão de P6


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


## Matriz das 30 críticas cruzadas


Linhas: revisores. Colunas: autores das reescritas. Os valores avaliam a qualidade dos textos e não devem ser confundidos com as notas das seis ideias. Pesos desta matriz: clareza 15%, solidez 35%, consistência 25%, estrutura 10%, originalidade 15%. São escolhas do painel, não da UFMG.

| Revisor / versão | P1 | P2 | P3 | P4 | P5 | P6 |

|---|---:|---:|---:|---:|---:|---:|

| P1 | — | 8,45 | 8,25 | 9,00 | 8,75 | 8,25 |

| P2 | 8,89 | — | 8,44 | 8,61 | 8,78 | 8,58 |

| P3 | 8,60 | 8,85 | — | 8,35 | 8,25 | 8,10 |

| P4 | 8,80 | 8,73 | 8,65 | — | 8,73 | 8,58 |

| P5 | 8,82 | 8,63 | 8,38 | 8,52 | — | 8,37 |

| P6 | 8,80 | 8,55 | 8,10 | 8,55 | 8,43 | — |


### Médias e variâncias por reescrita


| Versão | Média ponderada | Variância | Pareceres |

|---|---:|---:|---:|

| P1 | 8,78 | 0,0094 | 5 |

| P2 | 8,64 | 0,0192 | 5 |

| P4 | 8,60 | 0,0464 | 5 |

| P5 | 8,59 | 0,0442 | 5 |

| P6 | 8,37 | 0,0343 | 5 |

| P3 | 8,36 | 0,0341 | 5 |


## Críticas integrais



### Revisão cruzada P1


Correspondência revelada após a revisão: V1 = P2; V2 = P3; V3 = P6; V4 = P4; V5 = P5.


## SCORES

| Version | Clarity | Quality | Consistency | Structure | Originality |
|---------|---------|---------|-------------|-----------|-------------|
| V1 | 8 | 9 | 8 | 9 | 8 |
| V2 | 9 | 8 | 8 | 9 | 8 |
| V3 | 9 | 8 | 8 | 9 | 8 |
| V4 | 9 | 9 | 9 | 9 | 9 |
| V5 | 9 | 9 | 8 | 9 | 9 |

## CRITIQUES

### V1

Na ideia 6, tratar a caixa isolada como controle de perda evita comparar serviços com garantias diferentes; na ideia 2, incluir preparação e fila melhora a contabilidade.  
Na ideia 1, os testes de troca de nota e nullifier não demonstram extração sob simulação; a expressão “segurança exigida pelo Zswap” ainda precisa explicitar essa obrigação da composição.  
Na ideia 3, falta fixar os mesmos eventos de checagem para o controle e os certificados: contar uma prova por preço pode superestimar a economia quando nem toda cotação exige uma checagem.  
A fronteira de custo/latência da ideia 2 pode sustentar contribuição incremental, mas o texto ainda não identifica qual característica do fluxo Zswap torna a pergunta distinta de uma avaliação genérica de lotes.

### V2

Separar ocupação de profundidade na ideia 1 e comparar provas exatas nos mesmos eventos na ideia 3 são controles que eliminam fontes concretas de ganho aparente.  
Na ideia 4, a “identificação formal/experimental dos obstáculos” precisa produzir uma condição ou limite demonstrável; relatar dificuldade de integração, isoladamente, não caracteriza contribuição.  
Na ideia 5, “um honesto e sem conluio” deixa ambíguo se a restrição também impede colaboração entre o cliente malicioso e o outro servidor, o que altera a garantia pretendida.  
Na ideia 6, “divulgação de metadados delimitada” ainda não define os observáveis da ativação do histórico nem como comparar políticas com vazamentos diferentes.

### V3

O protocolo comum de reprodução e os testes de fronteira entre épocas, duplicatas e retomada interrompida da ideia 6 tornam a avaliação mais verificável sem exigir integração FHE prematura.  
Na ideia 3, “prova por cotação” pode criar um controle artificialmente caro: a contagem de provas evitadas precisa acompanhar a mesma demanda de checagens de saúde.  
Na ideia 5, pedir hipóteses separadas é adequado, mas o escopo ainda não escolhe o adversário e o conluio permitidos para comparar PRC, TAPIR com ZK e Merkle com ZK; testar um cliente conivente não resolve essa definição.

### V4

Na ideia 3, usar prova exata sob demanda, admitir cache e esclarecer o papel de p_max evita atribuir ao certificado economias produzidas pelo controle; a ideia 2 também incorpora lotes rejeitados.  
Na ideia 2, “minimiza custo” requer uma unidade ou pesos para CPU, comunicação e espera; sem essa definição, o resultado defensável é uma fronteira de alternativas, não uma política ótima única.  
A ideia 5 distingue corretamente a base aceita da decisão da autoridade, mas a evidência de TAPIR incorporável à apresentação ZK continua sendo hipótese de viabilidade: testes de falsificação e replay não demonstram a segurança dessa composição.

### V5

Medir intervalos inferíveis sem pressupor distribuição, na ideia 3, e comparar consultas sob demanda com calendário e preenchimento, na ideia 6, dá conteúdo verificável à análise de privacidade.  
Na ideia 3, o controle “prova por cotação” ainda pode inflar as provas evitadas; falta manter a mesma demanda de checagens ao comparar custo e utilidade.  
Na ideia 5, “um semi-honesto sem conluio” precisa indicar se a restrição abrange o cliente malicioso e o outro servidor; essa ambiguidade impede saber exatamente qual ataque a composição promete impedir.  
Na ideia 1, incluir 2¹⁸ notas no escopo mínimo elimina a condição de memória presente no original e aumenta o compromisso experimental antes de reproduzir e validar o gasto completo.


### Revisão cruzada P2


Correspondência revelada após a revisão: V1 = P4; V2 = P3; V3 = P1; V4 = P5; V5 = P6.


## SCORES

As notas avaliam a qualidade das reformulações como propostas de mestrado, não protocolos implementados nem probabilidades de ingresso.

| Version | Clarity | Quality | Consistency | Structure | Originality |
|---------|---------|---------|-------------|-----------|-------------|
| V1 | 8.5 | 8.8 | 8.5 | 8.5 | 8.5 |
| V2 | 8.7 | 8.5 | 8.4 | 8.6 | 8.0 |
| V3 | 9.0 | 9.0 | 8.6 | 9.2 | 8.8 |
| V4 | 8.8 | 9.0 | 8.5 | 8.9 | 8.6 |
| V5 | 8.8 | 8.7 | 8.3 | 8.6 | 8.5 |

## CRITIQUES

### V1
Na ideia 3, comparar as mesmas solicitações de checagem e incluir cache evita fabricar economia contando toda cotação como trabalho obrigatório.
Na ideia 2, incluir lotes rejeitados é útil, mas falta delimitar a carga de entradas inválidas e a regra de recuperação: essas escolhas podem determinar a fronteira custo–latência.
O critério de continuidade da ideia 5 precisa distinguir rejeição observada nos testes de uma propriedade justificada da relação criptográfica; os casos adversariais propostos não bastam para estabelecer segurança da composição.

### V2
Separar ocupação de profundidade da árvore na ideia 1 e contabilizar construção e atualização das tabelas PIR na 4 evita dois controles artificialmente fracos.
A ideia 3 melhora o comparador ao manter a demanda de checagens, mas a “métrica de divulgação” ainda não especifica como transformar apresentações observadas em limites inferíveis sobre garantia/dívida.
Na ideia 5, “um honesto e sem conluio” deixa ambíguo quem pode cooperar com o cliente malicioso; delimitar essas coalizões é necessário para interpretar a comparação com PRC e Merkle+ZK.

### V3
Batching aleatorizado, permutações, balanço e retomada após exceder a capacidade dão casos concretos de validação; mapear todos os auxiliares de Caulk+ na ideia 4 evita testar somente uma abertura KZG.
Na ideia 3, “prova por cotação” pode superestimar a vantagem: a comparação precisa manter os mesmos eventos de checagem e justificar quando o controle poderia reutilizar uma verificação já realizada.
Na ideia 2, aceitar resultados desfavoráveis é adequado, mas falta condicionar a continuidade a uma lacuna identificada na literatura: um modelo com medições negativas também pode apenas repetir um benchmark conhecido.

### V4
A aritmética exata de referência da ideia 3 e os testes de base divergente e falha seletiva da 5 tornam a validação concreta; versões, repetições e dispersão explicitadas melhoram a reprodução.
Na ideia 2, otimizar o prazo de fechamento sem definir regimes de chegada deixa o experimento subdeterminado: tráfego esparso e rajadas podem inverter a comparação entre políticas.
Na ideia 5, “um semi-honesto sem conluio” precisa esclarecer se a restrição vale apenas entre servidores ou também para cooperação com o cliente; essa diferença altera o adversário que a apresentação deve enfrentar.

### V5
Testar nota e autorização desencontradas, replay de época e retomada interrompida favorece a detecção de erros de vínculo; sementes e falhas registradas tornam os resultados auditáveis.
Na ideia 3, o escopo não enuncia o vínculo com garantia efetivamente bloqueada nem a exigência de cotação recente; a máquina de estados e os testes de fronteira precisam partir desses invariantes de segurança.
Fora da ideia 4, “orçamento inicial” e “etapa inicial” não têm prazo definido: faltam marcos que permitam abandonar uma integração inviável ainda a tempo de executar outra alternativa nos 24 meses.


### Revisão cruzada P3


Correspondência revelada após a revisão: V1 = P4; V2 = P6; V3 = P2; V4 = P1; V5 = P5.


Notas sobre a qualidade das reescritas como propostas de mestrado, considerando somente o material fornecido.

## SCORES

| Version | Clarity | Quality | Consistency | Structure | Originality |
|---------|---------|---------|-------------|-----------|-------------|
| V1 | 8 | 9 | 8 | 8 | 8 |
| V2 | 9 | 8 | 8 | 9 | 7 |
| V3 | 9 | 9 | 9 | 9 | 8 |
| V4 | 9 | 9 | 8 | 9 | 8 |
| V5 | 9 | 8 | 8 | 9 | 8 |

## CRITIQUES

### V1

A ideia 3 introduz o controle mais cuidadoso para a economia de provas: demanda efetiva e cache, evitando atribuir ganho à eliminação de verificações que nem seriam solicitadas.
A ideia 2 inclui lotes rejeitados e recuperação após falha, mas usa o “limiar já publicado” como critério de abandono sem identificar qual resultado anterior tornaria a pergunta redundante.
Na ideia 4, contabilizar pré-processamento e armazenamento é necessário, porém falta declarar por quantos clientes e épocas esses custos serão amortizados; isso pode inverter a comparação entre delegação e PIR.
Os campos repetidos facilitam a comparação, mas reuni-los em um único parágrafo por ideia dificulta localizar os marcos de continuidade e distinguir hipótese, controle e contribuição.

### V2

O protocolo comum de versões, hardware, sementes, repetições e dispersão torna os resultados comparáveis; a amortização por clientes na ideia 4 também trata um custo que avaliações apenas locais esconderiam.
Na ideia 3, o controle “prova por cotação” pode superestimar a economia se a saúde da posição só for verificada sob demanda; falta fixar solicitações idênticas e permitir o reaproveitamento já disponível no controle.
A ideia 6 coloca a caixa isolada ao lado das soluções com histórico, mas não explicita que ela deixa de oferecer a mesma recuperação após transbordamento; custo inferior com perda deve ser identificado separadamente.
As contribuições são delimitadas, porém “mapa reproduzível” e “caracterização experimental” ainda precisam apontar que hipótese específica será explicada; a padronização das medições, sozinha, não estabelece essa distinção.

### V3

A ideia 6 distingue expressamente a caixa isolada como controle de perda e usa varredura local como oráculo, evitando equiparar sistemas baratos que entregam funções diferentes.
Os controles com aritmética de precisão arbitrária e recomputação integral ajudam a detectar erros; o texto também exige argumentos de composição, sem apresentar os testes como demonstrações de segurança.
A ideia 4 inclui a manutenção de witnesses pré-computados, mas não fixa a amortização por clientes e épocas, deixando aberta uma escolha capaz de dominar o resultado de desempenho.
Exigir apenas algoritmo e argumentos “plausíveis” para essa ideia no mês 6 deixa o marco menos verificável que os argumentos “fechados” exigidos na ideia 1; convém definir qual evidência mínima autoriza a implementação extensa.

### V4

Os controles são particularmente concretos: Merkle com cache e atualização incremental, batching aleatorizado e download integral reduzem o risco de comparar a proposta apenas com alternativas artificialmente caras.
A ideia 3 vincula garantia bloqueada, domínio, estado, prazo e cotação recente; a métrica de redução das razões compatíveis torna a análise de informação mais examinável que uma referência genérica a vazamento.
Na ideia 2, os marcos exigem compatibilidade e comparação completa, mas não exigem distinguir a fronteira obtida dos benchmarks já existentes; esse ponto enfraquece a indicação categórica dessa alternativa como escolha principal.
Na ideia 6, “sem cobertura completa, interromper” é amplo demais: uma falha dentro das hipóteses exige correção, enquanto uma impossibilidade bem caracterizada pode justificar redução de escopo ou resultado negativo de pesquisa.

### V5

A ideia 3 propõe medir conjuntos de razões possíveis sem inventar uma distribuição probabilística; a ideia 6 contabiliza calendário fixo e preenchimento e delimita a completude pela retenção H.
O escopo mínimo da ideia 1 inclui até 2¹⁸ notas sem a condição de memória presente no original e nas demais versões; isso transforma um teste de escala opcional em compromisso inicial sem orçamento de recursos.
A ideia 3 vincula estado e vencimento, mas omite a exigência original de cotação recente: a validade temporal do certificado não garante, por si, a atualidade do preço usado pelo verificador.
O controle “prova por cotação” também precisa acompanhar as mesmas solicitações de verificação da alternativa; caso contrário, parte das provas evitadas pode vir de uma rotina desnecessária imposta apenas ao controle.


### Revisão cruzada P4


Correspondência revelada após a revisão: V1 = P1; V2 = P2; V3 = P3; V4 = P5; V5 = P6.


## SCORES

| Version | Clarity | Quality | Consistency | Structure | Originality |
|---------|---------|---------|-------------|-----------|-------------|
| V1 | 9 | 9 | 8.5 | 9 | 8.5 |
| V2 | 8.5 | 9 | 9 | 8.5 | 8 |
| V3 | 9 | 8.5 | 8.5 | 8.5 | 9 |
| V4 | 8.5 | 9 | 8.5 | 9 | 8.5 |
| V5 | 9 | 8.5 | 8.5 | 8.5 | 8.5 |

## CRITIQUES

### V1

A ideia 3 compara também renovação somente quando necessária: esse controle ajuda a distinguir economia produzida pelo certificado de economia produzida pela política de renovação.  
Por que eleger a ideia 2 antes de verificar interoperabilidade e a lacuna frente aos benchmarks? A preferência deveria depender desses resultados; a contribuição incremental pode ser válida, mas ainda precisa ser delimitada.  
Na ideia 6, quais hipóteses do backend excluem omissão de mensagens? Histórico retido e cursor confirmado não garantem completude contra servidor malicioso; “hipóteses do backend” deixa implícito demais se a garantia pressupõe operação honesta.

### V2

Na ideia 3, a referência com inteiros de precisão arbitrária e os testes de estado antigo tornam verificáveis erros de aritmética e invalidação; isso melhora a executabilidade do recorte.  
Como será medida a inferência sucessiva nessa mesma ideia? “Definir publicamente o que a sequência de faixas permite inferir” ainda não escolhe uma medida comparável entre faixas comuns e personalizadas.  
Na ideia 6, variar “anonimato” significa variar o conjunto de usuários, os metadados observáveis ou alguma medida de indistinguibilidade? A variável precisa ser definida para que o experimento de privacidade seja reproduzível.  
Na ideia 1, o marco de argumentos de composição fechados deve nomear as propriedades exigidas, incluindo extração sob simulação; os testes de troca de nota, ativo e nullifier não substituem esse argumento.

### V3

O controle da ideia 3 com limite inferior e prazo questiona uma escolha central: se a suficiência da garantia é monotônica no preço, por que renovar ao cruzar um teto? Isso pode mudar a conclusão sobre o benefício de certificar uma faixa.  
Na ideia 5, quem determina a raiz e a época aceitas? Falta separar resposta adulterada de uma base autenticada cujo conteúdo foi decidido fraudulentamente pela autoridade; autenticar a primeira não resolve o segundo problema.  
Na ideia 4, “preservar as hipóteses do mecanismo escolhido” ainda deixa em aberto servidor passivo ou ativo e vazamento em consultas repetidas. Como comparar delegação e PIR se esses modelos não forem explicitados antes das medições?

### V4

A ideia 1 explicita propriedades de extração, e a 4 inclui privacidade de consultas repetidas: ambas tornam obrigações de segurança mais precisas que uma lista de testes adversariais.  
Na ideia 5, “um semi-honesto sem conluio” permite que o outro servidor combine sua visão com a do cliente malicioso? O texto precisa esclarecer quais coalizões a composição PRC/TAPIR pretende tolerar, sem sugerir que os componentes já atendem conjuntamente a esse modelo.  
Na ideia 3, onde entra a regra de frescor do oráculo? Preço público, versão da posição e vencimento do certificado não bastam para rejeitar uma cotação antiga ainda dentro da faixa; esse requisito explícito do original desapareceu.  
Os cortes no mês 4 para as ideias 1 e 4 são mais rígidos que a janela geral de composição até o mês 8. Convém distinguir impossibilidade de obter a propriedade necessária de atraso em justificar uma adaptação ainda viável.

### V5

Tentar combinar pertencimento de uma nota com autorização de outra, na ideia 1, e interromper a retomada entre épocas, na 6, fornece casos adversariais concretos para o primeiro protótipo; esses testes precisam acompanhar os argumentos de composição e os invariantes declarados.  
Na ideia 3, onde se vincula a garantia efetivamente bloqueada e se rejeita cotação antiga? Versionar a posição e testar alteração da dívida não substitui essas duas condições, presentes no original.  
Ainda na ideia 3, “prova por cotação” corresponde à demanda real de checagens? Sem fixar os mesmos eventos de consulta para os controles, a economia pode refletir uma frequência artificial de produção de provas.  
Na ideia 5, declarar hipóteses separadas é uma tarefa futura, mas qual coalizão define desde já a pergunta: cliente malicioso sozinho ou em conluio com um servidor? Essa escolha determina a garantia adicional que será comparada com PRC e TAPIR.


### Revisão cruzada P5


Correspondência revelada após a revisão: V1 = P4; V2 = P2; V3 = P6; V4 = P1; V5 = P3.


## SCORES

| Version | Clarity | Quality | Consistency | Structure | Originality |
|---------|---------|---------|-------------|-----------|-------------|
| V1 | 8.7 | 8.6 | 8.4 | 8.7 | 8.2 |
| V2 | 8.8 | 8.7 | 8.6 | 8.8 | 8.2 |
| V3 | 8.8 | 8.3 | 8.3 | 8.7 | 8.0 |
| V4 | 9.0 | 8.9 | 8.7 | 9.2 | 8.4 |
| V5 | 8.5 | 8.4 | 8.2 | 8.5 | 8.4 |

## CRITIQUES

### V1

Na ideia 3, contar checagens efetivamente solicitadas e considerar cache evita atribuir ao certificado economia sobre provas desnecessárias; distinguir o papel de `p_max` também esclarece a hipótese experimental.
Na ideia 2, o critério “além do limiar já publicado” pressupõe um resultado anterior que o material fornecido não identifica; uma contribuição incremental sobre latência e falhas pode ser válida sem ultrapassar um limiar de desempenho.
Nas ideias 1 e 4, a falha da adaptação leva à interrupção, mas falta delimitar uma entrega aproveitável dessa investigação; o texto admite desempenho negativo, sem desenvolver igualmente o valor de caracterizar um obstáculo de composição.

### V2

Na ideia 5, distinguir a apresentação verificável por terceiros da verificação feita pelo cliente, e separar autenticidade da base da correção das decisões da autoridade, delimita precisamente a garantia pesquisada.
Na ideia 3, “prova por preço exato” não fixa a mesma demanda de checagens nem o reaproveitamento de verificações; esse controle pode superestimar a reutilização atribuída aos certificados.
Na ideia 6, o oráculo por varredura local dá um controle concreto para perdas, mas falta dizer qual informação observável será avaliada — atividade, duração da ausência ou volume recebido; contabilizar consultas e preenchimento não mede, sozinho, esse vazamento.

### V3

A convenção comum de versões, parâmetros, sementes, dispersão e falhas torna as comparações reproduzíveis sem repetir procedimentos em cada proposta.
Na ideia 3, o resumo perde o vínculo explícito com garantia efetivamente bloqueada e a exigência de cotação recente presentes no original; versionamento e testes de overflow não asseguram esses dois fatos.
Na ideia 4, a justificativa de privacidade precisa delimitar o adversário e o padrão de consultas; rejeitar respostas antigas ou alteradas cobre integridade, mas não demonstra que consultas sucessivas preservam o índice oculto.

### V4

Na ideia 3, vincular garantia bloqueada, domínio, versão e prazo, além de exigir oráculo recente, preserva condições que a desigualdade isolada não estabelece.
A escolha da ideia 2 como principal é mais forte que seu critério de continuidade: os marcos verificam compatibilidade e comparação, mas não exigem justificar a contribuição específica diante da literatura; um resultado incremental serve, desde que essa diferença esteja identificada.
Na ideia 5, a separação entre raiz confiável e decisões fraudulentas do publicador restringe corretamente a promessa; permanece em aberto se privacidade da base será requisito, escolha que pode alterar a comparabilidade com PRC.

### V5

Na ideia 3, comparar a mesma demanda de checagens com um certificado apenas de limite inferior e prazo permite descobrir se o teto de preço provoca renovações sem benefício para a saúde da posição.
Na ideia 1, incluir 2¹⁸ notas no escopo mínimo elimina a condição de memória do original; essa escala deve permanecer uma extensão condicionada aos recursos, para não comprometer a viabilidade do experimento inicial.
Na ideia 5, “raiz/época aceita” não explicita quem fixa a versão nem a confiança nessa autoridade; o texto distingue autenticidade de disponibilidade, mas ainda precisa separar autenticidade do registro da correção da decisão de revogar.


### Revisão cruzada P6


Correspondência revelada após a revisão: V1 = P3; V2 = P1; V3 = P2; V4 = P5; V5 = P4.


## SCORES

| Version | Clarity | Quality | Consistency | Structure | Originality |
|---------|---------|---------|-------------|-----------|-------------|
| V1 | 8.5 | 8.0 | 8.0 | 9.0 | 7.5 |
| V2 | 9.0 | 9.0 | 8.5 | 9.0 | 8.5 |
| V3 | 9.0 | 8.5 | 8.5 | 9.0 | 8.0 |
| V4 | 9.0 | 8.5 | 8.0 | 9.0 | 8.0 |
| V5 | 8.5 | 8.5 | 8.5 | 9.0 | 8.5 |

## CRITIQUES

### V1
A ideia 4 antecipa um teste decisivo: consumir o witness atualizado numa prova Caulk+ real; a ideia 6, porém, começa reproduzindo dois sistemas antes de testar a passagem entre épocas numa simulação simples.
Na ideia 2, “relação entre custo e latência” ganha controles úteis, mas o critério de continuidade não exige um lote agregado de provas reais nem fixa quando a incompatibilidade deve encerrar a tentativa.
Na ideia 5, escrever casos de falsificação explicita o problema, mas falta escolher um caso mínimo que atravesse consulta, credencial e apresentação; uma relação no papel ainda pode ocultar a inviabilidade dessa composição.

### V2
Os marcos de compatibilidade no mês 3 e comparação no mês 6 da ideia 2 tornam a integração verificável; simular renovações e cursores antes de SNARK/FHE também testa cedo as regras que justificam as propostas 3 e 6.
Na ideia 3, “prova por cotação” precisa usar a mesma demanda de checagens da alternativa: gerar uma prova a cada atualização do preço pode superestimar a economia quando ninguém solicita uma checagem.
Na ideia 1, “protótipo completo” até o mês 6 ainda pede um critério observável de aceitação da composição, como rejeitar uma nota diferente entre lookup e gasto; esse teste detecta um erro de vínculo, sem substituir o argumento de segurança exigido pelo texto.

### V3
Os testes de troca de nota, públicos alterados, rollback e aritmética de precisão arbitrária atacam falhas específicas; a varredura local como oráculo torna a completude da ideia 6 verificável antes da integração criptográfica.
Na ideia 4, aceitar algoritmo e argumentos “plausíveis” até o mês 6 é um marco fraco: conferir fórmulas por recomputação ainda não demonstra que os auxiliares atualizados alimentam uma prova Caulk+ real.
Na ideia 2, a contribuição permanece uma fronteira de custo/latência e a exigência de uma “pergunta adicional” não diz qual observação distinguiria o projeto de um benchmark existente; o plano de testes está mais determinado que o critério científico de continuidade.

### V4
A ideia 3 define uma métrica concreta de inferência sem assumir distribuição, e a ideia 5 exige evidência incorporável à apresentação ZK; ambas tornam pontos abstratos do original mais examináveis.
O cronograma reserva os meses 4–8 à composição mínima, mas as ideias 1, 4 e 5 condicionam a continuidade a resultados no mês 4; falta distinguir o que deve existir nessa data e o que ainda pode ficar para o oitavo mês.
Na ideia 3, a ligação ao estado e ao vencimento está explícita, mas a checagem de atualidade do oráculo desaparece: um certificado dentro do prazo ainda pode ser usado com cotação antiga, caso o verificador não rejeite esse evento.

### V5
A ideia 3 controla checagens efetivamente solicitadas e cache, evitando inflar a economia; a ideia 2 inclui lotes rejeitados e recuperação após falha, ampliando a avaliação além do caminho em que tudo funciona.
O calendário decide continuidade nos meses 4–6 e deixa composição para 7–14; falta exigir nessa primeira decisão uma demonstração mínima da integração arriscada, especialmente nas ideias 1 e 5, cujos primeiros passos permanecem descritivos.
Na ideia 5, explicitar quem publica o compromisso não determina sozinho a privacidade da consulta: o recorte precisa declarar a hipótese sobre o segundo servidor e o conluio tolerado antes de comparar PRC, TAPIR e Merkle+ZK.


## Síntese


O painel foi concluído em **15/09/2026**, com seis análises e trinta críticas cruzadas. P1 propôs a reescrita mais bem avaliada (8,78; variância 0,0094), seguida de P2 (8,64) e P4 (8,60). Essas notas avaliam textos, não ideias nem chances de ingresso. A síntese aproveita a estrutura de P1, os controles experimentais de P2/P3 e as exigências de segurança e privacidade de P4/P5. De P6, mantém a prioridade de um primeiro resultado pequeno e verificável.

**Principal: ideia 3 ou ideia 2?** P1 e P3 recomendaram a ideia 2; P2, P4, P5 e P6 recomendaram a 3. A decisão final é começar pela 3: tem a maior média e um primeiro experimento menor, adequado ao pedido de combinar técnicas existentes. A ideia 2 fica como reserva para swaps. Ambas mantêm suas posições quando retiramos qualquer um dos seis pareceres. Isso é estabilidade interna do painel, sem valor de previsão estatística sobre uma banca.

**Reserva: ideia 2 ou ideia 5?** P4 e P5 favorecem a 5 por sua pergunta de segurança. A síntese mantém a 2 como reserva prática porque sua viabilidade média é maior. A 5 passa a ser uma alternativa forte se a orientação favorecer composição e demonstrações de segurança. A diferença entre 5 e 6 é pequena e muda de sinal ao remover P5; não justifica descartar a 6.

**Novidade ou viabilidade?** A direção de VC/PCS da ideia 4 tem motivação explícita no paper de delegação. Isso não reduz o trabalho para construir a adaptação. Preservamos essa motivação, mas não a tratamos como uma simples troca de biblioteca. Nas ideias 1 e 2, a troca ou combinação genérica já conhecida não recebe crédito de novidade. A contribuição deve estar na pergunta específica, na composição justificada ou em uma caracterização que os trabalhos anteriores não entregam.

As críticas cruzadas levaram às seguintes correções concretas:

- **Empréstimos:** a preocupação de P3/P4 com uma comparação artificial foi incorporada: todos os controles recebem as mesmas solicitações de verificação e podem reutilizar resultados ainda válidos. Há também um controle com limite inferior e prazo, pois o teto de preço não fortalece a desigualdade de suficiência. Os vínculos de estado destacados por P1 e a observação acumulada destacada por P5 entram no modelo. Não se atribui uma distribuição probabilística à dívida sem declará-la.
- **Agregação:** os controles de P2/P3 contam CPU, bytes, latência, trabalho do agregador e rejeição de lotes inválidos sob a mesma política. Uma vantagem em um desses eixos não vira automaticamente vantagem total. A ideia precisa ir além da comparação de agregação e verificação em lote que SnarkPack já apresenta.
- **Revogação:** as exigências de P4/P5 são explícitas: cliente e um servidor podem cooperar no ataque; o outro servidor permanece honesto. A autoridade do estado aceito é separada dos servidores de consulta. A proteção deve chegar ao verificador mesmo quando o cliente ignora verificações locais.
- **Carteiras:** as objeções de P1/P5 sobre retenção e observações combinadas limitam a garantia ao histórico disponível dentro de H. A caixa recente isolada pode perder mensagens e não é um controle com funcionalidade equivalente. O processamento contínuo do histórico também entra na comparação.
- **KZG:** nas ideias 1 e 4, a síntese mantém a cobrança de P4 por vínculo à mesma nota e argumento de segurança. Conta ainda todos os witnesses auxiliares, armazenamento e manutenção do servidor, como exigido nas críticas experimentais. Um teste que aceita a prova ou a ausência de ataques encontrados não demonstra segurança da composição.

Os marcos iniciais de P6 são usados como verificações de viabilidade, sem transformar um prazo arbitrário em critério científico. Um ganho de desempenho negativo pode responder uma boa pergunta; uma integração que não funcionou, sozinha, não é contribuição. O documento consolidado separa pergunta, controles, primeiro resultado e motivo para reformular cada candidatura.

Na conferência final, foram revistas clareza, solidez, consistência e estrutura contra essas objeções. A originalidade permanece uma hipótese a verificar na literatura e com a orientação. As notas originais foram preservadas: a síntese não foi pontuada como se tivesse passado por uma nova rodada independente.


## Documento final consolidado


# Ranking das seis ideias para um mestrado no PPGCC/UFMG

Avaliação concluída em 15 de setembro de 2026; fontes institucionais consultadas em 14 de setembro de 2026.

A **ideia 3 — certificados de garantia por faixa de preços — é a recomendação principal**. A **ideia 2 — agregação de provas no Zswap — é a reserva mais próxima do interesse em swaps**. Elas permitem começar com componentes conhecidos e experimentos pequenos. A contribuição científica de ambas ainda precisa ser demonstrada.

Este é um painel de agentes de IA, sem vínculo com a banca da UFMG. As notas medem o mérito das formulações atuais como ponto de partida para um pré-projeto; **7,8/10 não significa 78% de chance de ingresso**. O currículo, a preparação e a disponibilidade de orientação não foram avaliados.

## Como as notas foram calculadas

Usamos a rubrica do [edital regular PPGCC 2026, Anexo V](https://ppgcc.dcc.ufmg.br/wp-content/uploads/2025/10/Edital-Regular_Ciencia-da-Computacao_MD_2026.pdf): problema/objetivos/aderência, 35%; originalidade/coerência, 35%; viabilidade/metodologia, 30%. A nota é a média de seis avaliações independentes em contexto, com os mesmos pesos. O edital exige NPP mínima de 70/100, mas o projeto representa 20% da nota final de ingresso. Nossa escala não substitui essa avaliação oficial. Foi usado o edital publicado na [página do programa](https://ppgcc.dcc.ufmg.br/editais/) na consulta de 14/09/2026.

| Posição | Ideia | Nota / 10 | Menor–maior parecer |
|---|---|---:|---:|
| 1º | [Ideia 3 — Empréstimo: certificado de garantia por faixa](../#loan-interval) | **7,8** | 7,67–8,04 |
| 2º | [Ideia 2 — Zswap: agregação com SnarkPack](../#swap-aggregation) | **7,5** | 6,95–8,05 |
| 3º | [Ideia 5 — Revogação privada de credenciais](../#revogacao) | **7,4** | 7,05–7,74 |
| 4º | [Ideia 6 — Recuperação de pagamentos após ficar offline](../#carteira) | **7,3** | 7,04–7,61 |
| 5º | [Ideia 4 — Atualização privada de witnesses KZG](../#kzg) | **6,8** | 6,37–7,01 |
| 6º | [Ideia 1 — Zswap: Merkle → KZG/Caulk+](../#swap-kzg) | **6,6** | 6,31–6,82 |

O intervalo exibido é o menor e o maior parecer, não uma margem de erro estatística. Os revisores compartilham modelo, fontes e rubrica. Ao retirar um parecer por vez, as ideias 3 e 2 continuam nas duas primeiras posições; 5 e 6 trocam de ordem em uma das seis recomputações. Portanto, não há razão forte para tratar a diferença entre 5 e 6 como decisiva.

## O que sustenta cada posição

**Ideia 3 — 1º lugar.** O circuito pode ser pequeno; a pesquisa está em quantificar a economia de provas, as recusas conservadoras e a informação revelada por sucessivas renovações. O principal risco é a proposta acabar sendo apenas uma desigualdade simples. [Zyga, seção 8.2](https://eprint.iacr.org/2025/1802) já apresenta empréstimos com preços dinâmicos. A diferenciação precisa estar na alternativa convencional e restrita por faixa, com análise própria. O controle deve gerar provas nas mesmas solicitações de verificação, não presumir trabalho obrigatório a cada cotação.

**Ideia 2 — 2º lugar.** Tem caminho de implementação relativamente previsível e medidas claras. A objeção mais forte é que [SnarkPack](https://eprint.iacr.org/2021/529) já estuda agregação versus verificação em lote. O recorte defensável é formação de lotes do Zswap sob limite de espera, contando dados públicos, mistura de provas de gasto/saída e tratamento de lotes inválidos. Apenas trocar uma chamada de biblioteca e repetir um gráfico seria fraco.

**Ideia 5 — 3º lugar.** A propriedade de segurança é relevante: impedir uma apresentação falsa mesmo quando o cliente coopera com um servidor. A limitação aparece no [PRC](https://www.usenix.org/conference/usenixsecurity26/presentation/edalatnejad). A dificuldade é ligar a autenticidade da resposta à prova recebida pelo verificador. [TAPIR](https://eprint.iacr.org/2025/2177) não resolve essa ligação sozinho; [ALLOSAUR](https://eprint.iacr.org/2022/1362) exige uma comparação cuidadosa de garantias e hipóteses. É a reserva preferida pelos dois avaliadores focados em segurança e privacidade.

**Ideia 6 — 4º lugar.** A necessidade de retomar consultas depois de ficar offline é clara. O risco está em integrar duas camadas caras e chamar de recuperação completa uma garantia sem retenção ou disponibilidade definidas. [Oblivious Signaling](https://www.usenix.org/conference/usenixsecurity26/presentation/shuhan) desloca custo para a entrega; [InstantOMR](https://www.usenix.org/conference/usenixsecurity26/presentation/liang) também admite processamento contínuo. Esses custos devem aparecer nos controles. A proximidade com a ideia 5 permite escolher conforme orientação e facilidade de reproduzir os artefatos.

**Ideia 4 — 5º lugar.** Tem uma das melhores motivações de novidade: o [paper de delegação privada](https://eprint.iacr.org/2026/832) indica VC/PCS como direção futura. A nota cai por viabilidade. A adaptação com índice oculto e resposta verificável ainda é o próprio problema criptográfico, e pode exigir criar um protocolo. Um recorte com poucas operações não implica uma demonstração de segurança curta.

**Ideia 1 — 6º lugar.** A troca genérica Merkle → KZG já tem anterioridade em [Semacaulk](https://kohweijie.com/articles/23/semacaulk.html). Ao mesmo tempo, integrar [Caulk+](https://eprint.iacr.org/2022/957) ao gasto do [Zswap](https://petsymposium.org/popets/2022/popets-2022-0120.pdf) exige provar que todos os componentes tratam a mesma nota e preservam as garantias do protocolo. Ela reúne risco de novidade e de implementação. Não é inviável, mas é a escolha menos favorável para começar com o escopo desejado.

## Decisões da síntese

O painel foi concluído em **15/09/2026**, com seis análises e trinta críticas cruzadas. P1 propôs a reescrita mais bem avaliada (8,78; variância 0,0094), seguida de P2 (8,64) e P4 (8,60). Essas notas avaliam textos, não ideias nem chances de ingresso. A síntese aproveita a estrutura de P1, os controles experimentais de P2/P3 e as exigências de segurança e privacidade de P4/P5. De P6, mantém a prioridade de um primeiro resultado pequeno e verificável.

**Principal: ideia 3 ou ideia 2?** P1 e P3 recomendaram a ideia 2; P2, P4, P5 e P6 recomendaram a 3. A decisão final é começar pela 3: tem a maior média e um primeiro experimento menor, adequado ao pedido de combinar técnicas existentes. A ideia 2 fica como reserva para swaps. Ambas mantêm suas posições quando retiramos qualquer um dos seis pareceres. Isso é estabilidade interna do painel, sem valor de previsão estatística sobre uma banca.

**Reserva: ideia 2 ou ideia 5?** P4 e P5 favorecem a 5 por sua pergunta de segurança. A síntese mantém a 2 como reserva prática porque sua viabilidade média é maior. A 5 passa a ser uma alternativa forte se a orientação favorecer composição e demonstrações de segurança. A diferença entre 5 e 6 é pequena e muda de sinal ao remover P5; não justifica descartar a 6.

**Novidade ou viabilidade?** A direção de VC/PCS da ideia 4 tem motivação explícita no paper de delegação. Isso não reduz o trabalho para construir a adaptação. Preservamos essa motivação, mas não a tratamos como uma simples troca de biblioteca. Nas ideias 1 e 2, a troca ou combinação genérica já conhecida não recebe crédito de novidade. A contribuição deve estar na pergunta específica, na composição justificada ou em uma caracterização que os trabalhos anteriores não entregam.

As críticas cruzadas levaram às seguintes correções concretas:

- **Empréstimos:** a preocupação de P3/P4 com uma comparação artificial foi incorporada: todos os controles recebem as mesmas solicitações de verificação e podem reutilizar resultados ainda válidos. Há também um controle com limite inferior e prazo, pois o teto de preço não fortalece a desigualdade de suficiência. Os vínculos de estado destacados por P1 e a observação acumulada destacada por P5 entram no modelo. Não se atribui uma distribuição probabilística à dívida sem declará-la.
- **Agregação:** os controles de P2/P3 contam CPU, bytes, latência, trabalho do agregador e rejeição de lotes inválidos sob a mesma política. Uma vantagem em um desses eixos não vira automaticamente vantagem total. A ideia precisa ir além da comparação de agregação e verificação em lote que SnarkPack já apresenta.
- **Revogação:** as exigências de P4/P5 são explícitas: cliente e um servidor podem cooperar no ataque; o outro servidor permanece honesto. A autoridade do estado aceito é separada dos servidores de consulta. A proteção deve chegar ao verificador mesmo quando o cliente ignora verificações locais.
- **Carteiras:** as objeções de P1/P5 sobre retenção e observações combinadas limitam a garantia ao histórico disponível dentro de H. A caixa recente isolada pode perder mensagens e não é um controle com funcionalidade equivalente. O processamento contínuo do histórico também entra na comparação.
- **KZG:** nas ideias 1 e 4, a síntese mantém a cobrança de P4 por vínculo à mesma nota e argumento de segurança. Conta ainda todos os witnesses auxiliares, armazenamento e manutenção do servidor, como exigido nas críticas experimentais. Um teste que aceita a prova ou a ausência de ataques encontrados não demonstra segurança da composição.

Os marcos iniciais de P6 são usados como verificações de viabilidade, sem transformar um prazo arbitrário em critério científico. Um ganho de desempenho negativo pode responder uma boa pergunta; uma integração que não funcionou, sozinha, não é contribuição. O documento consolidado separa pergunta, controles, primeiro resultado e motivo para reformular cada candidatura.

Na conferência final, foram revistas clareza, solidez, consistência e estrutura contra essas objeções. A originalidade permanece uma hipótese a verificar na literatura e com a orientação. As notas originais foram preservadas: a síntese não foi pontuada como se tivesse passado por uma nova rodada independente.

## Como apresentar cada ideia de forma mais forte

Estas reformulações melhoram o recorte, mas não recebem crédito retroativo no ranking. Escolher uma delas; não executar as seis como um único projeto.

### Ideia 1 — Custo completo de pertencimento privado KZG no Zswap

**Pergunta:** como capacidade e frequência de inserções afetam o gasto completo, mantendo as garantias originais? **Contribuição candidata:** composição explicitamente justificada e explicação dos custos dominantes.

Começar com dois ativos, capacidade fixa e 2¹⁰ notas. Comparar com Merkle original sob a mesma segurança, medindo manutenção, memória, prova completa e verificação. A nota usada no lookup deve ser a mesma da autorização, valor, ativo e nullifier. O primeiro resultado precisa ser uma relação composta e um gasto válido; um lookup isolado não basta. Interromper esse recorte se preservar a segurança exigir um sistema de provas novo sem plano delimitado.

### Ideia 2 — Agregação no Zswap sob limite de espera

**Pergunta:** qual relação entre custo total e latência surge ao variar tamanho e prazo de fechamento dos lotes? **Contribuição candidata:** modelo de formação de lotes validado com provas reais, explicando situações de benefício e de desperdício.

Verificar primeiro curvas, formatos e parâmetros de uma prova real. Depois comparar verificação individual, em lote e SnarkPack com as mesmas chegadas esparsas e em rajadas, separando provas por chave. Contar dados públicos, trabalho do agregador, número de verificadores, espera e custo de rejeitar um lote inválido. Fixar a regra de pré-validação e a proporção de entradas inválidas para não cobrar proteção diferente dos controles. Comparar CPU, bytes e latência separadamente; uma política “ótima” requer pesos ou restrições previamente definidos. A observação do agregador deve constar no modelo de privacidade. Encerrar a candidatura se não restar pergunta além do experimento já publicado.

### Ideia 3 — Reutilização e informação revelada por certificados de garantia

**Pergunta:** quanto custo se evita para cada nível de recusa conservadora e informação revelada? **Contribuição candidata:** caracterização conjunta desses três efeitos com um SNARK convencional.

Começar com uma garantia, uma dívida em unidade fixa, juros limitados e posição pseudônima versionada. Definir aritmética inteira, arredondamento conservador, ausência de overflow e vínculo a garantia efetivamente bloqueada. O verificador exige cotação recente, preço na faixa, prazo válido, política vinculada e versão vigente da posição. Mudanças na posição ou na política relevante invalidam o certificado; ele não autoriza repetir empréstimos.

Antes do circuito, construir um simulador de preço, solicitações de verificação e alterações de estado. Comparar prova exata sob a mesma demanda, faixas comuns e personalizadas, além de um certificado que divulga apenas o limite inferior com prazo. O teto de preço não fortalece a desigualdade para uma garantia não negativa; sua renovação precisa ter função explícita na política.

Medir provas geradas, tempo total, recusas conservadoras e o conjunto de razões garantia/dívida ainda compatíveis com as observações. Se usar entropia ou probabilidade de inferência, declarar a distribuição assumida. A sequência de certificados pode revelar mais que cada certificado isolado. Antes de propor a dissertação, confirmar que essa análise específica não está coberta pela literatura. Se restar só demonstrar a desigualdade, o tema precisa ser reformulado.

### Ideia 4 — Delegação privada de atualização de witnesses KZG

**Pergunta:** quanto trabalho pode sair da carteira sem revelar a posição, contando servidor e comunicação? **Contribuição candidata:** adaptação limitada com correção, privacidade e custo definidos.

Usar vetor fixo, inserções e uma nota por cliente. Primeiro atualizar localmente todo o material auxiliar que Caulk+ consome e gerar uma prova válida. Só depois tentar delegar. Comparar atualização local, recuperação PIR de witnesses pré-computados e a candidata, cobrando a manutenção das tabelas, o número de clientes e épocas usados na amortização e diferenças de confiança. Antes de implementação extensa, exigir equações e argumento de privacidade, incluindo consultas repetidas e falhas seletivas. Sem esse núcleo, não assumir que uma integração de bibliotecas resolverá o problema. Um resultado negativo precisa estabelecer um limite ou obstáculo preciso; dificuldade de integração, sozinha, não é contribuição.

### Ideia 5 — Revogação privada vinculada ao estado aceito

**Pergunta:** qual custo permite ao destinatário rejeitar registro falso ou antigo diante de cliente e um servidor maliciosos? **Contribuição candidata:** uma composição que transfira a garantia ao verificador.

Começar com dois servidores, estados ativa/revogada e compromisso por época. Permitir que um servidor malicioso coopere com o cliente malicioso; o outro segue o protocolo e não compartilha seu estado com essa coalizão. Distinguir a autoridade que decide o estado legítimo dos servidores que respondem às consultas. A raiz aceita e a regra de atualização precisam estar no modelo. O primeiro marco é uma apresentação que vincula credencial, índice oculto, registro e época, inclusive quando o cliente ignora verificações locais. Comparar Merkle+ZK com as mesmas garantias; PRC original e ALLOSAUR precisam de diferenças de modelo explicitadas. Se a proteção existir apenas para o cliente honesto, a proposta ainda não está resolvida. Testes de falsificação acompanham um argumento de segurança da composição; não o substituem.

### Ideia 6 — Retomada privada entre caixa recente e histórico

**Pergunta:** em quais cargas a composição reduz custo preservando recuperação dentro de uma retenção definida? **Contribuição candidata:** política de retomada com cobertura de épocas e custo de metadados explicitados.

Fixar a retenção H; a recuperação completa vale apenas para mensagens ainda retidas, com arquivo disponível e atualizações corretas. O estudo de privacidade considera horários, tamanhos, épocas consultadas e acionamento do histórico observados nas duas camadas. Simular transbordamento, mensagens nas fronteiras, duplicatas e retomadas interrompidas antes de integrar FHE. Comparar histórico isolado, inclusive processamento contínuo, com a combinação sob a mesma garantia de recuperação. A caixa isolada mede perda; não é alternativa funcional equivalente. Contar entrega, armazenamento, consultas e preenchimento. A ausência de um ataque nos testes não prova privacidade; a observação combinada das duas camadas precisa de argumento próprio.

## Próximo passo recomendado

Para a **ideia 3**, produzir uma página com pergunta, diferença para Zyga, modelo de estado e três controles experimentais. Em paralelo, construir o simulador determinístico de certificados, sem ainda implementar um protocolo de empréstimo completo. O resultado deve mostrar se há uma pergunta útil depois de corrigir a frequência das checagens e contabilizar o vazamento. Para a **ideia 2**, o primeiro marco alternativo é verificar a compatibilidade de uma prova real do Zswap com a agregação.

O quadro oficial de [docentes](https://ppgcc.dcc.ufmg.br/docentes/) e as [linhas de pesquisa](https://ppgcc.dcc.ufmg.br/linhas-de-pesquisa/) sustentam aderência temática a criptografia, segurança, sistemas e métodos formais. Não foi verificada a disponibilidade de orientação para esses recortes.

## Notas por critério e pareceres

| Ideia | Problema / aderência (35%) | Originalidade / coerência (35%) | Viabilidade (30%) |
|---|---:|---:|---:|
| Ideia 3 | 8,2 | 6,9 | 8,4 |
| Ideia 2 | 8,1 | 6,4 | 8,1 |
| Ideia 5 | 8,6 | 7,5 | 5,8 |
| Ideia 6 | 8,3 | 7,1 | 6,3 |
| Ideia 4 | 8,0 | 7,5 | 4,6 |
| Ideia 1 | 7,8 | 6,3 | 5,4 |

[Os seis pareceres, reescritas e 30 críticas cruzadas](panel.html) · [Dados das notas](scores.json) · [Método](methodology.md) · [Fontes institucionais](sources.json) · [Edital local, página 15](edital-ppgcc-2026.pdf#page=15) · [Relatório em Markdown](README.md)


