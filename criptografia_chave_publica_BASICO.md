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

Guia de estudo pros vídeos V6 (chave pública), V7 (RSA), V8 (curvas elípticas).
Linguagem simples. Exemplos com números pequenos. Lê de cima pra baixo.

---

## 0. A ideia central (leia isso primeiro)

Cripto simétrica: mesma chave pra fechar e abrir. Problema: como as duas partes
combinam a chave sem se encontrar?

Chave pública resolve isso. Cada pessoa tem **duas** chaves:

- **pública** — todo mundo pode ver
- **privada** — só o dono

Regras:

| Quero... | Uso |
|---|---|
| Mandar segredo pra Alice | cifro com a **pública da Alice**, ela abre com a **privada dela** |
| Provar que fui eu que escrevi | assino com a **minha privada**, todos verificam com a **minha pública** |

Tudo isso funciona porque existe uma operação **fácil de fazer, difícil de desfazer**:

- multiplicar dois primos é fácil; fatorar o produto é difícil → **RSA**
- calcular `g^x mod p` é fácil; achar `x` a partir do resultado é difícil → **Diffie-Hellman, ElGamal, DSA**
- somar pontos numa curva elíptica é fácil; achar quantas vezes somou é difícil → **ECC, ECDH, ECDSA**

Isso é "função de mão única" (one-way function). **É a base de tudo.**

---

# 1. Fundamentos de Teoria dos Números

## 1.1 Divisibilidade e primos

- **`a | b` ("a divide b")** — existe inteiro `k` com `b = a·k`.
  - *Exemplo:* `3 | 12` porque `12 = 3·4`.

- **Número primo** — inteiro `> 1` divisível só por `1` e por ele mesmo.
  - *Exemplos:* `2, 3, 5, 7, 11, 13, ...`

- **Teorema fundamental da aritmética** — todo inteiro `> 1` se escreve de **um único jeito** como produto de primos.
  - *Exemplo:* `360 = 2³·3²·5`.

- **mdc / gcd** — maior número que divide os dois ao mesmo tempo.
  - *Exemplo:* `gcd(12,18) = 6`.
  - Se `gcd(a,b) = 1` → são **coprimos** (primos entre si).

## 1.2 Aritmética modular

- **`a mod n`** — resto da divisão de `a` por `n`.
  - *Exemplo:* `17 mod 5 = 2`.

- **`a ≡ b (mod n)` ("congruente")** — `a` e `b` deixam o mesmo resto ao dividir por `n`.
  - *Exemplo:* `17 ≡ 2 (mod 5)`.

- **Intuição do relógio** — aritmética modular é como um relógio que dá a volta.
  - *Exemplo:* `mod 12`, `13 horas = 1 hora`.

- **O que continua valendo:**
  - soma, subtração e multiplicação funcionam normalmente → `(a+b) mod n`, `(a·b) mod n`
  - **divisão NÃO existe direto** → em vez de dividir, multiplica-se pelo **inverso**

- **Inverso multiplicativo** — `a⁻¹` é o número tal que `a·a⁻¹ ≡ 1 (mod n)`.
  - *Exemplo:* `mod 7`, `3·5 = 15 ≡ 1` → inverso de `3` é `5`.
  - > **Regra de ouro — decora:** existe inverso de `a mod n` **<=>** `gcd(a,n) = 1`.

## 1.3 Grupo — a estrutura que une tudo

- **Definição resumida:** um **grupo** é um conjunto `G` + **uma** operação `∗` que cumpre rigorosamente **4 axiomas**.
  - Pensa como "um conjunto com uma calculadora própria que nunca te joga para fora".

- **Os 4 axiomas — um por bullet para não confundir:**

  - **1. Fechamento** — se pegares dois elementos quaisquer de `G` e aplicares `∗`, o resultado **continua dentro** de `G`.
    - *Sem isso a operação te jogaria para fora do conjunto.*

  - **2. Associatividade** — a forma de agrupar não muda o resultado: `(a∗b)∗c = a∗(b∗c)`.

  - **3. Elemento neutro (identidade) `e`** — existe um elemento especial que não altera ninguém: `a∗e = a`.
    - *Exemplos:* `0` na adição, `1` na multiplicação.

  - **4. Elemento inverso** — para cada `a` existe um `a⁻¹` que desfaz a operação: `a∗a⁻¹ = e`.

- **Grupo abeliano (comutativo):**
  - Se além dos 4 axiomas ainda vale `a∗b = b∗a` para todo `a,b`, o grupo é **abeliano**.
  - **Em criptografia usamos quase sempre grupos abelianos.**

- **Nomenclatura — onde isso se encaixa na matemática?**
  - **Álgebra Abstrata** (ou Álgebra Moderna) é a área geral.
  - **Teoria de Grupos** é o sub-tópico exato que estuda grupos.
  - **Aritmética Modular** é o nome quando aplicamos isso a restos de divisão (`mod n`).
    - *Exemplo da apostila:* `Z*₇` é o **Grupo Multiplicativo de Inteiros Módulo 7** — um **Grupo Cíclico Finito**.
      - *Finito* porque tem poucos elementos (`6`).
      - *Cíclico* porque um gerador dá a volta e gera todo mundo.
  - **Hierarquia de estruturas (decora a escada):**
    - **Grupo:** `1` operação + `4` regras.
    - **Anel:** `2` operações (geralmente soma e multiplicação).
    - **Corpo (Field/Campo):** anel onde todo elemento (exceto `0`) tem inverso multiplicativo — onde a divisão funciona perfeitamente.

- **Por que importa para ti:**
  - Todos os esquemas abaixo (**DH, ElGamal, ECC**) são **o mesmo esquema** escrito em grupos diferentes.
  - Entende **grupo uma vez**, entende todos os protocolos.

### Ordem — Grupo vs. Elemento (a parte que mais confunde)

- **Ordem do grupo `|G|`** — quantidade total de elementos que o grupo tem.
  - *Exemplo:* `|Z*₇| = 6` porque `Z*₇ = {1,2,3,4,5,6}`.

- **Ordem de um elemento `a`** — o **menor** expoente `k > 0` necessário para que, ao aplicar a operação a si mesmo `k` vezes (`a^k`), **voltes ao elemento neutro `e`**.
  - *Intuição da pista circular:* imagina que estás a caminhar à volta de uma pista. A ordem é o número mínimo de passos até voltar exatamente à largada (`e = 1` na multiplicação).
  - *É sempre "elevado a algo"?*
    - **Em grupo multiplicativo (o da cripto, como na imagem)** → sim, é `a^k`.
    - **Em grupo aditivo** (operação é `+`) → seria `k·a = a+a+...+a = 0` até chegar no `0`.

- **Exemplo passo a passo — ordem do `2` em `Z*₇`:**
  - `2¹ = 2`
  - `2² = 4`
  - `2³ = 8 ≡ 1 (mod 7)` → **chegou no neutro!**
  - Logo, **ordem do `2` = 3**. Ele forma um ciclo curto que se repete: `2 → 4 → 1 → 2 → 4 → 1...`

