---
title: "Criptografia de Chave Pública — do zero, bem básico"
subtitle: "Guia de estudo pros vídeos V6 (chave pública), V7 (RSA), V8 (curvas elípticas)"
lang: pt-BR
fontsize: 11pt
geometry: margin=2.2cm
colorlinks: true
fontfamily: lmodern
monofont: "DejaVu Sans Mono"
monofontoptions: Scale=0.85
header-includes:
  - \usepackage{amsmath,amssymb,amsthm}
  - \usepackage{booktabs}
  - \usepackage{newunicodechar}
  - \newunicodechar{✓}{\ensuremath{\checkmark}}
  - \newunicodechar{✔}{\ensuremath{\checkmark}}
  - \newunicodechar{⚠}{\textbf{!}}
  - \newunicodechar{→}{\ensuremath{\rightarrow}}
  - \newunicodechar{⟷}{\ensuremath{\longleftrightarrow}}
  - \newunicodechar{≈}{\ensuremath{\approx}}
  - \newunicodechar{≤}{\ensuremath{\leq}}
  - \newunicodechar{≥}{\ensuremath{\geq}}
  - \newunicodechar{≠}{\ensuremath{\neq}}
  - \newunicodechar{∈}{\ensuremath{\in}}
  - \newunicodechar{⇒}{\ensuremath{\Rightarrow}}
  - \newunicodechar{⇔}{\ensuremath{\Leftrightarrow}}
  - \newunicodechar{ρ}{\ensuremath{\rho}}
  - \newunicodechar{φ}{\ensuremath{\varphi}}
  - \newunicodechar{λ}{\ensuremath{\lambda}}
  - \newunicodechar{₀}{\ensuremath{_{0}}}
  - \newunicodechar{₁}{\ensuremath{_{1}}}
  - \newunicodechar{₂}{\ensuremath{_{2}}}
  - \newunicodechar{₃}{\ensuremath{_{3}}}
  - \newunicodechar{₄}{\ensuremath{_{4}}}
  - \newunicodechar{₅}{\ensuremath{_{5}}}
  - \newunicodechar{₆}{\ensuremath{_{6}}}
  - \newunicodechar{₇}{\ensuremath{_{7}}}
  - \newunicodechar{₈}{\ensuremath{_{8}}}
  - \newunicodechar{₉}{\ensuremath{_{9}}}
  - \newunicodechar{⁰}{\ensuremath{^{0}}}
  - \newunicodechar{¹}{\ensuremath{^{1}}}
  - \newunicodechar{²}{\ensuremath{^{2}}}
  - \newunicodechar{³}{\ensuremath{^{3}}}
  - \newunicodechar{⁴}{\ensuremath{^{4}}}
  - \newunicodechar{⁵}{\ensuremath{^{5}}}
  - \newunicodechar{⁶}{\ensuremath{^{6}}}
  - \newunicodechar{⁷}{\ensuremath{^{7}}}
  - \newunicodechar{⁸}{\ensuremath{^{8}}}
  - \newunicodechar{⁹}{\ensuremath{^{9}}}
---

> **Como ler este guia — Estrutura de Explicabilidade Progressiva (Scaffolding) + Divisão Modular**
>
> Cada módulo deste guia é independente e segue **4 camadas** na ordem. Foi exatamente assim que o capítulo de Grupos (`Z*₇`) foi construido e validado contigo:
>
> 1.  **Visão Geral e Contextualização** — o mapa: o que é, por que existe, onde se encaixa.
> 2.  **Analogia Concreta** — tradução da abstração para algo visual/intuitivo (relógio, pista de corrida, ciclo que se repete).
> 3.  **Validação Prática com Números** — pegamos `Z*₇ = {1,2,3,4,5,6}` e calculamos passo a passo para o cérebro *ver* a regra funcionar.
> 4.  **Resumo Estruturado (Tabela/Listagem)** — consolidação escaneável para fechar o raciocínio e revisar antes da prova.
>
> Você pode ler um módulo inteiro de cima a baixo, ou pular direto para a Camada 4 para revisar. É o mesmo esqueleto em todos os capítulos densos.

Guia de estudo pros vídeos V6 (chave pública), V7 (RSA), V8 (curvas elípticas).
Linguagem simples. Exemplos com números pequenos. Lê de cima pra baixo.

---

## 0. A ideia central (leia isso primeiro)

> **Camada 1 — Visão Geral:** Este é o mapa de todo o guia. Se entenderes isto, todo o resto são detalhes.

Cripto simétrica: mesma chave pra fechar e abrir. Problema: como as duas partes combinam a chave sem se encontrar?

Chave pública resolve isso. Cada pessoa tem **duas** chaves:

- **pública** — todo mundo pode ver
- **privada** — só o dono

**Regras (decora):**

| Quero... | Uso |
|---|---|
| Mandar segredo pra Alice | cifro com a **pública da Alice**, ela abre com a **privada dela** |
| Provar que fui eu que escrevi | assino com a **minha privada**, todos verificam com a **minha pública** |

> **Camada 2 — Analogia Concreta:** Pensa em **cadeado e chave**. A chave pública é um cadeado aberto que a Alice espalha. Qualquer um tranca uma caixinha com ele. Só a chave privada dela abre. Assinar é o inverso: só você tem o carimbo, todos têm a régua para conferir.

Tudo isso funciona porque existe uma operação **fácil de fazer, difícil de desfazer**:

- multiplicar dois primos é fácil; fatorar o produto é difícil → **RSA**
- calcular `g^x mod p` é fácil; achar `x` a partir do resultado é difícil → **Diffie-Hellman, ElGamal, DSA**
- somar pontos numa curva elíptica é fácil; achar quantas vezes somou é difícil → **ECC, ECDH, ECDSA**

