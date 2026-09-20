---
author: Jeroen van de Graff ( anotações Arthur)
title: "Segurança Computacional (Katz & Lindell cap. 3)"
institute: DCC/UFMG
aspectratio: 169
header-includes:
      - \usepackage{amsmath,amssymb}
      - \usepackage{tikz}
      - \usetikzlibrary{patterns}
# pandoc aula2.md --pdf-engine=tectonic -o aula2.pdf
---

## Roteiro — Computational Security

- RSA
- Definição baseada em **vantagem** (advantage-based) — §2.6 $\Rightarrow$ §3.8
- **Semantic Security** — definição por *distinguisher* / indistinguibilidade (§3.14), *next-bit*
- **Pseudo Random Generators** (PRG)
- Encriptação a partir de PRG (§3.16)
- **Chosen Plaintext Attack — CPA** (§3.21) 

> Semantic Security (§3.10–3.12) — não está no livro.

---

## RSA 

1. Escolher $p, q$ primos de tamanho $1024$ bits.
2. Computar $n = p\cdot q$ — (GenKey). Note $\varphi(n) = |\mathbb{Z}_n^{*}|$.
3. Computar $\varphi = \varphi(n) = (p-1)(q-1)$.
4. Escolher $e = 65537$ e computar $d$ tal que
$$
ed \equiv 1 \pmod{\varphi}
$$

Operações:

$$
\mathrm{Enc}_{(n,e)}(m) = m^{e} \bmod n
\qquad
\mathrm{Dec}_{(n,d)}(c) = c^{d} \bmod n
$$

### Corretude

$$
\mathrm{Dec}(\mathrm{Enc}(m)) \equiv \mathrm{Dec}(m^{e} \bmod n) \equiv (m^{e})^{d}
$$

Como $ed \equiv 1 \pmod{\varphi} \iff ed = 1 + k\varphi$:

$$
(m^{e})^{d} \equiv m^{1 + k\varphi} \equiv m \cdot (m^{\varphi})^{k} \equiv m \cdot 1^{k} \equiv m
$$

logo $\mathrm{Dec} \to m$. (usa Euler: $m^{\varphi(n)} \equiv 1 \bmod n$, válido para
$\gcd(m,n)=1$; para os demais $m$ a igualdade ainda vale, via CRT em $\bmod p$ e $\bmod q$.)

---

## Goldwasser–Micali (GM) cryptosystem

Mensagens: $m_0 = \texttt{'YES'}$, $m_1 = \texttt{'NO'}$. A encriptação usa
**randomness**, então cada mensagem tem *muitos* cifrados possíveis:

$$
\mathrm{Enc}(\texttt{'YES'}) \to \{c_1, c_2, \dots\}
\qquad
\mathrm{Enc}(\texttt{'NO'}) \to \{c_1', c_2', \dots\}
$$

Os dois conjuntos são **disjuntos** (senão $\mathrm{Dec}$ não funcionaria); o ponto é que
são computacionalmente indistinguíveis. É isso que permite ser CPA-seguro, coisa que
RSA "livro-texto" (determinístico) não é.

Propriedade homomórfica:

$$
\mathrm{Enc}(m_1)\cdot \mathrm{Enc}(m_2) = \mathrm{Enc}(m_1 \oplus m_2)
$$

(em GM a mensagem é um **bit** e o produto dos cifrados decripta para o XOR;
a versão com $m_1 \cdot m_2$ é a do RSA, que é multiplicativo.)

### Resíduos quadráticos

**Módulo primo $p$.** $y$ é raiz quadrada de $x \bmod p$ se $y^2 \equiv x \bmod p$.
Em $\mathbb{Z}_p^{*}$ (que tem $p-1$ elementos):

- $\dfrac{p-1}{2}$ são resíduos quadráticos (têm raiz) — escrevemos $\left(\tfrac{x}{p}\right) = +1$
- $\dfrac{p-1}{2}$ não são — $\left(\tfrac{x}{p}\right) = -1$

Aqui decidir é **fácil**: critério de Euler, $x^{(p-1)/2} \bmod p$.

**Módulo composto $N = p\cdot q$.** Cada $x \in \mathbb{Z}_N^{*}$ tem um status mod $p$ e um
status mod $q$ (CRT), dando 4 células de tamanho $\tfrac{(p-1)(q-1)}{4}$ cada.
O símbolo de **Jacobi** é o produto dos dois:
$\left(\tfrac{x}{N}\right) = \left(\tfrac{x}{p}\right)\left(\tfrac{x}{q}\right)$ — e é computável
em tempo polinomial **sem** fatorar $N$.

