So there is a big update actually regarding your side sorry for it essentially this taking little bit longer but had lot of things on my own. But, the sort like verification Of all these consensus On let's say Ethereum and, lets'a multiple storage slots verification And later you know having this in circuit then later proving it to somebody In combination like both of those So start with a complete information that essentially It happened unchanged something some facts have been changed I built Essentially sort Like update regarding this you know open VMs is like zkvm Essentially on the Developed by axiom And essentially This Is Recently developed acceleration for The AMD chips to those guys chips to those guys and I have this on my repo. And essentially the idea is that it's right now there are whole pipeline of proving, but block really exists in a chain plus multiple that block really exists on the chain plus let's say, multiple hundred of storage slots or many construct essentially. It takes around a century forty-five seconds and 40 second to settle this proof on chains with Halo 2 so it really good performance, It is like 40 seconds to settle the complete information Like I said The consensus settlement Like I said, the consensus settlement and let's say hundreds storage slots. This is 40 seconds so essentially this proof can go to other chain And be settled there like no problem with that So it seems sort of a average time Of these information going from chain To change It's forty second Actually thats pretty fast i don't know any more performant essentially solution yet Of course apart from using some let say you now proving networks maybe they can achieve something similar or faster But i dont'know maybe they can achieve something similar or faster, but I don't know. So that's the update actually recently and was working on this because we needed for financial application building The Prime Broadcreditions And sort of cross-chain settlement Of information is pretty crucial again let say so yeah This what going On an essentially it 40 seconds now, uh...it was couple hours easily like a couple strong couple of hours essentially but currently 42nds thanks to the GPU accelerations Okay so that' s The update - Let me know Like do you think if You need And stuff That do you think if needed and stuff like that? So let me know your sort of take on the position in everything. Just giving them because it's actually relevant to Stay take care Cheers!

# Atualização Bartown — Herodotus + openVM/Axiom

> Transcrição/edit da conversa com Bartown. Contexto: pipeline de prova cross-chain da Herodotus usando zkVM openVM (Axiom) com aceleração GPU AMD.

## O que mudou

Bartown montou um pipeline completo de prova que combina **duas peças**:

1. **Verificação de consenso** — provar que um block realmente existe na chain (Ethereum / rollup).
2. **Verificação de múltiplos storage slots** — provar o conteúdo de centenas de slots nesse mesmo block.

As duas são levadas para um **circuit** único e provadas juntas. O resultado é uma prova que pode ser enviada para qualquer outra chain e liquidada lá.

## Stack

| Peça | Tecnologia |
|---|---|
| zkVM | **openVM** (Axiom) |
| Proving system | **Halo 2** |
| Aceleração | GPU AMD (driver/recente) |
| Aplicação-alvo | "Prime Broadcreditions" — app financeira com settlement cross-chain |

## Performance (antes → agora)

| Métrica | Antes | Agora |
|---|---|---|
| Tempo de prova + settlement | **horas** (couple of hours) | **~40–45 segundos** |
| Conteúdo provado | — | 1 block + centenas de storage slots |

> Bartown: *"40 seconds to settle the complete information — consensus + hundreds of storage slots. This proof can go to other chain and be settled there, no problem."*

## Por que importa

- Settlement cross-chain a **~40s** é competitivo com o que redes de provadores dedicadas conseguem. Bartown diz não conhecer solução mais performante fora essas redes.
- Aceleração veio de suporte GPU AMD recém-lançado pela Axiom — antes era CPU-only e levava horas.
- Caso de uso é financeiro: settlement de informação entre chains é o gargalo de apps como a Prime Broadcreditions.

## Pontos abertos / pra discutir

- Comparar 40s da Herodotus/openVM com Broadcaster (ERC-7888) que é MPT puro — sem ZK, então tempo é "tempo de submit da tx" (não tem proving step). Trade-off: simplicidade/custo vs prova sucinta.
- Bartown pediu feedback sobre a abordagem — vale perguntar: ele está expondo isso como serviço, integrado à Herodotus, ou é projeto interno?

---

*Fonte: áudio transcrito em ~2 min, ~450 palavras. Edição: limpeza de fala + estruturação técnica.*