Isso é "função de mão única" (one-way function). **É a base de tudo.**

> **Camada 4 — Resumo:** Simétrica = 1 chave compartilhada. Assimétrica = par (pública/privada). Cifrar = pública do destinatário. Assinar = privada do autor. Segurança = problema matemático difícil.

---

# 1. Fundamentos de Teoria dos Números

> Este capítulo é dividido em módulos. O módulo **1.3 (Grupos)** é o exemplar completo do Scaffolding — os demais seguem a mesma lógica de forma mais leve.

## 1.1 Divisibilidade e primos

**Camada 1 — Visão Geral:** Vocabulário mínimo para falar de RSA e grupos.

- **`a | b` ("a divide b")** — existe inteiro `k` com `b = a·k`. *Exemplo:* `3 | 12` porque `12 = 3·4`.
- **Número primo** — inteiro `> 1` divisível só por `1` e por ele mesmo. *Exemplos:* `2, 3, 5, 7, 11, 13, ...`
- **Teorema fundamental da aritmética** — todo inteiro `> 1` se escreve de **um único jeito** como produto de primos. *Exemplo:* `360 = 2³·3²·5`.
- **mdc / gcd** — maior número que divide os dois. *Exemplo:* `gcd(12,18) = 6`. Se `gcd(a,b) = 1` → são **coprimos**.

**Camada 2 — Analogia:** Primos são os "átomos" — blocos indivisíveis. O teorema fundamental diz que toda molécula (número) tem uma decomposição atômica única.

**Camada 3 — Validação:** `gcd(12,18)`: divisores de 12 = {1,2,3,4,6,12}, de 18 = {1,2,3,6,9,18} → maior comum = 6.

**Camada 4 — Resumo:** `a|b` ⇔ `b = ak`. Primo = só 1 e ele mesmo. `gcd=1` ⇔ coprimos (condição para existir inverso).

## 1.2 Aritmética modular

**Camada 1 — Visão Geral:** Vamos fazer contas num mundo finito onde tudo dá a volta.

- **`a mod n`** — resto da divisão. *Ex:* `17 mod 5 = 2`.
- **`a ≡ b (mod n)`** — mesmo resto. *Ex:* `17 ≡ 2 (mod 5)`.
- **O que vale:** soma, subtração, multiplicação funcionam → `(a+b) mod n`. **Divisão NÃO existe direto** → multiplica-se pelo **inverso**.
- **Inverso multiplicativo** — `a⁻¹` com `a·a⁻¹ ≡ 1 (mod n)`. *Ex:* `mod 7`, `3·5 =15 ≡1` → inverso de `3` é `5`.
  > **Regra de ouro:** existe inverso de `a mod n` **<=>** `gcd(a,n)=1`.

**Camada 2 — Analogia Concreta (Relógio):** `mod 12`: `13 horas = 1 hora`. O relógio dá a volta, mas a aritmética continua. É por isso que `a+12 ≡ a`.

**Camada 3 — Validação com `Z*₇`:** Vamos testar o inverso na prática: `3·5=15`. `15 ÷7 =2 resto 1` → `15 ≡1` ✓. Logo `5` desfaz `3` em `mod 7`.

**Camada 4 — Resumo:**

| Conceito | Teste rápido |
|---|---|
| `a mod n` | resto |
| Inverso existe? | Só se `gcd(a,n)=1` |
| Divisão | `a / b = a · b⁻¹` |

## 1.3 Grupo — a estrutura que une tudo [MÓDULO EXEMPLAR COMPLETO]

> Este é o módulo onde o Scaffolding foi validado contigo. Use-o como molde para os demais.

### Camada 1 — Visão Geral e Contextualização

- **Definição:** um **grupo** é um conjunto `G` + **uma** operação `∗` com **4 axiomas**. Pensa como "um conjunto com uma calculadora própria que nunca te joga para fora".
- **Os 4 axiomas:**

  1. **Fechamento** — `a∗b` continua dentro de `G`.
  2. **Associatividade** — `(a∗b)∗c = a∗(b∗c)`.
  3. **Elemento neutro `e`** — `a∗e = a` (ex: `0` na soma, `1` na multiplicação).
  4. **Elemento inverso** — todo `a` tem `a⁻¹` com `a∗a⁻¹ = e`.

- **Grupo abeliano:** se ainda vale `a∗b = b∗a`. Em cripto usamos quase sempre abelianos.
- **Onde se encaixa:**
  - **Álgebra Abstrata** = área geral. **Teoria de Grupos** = sub-tópico. **Aritmética Modular** = grupos com `mod n`.
  - *Exemplo da apostila:* `Z*₇` é o **Grupo Multiplicativo de Inteiros Módulo 7** — **Grupo Cíclico Finito** (finito =6 elementos; cíclico =um gerador dá a volta).
  - **Escada:** **Grupo** (1 operação +4 regras) → **Anel** (2 operações) → **Corpo** (anel onde todo ≠0 tem inverso).

- **Por que importa:** DH, ElGamal, ECC são **o mesmo esquema** em grupos diferentes. Entende grupo uma vez, entende todos.

### Camada 2 — Analogia Concreta (Pista de Corrida)

- **Ordem do grupo `|G|`:** tamanho da pista — quantas posições existem.
- **Ordem de um elemento `a`:** número mínimo de passos (`a^k`) até voltar à largada (`e=1`). É o tamanho do *ciclo* que aquele elemento cria.
- **Em grupo multiplicativo:** `a^k`. Em grupo aditivo: `k·a = 0`.