- **Teorema de Lagrange — desmistificado:**
  - **Enunciado:** a ordem de **qualquer** elemento **divide** exatamente a ordem total do grupo.
  - **Teste prático com `|G| = 6`:**
    - ordem do `2` = `3` → `3` divide `6`? **Sim** (`6 ÷ 3 = 2`, resto zero) ✔
    - ordem do `3` = `6` → `6` divide `6`? **Sim** ✔
    - **Consequência:** nunca poderá existir um elemento de ordem `4` num grupo de ordem `6`, porque `4` não divide `6`.
  - **Consequência direta (fórmula que aparece na imagem): `a^|G| = e` sempre, para qualquer `a`:**
    - *Por quê?* Se `ord(a)` divide `|G|`, então `|G| = k·ord(a)` e `a^|G| = (a^ord(a))^k = e^k = e`.
    - *Teste sem fazer conta longa:*
      - `2⁶ = (2³)² = 1² = 1` ✔
      - `3⁶ = 1` ✔

### Grupo cíclico e gerador (elemento primitivo)

- **Definição:**
  - Grupo é **cíclico** se existe **pelo menos um** elemento especial `g` — o **gerador** — capaz de gerar **todos** os outros só sendo elevado sucessivamente.
  - Fórmula: `G = { g¹, g², g³, ..., g^|G| = e }`.

- **Exemplo completo que prova que `3` é gerador de `Z*₇`:**
  - `3¹ = 3`
  - `3² = 9 ≡ 2`
  - `3³ = 6`
  - `3⁴ = 18 ≡ 4`
  - `3⁵ = 12 ≡ 5`
  - `3⁶ = 15 ≡ 1` (neutro)
  - → Gerou `{1,2,3,4,5,6}` **todos**. Logo, `3` é gerador. Ordem `= 6 = |G|`.

- **Contra-exemplo — por que `2` NÃO é gerador:**
  - `2¹ = 2`, `2² = 4`, `2³ = 1`, `2⁴ = 2` ... → só gera `{2,4,1}` (ciclo de tamanho `3`).
  - Ordem `3 ≠ 6` → não gerou o grupo todo.

- **Tabela completa — ordem de TODOS os elementos de `Z*₇` (o que pediste):**

  | Elemento `a` | Potências até voltar ao `1` | Ordem `ord(a)` | É gerador? | Comentário |
  |---|---|---|---|---|
  | `1` | `1¹ = 1` | **1** | Não | Neutro sempre tem ordem `1` |
  | `2` | `2, 4, 1` | **3** | Não | Ciclo curto |
  | `3` | `3, 2, 6, 4, 5, 1` | **6** | **Sim** | Gera tudo |
  | `4` | `4, 2, 1` | **3** | Não | Mesmo ciclo do `2` (é `2²`) |
  | `5` | `5, 4, 6, 2, 3, 1` | **6** | **Sim** | Outro gerador! |
  | `6` | `6, 1` | **2** | Não | `6 ≡ -1`, sempre ordem `2` |

  - *Repara:* todas as ordens (`1,2,3,6`) **dividem** `|G| = 6` — **Lagrange conferido na prática!**
  - *Regra prática que cai em prova:* número de geradores = `φ(|G|)`. Aqui `φ(6)=2` → exatamente `3` e `5`.

## 1.4 Os dois grupos mod N

**`Z_N` (aditivo)** = `{0, 1, ..., N-1}` com **soma** mod N.
Sempre grupo, sempre cíclico (gerador = 1), tamanho `N`.

**`Z*_N` (multiplicativo)** = os elementos de `{1,...,N-1}` que são **coprimos com N**,
com **multiplicação** mod N.
Só entram os coprimos porque só eles têm inverso.

- `Z*₇ = {1,2,3,4,5,6}` → 6 elementos (7 é primo, todos entram)
- `Z*₁₀ = {1,3,7,9}` → 4 elementos (2,4,5,6,8 compartilham fator com 10)

> `Z*_p` com `p` primo é **sempre cíclico**. Isso é o que faz o Diffie-Hellman funcionar.

## 1.5 Função phi de Euler

`φ(N)` = quantos números de 1 a N são coprimos com N = **tamanho de `Z*_N`**.

Regras que você precisa:

| Caso | Fórmula | Exemplo |
|---|---|---|
| `p` primo | `φ(p) = p-1` | `φ(7)=6` |
| `p`, `q` primos distintos | `φ(pq) = (p-1)(q-1)` | `φ(15)=2·4=8` |
| `p^k` | `φ(p^k) = p^k − p^(k−1)` | `φ(8)=8-4=4` |

**A segunda linha é o coração do RSA.** Quem sabe `p` e `q` calcula `φ(N)` na hora.
Quem só tem `N` teria que fatorar — inviável se `N` é grande.

## 1.6 Euler e Fermat

**Teorema de Euler**: se `gcd(a,N)=1` então `a^φ(N) ≡ 1 (mod N)`.

**Pequeno Teorema de Fermat** (caso especial, N primo `p`):
`a^(p−1) ≡ 1 (mod p)` para `a` não múltiplo de `p`.

Uso prático: **reduzir expoentes**. `3^100 mod 7` → `100 mod 6 = 4` → `3⁴ = 81 ≡ 4 (mod 7)`.
É isso que permite RSA "desfazer" a cifragem.

## 1.7 Teorema Chinês do Resto (CRT) — opcional

Se `n₁, n₂` coprimos, o sistema
`x ≡ a₁ (mod n₁)` e `x ≡ a₂ (mod n₂)`
tem solução única mod `n₁n₂`.

Uso em RSA: em vez de calcular mod `N = pq` (números enormes), calcula-se
separado mod `p` e mod `q` (metade do tamanho) e recombina. **~4x mais rápido**
na decifragem/assinatura. Cuidado: implementação com CRT é vulnerável a
ataques de falha (fault attacks) se não checar o resultado.

---

# 2. Teoria dos Números Algorítmica

Ou: "quais contas eu consigo fazer rápido".

## 2.1 Euclides (gcd)

Ideia: `gcd(a,b) = gcd(b, a mod b)`, até o resto ser 0.

```
gcd(252, 198)
252 = 1·198 + 54
198 = 3·54  + 36
 54 = 1·36  + 18
 36 = 2·18  +  0   → gcd = 18
```
Rápido: ~log(n) passos.

## 2.2 Euclides Estendido → inverso

Além do gcd, acha `x, y` com `a·x + b·y = gcd(a,b)`.

Se `gcd(a,N)=1`: `a·x + N·y = 1` → mod N vira `a·x ≡ 1` → **`x` é o inverso de `a`**.

É assim que o RSA calcula `d` a partir de `e`. Único jeito prático.

## 2.3 Exponenciação modular (square-and-multiply)

Calcular `a^b mod n` sem fazer `b` multiplicações.

