---
author: Jeroen van de Graff ( anotações Arthur)
title: "Sigilo Perfeito (Katz & Lindell §2.1–2.2)"
institute: DCC/UFMG
aspectratio: 169
header-includes:
      - \usepackage{amsmath,amssymb}
      - \usepackage{tikz}
      - \usetikzlibrary{patterns}
# pandoc aula1.md --pdf-engine=tectonic -o aula1.pdf
---

## K&L §2.1 — Notação

Espaços (todos caligráficos):

- $k \in \mathcal{K}$, com distribuição $\Pr[K=k]$ — espaço de chaves
- $m \in \mathcal{M}$, com distribuição $\Pr[M=m]$ — espaço de mensagens
- $c \in \mathcal{C}$, com distribuição $\Pr[C=c]$ — espaço de textos cifrados

Esquema de encriptação $(\mathrm{Gen},\mathrm{Enc},\mathrm{Dec})$, com $\lambda$ o
parâmetro de segurança (K&L escreve $1^{n}$):

$$
k \leftarrow \mathrm{Gen}(1^{\lambda}) \qquad
c := \mathrm{Enc}_k(m) \qquad
m' := \mathrm{Dec}_k(c)
$$

### Exemplo 2.1 — Shift Cipher

$$
\mathcal{M} = \{a,\dots,z\}, \qquad
\mathcal{K} = \{0,\dots,25\}, \qquad
\mathcal{C} = \{A,\dots,Z\}
$$

Distribuições assumidas:

$$
\Pr[K=k] = \tfrac{1}{26}, \qquad
\Pr[M=a] = \tfrac{7}{10}, \qquad
\Pr[M=z] = \tfrac{3}{10}
$$

**Pergunta:** $\Pr[C = \texttt{'B'}]\ ?$

O texto cifrado $\texttt{B}$ só ocorre em dois casos disjuntos:

$$
(M = \texttt{'a'} \wedge K = 1) \quad \text{ou} \quad (M = \texttt{'z'} \wedge K = 2)
$$

Logo:

$$
\begin{aligned}
\Pr[C=\texttt{'B'}]
&= \Pr[M=\texttt{'a'} \wedge K=1] + \Pr[M=\texttt{'z'} \wedge K=2] \\
&= \Pr[M=\texttt{'a'}]\cdot\Pr[K=1] + \Pr[M=\texttt{'z'}]\cdot\Pr[K=2] \\
&= \tfrac{7}{10}\cdot\tfrac{1}{26} + \tfrac{3}{10}\cdot\tfrac{1}{26}
 = \tfrac{1}{26}
\end{aligned}
$$

(usa independência entre $M$ e $K$).

### Probabilidade a posteriori (Bayes)

$$
\begin{aligned}
\Pr[M=a \mid C=B]
&= \frac{\Pr[C=B \mid M=a]\cdot \Pr[M=a]}{\Pr[C=B]} \\
&= \frac{\tfrac{1}{26}\cdot \tfrac{7}{10}}{\tfrac{1}{26}}
 = \tfrac{7}{10}
\end{aligned}
$$

Ou seja: observar $C=B$ **não** alterou a crença sobre $M$ — a posteriori é igual à a
priori. Isso é exatamente a condição da Def. 2.3 a seguir, verificada para um par
$(m,c)$ específico; o shift cipher de **uma letra** com $|\mathcal{K}|=|\mathcal{M}|=26$
de fato é perfeitamente secreto. O Ex. 2.4 mostra que isso quebra com duas letras.

---

## Definição 2.3 — Sigilo Perfeito

$(\mathrm{Gen},\mathrm{Enc},\mathrm{Dec})$ é **perfeitamente secreto** se, para toda
distribuição de probabilidade sobre $\mathcal{M}$, todo $m \in \mathcal{M}$ e todo
$c \in \mathcal{C}$ com $\Pr[C=c] > 0$:

$$
\Pr[M=m \mid C=c] = \Pr[M=m]
$$

Formulação equivalente ("old book"):

$$
\Pr[C=c \mid M=m] = \Pr[C=c]
$$

### Mais sobre a Def. 2.3 — por que são equivalentes

Pela regra do produto, ambos os lados são a probabilidade conjunta:

$$
\Pr[M=m \mid C=c]\cdot\Pr[C=c] \;=\; \Pr[C=c\mid M=m]\cdot \Pr[M=m]
$$

$$
\Pr[C=c]\cdot \Pr[M=m\mid C=c] \;=\; \Pr[\,M=m \,\wedge\, C=c\,]
$$