### Camada 3 — Validação Prática com Números (`Z*₇ = {1,2,3,4,5,6}`, `|G|=6`)

**Ordem do `2` passo a passo:**
- `2¹ =2`, `2²=4`, `2³=8 ≡1 (mod 7)` → chegou no neutro! **ordem=3** → ciclo `2→4→1→2...`

**Teorema de Lagrange (desmistificado):** ordem de qualquer elemento **divide** `|G|`.
- Teste: `ord(2)=3` divide 6? `6÷3=2` ✔. `ord(3)=6` divide 6? Sim ✔. Nunca existirá ordem 4 em grupo de ordem 6.

**Consequência:** `a^|G| = e` sempre. *Teste:* `2⁶=(2³)²=1²=1` ✔

**Grupo cíclico e gerador:**
- Definição: existe `g` tal que `G = { g¹, g², ..., g^|G|=e }`.
- **Prova que `3` é gerador:** `3¹=3`, `3²=9≡2`, `3³=6`, `3⁴=18≡4`, `3⁵=12≡5`, `3⁶=15≡1` → gerou todos → **Sim, ordem 6**.
- **Contra-exemplo `2`:** `2,4,1,2...` só 3 elementos → **Não é gerador** (ordem 3≠6).

### Camada 4 — Resumo Estruturado (Tabela que você pediu)

| Elemento `a` | Potências até `1` | Ordem `ord(a)` | É gerador? | Comentário |
|---|---|---|---|---|
| `1` | `1` | **1** | Não | Neutro sempre 1 |
| `2` | `2,4,1` | **3** | Não | Ciclo curto |
| `3` | `3,2,6,4,5,1` | **6** | **Sim** | Gera tudo |
| `4` | `4,2,1` | **3** | Não | Mesmo ciclo do `2` |
| `5` | `5,4,6,2,3,1` | **6** | **Sim** | Outro gerador! |
| `6` | `6,1` | **2** | Não | `6≡-1` sempre ordem 2 |

*Repara:* todas as ordens (1,2,3,6) **dividem** 6 — **Lagrange conferido!** Número de geradores = `φ(|G|)` → `φ(6)=2` → `3` e `5`.

## 1.4 Os dois grupos mod N

**Camada 1 — Visão Geral:**
- **`Z_N` (aditivo)** = `{0,...,N-1}` com soma `mod N`. Sempre grupo, cíclico (gerador 1), tamanho `N`.
- **`Z*_N` (multiplicativo)** = `{1,...,N-1}` coprimos com `N` com multiplicação `mod N`. Só coprimos têm inverso.

**Camada 2 — Analogia:** `Z_N` é o relógio com N horas. `Z*_N` é só os ponteiros que conseguem voltar atrás (têm inverso).

**Camada 3 — Validação (`Z*₇` vs `Z*₁₀`):**
- `Z*₇={1,2,3,4,5,6}` →6 elementos (primo, todos entram)
- `Z*₁₀={1,3,7,9}` →4 elementos (2,4,5,6,8 compartilham fator com 10 e não têm inverso)

**Camada 4 — Resumo:** `Z*_p` com `p` primo é **sempre cíclico** → base do Diffie-Hellman.

## 1.5 Função phi de Euler

**Camada 1 — Visão Geral:** `φ(N)` = quantos números `1..N` são coprimos com `N` = **tamanho de `Z*_N`**.

| Caso | Fórmula | Exemplo |
|---|---|---|
| `p` primo | `φ(p)=p-1` | `φ(7)=6` |
| `p,q` distintos | `φ(pq)=(p-1)(q-1)` | `φ(15)=8` |
| `p^k` | `φ(p^k)=p^k-p^(k-1)` | `φ(8)=4` |

**Camada 2 — Analogia:** `φ(N)` conta quantos participantes *podem* ter inverso na festa.

**Camada 3 — Validação (coração do RSA):** Quem sabe `p,q` calcula `φ(N)` em 1 multiplicação. Quem só tem `N` precisa fatorar — inviável se `N` grande.

**Camada 4 — Resumo:** Segunda linha `(p-1)(q-1)` é a porta dos fundos do RSA.

## 1.6 Euler e Fermat

**Camada 1 — Visão Geral:** Teoremas que permitem "reduzir expoentes".
- **Euler:** se `gcd(a,N)=1` → `a^φ(N) ≡1 (mod N)`.
- **Fermat (caso primo):** `a^(p-1) ≡1 (mod p)`.

**Camada 2 — Analogia:** São atalhos — como saber que dar 100 voltas na pista de 6 posições é igual a dar 4.

**Camada 3 — Validação:** `3^100 mod7`: `φ(7)=6`, `100 mod6=4` → `3⁴=81≡4`. Sem teorema faríamos 100 multiplicações.

**Camada 4 — Resumo:** Permitem RSA desfazer a cifragem: `m^(ed) ≡ m`.

## 1.7 Teorema Chinês do Resto (CRT) — opcional

**Camada 1 — Visão Geral:** Se `n₁,n₂` coprimos, `x≡a₁ (mod n₁)` e `x≡a₂ (mod n₂)` tem solução única `mod n₁n₂`.

**Camada 2 — Analogia:** É como descobrir a hora exata sabendo a hora em dois relógios diferentes.

**Camada 3 — Validação (uso RSA):** Em vez de calcular `mod N=pq` (2048 bits), calcula `mod p` e `mod q` (1024 bits cada) e recombina → **~4× mais rápido**.