Escreve `b` em binário, e para cada bit: eleva ao quadrado; se o bit é 1,
multiplica por `a`. Reduz mod `n` a cada passo (nunca deixa crescer).

`3^13 mod 7`, `13 = 1101₂`:
```
bit 1 → 1²·3 = 3
bit 1 → 3²·3 = 27 ≡ 6
bit 0 → 6²   = 36 ≡ 1
bit 1 → 1²·3 = 3      → resposta 3
```
Custo: ~log₂(b) passos em vez de b. **2048 passos em vez de 2^2048.**
É o que torna RSA possível.

> Versão ingênua vaza os bits do expoente por tempo/consumo → *side-channel*.
> Na prática usa-se versões de tempo constante (Montgomery ladder).

## 2.4 Teste de primalidade

Precisamos gerar primos gigantes (1024+ bits). Não dá pra fatorar pra testar —
usa-se testes **probabilísticos**.

**Teste de Fermat**: escolhe `a` aleatório, testa `a^(n−1) ≡ 1 (mod n)`.
Se falhar → composto, certeza. Se passar → *provavelmente* primo.
Problema: **números de Carmichael** (561, 1105, ...) passam pra todo `a`. Fraco.

**Miller–Rabin** (o usado de verdade): escreve `n−1 = 2^s·d` com `d` ímpar.
Testa se `a^d ≡ 1` ou se algum `a^(2^r·d) ≡ −1`. Se nenhum, é composto.
- cada rodada com `a` aleatório: erro ≤ 1/4
- k rodadas: erro ≤ `4^(-k)`. Com k=40 o erro é menor que falha de hardware.

**Gerar primo de n bits:**
1. sorteia n bits aleatórios, força bit mais alto e bit mais baixo = 1 (tamanho certo + ímpar)
2. divisão de teste por primos pequenos (elimina ~80% rápido)
3. Miller–Rabin k vezes
4. falhou → volta ao passo 1

Pelo Teorema dos Números Primos, ~1 em cada `ln(2^n)` números é primo → pra 1024
bits, ~1 em 710. Poucas tentativas.

## 2.5 Ataques — fatoração

| Algoritmo | Quando funciona | Custo |
|---|---|---|
| Divisão de teste | fatores pequenos | `O(√N)` |
| **Pollard p−1** | se `p−1` só tem fatores pequenos ("smooth") | rápido nesse caso |
| **Pollard rho** | genérico, fatores médios | `O(N^(1/4))` |
| **Crivo quadrático (QS)** | N até ~100 dígitos | subexponencial |
| **Crivo de corpo numérico (NFS)** | melhor conhecido hoje | subexponencial |

→ Por isso `p` e `q` do RSA são escolhidos grandes, aleatórios, de tamanho
parecido (mas não perto demais) e com `p−1` não-smooth.

## 2.6 Ataques — log discreto (DL)

Achar `x` em `g^x = h`.

| Algoritmo | Custo | Obs |
|---|---|---|
| Força bruta | `O(n)` | n = ordem do grupo |
| **Baby-step giant-step** | `O(√n)` tempo **e memória** | troca memória por tempo |
| **Pollard rho** | `O(√n)` tempo, memória ~0 | o usado na prática |
| **Pohlig–Hellman** | quebra em cada fator primo de `n` | **por isso a ordem tem que ter um fator primo grande** |
| **Index calculus** | subexponencial | **só funciona em `Z*_p`, NÃO em curvas elípticas** |

> **Essa última linha é a resposta de "por que ECC usa chaves menores".**

## 2.7 Tamanhos de chave recomendados

| Segurança | Simétrico | RSA / DH (`Z*_p`) | ECC |
|---|---|---|---|
| 80 bits (legado) | 80 | 1024 | 160 |
| **112 bits** | 112 | 2048 | 224 |
| **128 bits (padrão hoje)** | 128 | 3072 | 256 |
| 192 bits | 192 | 7680 | 384 |
| 256 bits | 256 | 15360 | 512 |

RSA cresce muito porque o NFS é subexponencial; ECC cresce linearmente (2× a
segurança) porque só existe ataque genérico `O(√n)`.

---

# 3. Hipóteses de Dificuldade (hardness assumptions)

Nada em cripto de chave pública é *provado* seguro. Tudo se apoia em
"acreditamos que esse problema é difícil".

**Hipótese da fatoração** — dado `N = pq` com `p,q` primos grandes aleatórios,
é inviável achar `p` e `q`.

**Hipótese RSA** — dado `N`, `e` e `y = x^e mod N`, é inviável achar `x`.
(Mais forte: se você fatora, você quebra RSA. O contrário não se sabe.)

**Log discreto (DL)** — em grupo cíclico `G` de gerador `g`: dado `h = g^x`,
achar `x` é inviável.

**Diffie-Hellman computacional (CDH)** — dados `g^a` e `g^b`, calcular `g^(ab)`.

**Diffie-Hellman decisional (DDH)** — dados `g^a`, `g^b`, `g^c`, decidir se
`c = ab` ou se `c` é aleatório. **Mais forte que CDH.**

Relação: `DDH difícil => CDH difícil => DL difícil`.
(quebrar DL quebra tudo; DDH é a hipótese mais exigente)

**Cuidado:** DDH é **falsa** em `Z*_p` inteiro, porque o símbolo de Legendre
vaza 1 bit. Solução: trabalhar no **subgrupo de ordem prima `q`** dentro de
`Z*_p` (escolhe `p = 2q+1`, "primo seguro", e usa os resíduos quadráticos).
Isso também mata Pohlig–Hellman. Por isso todo padrão fala em `(p, q, g)`.

**Curvas elípticas** — mesmo jogo, outro grupo. Como não existe index calculus
lá, o melhor ataque é `O(√n)` genérico → chaves ~12× menores pra mesma segurança.

---

# 4. Troca de Chaves

## 4.1 O problema da distribuição de chaves

Com `n` pessoas e só cripto simétrica: `n(n−1)/2` chaves. 1000 pessoas = ~500 mil
chaves, cada uma entregue por canal seguro. Inviável. Essa é a **motivação
histórica** da chave pública (Diffie–Hellman, 1976).

## 4.2 Diffie–Hellman (DHKE)

Público: primo `p`, gerador `g`.

```
Alice                              Bob
a aleatório                        b aleatório
A = g^a mod p   ──── A ────▶
                ◀─── B ────        B = g^b mod p
s = B^a = g^(ab)                   s = A^b = g^(ab)
```
Os dois chegam no **mesmo** `s` sem nunca mandá-lo. Espião vê `p, g, A, B` e
precisaria resolver CDH.

Exemplo numérico (`p=23, g=5`): `a=6 → A=8`; `b=15 → B=19`;
`s = 19^6 mod 23 = 2` e `s = 8^15 mod 23 = 2`. ✓

Na prática `s` passa por um **KDF** antes de virar chave de AES.

## 4.3 Man-in-the-middle

DH puro **não autentica ninguém**. Mallory no meio:

```
Alice ──A──▶ Mallory ──M──▶ Bob
Alice ◀─M─── Mallory ◀──B── Bob
```
Mallory tem uma chave com Alice e outra com Bob, decifra e re-cifra tudo. Os
dois acham que estão seguros.

**Conserto:** autenticar as mensagens do DH — assinatura digital (§6) +
certificado (§6.5). É exatamente isso que o TLS faz.

---

# 5. Cifragem de Chave Pública

## 5.1 Sintaxe e segurança

Três algoritmos:
- `Gen() → (pk, sk)`
- `Enc(pk, m) → c`
- `Dec(sk, c) → m`

**CPA-segurança** (chosen-plaintext): adversário escolhe dois textos `m₀, m₁`,
recebe a cifra de um deles, não consegue adivinhar qual.
→ **Exige cifragem aleatorizada.** Determinístico nunca é CPA-seguro (basta o
atacante cifrar `m₀` e comparar).

**CCA-segurança** (chosen-ciphertext): o adversário ainda pode pedir a
decifragem de cifras que ele escolher (menos a alvo). É o que se exige na
prática — o mundo real tem atacantes que mandam cifras malformadas e observam
a reação. CCA implica **não-maleabilidade**: não dá pra pegar `c` e produzir
`c'` que decifra em algo relacionado.

## 5.2 Cifragem híbrida / KEM-DEM

Chave pública é **lenta** e só cifra mensagens pequenas. Então:

1. **KEM** (Key Encapsulation) — usa chave pública pra transportar uma chave simétrica `k` aleatória
2. **DEM** (Data Encapsulation) — cifra a mensagem de verdade com `k` usando AES-GCM

`c = (Enc_pk(k), AES_k(m))`

**Todo sistema real é híbrido.** TLS, PGP, Signal, age — todos.
Regra: a segurança do híbrido é a do elo mais fraco (KEM CCA + DEM CCA → híbrido CCA).

## 5.3 ElGamal (baseado em DDH)

É o DH transformado em cifra.

- **Chaves**: `sk = x`, `pk = h = g^x`
- **Cifrar `m`**: sorteia `r`, envia `c = (g^r, m·h^r)`
- **Decifrar** `(c₁,c₂)`: `m = c₂ / c₁^x`, porque `c₁^x = g^(rx) = h^r`

Propriedades:
- **aleatorizado** (`r` novo a cada vez) → CPA-seguro sob DDH ✔
- **expande 2×** a mensagem
- **maleável**: multiplica `c₂` por `t` e a mensagem vira `m·t` → **NÃO é CCA-seguro**
  (essa maleabilidade é homomórfica e é usada de propósito em voto eletrônico)
- `r` **nunca** pode repetir

**KEM baseado em DDH** (versão moderna, é o que se usa): manda só `c₁ = g^r` e
define a chave como `k = KDF(h^r)`. Sem multiplicação, sem maleabilidade.
Isso é o **ECIES / HPKE**.

## 5.4 RSA cru ("textbook")

- **Gen**: escolhe primos `p,q`; `N = pq`; `φ(N) = (p−1)(q−1)`;
  escolhe `e` com `gcd(e,φ)=1` (quase sempre `e = 65537`);
  calcula `d = e⁻¹ mod φ(N)` (Euclides estendido).
  `pk = (N,e)`, `sk = d`.
- **Enc**: `c = m^e mod N`
- **Dec**: `m = c^d mod N`

**Por que volta?** `c^d = m^(ed)`, e `ed ≡ 1 (mod φ)` → `ed = 1 + kφ` →
`m^(1+kφ) = m·(m^φ)^k ≡ m·1 = m` (Euler).

Exemplo miniatura: `p=3, q=11 → N=33, φ=20`. `e=3` → `d=7` (`3·7=21≡1 mod 20`).
`m=4`: `c = 4³ = 64 ≡ 31`. `31^7 mod 33 = 4`. ✓

**Por que é INSEGURO assim:**
1. **determinístico** → não é CPA-seguro; dá pra montar dicionário (ex.: cifrar
   "sim"/"não" e comparar)
2. **maleável** → `c·s^e` decifra em `m·s`
3. **`m` pequeno** → se `m^e < N` não tem redução nenhuma, basta tirar a raiz `e`-ésima nos inteiros
4. **mesmo `m` pra `e` destinatários** → ataque de broadcast de Håstad (via CRT)

> **Nunca use RSA sem padding.** Nunca.

## 5.5 Padding — PKCS #1 v1.5

`EM = 0x00 || 0x02 || PS (bytes aleatórios não-nulos) || 0x00 || m`

Adiciona aleatoriedade → resolve o determinismo. Mas:
**Ataque de Bleichenbacher (1998)**: se o servidor responde diferente para
padding válido/inválido, o atacante decifra a mensagem com ~1 milhão de
consultas ("million message attack"). Um oráculo de 1 bit basta.
Ressurgiu como **ROBOT** em 2017 — ainda havia servidores vulneráveis.
→ v1.5 para **cifragem** é legado. Evitar.

## 5.6 OAEP (PKCS #1 v2)

Padding com estrutura Feistel usando duas funções de hash (máscaras):

```
m → [ m ‖ padding ‖ hash(label) ] ⊕ MGF(r)   e   r ⊕ MGF(daquilo)
```

- CCA-seguro **no modelo do oráculo aleatório** (ROM)
- decifragem devolve erro **único** e em tempo constante — sem oráculo pra Bleichenbacher
- **é o que você deve usar** se for usar RSA pra cifrar

Resumo prático: **cifra nova hoje → ECDH/HPKE ou RSA-OAEP. Nunca RSA cru, nunca v1.5.**

---

# 6. Assinaturas Digitais

## 6.1 Sintaxe e segurança

- `Gen() → (pk, sk)`
- `Sign(sk, m) → σ`
- `Verify(pk, m, σ) → 0/1`

**Assina com a privada, verifica com a pública.** É o inverso da cifragem.

Segurança = **EUF-CMA** (existential unforgeability under chosen-message attack):
mesmo vendo assinaturas de mensagens que ele escolheu, o atacante não consegue
produzir assinatura válida para **nenhuma** mensagem nova.

Dá três coisas: **autenticidade**, **integridade**, **não-repúdio** (o MAC dá as
duas primeiras, mas não a terceira — porque com MAC os dois lados têm a mesma chave).

## 6.2 Hash-and-sign

Assinatura pública é lenta e limitada em tamanho. Então assina-se o **hash**:

`σ = Sign(sk, H(m))`

Segurança depende de `H` ser **resistente a colisão**: se o atacante acha
`m ≠ m'` com `H(m) = H(m')`, uma assinatura serve pras duas.
→ É por isso que MD5 e SHA-1 estão banidos (ver ataque de colisão em
certificados, Flame/SHAttered). Use SHA-256+.

## 6.3 Assinaturas RSA