\begin{center}
\begin{minipage}{\linewidth}
\centering
É a interseção dos eventos $M=m$ e $C=c$ (região hachurada):
\par\medskip
\begin{tikzpicture}[line width=0.8pt, font=\normalsize]
  % A hachura fica restrita à interseção dos dois eventos.
  \begin{scope}
    \clip (-1.15,0) circle (1.7cm);
    \fill[pattern=north east lines, pattern color=black!75]
      (1.15,0) circle (1.7cm);
  \end{scope}
  \draw (-1.15,0) circle (1.7cm);
  \draw (1.15,0) circle (1.7cm);
  \node[above=5pt] at (-1.15,1.7) {$M=m$};
  \node[above=5pt] at (1.15,1.7) {$C=c$};
  \node[below, align=center] (intersecao) at (0,-2.0)
    {$\{M=m\}\cap\{C=c\}$};
  \draw[->] (intersecao.north) -- (0,-0.65);
\end{tikzpicture}
\par\smallskip
{\small A probabilidade dessa interseção é $\Pr[M=m\wedge C=c]$.\\
As áreas são esquemáticas, sem escala de probabilidade.\par}
\end{minipage}
\end{center}

Ler dos dois lados:

- $\Pr[C=c]\cdot\Pr[M=m \mid C=c]$ — pega o disco $C=c$ inteiro, fica com a fatia dele que também é $M=m$.
- $\Pr[M=m]\cdot\Pr[C=c \mid M=m]$ — pega o disco $M=m$ inteiro, fica com a fatia dele que também é $C=c$.

As duas rotas chegam na mesma área hachurada — daí a igualdade.

### Exemplo 2.4 — Shift Cipher NÃO é perfeito

Suponha $\mathcal{M} = \{\texttt{aa}, \texttt{ab}\}$ com distribuição uniforme, isto é
$\Pr[M=\texttt{aa}] = \Pr[M=\texttt{ab}] = \tfrac{1}{2}$. Tome $c = \texttt{XX}$.
Como o **mesmo** shift $k$ é aplicado às duas letras, $c=\texttt{XX}$ só pode vir de uma
mensagem com as duas letras iguais ($\texttt{aa}, \texttt{bb}, \dots$):

$$
\Pr[M=\texttt{ab} \mid C=\texttt{XX}] = 0
\qquad\text{mas}\qquad
\Pr[M=\texttt{ab}] = \tfrac{1}{2} \neq 0
$$

Viola a definição.

---

## Lema 2.5

$(\mathrm{Gen},\mathrm{Enc},\mathrm{Dec})$ é perfeitamente secreto **se e somente se**
para todos $m, m' \in \mathcal{M}$ e todo $c \in \mathcal{C}$:

$$
\underbrace{\Pr[\mathrm{Enc}_K(m) = c]}_{p_c} \;=\; \underbrace{\Pr[\mathrm{Enc}_K(m') = c]}_{p_{c'}}
$$

(probabilidade sobre a escolha aleatória de $K$).

**Cuidado com a notação:** $\Pr[\mathrm{Enc}_K(M) = c \mid M=m]$ é o mesmo que
$\Pr[\mathrm{Enc}_K(m) = c \mid M=m]$, que por independência de $K$ e $M$ é
$\Pr[\mathrm{Enc}_K(m)=c]$.

### Prova (esboço)

$$
\begin{aligned}
\Pr[C=c \mid M=m]
&= \Pr[\mathrm{Enc}_K(M) = c \mid M = m] \\
&= \Pr[\mathrm{Enc}_K(m) = c \mid M = m] \\
&= \Pr[\mathrm{Enc}_K(m) = c]
\end{aligned}
$$

E, pela lei da probabilidade total,

$$
\begin{aligned}
\Pr[C=c]
&= \sum_{m' \in \mathcal{M}} \Pr[C=c \mid M=m']\cdot \Pr[M=m'] \\
&= \sum_{m' \in \mathcal{M}} \Pr[\mathrm{Enc}_K(m') = c]\cdot \Pr[M=m'] \\
&= \Pr[\mathrm{Enc}_K(m) = c] \cdot \underbrace{\sum_{m' \in \mathcal{M}} \Pr[M=m']}_{=\,1} \\
&= \Pr[\mathrm{Enc}_K(m) = c] \;=\; \Pr[C=c\mid M=m]
\end{aligned}
$$

onde o passo chave é justamente a hipótese $p_c = p_{c'}$ (o valor não depende de $m'$,
então sai do somatório). Conclusão: $p_c = \Pr[C=c] = p_{c'}$ — todas as mensagens
induzem a mesma distribuição de cifrados.

---

## Experimento do adversário (jogo de indistinguibilidade)

$$
\begin{array}{ccc}
\textbf{Adv} & \xrightarrow{\;\;m_0,\,m_1\;\;} & \textbf{ORACLE} \\[2pt]
             & \xleftarrow{\;\;\;\;c\;\;\;\;}  & b \xleftarrow{R} \{0,1\} \\[2pt]
\text{guess } b' & & c = \mathrm{Enc}_K(m_b)
\end{array}
$$

1. O adversário escolhe $m_0, m_1$ e envia ao oráculo.
2. O oráculo sorteia $b \in_R \{0,1\}$, gera $k \leftarrow \mathrm{Gen}$, devolve $c = \mathrm{Enc}_k(m_b)$.
3. O adversário devolve um palpite $b'$.

O adversário **vence** se $b' = b$. Ele não deve conseguir distinguir se $c$ cifra
$m_0$ ou $m_1$ — sua probabilidade de acerto deve ser a de um cara-ou-coroa, $1/2$,
já que são duas mensagens.

### Def. 2.6 + Lema 2.7

$(\mathrm{Gen},\mathrm{Enc},\mathrm{Dec})$ é encriptação perfeita **se e somente se**

$$
\Pr[\text{Adv vence}] = \frac{1}{2}
$$

---

## One-Time Pad

$$
\mathcal{M} = \mathcal{K} = \mathcal{C} = \{0,1\}^{\ell}
$$

- $\mathrm{Gen}$: $k \in_R \{0,1\}^{\ell}$ (uniforme)
- $c := \mathrm{Enc}_k(m) = m \oplus k$
- $m' := \mathrm{Dec}_k(c) = c \oplus k$

### Prova de sigilo perfeito

$$
\begin{aligned}
\Pr[C = c \mid M = m]
&= \Pr[K \oplus m = c \mid M=m] \\
&= \Pr[K = m \oplus c \mid M=m] \\
&= 2^{-\ell}
\end{aligned}
$$

pois $K$ é uniforme em $\{0,1\}^{\ell}$ e $m \oplus c$ é um valor fixo.

$$
\begin{aligned}
\Pr[C=c]
&= \sum_{m \in \mathcal{M}} \underbrace{\Pr[C=c\mid M=m]}_{=\,2^{-\ell}\ \text{(acima)}} \cdot \Pr[M=m] \\
&= 2^{-\ell} \underbrace{\sum_{m\in\mathcal{M}} \Pr[M=m]}_{=\,1}
 \;=\; 2^{-\ell}
\end{aligned}
$$

Logo $\Pr[C=c \mid M=m] = \Pr[C=c]$ — sigilo perfeito.

---

## Teorema 2.11 — $|\mathcal{K}| \geq |\mathcal{M}|$

Se $(\mathrm{Gen},\mathrm{Enc},\mathrm{Dec})$ é perfeitamente secreto, então
$|\mathcal{K}| \geq |\mathcal{M}|$ (limite de tamanho).

**Prova (por contradição).** Suponha $|\mathcal{K}| < |\mathcal{M}|$.

Defina o conjunto de mensagens alcançáveis a partir de $c$:

$$
\mathcal{M}(c) = \{\, m \in \mathcal{M} \;:\; \mathrm{Enc}_k(m) = c \ \text{ para algum } k \,\}
$$

Cada chave produz no máximo uma mensagem em $\mathcal{M}(c)$, logo

$$
|\mathcal{M}(c)| \leq |\mathcal{K}| < |\mathcal{M}|
$$

\begin{center}
\begin{minipage}{\linewidth}
\centering
Então existe uma mensagem $m'\in\mathcal{M}$ fora de $\mathcal{M}(c)$:
\par\medskip
\begin{tikzpicture}[line width=0.8pt, font=\normalsize]
  \draw (0,0) ellipse (3.3cm and 1.65cm);
  \node[above=5pt] at (0,1.65) {$\mathcal{M}$: todas as mensagens};
  \filldraw[fill=black!8] (-1.1,0) ellipse (1.55cm and 1.1cm);
  \node at (-1.1,0.3) {$\mathcal{M}(c)$};
  \node at (-1.1,-0.3) {$|\mathcal{M}(c)|\leq|\mathcal{K}|$};
  \fill (1.7,0) circle (2pt) node[above right=3pt] {$m'$};
\end{tikzpicture}
\par\smallskip
{\small $m'\in\mathcal{M}$ e $m'\notin\mathcal{M}(c)$: nenhuma chave cifra $m'$ como $c$.\par}
\end{minipage}
\end{center}

$\mathcal{M}(c)$ contém as mensagens que podem gerar $c$. Como tem menos elementos
que $\mathcal{M}$, algum $m'$ fica de fora. Para esse $m'$:

$$
\Pr[M = m' \mid C = c] = 0 \;\neq\; \Pr[M = m']
$$

o que **viola a definição de sigilo perfeito**.

> Conclusão: a cardinalidade do espaço de chaves tem que ser pelo menos a do espaço
> de mensagens — a chave precisa ser tão longa quanto a mensagem (como no OTP).