**Camada 4 — Resumo:** Rápido, mas se não checar o resultado, sofre *fault attack*. Por isso implementações sérias verificam.

---

# 2. Teoria dos Números Algorítmica

> **Scaffolding deste capítulo:** Cada algoritmo segue Visão Geral → Analogia → Conta na mão com números pequenos → Tabela de custo.

## 2.1 Euclides (gcd)

**Camada 1 — Visão Geral:** `gcd(a,b)=gcd(b, a mod b)` até resto 0. `~log(n)` passos.

**Camada 3 — Validação:**
```
gcd(252,198)
252=1·198+54
198=3·54+36
 54=1·36+18
 36=2·18+0 → gcd=18
```

**Camada 4 — Resumo:** Rápido, base de tudo.

## 2.2 Euclides Estendido → inverso

**Camada 1 — Visão Geral:** Além do gcd, acha `x,y` com `a·x+b·y=gcd`. Se `gcd(a,N)=1`, então `a·x≡1` → `x` é o inverso.

**Camada 2 — Analogia:** É a "receita" para desfazer a divisão.

**Camada 3 — Validação:** É assim que RSA calcula `d = e⁻¹ mod φ(N)`. Único jeito prático.

**Camada 4 — Resumo:** Sem estendido, não há RSA.

## 2.3 Exponenciação modular (square-and-multiply)

**Camada 1 — Visão Geral:** Calcular `a^b mod n` sem `b` multiplicações. Escreve `b` em binário: quadrado + multiplica se bit=1.

**Camada 3 — Validação (`3^13 mod7`, `13=1101₂`):**
```
bit1 →1²·3=3
bit1 →3²·3=27≡6
bit0 →6²=36≡1
bit1 →1²·3=3 → resposta 3
```
**Custo:** `~log₂(b)` → 2048 passos em vez de `2^2048`. Torna RSA possível.

**Camada 2/4 — Analogia e Alerta:** Versão ingênua vaza bits por tempo → usa Montgomery ladder (tempo constante).

## 2.4 Teste de primalidade

**Camada 1 — Visão Geral:** Precisamos gerar primos de 1024+ bits. Testes probabilísticos.
- **Fermat:** `a^(n-1)≡1?` Se falhar → composto. Se passar → provavelmente primo. Fraco (Carmichael 561...).
- **Miller–Rabin (usado):** escreve `n-1=2^s·d`. Testa `a^d≡1` ou `a^(2^r·d)≡-1`. Cada rodada erro ≤1/4 → 40 rodadas erro < falha de hardware.

**Camada 3 — Validação (receita):** 1. sorteia ímpar com bit topo 1 →2. divide por primos pequenos →3. Miller-Rabin k vezes →4. falhou volta. Pelo Teorema dos Primos, ~1 em 710 tentativas para 1024 bits.

## 2.5 Ataques — fatoração

**Camada 4 — Resumo Estruturado:**

| Algoritmo | Quando funciona | Custo |
|---|---|---|
| Divisão de teste | fatores pequenos | `O(√N)` |
| **Pollard p−1** | `p-1` só fatores pequenos | rápido |
| **Pollard rho** | genérico | `O(N^(1/4))` |
| **Crivo quadrático** | N até ~100 dígitos | subexp. |
| **NFS** | melhor hoje | subexp. |

*Implicação:* escolha `p,q` grandes, aleatórios, tamanho parecido, `p-1` não-smooth.

## 2.6 Ataques — log discreto (DL)

**Camada 1 — Visão Geral:** Achar `x` em `g^x=h`.

| Algoritmo | Custo | Obs |
|---|---|---|
| Força bruta | `O(n)` | |
| **Baby-step giant-step** | `O(√n)` tempo e memória | troca |
| **Pollard rho** | `O(√n)` tempo, memória ~0 | usado na prática |
| **Pohlig–Hellman** | quebra por fator primo de `n` | **por isso ordem precisa fator primo grande** |
| **Index calculus** | subexp. | **só em `Z*_p`, NÃO em curvas** |

> **Camada 4 — Resumo:** Última linha explica "por que ECC usa chaves menores".

## 2.7 Tamanhos de chave recomendados

**Camada 4 — Resumo:**

| Segurança | Simétrico | RSA/DH (`Z*_p`) | ECC |
|---|---|---|---|
| 112 bits | 112 | 2048 | 224 |
| **128 bits (hoje)** | 128 | 3072 | 256 |
| 256 bits | 256 | 15360 | 512 |

RSA cresce muito (NFS subexp.), ECC cresce linear (2× segurança) — só ataque genérico `O(√n)`.

---

# 3. Hipóteses de Dificuldade (hardness assumptions)

**Camada 1 — Visão Geral:** Nada é provado seguro. Tudo assume "este problema é difícil".

- **Fatoração:** dado `N=pq`, achar `p,q` é inviável.
- **RSA:** dado `N,e,y=x^e`, achar `x` é inviável (mais forte que fatoração).
- **DL:** dado `h=g^x`, achar `x` é inviável.
- **CDH:** dados `g^a,g^b`, calcular `g^(ab)`.
- **DDH:** dados `g^a,g^b,g^c`, decidir se `c=ab` ou aleatório. **Mais forte que CDH.**

**Relação:** `DDH difícil ⇒ CDH difícil ⇒ DL difícil`.

**Camada 2 — Analogia:** Quebrar DL quebra tudo; DDH é a hipótese mais exigente (exige indistinguibilidade).

**Camada 3 — Validação:** **Cuidado:** DDH é **falsa** em `Z*_p` inteiro (Legendre vaza 1 bit). Solução: subgrupo de ordem prima `q` (`p=2q+1`, primo seguro, resíduos quadráticos). Mata Pohlig-Hellman.