\begin{center}
\begin{tikzpicture}[scale=1.0]
  \fill[pattern=north east lines, pattern color=black!25] (0,0) rectangle (2.6,1.5);
  \fill[pattern=north east lines, pattern color=black!25] (2.6,-1.5) rectangle (5.2,0);
  \draw[thick] (0,-1.5) rectangle (5.2,1.5);
  \draw[thick] (2.6,-1.5) -- (2.6,1.5);
  \draw[thick] (0,0) -- (5.2,0);
  % rotulos colunas (mod q)
  \node[above] at (1.3,1.6) {\footnotesize QR mod $q$};
  \node[above] at (3.9,1.6) {\footnotesize NQR mod $q$};
  \node[above] at (2.6,2.15) {\small $\bmod q$};
  % rotulos linhas (mod p)
  \node[left] at (-0.15,0.75) {\footnotesize QR mod $p$};
  \node[left] at (-0.15,-0.75) {\footnotesize NQR mod $p$};
  \node[left,rotate=90] at (-2.0,0) {\small $\bmod p$};
  % celulas
  \node[align=center] at (1.3,0.75) {\footnotesize Jacobi $+1$\\[-1pt] \footnotesize \textbf{é QR mod $N$}};
  \node[align=center] at (3.9,0.75) {\footnotesize Jacobi $-1$};
  \node[align=center] at (1.3,-0.75) {\footnotesize Jacobi $-1$};
  \node[align=center] at (3.9,-0.75) {\footnotesize Jacobi $+1$\\[-1pt] \footnotesize \textbf{não é QR mod $N$}};
  \draw[->,gray] (6.9,0.75) -- (5.35,0.55);
  \draw[->,gray] (6.9,0.75) -- (5.35,-0.55);
  \node[right,align=left] at (6.9,0.75) {\footnotesize hachurado $=$\\[-1pt] \footnotesize Jacobi $+1$ $(J_N^{+1})$};
\end{tikzpicture}
\end{center}

O Jacobi separa hachurado de não-hachurado, mas **não** distingue as duas células da
diagonal. Essa é a **Quadratic Residuosity Assumption (QRA)**: dado $x$ com
$\left(\tfrac{x}{N}\right)=+1$, decidir se $x$ é QR mod $N$ é difícil sem conhecer $p,q$.

**É daí que sai o GM:** $\mathrm{Enc}(0) = r^{2}$, $\mathrm{Enc}(1) = x_0 \cdot r^{2}$, com $r$
aleatório e $x_0$ um pseudoquadrado fixo (célula de baixo). Os dois cifrados vivem na
diagonal hachurada — distingui-los *é* o problema QRA.

---

## Concrete approach

Um esquema é $(t,\varepsilon)$-**seguro** se qualquer adversário rodando por tempo $t$
consegue quebrá-lo com probabilidade $\leq \varepsilon$.

$$
2^{64} \longrightarrow 2^{128}
$$

## Asymptotic approach

Um esquema é seguro se todo adversário **PPT** (Probabilistic Polynomial Time) tem
sucesso com probabilidade **desprezível** (negligible):

$$
f(n) < \frac{1}{\mathrm{poly}(n)}
$$

(informalmente; a versão precisa — *para todo* polinômio, *para todo* $n$ grande — está
logo abaixo.)

Propriedades de funções desprezíveis:

- $\mathrm{negl}_1(n) + \mathrm{negl}_2(n)$ também é desprezível
- $p(n)\cdot \mathrm{negl}(n) < \mathrm{negl}'(n)$ (polinômio vezes desprezível ainda é desprezível)

**Definição.** Um esquema é seguro se, para todo adversário PPT $\mathcal{A}$ e todo
polinômio $p$, existe $N$ tal que para todo $n > N$:

$$
\Pr[\text{success}] < \frac{1}{p(n)}
$$

---

## Esquema de encriptação de chave privada

$$
\begin{aligned}
\mathrm{Gen} &: \text{entrada } 1^{n};\ \text{saída: chave aleatória } k \\
\mathrm{Enc} &: c \leftarrow \mathrm{Enc}_k(m) \\
\mathrm{Dec} &: m' := \mathrm{Dec}_k(c)
\end{aligned}
$$

### EAV-security (eavesdrop)

- adversário passivo, **uma** única observação
- Adv é PPT

$$
\begin{array}{ccc}
\mathcal{A} & \xrightarrow{\;\;m_0,\,m_1\;\;} & \textbf{ORACLE} \\[2pt]
            & \xleftarrow{\;c=\mathrm{Enc}_k(m_b)\;} & b \xleftarrow{R} \{0,1\}