**RSA cru**: `σ = m^d mod N`, verifica `σ^e ≡ m`. **Quebrado:**
- forja trivial: escolhe `σ` qualquer, a "mensagem" é `σ^e`
- multiplicativa: `σ₁·σ₂` assina `m₁·m₂`

**RSA-FDH** (Full Domain Hash): `σ = H(m)^d mod N`, com `H` mapeando pra todo
`Z_N`. Provável EUF-CMA no ROM. Conceitualmente o certo; na prática o padrão é
**RSA-PSS** (probabilístico, com salt, prova mais apertada).

**PKCS #1 v1.5 para assinatura**: `EM = 0x00||0x01||0xFF...0xFF||0x00||DigestInfo||H(m)`.
Padding determinístico, sem salt. Continua **onipresente** (certificados X.509,
JWT RS256). Não é quebrado em si — mas verificadores relaxados sofrem o
**ataque de Bleichenbacher de assinatura (e=3)**: se a implementação não checa
que o padding preenche o bloco *inteiro*, dá pra forjar assinatura só tirando
raiz cúbica. → verificação correta: **re-codificar e comparar byte a byte**,
nunca fazer parsing.

> Para assinar hoje: **Ed25519** ou **ECDSA P-256**; RSA-PSS se precisar de RSA.

## 6.4 DSA e ECDSA

DSA trabalha no subgrupo de ordem prima `q` dentro de `Z*_p`. ECDSA é o mesmo
em curva elíptica. Assinatura = par `(r, s)`.

**ECDSA — assinar `m`** com privada `d`, gerador `G` de ordem `n`:
1. `e = H(m)` (truncado pro tamanho de `n`)
2. sorteia **nonce** `k` em `[1, n−1]`
3. `R = kG`; `r = R.x mod n` (se 0, refaz)
4. `s = k⁻¹(e + r·d) mod n` (se 0, refaz)
5. assinatura = `(r, s)`

**Verificar** com pública `Q = dG`:
`u₁ = e·s⁻¹`, `u₂ = r·s⁻¹`, `P = u₁G + u₂Q`; válido se `P.x mod n == r`.

**⚠ O `k` é a parte mortal:**
- `k` repetido em duas mensagens → duas equações, duas incógnitas → **a chave
  privada sai por álgebra simples**. Foi assim que quebraram o **PS3 da Sony
  (2010)** e carteiras Bitcoin com RNG ruim no Android (2013).
- `k` com poucos bits enviesados → ataques de rede (lattice) recuperam a chave
  com algumas centenas de assinaturas.

**Conserto: RFC 6979** — `k` determinístico derivado de `HMAC(sk, H(m))`.
Ou use **Ed25519**, que já nasce determinístico e sem essas armadilhas.

Também: ECDSA é **maleável** — `(r, −s mod n)` também é válida. Origem da
maleabilidade de transações no Bitcoin; resolvido exigindo `s` "low".

## 6.5 Certificados e PKI

Volta ao MITM do §4.3: **como sei que essa chave pública é mesmo da Alice?**

**Certificado** = declaração assinada por uma Autoridade Certificadora (CA):
> "a chave pública `pk` pertence a `exemplo.com`, válida até 2027" — assinado pela CA

Verificação = **cadeia de confiança**:
```
Raiz (auto-assinada, já no seu SO/navegador)
  └── CA intermediária
        └── certificado do site
```
Você confia na raiz (ela veio pré-instalada), ela avaliza a intermediária, que
avaliza o site. Só precisa confiar em poucas raízes, não em milhões de sites.

Conteúdo de um X.509: sujeito, chave pública, emissor, validade, usos permitidos,
número de série, assinatura da CA.

**Revogação** (chave vazou antes do vencimento): CRL (listas, grandes e lentas),
**OCSP** (consulta online, vaza privacidade), **OCSP stapling** (servidor
entrega a prova — melhor), validade curta (Let's Encrypt, 90 dias — a abordagem
que venceu na prática).

**Fraquezas reais da PKI**: qualquer CA pode emitir pra qualquer domínio
(DigiNotar, 2011 — CA comprometida emitiu certificado do Google);
mitigação atual = **Certificate Transparency** (todo certificado vai num log
público auditável).

---

# 7. Curvas Elípticas (V8)

## 7.1 O que é

Sobre um corpo finito `F_p`, a curva de Weierstrass:

`y² = x³ + ax + b  (mod p)`, com `4a³ + 27b² ≠ 0` (evita pontos singulares)

Os **pontos** `(x,y)` que satisfazem isso, **mais** um ponto especial no
infinito `O`, formam um **grupo**.

## 7.2 A lei de grupo (operação = "soma de pontos")

- **Identidade**: `O`. `P + O = P`
- **Inverso**: `−P = (x, −y)` (reflexão no eixo x)
- **`P + Q`**: traça a reta por `P` e `Q`; ela corta a curva num terceiro ponto;
  **reflete no eixo x** → esse é `P+Q`
- **`P + P` (dobra)**: usa a **tangente** em `P`, mesma regra

Fórmulas (inclinação `λ`):
- `P ≠ Q`: `λ = (y₂−y₁)/(x₂−x₁)`
- `P = Q`: `λ = (3x₁² + a)/(2y₁)`
- e então `x₃ = λ² − x₁ − x₂`, `y₃ = λ(x₁ − x₃) − y₁`

(divisão = multiplicar pelo inverso mod p, §2.2)

**Multiplicação escalar** `kP = P+P+...+P` (k vezes) — calculada por
double-and-add, o análogo exato do square-and-multiply.

> Dicionário: multiplicação mod p ⟷ soma de pontos; exponenciação `g^x` ⟷ `xP`.
> **É o mesmo grupo abstrato.** Todo esquema traduz direto.

## 7.3 ECDLP

Dado `P` e `Q = kP`, achar `k`.

Fácil calcular `kP`; inviável voltar. **Não existe index calculus para curvas
elípticas** — só ataques genéricos `O(√n)` (Pollard rho).

Consequência: chave de 256 bits em curva ≈ 128 bits de segurança ≈ RSA de 3072 bits.
Daí: chaves menores, assinaturas menores, contas mais rápidas, menos bateria.

**Curvas a evitar**: ordem com só fatores pequenos (Pohlig–Hellman), curvas
anômalas (`#E = p`), curvas supersingulares (ataques MOV/pareamento).
→ **Use curvas padronizadas**: P-256, P-384, secp256k1 (Bitcoin/Ethereum),
Curve25519 (a mais amigável a implementação).

## 7.4 Parâmetros de domínio

`(p, a, b, G, n, h)` — corpo, coeficientes, ponto gerador, ordem de `G` (primo),
e cofator `h = #E/n`.

Chave privada: `d` aleatório em `[1, n−1]`. Chave pública: `Q = dG`.

## 7.5 ECDH

Idêntico ao DH, trocando expoente por escalar:

```
Alice: d_A, Q_A = d_A·G   ──Q_A──▶
                          ◀─Q_B──   Bob: d_B, Q_B = d_B·G
segredo = d_A·Q_B = d_A·d_B·G = d_B·Q_A
```
Usa-se só a coordenada `x`, passada por um KDF.