**Camada 4 — Resumo:** Curvas elípticas: mesmo jogo, outro grupo. Sem index calculus → chaves ~12× menores.

---

# 4. Troca de Chaves

## 4.1 O problema da distribuição de chaves

**Camada 1 — Visão Geral:** Com só simétrica, `n` pessoas precisam `n(n-1)/2` chaves. 1000 pessoas =500 mil chaves. Inviável. Motivação histórica da chave pública (1976).

## 4.2 Diffie–Hellman (DHKE)

**Camada 1 — Visão Geral:** Público: primo `p`, gerador `g`.

```
Alice                              Bob
a aleatório                        b aleatório
A = g^a mod p   ──── A ────▶
                ◀─── B ────        B = g^b mod p
s = B^a = g^(ab)                   s = A^b = g^(ab)
```

**Camada 2 — Analogia (Mistura de tintas):** Alice e Bob têm uma cor pública `g`. Cada um mistura sua cor secreta (`a`/`b`) e troca o resultado. O espião vê as misturas, mas não consegue desfazer a mistura.

**Camada 3 — Validação (`p=23,g=5`):** `a=6→A=8`, `b=15→B=19`, `s=19⁶≡2` e `8¹⁵≡2` ✓. Espião vê `p,g,A,B` e precisaria resolver CDH. Na prática `s` passa por KDF antes de virar AES.

**Camada 4 — Resumo:** Sem KDF, sem autenticação.

## 4.3 Man-in-the-middle

**Camada 1 — Visão Geral:** DH puro **não autentica**.

```
Alice ──A──▶ Mallory ──M──▶ Bob
Alice ◀─M─── Mallory ◀──B── Bob
```

**Camada 2 — Analogia:** Mallory faz duas trocas separadas e fica no meio lendo tudo.

**Camada 3 — Validação:** Com `M` diferentes, ambos acham que estão seguros mas não estão.

**Camada 4 — Resumo:** **Conserto:** autenticar DH com assinatura + certificado (§6) — é o TLS.

---

# 5. Cifragem de Chave Pública

## 5.1 Sintaxe e segurança

**Camada 1 — Visão Geral:** `Gen()→(pk,sk)`, `Enc(pk,m)→c`, `Dec(sk,c)→m`.

- **CPA:** adversário escolhe `m₀,m₁`, recebe cifra de um, não adivinha. **Exige aleatorização** — determinístico nunca é CPA-seguro.
- **CCA:** adversário ainda pode pedir decifragens (menos a alvo). Exige não-maleabilidade. É o que se exige na prática.

## 5.2 Cifragem híbrida / KEM-DEM

**Camada 1 — Visão Geral:** Chave pública é lenta e só cifra pouco. Então:
1. **KEM:** transporta chave simétrica `k` aleatória com chave pública
2. **DEM:** cifra mensagem com `k` via AES-GCM → `c=(Enc_pk(k), AES_k(m))`

**Camada 4 — Resumo:** Todo sistema real é híbrido (TLS, PGP, Signal). Segurança = elo mais fraco.

## 5.3 ElGamal (baseado em DDH)

**Camada 1 — Visão Geral:** DH transformado em cifra.
- Chaves: `sk=x`, `pk=h=g^x`
- Cifrar `m`: sorteia `r`, `c=(g^r, m·h^r)`
- Decifrar `(c₁,c₂)`: `m=c₂/c₁^x`

**Camada 3 — Validação:** `c₁^x = g^(rx)=h^r` → cancela.

**Camada 4 — Resumo:**

| Propriedade | Valor |
|---|---|
| Aleatorizado? | Sim → CPA-seguro sob DDH ✔ |
| Expansão | 2× |
| Maleável? | Sim → **NÃO CCA-seguro** (útil em voto eletrônico) |
| Reuso de `r`? | **Nunca** |

*Versão moderna (KEM):* manda só `c₁=g^r`, `k=KDF(h^r)` → ECIES/HPKE.

## 5.4 RSA cru ("textbook")

**Camada 1 — Visão Geral:**
- **Gen:** `p,q`, `N=pq`, `φ=(p-1)(q-1)`, `e=65537`, `d=e⁻¹ mod φ`, `pk=(N,e)`, `sk=d`.
- **Enc:** `c=m^e mod N`, **Dec:** `m=c^d mod N`.

**Camada 2 — Analogia:** Fechar cadeado = elevar a `e`, abrir = elevar a `d`. Só quem sabe `φ` (quem fatorou) sabe `d`.

**Camada 3 — Validação (miniatura `p=3,q=11,N=33,φ=20,e=3,d=7,m=4`):** `c=4³=64≡31`, `31⁷ mod33=4` ✓. Por quê? `ed=1+kφ` → `m^(1+kφ)=m·(m^φ)^k≡m`.

**Camada 4 — Resumo (por que é INSEGURO sem padding):**
1. determinístico → não CPA-seguro
2. maleável → `c·s^e` decifra `m·s`
3. `m` pequeno sem redução → raiz e-ésima
4. broadcast com mesmo `m` → Håstad
> **Nunca use RSA sem padding.**

## 5.5 Padding — PKCS #1 v1.5

**Camada 1 — Visão Geral:** `EM=0x00||0x02||PS||0x00||m` → adiciona aleatoriedade.

**Camada 3 — Validação (ataque):** **Bleichenbacher (1998):** oráculo de 1 bit (padding válido/inválido) decifra com ~1M consultas. Voltou como ROBOT em 2017.