\end{array}
$$

O adversário **produz um palpite** $b'$ e **vence se** $b = b'$.

**Definição.** $\Pi = (\mathrm{Gen},\mathrm{Enc},\mathrm{Dec})$ tem *indistinguishable
encryptions* na presença de um eavesdropper se para todo PPT $\mathcal{A}$ existe
$\mathrm{negl}$ tal que

$$
\Pr\!\left[\mathrm{PrivK}^{\mathrm{eav}}_{\mathcal{A},\Pi}(n) = \text{SUCCESS}\right]
\;\leq\; \frac{1}{2} + \mathrm{negl}(n)
\;\approx\; \frac{1}{2}
$$

---

## Semantic security — versão com predicado

Seja $B$ um predicado sobre a mensagem, p.ex.

$$
B(m_0) = 0, \qquad B(m_1) = 1
$$

Exige-se

$$
\Pr[B(m) = 1 \mid m = m_0] \;\approx\; \Pr[B(m)=1 \mid m = m_1]
$$

Se as probabilidades são iguais, é o mesmo que um palpite aleatório — o adversário
não sabe qual mensagem é qual, não ganha nada bisbilhotando.

Para uma mensagem por blocos $m = m_1 m_2 m_3 \dots m_k$, com $c = \mathrm{Enc}_k(m)$,
pergunta-se por qualquer função $f(m) \to \{0,1\}$.

### Next-bit predictability

Dado $r_1, \dots, r_n$, prever $r_{n+1} = 0$ ou $1$:

$$
\Pr[\text{SUCCESS}] \leq \tfrac{1}{2} + \mathrm{negl}
$$

---

## Definição — Pseudo Random (Bit/Number) Generator, PRG $G$

$$
s \longmapsto G(s), \qquad |s| = n,\quad |G(s)| = \ell(n)
$$

Para todo *distinguisher* PPT $D$ existe $\mathrm{negl}(n)$ tal que, com
$r \xleftarrow{R} \{0,1\}^{\ell(n)}$:

$$
\Big|\Pr[D(G(s)) = 1] - \Pr[D(r) = 1]\Big| < \mathrm{negl}(n)
$$

### Expansão: $n \to 2n$

$G: \{0,1\}^{n} \to \{0,1\}^{2n}$ — dobra o tamanho? A imagem é minúscula:

Exemplo $n = 5$:

$$
2^{5} = 32 \ \text{valores possíveis} \quad\subseteq\quad \{0,1\}^{10} = 1024 \ \text{valores}
$$

- $32$ valores com probabilidade $\tfrac{1}{32}$
- $992$ valores com probabilidade $0$
- uniforme daria $p = \tfrac{1}{1024}$

Seed $= 5$, expande para $10$: gera saída de tamanho $10$, mas só cai nos $32$ iniciais.

De forma geral:

$$
k \in \{0,1\}^{n} \Rightarrow \mathrm{Im}(G) \subseteq \{0,1\}^{2n},
\qquad |\mathrm{Im}(G)| = 2^{n}
$$

$$
\frac{2^{n}}{2^{2n}} = \frac{1}{2^{n}}
$$

Probabilidade de **cada string** $w \in \{0,1\}^{2n}$ individual:

|                            | Uniform       | PRG        |
|----------------------------|---------------|------------|
| $w \in \mathrm{Im}(G)$     | $1/2^{2n}$    | $1/2^{n}$  |
| $w \notin \mathrm{Im}(G)$  | $1/2^{2n}$    | $0$        |

(confere com o exemplo $n=5$: uniforme dá $1/1024$ a cada string; o PRG dá $1/32$ às $32$
strings da imagem e $0$ às outras $992$.)

A massa total que a uniforme coloca dentro de $\mathrm{Im}(G)$ é
$\dfrac{2^{n}}{2^{2n}} = \dfrac{1}{2^{n}}$ — desprezível. Logo **existe** um distinguisher
trivial ("$w$ está em $\mathrm{Im}(G)$?") com vantagem $\approx 1$, mas ele **não é PPT**:
testar isso exige percorrer as $2^{n}$ seeds. Por isso a definição de PRG quantifica só
sobre distinguishers polinomiais.

---

## Dois tipos de definição

**1. Duas distribuições indistinguíveis**

$$
\big|\Pr[D(\mathrm{Enc}(m_0))=1] - \Pr[D(\mathrm{Enc}(m_1))=1]\big| < \frac{1}{\mathrm{poly}}
$$

