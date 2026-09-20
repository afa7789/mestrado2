# Nota — Resumo do Projeto (Intents Cross-Chain Trustless via ZK)

> Anotação de contexto do projeto. Resumo de conversa/áudios que motivam esta bibliografia.

## Tópico principal

Construir um **protocolo de intents cross-chain trustless** usando provas Zero-Knowledge.

Fluxo de alto nível:

1. Um usuário assina um **intent** na Chain A.
2. O intent é verificado e liquidado por um smart contract na Chain A.
3. A Chain B recebe uma **prova criptográfica** de que a liquidação realmente aconteceu.
4. A Chain B pode continuar a execução com segurança, sem confiar em nenhum relayer centralizado.

Em vez de depender de um backend confiável, a comunicação entre chains deve, no futuro, ser
protegida por **provas ZK**.

---

## Componentes necessários

### 1. Storage Proof
Prova que um determinado valor existe no storage de um contrato Ethereum, via inclusão na
**Merkle Patricia Trie (MPT)**. A prova deve virar uma prova ZK verificável por outra chain.

```
Contract Storage → MPT Proof → Zero-Knowledge Proof → Verificado em outra chain
```

### 2. Consensus Proof
Storage proofs sozinhos não bastam. É preciso provar também que:
- o bloco realmente pertence à blockchain;
- a transação realmente aconteceu;
- o state update faz parte da cadeia canônica da Ethereum.

Isso é o **"consensus proving"**. Só após provar **validade do bloco** + **inclusão no storage**
outra chain pode confiar na informação.

---

## Arquitetura geral (objetivo)

```
User assina Intent
   ↓
Chain A verifica assinatura
   ↓
Estado do contrato muda
   ↓
Storage Proof + Consensus Proof
   ↓
Zero-Knowledge Proof
   ↓
Verificado na Chain B → continua execução
```

---

## Recursos mencionados

Não existe um paper escrito sobre este tópico específico. As referências recomendadas foram:

**Herodotus** — documentação, landing page, repositórios GitHub. Cobre: Storage Proofs, Merkle
Patricia Trie, Cairo, provas ZK, geração e verificação de storage proofs, verificação de MPT. A
documentação foi descrita como "a coisa mais próxima de um paper".

**Bankai** — outra empresa trabalhando em **consensus proving**; também tem documentação. Um dos
fundadores mencionados foi **Paul**. Havia incerteza sobre se a empresa ainda está ativa. *(Confirmado
nesta pesquisa: ativa; Paul = Paul Etscheit; ver `herodotus_bankai_REFERENCES.md` e `bankai_research_paper.pdf`.)*

---

## Status atual do projeto

A arquitetura trustless **ainda NÃO foi totalmente implementada**. A implementação atual usa um
**backend tradicional** (confiável) para comunicação cross-chain:

```
Chain A → Backend (confiável) → Chain B
```

### Por que o foco mudou
O time priorizou **DeFi** e um protocolo de **Prime Brokerage**. Em vez de construir a infraestrutura
trustless complexa de imediato, decidiram: (1) construir um produto funcional; (2) ganhar usuários;
(3) aumentar TVL; (4) com tração suficiente, substituir o backend confiável pela arquitetura trustless
baseada em ZK. O sistema trustless continua planejado — será "encaixado" (patched into) no protocolo depois.

### Prime Brokerage protocol
Projeto atual: arquitetura baseada em intents; fluxo cross-chain; hoje via backends comuns; migração
futura para Storage Proofs + Consensus Proofs + ZK. A camada de segurança cross-chain é vista como uma
melhoria de estágio posterior, não requisito imediato. *(Whitepaper: `05_Herodotus_DALOC_Whitepaper.pdf`.)*

### Arquitetura futura esperada
```
Chain A → Consensus Proof + Storage Proof → Zero-Knowledge Proof → Chain B   (sem backend confiável)
```

---

## Respostas às perguntas do Arthur

**P: Têm algum paper sobre storage proofs com ZK?**
R: Não. Recomendação: estudar a documentação e o GitHub da Herodotus, e possivelmente a documentação
da Bankai para consensus proving.

**P: Vocês terminaram o projeto?**
R: Não completamente. O Prime Brokerage protocol está sendo construído e já funciona hoje. Porém,
comunicação cross-chain trustless, verificação ZK, storage proofs e consensus proofs ainda não foram
integrados — estão planejados para um estágio futuro, após o protocolo ganhar tração e TVL.

---

## Papers sugeridos para leitura (já nesta biblioteca)

- zkBridge: Trustless Cross-chain Bridges Made Practical → `01_zkBridge_2210.00264.pdf`
- Historical and Multichain Storage Proofs → `03_Historical_Multichain_Storage_Proofs_2411.00193.pdf`
- Zendoo: a zk-SNARK Verifiable Cross-Chain Transfer Protocol → `06_Zendoo_2002.01847.pdf`
- Ethereum Yellow Paper (State Trie) → `00_Ethereum_Yellow_Paper.pdf`
- EIP-1186 (`eth_getProof`) → `02_EIP-1186_eth_getProof.md`
- Documentação da Herodotus → `04a_*.md`, `04b_*.md`, `herodotus_bankai_REFERENCES.md`

> Materiais adicionais para futuras iterações: ver `FUTURE_materials_to_explore.md`.