**Camada 4 — Resumo:** Legado para cifragem, evitar.

## 5.6 OAEP (PKCS #1 v2)

**Camada 1 — Visão Geral:** Padding Feistel com hashes/máscaras, CCA-seguro no ROM, erro único em tempo constante.

**Camada 4 — Resumo:** **Use ECDH/HPKE ou RSA-OAEP. Nunca cru, nunca v1.5.**

---

# 6. Assinaturas Digitais

## 6.1 Sintaxe e segurança

**Camada 1 — Visão Geral:** `Gen`, `Sign(sk,m)→σ`, `Verify(pk,m,σ)→0/1`. **Assina com privada, verifica com pública.**

- **EUF-CMA:** mesmo vendo assinaturas escolhidas, não forja nova.
- Dá **autenticidade, integridade, não-repúdio** (MAC não dá a terceira).

## 6.2 Hash-and-sign

**Camada 1 — Visão Geral:** Assina `σ=Sign(sk, H(m))` — mais rápido.

**Camada 3 — Validação:** Precisa `H` **resistente a colisão**: se `H(m)=H(m')`, uma assinatura vale pra duas → adeus MD5/SHA-1 (Flame, SHAttered). Use SHA-256+.

## 6.3 Assinaturas RSA

**Camada 1 — Visão Geral:**
- **Cru:** `σ=m^d` → quebrado (forja trivial, multiplicativo).
- **FDH:** `σ=H(m)^d` → EUF-CMA no ROM.
- **v1.5:** `EM=0x00||0x01||FF..||00||DigestInfo||H(m)` → onipresente, mas verificadores relaxados sofrem Bleichenbacher `e=3` (raiz cúbica).

**Camada 4 — Resumo:** Hoje: **Ed25519** ou **ECDSA P-256**; RSA-PSS se precisar RSA.

## 6.4 DSA e ECDSA

**Camada 1 — Visão Geral:** Trabalham em subgrupo ordem prima `q`. Assinatura = `(r,s)`.

**ECDSA — assinar `m` com privada `d`, gerador `G` ordem `n`:**
1. `e=H(m)`, 2. sorteia `k∈[1,n-1]`, 3. `R=kG`, `r=R.x mod n`, 4. `s=k⁻¹(e+r·d) mod n`, 5. `(r,s)` → Verificar: `u₁=e·s⁻¹`, `u₂=r·s⁻¹`, `P=u₁G+u₂Q`, válido se `P.x≡r`.

**Camada 2 — Analogia (A parte mortal):** `k` é como o **papel carbono** — se reutilizar, a mensagem secreta vaza.

**Camada 3 — Validação (desastre real):** `k` repetido → `s₁−s₂=k⁻¹(e₁−e₂)` → `k=(e₁−e₂)/(s₁−s₂)`, `d=(s₁k−e₁)/r` → **PS3 (2010)** e carteiras Bitcoin Android (2013) quebrados. `k` enviesado → lattice attack.

**Camada 4 — Resumo:** **Conserto:** RFC 6979 (`k` determinístico via HMAC) ou **Ed25519** (já determinístico). ECDSA é maleável `(r,−s)` → exige `s` low (Bitcoin).

## 6.5 Certificados e PKI

**Camada 1 — Visão Geral:** Como sei que `pk` é da Alice? **Certificado** = declaração assinada por CA.

```
Raiz (auto-assinada, no SO)
 └── CA intermediária
       └── certificado do site
```

**Camada 3 — Validação:** Conteúdo X.509, revogação (CRL, OCSP, stapling, validade curta 90d), fraqueza DigiNotar 2011 → Certificate Transparency.

**Camada 4 — Resumo:** Cadeia de confiança — só confia em poucas raízes.

---

# 7. Curvas Elípticas (V8)

## 7.1 O que é

**Camada 1 — Visão Geral:** Sobre `F_p`, `y²=x³+ax+b (mod p)`, `4a³+27b²≠0`. Pontos `(x,y)` + `O` formam **grupo**.

## 7.2 A lei de grupo

**Camada 1 — Visão Geral:**
- Identidade `O`, inverso `−P=(x,−y)`, `P+Q` = reta por `P,Q` corta curva em terceiro ponto, reflete no eixo x, `P+P` = tangente.

**Camada 2 — Analogia:** É como jogar bilhar numa mesa curva — a bola quica e volta.

**Camada 3 — Validação (fórmulas):** `P≠Q: λ=(y₂−y₁)/(x₂−x₁)`, `P=Q: λ=(3x₁²+a)/(2y₁)`, `x₃=λ²−x₁−x₂`, `y₃=λ(x₁−x₃)−y₁` (divisão = inverso mod p). `kP` = double-and-add.

**Camada 4 — Resumo:** Dicionário: `g^x ⟷ xP`. Mesmo grupo abstrato.

## 7.3 ECDLP

**Camada 1 — Visão Geral:** Dado `Q=kP`, achar `k` é fácil calcular, inviável voltar. **Sem index calculus** → só `O(√n)` (Pollard rho).

**Camada 4 — Resumo:** 256 bits curva ≈128 bits segurança ≈ RSA 3072 → chaves menores, mais rápido. Evitar ordens com fatores pequenos, curvas anômalas/supersingulares → use P-256, secp256k1, Curve25519.

## 7.4 Parâmetros de domínio

`(p,a,b,G,n,h)` — corpo, coeficientes, gerador, ordem prima `n`, cofator `h=#E/n`. `d∈[1,n-1]`, `Q=dG`.

## 7.5 ECDH