**ECDHE** (E = ephemeral): chaves novas a cada sessão → **forward secrecy**
(vazar a chave de longo prazo depois não decifra o tráfego passado).
É o padrão do TLS 1.3. **X25519** é a variante mais usada.

## 7.6 ECDSA

Já está no §6.4. Só lembrando o que mais cai: **nonce `k` único e imprevisível
ou a chave privada vaza.**

---

# 8. Aprofundamentos (contas na mão)

## 8.1 Teorema Chinês do Resto — exemplo completo

Problema clássico: achar `x` com

```
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)
```

**Receita (construtiva):** `N = 3·5·7 = 105`. Para cada congruência `i`:

| i | `n_i` | `a_i` | `N_i = N/n_i` | `y_i = N_i⁻¹ mod n_i` | `a_i·N_i·y_i` |
|---|---|---|---|---|---|
| 1 | 3 | 2 | 35 | `35 ≡ 2 (mod 3)` → `2⁻¹ = 2` | `2·35·2 = 140` |
| 2 | 5 | 3 | 21 | `21 ≡ 1 (mod 5)` → `1⁻¹ = 1` | `3·21·1 = 63` |
| 3 | 7 | 2 | 15 | `15 ≡ 1 (mod 7)` → `1⁻¹ = 1` | `2·15·1 = 30` |

`x = 140 + 63 + 30 = 233`, e `233 mod 105 = 23`.

Confere: `23 = 3·7+2` ✓, `23 = 5·4+3` ✓, `23 = 7·3+2` ✓.

**Por que funciona:** cada termo `a_i·N_i·y_i` vale `a_i` módulo `n_i` (porque
`N_i·y_i ≡ 1`) e vale **0** módulo todos os outros (porque `N_i` é múltiplo
deles). Ou seja, cada parcela "acende" só a sua congruência. É uma base
canônica — a mesma ideia de vetor unitário.

**Leitura estrutural:** o CRT diz que `Z_105 ≅ Z_3 × Z_5 × Z_7` como anéis.
Trabalhar mod `N` = trabalhar em paralelo mod cada fator. Guarde isso: é a
razão de o RSA-CRT funcionar, e é a razão de o ataque de Håstad funcionar.

## 8.2 RSA-CRT — como a decifragem fica 4× mais rápida

Custo de exponenciação modular ≈ cúbico no tamanho do módulo. Se eu troco uma
conta mod `N` (2048 bits) por **duas** contas mod `p` e mod `q` (1024 bits cada),
pago `2·(1/2)³ = 1/4`. Daí o "4×".

**Pré-computado junto com a chave privada** (está lá dentro do seu arquivo `.pem`):

```
d_p    = d mod (p−1)
d_q    = d mod (q−1)
q_inv  = q⁻¹ mod p
```

**Decifrar `c`:**
```
m₁ = c^d_p mod p
m₂ = c^d_q mod q
h  = q_inv · (m₁ − m₂) mod p
m  = m₂ + h·q
```

Conferindo com o exemplo miniatura do §5.4 (`p=3, q=11, N=33, e=3, d=7, c=31`):

```
d_p   = 7 mod 2  = 1
d_q   = 7 mod 10 = 7
q_inv = 11⁻¹ mod 3 = 2⁻¹ mod 3 = 2

m₁ = 31¹ mod 3  = 1
m₂ = 31⁷ mod 11 = 9⁷ mod 11 = 4
h  = 2·(1 − 4) mod 3 = −6 mod 3 = 0
m  = 4 + 0·11 = 4    ✓  (bate com o m original)
```

> **⚠ Armadilha real — ataque de Bellcore (fault attack).** Se um bit der erro
> em `m₁` (raio cósmico, glitch de tensão, laser num smartcard) e a assinatura
> errada `σ'` sair, então `gcd(σ'^e − m, N) = q`. **Um único erro entrega a chave
> privada.** Por isso toda implementação séria de RSA-CRT **verifica o resultado**
> (`σ^e ≟ m`) antes de devolver.

## 8.3 Soma de pontos em curva elíptica — contas de verdade

Curva `E: y² = x³ + 2x + 2` sobre `F₁₇`. Ponto base `P = (5, 1)`.

Confere que `P` está na curva: `5³ + 2·5 + 2 = 137`, e `137 mod 17 = 1`.
`y² = 1² = 1`. ✓

### Dobrar: `2P = P + P`

Usa a **tangente**, `λ = (3x₁² + a) / (2y₁)`:

```
numerador   = 3·5² + 2 = 77 ≡ 77 − 68 = 9  (mod 17)
denominador = 2·1 = 2;  2⁻¹ mod 17 = 9     (porque 2·9 = 18 ≡ 1)
λ = 9 · 9 = 81 ≡ 81 − 68 = 13              (mod 17)

x₃ = λ² − 2x₁ = 169 − 10 = 159 ≡ 6         (17·9 = 153)
y₃ = λ(x₁ − x₃) − y₁ = 13·(5 − 6) − 1 = −14 ≡ 3
```
**`2P = (6, 3)`**. Confere: `6³ + 12 + 2 = 230 ≡ 9 (mod 17)` e `3² = 9`. ✓

### Somar dois pontos diferentes: `3P = 2P + P`

Usa a **reta secante**, `λ = (y₂ − y₁)/(x₂ − x₁)`, com `P=(5,1)`, `2P=(6,3)`:

```
λ = (3 − 1)/(6 − 5) = 2/1 = 2

x₃ = λ² − x₁ − x₂ = 4 − 5 − 6 = −7 ≡ 10    (mod 17)
y₃ = λ(x₁ − x₃) − y₁ = 2·(5 − 10) − 1 = −11 ≡ 6
```
**`3P = (10, 6)`**. Confere: `10³ + 20 + 2 = 1022 ≡ 2 (mod 17)` e `6² = 36 ≡ 2`. ✓

Seguindo assim, o grupo gerado por `P` tem **19 pontos** (`19P = O`) — ordem
prima, exatamente o que se quer numa curva de cripto.

**Três observações que valem a nota da prova:**

1. Toda "divisão" virou **inverso modular** (Euclides estendido, §2.2). Inverter
   é caro — por isso implementações reais usam **coordenadas projetivas/Jacobianas**,
   que adiam a inversão para o fim.
2. `P + (−P) = O`: a reta por `(x,y)` e `(x,−y)` é **vertical**, não corta a
   curva em terceiro ponto — daí a necessidade do ponto no infinito.
3. **Double-and-add** é o mesmo algoritmo do §2.3. Para `13P` (`1101₂`):
   `P → 2P → 3P → 6P → 12P → 13P`. Versão ingênua ramifica conforme o bit e
   **vaza a chave privada por timing** → use Montgomery ladder (tempo constante).

## 8.4 Baby-step Giant-step (BSGS)

Resolver `g^x = h` num grupo de ordem `n`, sem força bruta.

