# Mestrado UFMG — página principal

Atualizado em 2026-07-14.

Esta pasta passa a ser a fonte principal para acompanhar o mestrado de Arthur, a comunicação com o Prof. Jeroen van de Graaf e a pesquisa técnica relacionada.

## Estado atual

- **Instituição pretendida:** PPGCC/UFMG.
- **Possível orientador:** Prof. Jeroen van de Graaf.
- **Situação:** contato realizado e reunião presencial concluída em 2026-07-14; orientação e admissão ainda precisam ser formalizadas.
- **Objetivo:** produzir pesquisa com potencial de publicação e também uma implementação concreta.
- **Direção técnica em exploração:** intents cross-chain trustless usando storage proofs, consensus proofs e zero-knowledge proofs.

## Onde está cada informação

- [`JEROEN_COMMUNICATION.md`](JEROEN_COMMUNICATION.md): histórico das conversas, decisões e próximos contatos.
- [`NOTES_project_summary.md`](NOTES_project_summary.md): resumo técnico da direção atual e sua arquitetura.
- [`README.md`](README.md): índice e ordem de leitura da biblioteca técnica.
- [`PROJECT_IDEAS_JEROEN.md`](PROJECT_IDEAS_JEROEN.md): banco anterior de ideias de pesquisa alinhadas a Jeroen.
- [`devcon_devconnect_ZK_REFERENCES.md`](devcon_devconnect_ZK_REFERENCES.md): vídeos, eventos e referências complementares de ZK (inclui IC3 — grupo de pesquisa acadêmico).

## Hipótese de projeto atual

Construir ou estudar uma arquitetura em que uma chain verifique, sem confiar em backend ou relayer centralizado, que um evento ocorreu em outra chain:

```text
Intent assinado
  -> liquidação na Chain A
  -> prova de consenso/canonicidade do bloco
  -> prova de inclusão do estado
  -> prova ZK
  -> verificação e continuação na Chain B
```

Essa hipótese conecta diretamente:

- experiência de Arthur com EVM, Solidity, Go, rollups e infraestrutura blockchain;
- interesse comunicado a Jeroen em ZK, consenso, paper e implementação;
- materiais já reunidos sobre zkBridge, Herodotus, Bankai, Zendoo, Miden e Aztec.

Ela ainda deve ser tratada como **direção em exploração**, não como tema aprovado pelo orientador.

## Próximas ações

- [ ] Registrar com mais detalhes o que Jeroen e os alunos disseram na reunião.
- [ ] Confirmar com Jeroen se ele aceita orientar formalmente e qual é o próximo passo no PPGCC.
- [ ] Validar se intents cross-chain trustless é um problema adequado para o mestrado.
- [ ] Transformar a ideia em pergunta de pesquisa, hipótese, contribuição e escopo de protótipo.
- [ ] Completar a primeira rodada de leitura conforme a ordem do `README.md`.
- [ ] Criar notas individuais para cada paper lido: problema, método, limitações e relação com o projeto.
- [ ] Verificar edital, calendário, documentos, seleção e possibilidade de bolsa na UFMG.
- [ ] Preparar proposta preliminar e adaptar o CV acadêmico.

## Regra de manutenção

Novas comunicações com Jeroen devem ser registradas em `JEROEN_COMMUNICATION.md`. Decisões de projeto e mudanças de escopo devem ser refletidas aqui e em `NOTES_project_summary.md`. Papers e referências técnicas devem continuar indexados no `README.md`.