**Camada 1 — Visão Geral:** Idêntico ao DH com escalares:
```
Alice: d_A, Q_A=d_A·G ──Q_A──▶
                          ◀─Q_B──  Bob: d_B, Q_B=d_B·G
segredo=d_A·Q_B = d_A·d_B·G
```

**Camada 3 — Validação:** Usa só `x` + KDF. **ECDHE** (efêmero) → **forward secrecy** (TLS 1.3, X25519).

## 7.6 ECDSA

Já em §6.4. **Regra de ouro:** `k` único ou chave vaza.

---

# 8. Aprofundamentos (contas na mão)

> Cada aprofundamento segue o mesmo Scaffolding — agora é você fazendo a conta.

## 8.1 Teorema Chinês do Resto — exemplo completo

**Camada 1 — Visão Geral:** Achar `x` com `x≡2(3), x≡3(5), x≡2(7)`. `N=105`.

| i | `n_i` | `a_i` | `N_i=N/n_i` | `y_i=N_i⁻¹ mod n_i` | `a_i·N_i·y_i` |
|---|---|---|---|---|---|
|1|3|2|35|`35≡2→2⁻¹=2`|`2·35·2=140`|
|2|5|3|21|`21≡1→1`|`3·21·1=63`|
|3|7|2|15|`15≡1→1`|`2·15·1=30`|

**Camada 3 — Validação:** `x=233≡23`, confere `23=3·7+2` ✓ etc.

**Camada 2/4 — Analogia e Resumo Estrutural:** Cada termo "acende" só sua congruência (base canônica, vetor unitário). `Z_105 ≅ Z_3×Z_5×Z_7`.

## 8.2 RSA-CRT — como a decifragem fica 4× mais rápida

**Camada 1 — Visão Geral:** Custo cúbico → duas contas 1024 bits custam `2·(1/2)³=1/4`.

**Pré-computado:** `d_p=d mod(p-1)`, `d_q=d mod(q-1)`, `q_inv=q⁻¹ mod p`.

**Camada 3 — Validação (`p=3,q=11,N=33,e=3,d=7,c=31`):**
```
d_p=1, d_q=7, q_inv=2
m₁=31¹ mod3=1, m₂=9⁷ mod11=4, h=2·(1−4)≡0, m=4+0·11=4 ✓
```

**Camada 4 — Alerta (Bellcore):** Um erro em `m₁` → `gcd(σ'^e−m,N)=q` → **verifique `σ^e≟m` antes de devolver**.

## 8.3 Soma de pontos em curva elíptica — contas de verdade

**Curva `E: y²=x³+2x+2` sobre `F₁₇`, `P=(5,1)`** (confere: `137≡1`, `1²=1` ✓)

**Camada 3 — Validação:**
- **Dobrar `2P` (tangente):** `λ=(3·25+2)/(2)=77/2≡9·9=13`, `x₃=169−10≡6`, `y₃=13·(5−6)−1≡3` → `2P=(6,3)` ✓
- **Somar `3P=2P+P` (secante):** `λ=(3−1)/(6−5)=2`, `x₃=4−5−6≡10`, `y₃=2·(5−10)−1≡6` → `(10,6)` ✓ → grupo tem 19 pontos (ordem prima).

**Camada 4 — Resumo:** Toda divisão virou inverso modular (caro → coordenadas projetivas). `P+(−P)=O` (vertical). Double-and-add vaza por timing → Montgomery ladder.

## 8.4 Baby-step Giant-step (BSGS)

**Camada 1 — Visão Geral:** Resolver `g^x=h` sem força bruta. Truque: `x=i·m+j`, `m=⌈√n⌉`, `g^j = h·(g^(−m))^i`.

**Camada 3 — Validação (`5^x≡7 mod23, n=22,m=5`):**
Baby steps `5^j`: 1,5,2,10,4; `c=20⁻¹≡15`; Giant steps: `7→13→11→4` (achou `j=4` em `i=3`) → `x=3·5+4=19` ✓.
Custo `O(√n)` tempo **e** memória → `2¹²⁸` para 256 bits → inviável.

**Camada 4 — Resumo:** Raise de baseline — grupos <2¹⁶⁰ são quebráveis.

## 8.5 Pollard rho

**Camada 1 — Visão Geral:** Mesmo tempo `O(√n)` mas **memória O(1)** — ataque prático contra ECDLP.

**Camada 2 — Analogia (Aniversário):** Passeio pseudoaleatório `g^a·h^b` particionado em 3 regiões; após `~1.25√n` entra em ciclo (formato ρ).

**Camada 3 — Validação:** Detecção Floyd (2 ponteiros), extração `a₁+xb₁≡a₂+xb₂` → `x=(a₁−a₂)/(b₂−b₁)`.

**Camada 4 — Resumo:** Paralelizável (Van Oorschot–Wiener), melhor ataque contra ECDLP → `n` bits ⇒ `n/2` segurança → `256→128`.

---

# 9. Exercícios (com respostas)

Faça no papel antes de olhar. Respostas logo abaixo de cada bloco.

## Bloco A — números e grupos

1. Calcule `gcd(1071, 462)` por Euclides.
2. Ache `17⁻¹ mod 43` (Euclides estendido).
3. Quanto vale `φ(100)`? E `φ(143)`?
4. Calcule `7^222 mod 11` usando Fermat.
5. `Z*₁₅` tem quantos elementos? Liste-os. É cíclico?
6. Em `Z*₁₁`, qual a ordem do elemento `3`? Ele é gerador?

<details><summary><b>Respostas A</b></summary>