**Truque:** escreve `x = i·m + j`, com `m = ⌈√n⌉` e `0 ≤ i, j < m`.
Então `g^(im+j) = h` => `g^j = h · (g^(−m))^i`.

```
1. m = ⌈√n⌉
2. BABY STEPS: monta tabela hash { g^j → j } para j = 0..m−1     (√n memória)
3. c = g^(−m)   (um inverso, calculado uma vez)
4. GIANT STEPS: para i = 0..m−1, calcula γ = h·c^i
                se γ está na tabela com valor j → x = i·m + j     (√n tempo)
```

**Exemplo:** resolver `5^x ≡ 7 (mod 23)`. Aqui `g = 5` é raiz primitiva,
ordem `n = 22`, logo `m = ⌈√22⌉ = 5`.

**Baby steps** — tabela de `5^j mod 23` para `j = 0..4`:

| `j` | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `5^j` | 1 | 5 | 2 | 10 | 4 |

**O passo gigante:** `c = g^(−m) = (5⁵)⁻¹ = 20⁻¹ ≡ 15 (mod 23)`
(confere: `20·15 = 300 = 13·23 + 1` ✓)

| `i` | `γ = 7 · 15^i mod 23` | está na tabela? |
|---|---|---|
| 0 | 7 | não |
| 1 | `7·15 = 105 ≡ 13` | não |
| 2 | `13·15 = 195 ≡ 11` | não |
| 3 | `11·15 = 165 ≡ 4` | **sim → j = 4** |

`x = i·m + j = 3·5 + 4 = 19`.
Confere: `5¹⁹ mod 23 = 7` ✓

Repare o que aconteceu: em vez de testar 22 expoentes, fiz 5 baby steps + 4
giant steps. Com `n = 10¹²`, seria 1 milhão em vez de 1 trilhão.

**Custo:** `O(√n)` tempo **e** `O(√n)` memória. Para `n ≈ 2²⁵⁶`, seriam `2¹²⁸`
entradas de tabela — mais memória que átomos acessíveis. Por isso 256 bits basta.

**Moral:** BSGS é o "raise de baseline". Qualquer grupo com ordem menor que ~2¹⁶⁰
é quebrável só com isso. É o motivo de existir um **piso** de tamanho de chave.

## 8.5 Pollard rho

Mesmo custo de tempo do BSGS (`O(√n)`) mas com **memória O(1)**. É o ataque
prático de verdade contra ECDLP.

**Ideia — paradoxo do aniversário.** Defina um passeio pseudoaleatório no grupo
onde cada posição é sempre da forma `g^a · h^b`, com `a, b` conhecidos:

```
partição o grupo em 3 regiões S₁, S₂, S₃ por alguma função barata de x

x ∈ S₁ →  x ← h·x      (b ← b+1)
x ∈ S₂ →  x ← x²       (a ← 2a, b ← 2b)
x ∈ S₃ →  x ← g·x      (a ← a+1)
```

Como o grupo é finito, o passeio **entra num ciclo** — o formato ρ que dá nome
ao algoritmo (uma "cauda" + um "laço"). Pelo paradoxo do aniversário, isso
acontece após ~`1.25·√n` passos.

**Detecção do ciclo (Floyd):** roda duas cópias, uma a 1 passo por iteração e
outra a 2 passos, até baterem. Memória: dois pontos. Só isso.

**Extração da resposta:** ao colidir, temos
`g^a₁ h^b₁ = g^a₂ h^b₂`. Com `h = g^x`:

```
a₁ + x·b₁ ≡ a₂ + x·b₂   (mod n)
x ≡ (a₁ − a₂) · (b₂ − b₁)⁻¹   (mod n)
```
Uma inversão modular e a chave privada sai.

**Pollard rho para fatorar** é o primo-irmão: mesmo passeio, mas em `Z_N`, com
`x ← x²+1`, procurando `gcd(|x_i − x_j|, N) > 1`. Acha um fator `p` em
`O(√p) = O(N^(1/4))`.

**Por que isso fixa os tamanhos de chave:**
- é **paralelizável** com ganho linear (versão de Van Oorschot–Wiener, com
  "distinguished points") — `k` máquinas dão `k` vezes mais rápido
- é o **melhor ataque conhecido contra ECDLP**, porque não há index calculus lá
- logo, curva de `n` bits => `n/2` bits de segurança. **256 → 128.** Fim.

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

1. `1071 = 2·462 + 147`; `462 = 3·147 + 21`; `147 = 7·21 + 0` → **21**.
2. `43 = 2·17 + 9`; `17 = 1·9 + 8`; `9 = 1·8 + 1`. Voltando:
   `1 = 9 − 8 = 9 − (17 − 9) = 2·9 − 17 = 2(43 − 2·17) − 17 = 2·43 − 5·17`.
   → `−5·17 ≡ 1` → **`17⁻¹ = 38`**. (Confere: `17·38 = 646 = 15·43 + 1` ✓)
3. `100 = 2²·5²` → `φ = 100·(1−½)(1−⅕) = 40`. `143 = 11·13` → `10·12 = 120`.
4. `φ(11) = 10`, `222 mod 10 = 2` → `7² = 49 ≡ 5`.
5. `φ(15) = 8`: `{1,2,4,7,8,11,13,14}`. **Não é cíclico** — todo elemento tem
   ordem ≤ 4 (`Z*₁₅ ≅ Z₂ × Z₄`). Só `Z*_n` com `n = 1,2,4,p^k,2p^k` é cíclico.
6. `3¹=3, 3²=9, 3³=5, 3⁴=4, 3⁵=1` → **ordem 5**. `|Z*₁₁| = 10` ≠ 5 → **não é gerador**.

</details>

## Bloco B — RSA

7. `p = 5`, `q = 11`, `e = 3`. Ache `N`, `φ(N)` e `d`.
8. Com essa chave, cifre `m = 9` e decifre de volta.
9. Alice publica `N = 3233`, `e = 17`. Ela usou `p = 61`, `q = 53`. Qual é `d`?
10. Por que `e = 65537` e não `e = 3` nos padrões modernos?
11. Mostre a maleabilidade: dado `c = m^e`, como produzir a cifra de `2m` sem saber `m`?

<details><summary><b>Respostas B</b></summary>

7. `N = 55`, `φ = 4·10 = 40`. `d = 3⁻¹ mod 40 = 27` (`3·27 = 81 = 2·40+1`).
8. `c = 9³ = 729 = 13·55 + 14` → `c = 14`.
   `14^27 mod 55`: `14² = 196 ≡ 31`; `14⁴ ≡ 31² = 961 ≡ 26`; `14⁸ ≡ 26² = 676 ≡ 16`;
   `14¹⁶ ≡ 16² = 256 ≡ 36`. `27 = 16+8+2+1` → `36·16·31·14 mod 55`:
   `36·16 = 576 ≡ 26`; `26·31 = 806 ≡ 31`; `31·14 = 434 ≡ 9` ✓
