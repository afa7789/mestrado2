---
author:  Jeroen van de Graaf
title: Gabarito P1 Turma Z
institute: DCC/UFMG
aspectratio: 169
header-includes:
      - \usepackage{epsdice}
# pandoc file.md -o file.pdf
---





### Questão 1

**a)** $99999/9=11111; 9999/9 =1111; 11111-1111=10000$

**b)** 

$10000+18000-2000=26000$

**(c)**

$9 \cdot 9 \cdot 8 \cdot 7 \cdot 6 = 27216$

**(d)**

$100+90+90=280$

### Questão 2

**(a)**

$x_1+x_2+x_3+x_4+x_5=9$ com $1 \leq x_1 \leq 9\ ;\ 0 \leq x_1 \leq 9$ dando $C(5-1+8,8)=C(12,4)=495$

**(b)**

Um dígito não pode ser maior que $9$ então $C(20,17)- C(11,8) - 3 \cdot C(10,7)$

**(c)**

Igual MegaSena: escolher 5 dígitos do conjunto $\{9,8,7,6,5,4,3,2,1,0\}\rightarrow C(10,5)=525$

### Questão 3

$|A|=20$, portanto existem $2^{20}$ possíveis subconjuntos $B\subseteq A$, e portanto $2^{20}$ somas diferente. Mas $2^{20} = (2^{10})^2 = 1024^2 > 1\ 000\ 000$, o último sendo o número de possibilidades considerando os últimos seis dígitos das somas. 

\newpage

### Questão 4

**(a)**

Considere um exemplo:
$$
\dfrac{\binom{10}{7}}{\binom{9}{6}}=\dfrac{\frac{10!}{7!3!}}{\frac{9!}{6!3!}}=\dfrac{10!}{9!}\dfrac{6!}{7!}=\dfrac{10}{7}
$$
Analogamente obtemos
$$
\dfrac{\binom{n}{k}}{\binom{n-1}{k-1}}=\dfrac{\frac{n!}{k!(n-k)!}}{\frac{(n-1)!}{(k-1)!((n-1)-(k-1))!}}=\dfrac{n!}{(n-1)!}\dfrac{(k-1)!}{k!}=\dfrac{n}{k}
$$
**(b)**
$$
\dfrac{n-k+1}{k}
$$

### Questão 5

**(a)**
$$
(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k}y^k \rightarrow x^{15-k}=x^8 \rightarrow k=7 \rightarrow \binom{15}{7}\cdot (2)^8 \cdot (-1)^7
$$
**(b)**

$$
\binom{15}{4} \cdot 2^{11}
$$

### Questão 6

**(a)**

Fica obvio que  $f(x) \in O(x^3)$ então o foco é encontrar as constantes da definição. Existem várias escolhas.



**(b)**

Numerador: $4n^2+10 \leq 4n^2+4n^2$; denominador: $\dfrac{1}{n+ \log n} \leq \dfrac{1}{n}$.

Portanto $f(n) \leq \dfrac{8n^2}{n} = 8n$.  Então $f(n) \in O(n)$ com $C=8$ para $n \geq 1$

Um erro comum é calcular o denominador errado: $n + \log n \leq 2n$, mas $\dfrac{1}{n+ \log n} \not \leq \dfrac{1}{2n}$; para $n=1$ temos $\dfrac{1}{1+0} \not \leq \dfrac{1}{2 \cdot 1}$.



### Questão 7

Multiplicando todos os termos, percebe-se que $n^2 \log^2 n = n^2 (\log n)^2$ é a maior ordem.

### Questão 8

**(a)** $O(n^3 \log n)$

**(b)** $O(n^{2^n})$