1. `1071=2·462+147`; `462=3·147+21`; `147=7·21+0` → **21**.
2. `43=2·17+9`; `17=1·9+8`; `9=1·8+1`. Voltando → `−5·17≡1` → **`17⁻¹=38`**.
3. `100=2²·5²→40`, `143=11·13→120`.
4. `φ(11)=10`, `222 mod10=2` → `49≡5`.
5. `φ(15)=8`: `{1,2,4,7,8,11,13,14}`. **Não cíclico** — ordem ≤4 (`Z*₁₅≅Z₂×Z₄`).
6. `3¹=3,3²=9,3³=5,3⁴=4,3⁵=1` → **ordem 5** ≠10 → **não é gerador**.

</details>

## Bloco B — RSA

7. `p=5,q=11,e=3`. Ache `N,φ(N),d`.
8. Com essa chave, cifre `m=9` e decifre.
9. Alice publica `N=3233,e=17` com `p=61,q=53`. Qual é `d`?
10. Por que `e=65537` e não `e=3`?
11. Mostre a maleabilidade: dado `c=m^e`, como produzir cifra de `2m`?

<details><summary><b>Respostas B</b></summary>

7. `N=55,φ=40,d=27`.
8. `c=14`, `14^27 mod55=9` ✓ (detalhes no guia)
9. `φ=3120,d=2753`.
10. `e=3` frágil (sem redução, Håstad precisa 3 destinatários). `65537=2¹⁶+1` tem 2 bits 1 (17 quadrados +1 mult) e é grande o bastante.
11. `c'=c·2^e mod N` → `Dec(c')=2m` → não CCA-seguro.

</details>

## Bloco C — DH, ElGamal, assinaturas

12. `p=23,g=5,a=4,b=3`. Qual segredo comum?
13. O que Eve vê? Por que não consegue?
14. Em ElGamal, reuso de `r` com `m₁,m₂` e Eve conhece `m₁`?
15. Duas assinaturas ECDSA `(r,s₁),(r,s₂)` mesmo `r`! Derive `k` e `d`.
16. Por que assinar `H(m)` exige resistência a colisão, não só unidirecional?

<details><summary><b>Respostas C</b></summary>

12. `A=4,B=10,s=18` ✓
13. Vê `p,g,A,B`. Precisaria DL ou CDH — com 3072 bits não.
14. `c₂=m·h^r` → `m₂=m₁·c₂⁽²⁾/c₂⁽¹⁾` → **nonce reusado = mensagem vazada**.
15. `k=(e₁−e₂)/(s₁−s₂)`, `d=(s₁k−e₁)/r` → PS3/Android.
16. Unidirecional não basta: forjador acha `H(m)=H(m')`, te faz assinar `m`, vale pra `m'` → precisa colisão (MD5, SHA-1 quebrados).

</details>

## Bloco D — conceitual (uma frase)

17. Por que `φ(pq)=(p-1)(q-1)` é a porta dos fundos do RSA?
18. Diferença prática CPA vs CCA — cenário real?
19. Por que DDH é falsa em `Z*_p` e como o padrão conserta?
20. Por que ECC 256 bits ≈ RSA 3072 bits?

<details><summary><b>Respostas D</b></summary>

17. Quem sabe `p,q` calcula `φ` e `d`; quem só tem `N` precisa fatorar. Conhecer `φ(N)` ⇔ fatorar `N`.
18. CPA = passivo; CCA = manda cifras e observa. Cenário: servidor responde "padding inválido" → Bleichenbacher decifra. CPA não cobre, CCA sim.
19. Legendre vaza 1 bit. Conserto: subgrupo ordem prima `q` (`p=2q+1`).
20. `Z*_p` tem index calculus subexp. → `p` enorme; curvas só Pollard rho `O(√n)` → `n/2` segurança.

</details>

---

# 10. Colinhas finais

## Quem resolve o quê

| Esquema | Grupo | Hipótese | Serve pra |
|---|---|---|---|
| RSA | `Z*_N` | fatoração / RSA | cifrar + assinar |
| DH / ECDH | `Z*_p` / curva | CDH / DDH | trocar chave |
| ElGamal | `Z*_p` / curva | DDH | cifrar |
| DSA / ECDSA | subgrupo ordem `q` / curva | DL | assinar |

## Erros clássicos (todos já derrubaram sistemas reais)

1. RSA sem padding
2. Reusar nonce `k` no (EC)DSA
3. DH sem autenticação → MITM
4. Confundir cifragem com assinatura
5. RNG fraco
6. Verificar padding por parsing
7. Comparação não constante → side-channel

## O que usar hoje

- **Troca de chave**: X25519 (ECDHE)
- **Assinatura**: Ed25519, ou ECDSA P-256
- **Cifragem pública**: HPKE / ECIES; RSA-OAEP se obrigado
- **Hash**: SHA-256 ou SHA-3
- **Simétrico**: AES-256-GCM ou ChaCha20-Poly1305

## Para responder em aula, saiba dizer em uma frase

- por que `φ(pq)=(p-1)(q-1)` é o segredo do RSA
- por que RSA cru não é CPA-seguro
- por que DH sofre MITM
- por que ECC usa chaves menores (sem index calculus)
- por que reusar `k` vaza a chave
- diferença CPA×CCA, CDH×DDH, MAC×assinatura

---

## Referências

- Menezes, van Oorschot, Vanstone — *Handbook of Applied Cryptography* — cap. 2,3,4,8,11
- Katz & Lindell — *Introduction to Modern Cryptography* — CPA/CCA/EUF-CMA
- Hoffstein, Pipher, Silverman — *An Introduction to Mathematical Cryptography* — curvas
- Nigel Smart — *Cryptography Made Simple*

