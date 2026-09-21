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