$$
\big|\underbrace{\Pr[D(G(k))=1]}_{\text{PRG}} - \underbrace{\Pr[D(w)=1]}_{\text{Uniform}}\big| < \frac{1}{\mathrm{poly}}
$$

**2. Advantage-based**

- envolve um **jogo**
- o adversário tem que adivinhar $b' \in \{0,1\}$
- o adversário vence com $\Pr[\;] \leq \tfrac{1}{2} + \tfrac{1}{\mathrm{poly}}$

---

## Encriptação a partir de um PRG

$$
\Pi:\quad
\begin{cases}
\mathrm{Enc}_k(m) = m \oplus G(k) \\
\mathrm{Dec}_k(c) = c \oplus G(k)
\end{cases}
$$

com $n \to \ell(n)$, isto é $|k| = n$ e $|m| = \ell(n)$ — a chave é **menor** que a mensagem
(ao contrário do OTP). Isso **não** contradiz o Teorema 2.11 da aula passada
($|\mathcal{K}| \geq |\mathcal{M}|$): aquele teorema é sobre sigilo *perfeito*; aqui o
esquema é apenas computacionalmente seguro.

**Teorema (redução).** Um ataque contra $\Pi$ (protocolo) pode ser transformado num
ataque contra o PRG $G$.

### Prova (esboço) — construir o distinguisher $D(w)$

1. obter $m_0, m_1$ do adversário $\mathcal{A}$
2. escolher um bit $b$, definir $c = w \oplus m_b$ e devolver $c$ a $\mathcal{A}$
3. $\mathcal{A}$ devolve $b'$; $D$ produz $1$ sse $b = b'$

$$
\begin{array}{ccc}
\mathcal{A} & \xrightarrow{\;\;m_0,\,m_1\;\;} & b \in \{0,1\} \\[2pt]
\text{guess } b' & \xleftarrow{\;\mathrm{Enc}(m_b)\;} &
\end{array}
\qquad
\begin{cases}
b = b' \Rightarrow \text{SUCCESS} \\
b \neq b' \Rightarrow \text{FAIL}
\end{cases}
$$

**Caso 1 — $w$ uniforme.** Então $c = w \oplus m_b$ é um one-time pad perfeito:

$$
\Pr[D(w)=1] = \Pr\!\left[\mathrm{PrivK}^{\mathrm{eav}}_{\mathcal{A},\widetilde{\Pi}}(n)=1\right] = \frac{1}{2}
$$

**Caso 2 — $w = G(k)$.** Então o jogo é exatamente $\Pi$:

$$
\Pr[D(G(k))=1] = \Pr\!\left[\mathrm{PrivK}^{\mathrm{eav}}_{\mathcal{A},\Pi}(n)=1\right]
$$

Pela definição de PRG a diferença é desprezível, logo

$$
\left|\Pr\!\left[\mathrm{PrivK}^{\mathrm{eav}}_{\mathcal{A},\Pi}(n)=1\right] - \frac{1}{2}\right|
< \frac{1}{\mathrm{poly}}
$$


---

## Experimentos: EAV vs CPA

### EAV-experiment

$$
\begin{array}{ccc}
\text{Adv escolhe } m_0, m_1 & \xrightarrow{\hspace{2.2cm}} & \textbf{ORACLE},\ b \in \{0,1\} \\[2pt]
\text{guess } b' & \xleftarrow{\;\;\mathrm{Enc}(m_b)\;\;} &
\end{array}
$$

Se $b = b'$ então **Adv vence**.

### CPA-experiment (Chosen Plaintext Attack)

O adversário tem acesso a um oráculo de encriptação **livremente**, antes do desafio:

$$
\begin{array}{ccc}
\text{Adv} & \xrightarrow{\;\;\;\;m\;\;\;\;} & \textbf{ORACLE}:\ c = \mathrm{Enc}_k(m) \ \{\text{livre}\} \\[2pt]
           & \xleftarrow{\;\;\;\;c\;\;\;\;}  & \\[6pt]
\text{então Adv escolhe } m_0, m_1 & \xrightarrow{\hspace{2.2cm}} & b \in \{0,1\} \\[2pt]
\text{guess } b' & \xleftarrow{\hspace{2.2cm}} &
\end{array}
$$

Se $b = b'$ então **vence**.

> Consequência: encriptação CPA-segura **precisa ser randomizada** — determinística
> perde na hora, pois o adversário pede $\mathrm{Enc}(m_0)$ ao oráculo e compara.