9. `φ = 60·52 = 3120`; `d = 17⁻¹ mod 3120 = 2753` (`17·2753 = 46801 = 15·3120+1`).
   *(É o exemplo da Wikipédia — bom pra treinar.)*
10. `e = 3` é rápido mas frágil: `m³ < N` sem padding quebra direto, e o ataque de
    broadcast de Håstad precisa de só 3 destinatários. `65537 = 2¹⁶+1` tem **dois
    bits 1** (ainda rápido: 17 quadrados + 1 multiplicação) e é grande o bastante
    para matar esses ataques.
11. `c' = c · 2^e mod N`. Aí `Dec(c') = (m^e · 2^e)^d = (2m)^e·d = 2m`. Nenhum
    conhecimento de `m` foi necessário → **é por isso que RSA cru não é CCA-seguro**.

</details>

## Bloco C — DH, ElGamal, assinaturas

12. `p = 23`, `g = 5`, Alice tem `a = 4`, Bob tem `b = 3`. Qual o segredo comum?
13. No exercício acima, o que Eve vê no fio? Por que ela não consegue o segredo?
14. Em ElGamal, o que acontece se Bob reusa o mesmo `r` para duas mensagens
    `m₁` e `m₂`, e Eve conhece `m₁`?
15. Duas assinaturas ECDSA `(r, s₁)` e `(r, s₂)` — mesmo `r`! — sobre `e₁ ≠ e₂`.
    Derive `k` e depois a chave privada `d`.
16. Por que assinar `H(m)` em vez de `m` exige que `H` seja resistente a colisão,
    e não só unidirecional?

<details><summary><b>Respostas C</b></summary>

12. `A = 5⁴ = 625 ≡ 4 (mod 23)`; `B = 5³ = 125 ≡ 10`.
    `s = B^a = 10⁴ = 10000 ≡ 18`; `s = A^b = 4³ = 64 ≡ 18`. → **18** ✓
13. Eve vê `p=23, g=5, A=4, B=10`. Precisaria resolver o **log discreto**
    (`5^a ≡ 4`) ou o **CDH** direto. Com `p` de 23 é trivial na mão; com `p` de
    3072 bits, não. *A segurança é só o tamanho.*
14. `c₂ = m·h^r`. Duas cifras com o mesmo `r` dão `c₂⁽¹⁾/c₂⁽²⁾ = m₁/m₂`.
    Sabendo `m₁`, sai `m₂ = m₁·c₂⁽²⁾/c₂⁽¹⁾`. **Nonce reusado = mensagem vazada.**
    Mesma estrutura do erro do one-time pad reusado.
15. Mesmo `r` => mesmo `k` (pois `r = (kG).x`). De `s = k⁻¹(e + rd)`:
    ```
    s₁ − s₂ = k⁻¹(e₁ − e₂)   →   k = (e₁ − e₂)·(s₁ − s₂)⁻¹ mod n
    d = (s₁·k − e₁) · r⁻¹ mod n
    ```
    Duas subtrações e duas inversões. **Foi literalmente isso no PS3 e nas
    carteiras Bitcoin do Android.**
16. Unidirecional só impede achar `m` a partir de `H(m)`. Mas o forjador não
    precisa disso: ele pega **duas** mensagens suas `m` (benigna) e `m'`
    (maliciosa) com `H(m) = H(m')`, te faz assinar `m`, e a **mesma assinatura
    vale para `m'`** — `Verify` só olha o hash. Logo o requisito é **colisão**.
    É o ataque que aposentou MD5 (certificado falso da CA, Flame, 2012) e SHA-1
    (SHAttered, 2017).

</details>

## Bloco D — conceitual (responda em uma frase)

17. Por que `φ(pq) = (p−1)(q−1)` é exatamente *a* porta dos fundos do RSA?
18. Diferença prática entre CPA-seguro e CCA-seguro — dê um cenário real onde a
    diferença importa.
19. Por que DDH é falsa em `Z*_p` inteiro, e como o padrão conserta?
20. Explique em uma frase por que ECC de 256 bits ≈ RSA de 3072 bits.

<details><summary><b>Respostas D</b></summary>

17. Quem sabe `p,q` calcula `φ` numa multiplicação e daí `d = e⁻¹ mod φ`; quem só
    tem `N` precisaria fatorar. **Conhecer `φ(N)` é equivalente a fatorar `N`.**
18. CPA supõe atacante passivo; CCA supõe que ele **manda cifras e observa a
    resposta**. Cenário: servidor TLS que responde "padding inválido" —
    Bleichenbacher usa esse único bit para decifrar a chave de sessão. CPA não
    cobre isso; CCA sim.
19. O **símbolo de Legendre** (é ou não resíduo quadrático) é calculável em tempo
    polinomial e vaza 1 bit sobre o expoente — suficiente para distinguir `g^ab`
    de aleatório. Conserto: trabalhar no **subgrupo de ordem prima `q`** (primo
    seguro `p = 2q+1`, `g` gerador dos resíduos quadráticos).
20. Em `Z*_p` existe **index calculus** (subexponencial), então `p` precisa ser
    enorme; em curvas só existe Pollard rho genérico (`O(√n)`), então
    `n` bits => `n/2` bits de segurança, e `256/2 = 128`.

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
2. Reusar o nonce `k` no (EC)DSA
3. DH sem autenticação → MITM
4. Confundir cifragem com assinatura ("cifrar com a privada" não é assinar)
5. Gerador de aleatórios fraco — mata tudo, não importa a matemática
6. Verificar padding v1.5 por parsing em vez de re-codificar
7. Comparação de tempo não constante → side-channel

## O que usar hoje

- **Troca de chave**: X25519 (ECDHE)
- **Assinatura**: Ed25519, ou ECDSA P-256
- **Cifragem pública**: HPKE / ECIES; RSA-OAEP se obrigado
- **Hash**: SHA-256 ou SHA-3
- **Simétrico**: AES-256-GCM ou ChaCha20-Poly1305

## Para responder em aula, saiba dizer em uma frase

- por que `φ(pq) = (p−1)(q−1)` é o segredo do RSA
- por que RSA cru não é CPA-seguro
- por que DH sozinho sofre MITM
- por que ECC usa chaves menores (ausência de index calculus)
- por que reusar `k` no ECDSA vaza a chave privada
- diferença CPA × CCA, CDH × DDH, MAC × assinatura

---

## Referências

- Menezes, van Oorschot, Vanstone — *Handbook of Applied Cryptography* (grátis:
  cacr.uwaterloo.ca/hac) — cap. 2 (números), 3 (hipóteses), 4 (primalidade),
  8 (cifragem pública), 11 (assinaturas)
- Katz & Lindell — *Introduction to Modern Cryptography* — melhor para as
  definições de segurança (CPA/CCA/EUF-CMA)
- Hoffstein, Pipher, Silverman — *An Introduction to Mathematical Cryptography* —
  melhor para curvas elípticas
- Nigel Smart — *Cryptography Made Simple*
