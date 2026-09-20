# QAP do zero ao hero --- versão detalhada

> Guia complementar ao texto **"Quadratic Arithmetic Programs: from Zero
> to Hero"**, de Vitalik Buterin.
>
> Objetivo: tornar explícitas as etapas que o texto original comprime,
> principalmente:
>
> 1.  código → flattening;
> 2.  flattening → gates;
> 3.  gates → R1CS `(A, B, C)`;
> 4.  R1CS → interpolação de Lagrange;
> 5.  interpolação → polinômios `A_i(x), B_i(x), C_i(x)`;
> 6.  polinômios → teste QAP;
> 7.  `t(x) = A(x)B(x)-C(x)` → divisibilidade por `Z(x)`.
>
> O exemplo inteiro usa:
>
> ``` text
> qeval(x):
>     y = x^3
>     return x + y + 5
> ```
>
> com `x = 3`.

------------------------------------------------------------------------

## 1. A ideia geral

O pipeline pode ser visto assim:

``` mermaid
flowchart LR
    P["Programa<br/>y = x³<br/>out = x + y + 5"]
    F["Flattening<br/>4 operações simples"]
    G["Gates<br/>4 gates aritméticos"]
    R["R1CS<br/>4 constraints<br/>A, B, C"]
    I["Interpolação de Lagrange<br/>por coluna"]
    Q["QAP<br/>polinômios Aᵢ, Bᵢ, Cᵢ"]
    T["t(x) = A(x)B(x) - C(x)"]
    Z["Z(x)<br/>zera nos pontos dos gates"]
    V["Verificação<br/>Z(x) divide t(x)"]

    P --> F --> G --> R --> I --> Q --> T
    T --> V
    Z --> V
```

A informação **não aparece magicamente** quando chegamos ao QAP. Ela é a
mesma informação do R1CS, apenas reorganizada.

A mudança fundamental é:

``` text
R1CS:
    muitas constraints separadas

QAP:
    uma única identidade polinomial
    que precisa ser válida simultaneamente nos pontos
    associados às constraints.
```

------------------------------------------------------------------------

# 2. O exemplo original

O programa é:

``` text
y = x^3
return x + y + 5
```

Para `x = 3`:

``` text
y   = 3³ = 27
out = 3 + 27 + 5
    = 35
```

Portanto:

``` text
x   = 3
y   = 27
out = 35
```

Mas o zk-SNARK não quer simplesmente receber esses três números.

Precisamos transformar o cálculo em uma estrutura que permita verificar:

> "Existe uma atribuição de valores intermediários que faz todas as
> operações serem consistentes?"

------------------------------------------------------------------------

# 3. Flattening

O primeiro passo é quebrar expressões complexas em operações simples.

O código original:

``` text
y = x^3
return x + y + 5
```

vira:

``` text
sym_1 = x * x
y     = sym_1 * x
sym_2 = y + x
~out  = sym_2 + 5
```

Cada linha agora pode ser tratada como um gate.

``` mermaid
flowchart LR
    X["x = 3"]
    G1["Gate 1<br/>sym_1 = x × x"]
    G2["Gate 2<br/>y = sym_1 × x"]
    G3["Gate 3<br/>sym_2 = y + x"]
    G4["Gate 4<br/>out = sym_2 + 5"]

    X --> G1 --> G2 --> G3 --> G4
```

A execução é:

``` text
x     = 3

sym_1 = 3 × 3
      = 9

y     = 9 × 3
      = 27

sym_2 = 27 + 3
      = 30

out   = 30 + 5
      = 35
```

O witness será construído a partir exatamente desses valores.

------------------------------------------------------------------------

# 4. O que é um gate aqui?

Um ponto importante que o texto original passa relativamente rápido:

> O "gate" não é ainda um vetor.

O gate é a **operação aritmética** que queremos impor.

Por exemplo:

``` text
Gate 1:

sym_1 = x × x
```

Podemos pensar:

``` text
left  = x
right = x
out   = sym_1
```

Outro:

``` text
Gate 3:

sym_2 = y + x
```

Aqui temos:

``` text
left  = y + x
right = 1
out   = sym_2
```

Essa segunda representação é importante porque o R1CS só possui a forma:

``` text
(A · s) × (B · s) = C · s
```

Ou seja, precisamos transformar qualquer operação em:

``` text
algo × algo = resultado
```

Para uma soma:

``` text
y + x = sym_2
```

usamos:

``` text
(y + x) × 1 = sym_2
```

É exatamente daí que aparecem os vetores `A`, `B` e `C`.

------------------------------------------------------------------------

# 5. Antes do R1CS: precisamos escolher as variáveis

O R1CS trabalha com um vetor global de variáveis.

O texto escolhe esta ordem:

``` text
index:    0       1       2        3       4      5

         ~one     x      ~out    sym_1     y     sym_2
```

Ou seja:

``` text
s = [
    ~one,
    x,
    ~out,
    sym_1,
    y,
    sym_2
]
```

O `~one` é uma variável especial:

``` text
~one = 1
```

Ela permite representar constantes e transformar somas em multiplicações
por `1`.

Para o exemplo:

``` text
x     = 3
out   = 35
sym_1 = 9
y     = 27
sym_2 = 30
```

Então o witness é:

``` text
s = [1, 3, 35, 9, 27, 30]
```

O texto original apresenta exatamente esse witness.
fileciteturn0file0L103-L109

------------------------------------------------------------------------

# 6. Como um gate vira A, B e C?

Esta é uma das etapas que vale a pena deixar explícita.

Considere:

``` text
s = [1, 3, 35, 9, 27, 30]
      ↑  ↑   ↑   ↑   ↑   ↑
     one x  out sym1  y sym2
```

Um vetor R1CS não guarda diretamente o valor da variável.

Ele guarda **coeficientes que selecionam ou combinam variáveis**.

A operação:

``` text
x
```

pode ser representada por:

``` text
[0, 1, 0, 0, 0, 0]
```

porque:

``` text
[0,1,0,0,0,0] · s
=
0·1 + 1·x + 0·out + ...
=
x
```

A operação:

``` text
y + x
```

vira:

``` text
[0, 1, 0, 0, 1, 0]
```

porque:

``` text
[0,1,0,0,1,0] · s
=
x + y
```

A constante `1` vira:

``` text
[1,0,0,0,0,0]
```

porque:

``` text
[1,0,0,0,0,0] · s
=
1
```

E `sym_2 + 5` pode ser:

``` text
[5,0,0,0,0,1]
```

porque:

``` text
[5,0,0,0,0,1] · s
=
5·1 + sym_2
=
5 + sym_2
```

------------------------------------------------------------------------

# 7. Gate 1 → R1CS

Gate:

``` text
sym_1 = x × x
```

Queremos:

``` text
x × x = sym_1
```

Portanto:

``` text
A₁ = [0,1,0,0,0,0]
B₁ = [0,1,0,0,0,0]
C₁ = [0,0,0,1,0,0]
```

Visualmente:

``` text
             s
             │
       ┌─────┴─────┐
       │            │
      A₁           B₁
       │            │
      x            x
       └─────×──────┘
             │
          sym_1
             ↑
            C₁
```

Matematicamente:

``` text
(A₁ · s)(B₁ · s) = C₁ · s

x × x = sym_1
```

Com o witness:

``` text
A₁ · s = 3
B₁ · s = 3
C₁ · s = 9

3 × 3 = 9
```

------------------------------------------------------------------------

# 8. Gate 2 → R1CS

Gate:

``` text
y = sym_1 × x
```

Queremos:

``` text
sym_1 × x = y
```

Então:

``` text
A₂ = [0,0,0,1,0,0]
B₂ = [0,1,0,0,0,0]
C₂ = [0,0,0,0,1,0]
```

Porque:

``` text
A₂ · s = sym_1 = 9
B₂ · s = x     = 3
C₂ · s = y     = 27
```

Logo:

``` text
9 × 3 = 27
```

------------------------------------------------------------------------

# 9. Gate 3 → R1CS

Gate:

``` text
sym_2 = y + x
```

O R1CS quer multiplicação, então escrevemos:

``` text
(y + x) × 1 = sym_2
```

Agora fica claro por que precisamos de `~one`.

Temos:

``` text
A₃ = [0,1,0,0,1,0]
B₃ = [1,0,0,0,0,0]
C₃ = [0,0,0,0,0,1]
```

Logo:

``` text
A₃ · s = x + y
       = 3 + 27
       = 30

B₃ · s = 1

C₃ · s = sym_2
       = 30
```

Portanto:

``` text
30 × 1 = 30
```

------------------------------------------------------------------------

# 10. Gate 4 → R1CS

Gate:

``` text
out = sym_2 + 5
```

Transformamos:

``` text
(sym_2 + 5) × 1 = out
```

Então:

``` text
A₄ = [5,0,0,0,0,1]
B₄ = [1,0,0,0,0,0]
C₄ = [0,0,1,0,0,0]
```

Com o witness:

``` text
A₄ · s = 5 + 30 = 35
B₄ · s = 1
C₄ · s = 35
```

Logo:

``` text
35 × 1 = 35
```

O texto original lista os quatro gates e seus vetores `A`, `B`, `C`
exatamente dessa forma. fileciteturn0file0L53-L61
fileciteturn0file0L63-L101

------------------------------------------------------------------------

# 11. Agora sim: o R1CS completo

Temos quatro constraints.

É importante perceber a diferença entre:

``` text
A₁, B₁, C₁
A₂, B₂, C₂
A₃, B₃, C₃
A₄, B₄, C₄
```

e as matrizes:

``` text
A
B
C
```

As matrizes simplesmente colocam os vetores de cada constraint como
linhas.

``` text
A =

[ 0 1 0 0 0 0 ]   ← constraint 1
[ 0 0 0 1 0 0 ]   ← constraint 2
[ 0 1 0 0 1 0 ]   ← constraint 3
[ 5 0 0 0 0 1 ]   ← constraint 4
```

``` text
B =

[ 0 1 0 0 0 0 ]
[ 0 1 0 0 0 0 ]
[ 1 0 0 0 0 0 ]
[ 1 0 0 0 0 0 ]
```

``` text
C =

[ 0 0 0 1 0 0 ]
[ 0 0 0 0 1 0 ]
[ 0 0 0 0 0 1 ]
[ 0 0 1 0 0 0 ]
```

O texto apresenta justamente essas três matrizes.
fileciteturn0file0L111-L130

A condição do R1CS é:

``` text
(A · s) ⊙ (B · s) = C · s
```

onde `⊙` é multiplicação elemento a elemento.

Para nosso witness:

``` text
A · s = [3, 9, 30, 35]

B · s = [3, 3, 1, 1]

C · s = [9, 27, 30, 35]
```

Portanto:

``` text
[3, 9, 30, 35]
        ⊙
[3, 3, 1, 1]
        =
[9, 27, 30, 35]
```

ou:

``` text
3  × 3  = 9
9  × 3  = 27
30 × 1  = 30
35 × 1  = 35
```

Esse é o R1CS.

------------------------------------------------------------------------

# 12. A transição importante: R1CS → QAP

Agora vem a parte que normalmente parece "mágica".

Temos:

``` text
4 constraints
×
6 variáveis
```

O R1CS pode ser visualizado como:

``` text
             variáveis
           one x out s1 y s2
            ↓  ↓  ↓  ↓  ↓  ↓

constraint 1   0  1  0  0  0  0
constraint 2   0  0  0  1  0  0
constraint 3   0  1  0  0  1  0
constraint 4   5  0  0  0  0  1
```

A ideia do QAP é trocar:

``` text
4 linhas de valores
```

por:

``` text
polinômios que reproduzem essas 4 linhas
```

E aqui está o ponto mais importante:

> **A interpolação é feita coluna por coluna, não linha por linha.**

------------------------------------------------------------------------

# 13. Por que aparecem os pontos 1, 2, 3, 4?

Associamos cada constraint a uma coordenada `x`:

``` text
constraint 1 → x = 1
constraint 2 → x = 2
constraint 3 → x = 3
constraint 4 → x = 4
```

Portanto:

``` text
x-coordinate:

1     2     3     4
│     │     │     │
│     │     │     │
C1    C2    C3    C4
```

Esses pontos não são valores do witness.

Eles são apenas **rótulos matemáticos para as constraints**.

Isso é crucial.

``` text
x = 1
```

no QAP não significa:

``` text
input = 1
```

Significa:

``` text
"estamos olhando para a constraint 1"
```

Da mesma maneira:

``` text
x = 2 → constraint 2
x = 3 → constraint 3
x = 4 → constraint 4
```

O texto explica que avaliar os polinômios nesses pontos recupera as
constraints correspondentes. fileciteturn0file0L133-L137

------------------------------------------------------------------------

# 14. O que exatamente é interpolado?

Pegue a primeira coluna de `A`.

``` text
A:

[0 1 0 0 0 0]
[0 0 0 1 0 0]
[0 1 0 0 1 0]
[5 0 0 0 0 1]
 ↑
 coluna do ~one
```

Essa coluna é:

``` text
[0, 0, 0, 5]
```

Agora associamos os valores aos pontos das constraints:

``` text
x    valor

1 → 0
2 → 0
3 → 0
4 → 5
```

Queremos um polinômio `A₀(x)` que satisfaça:

``` text
A₀(1) = 0
A₀(2) = 0
A₀(3) = 0
A₀(4) = 5
```

Esse polinômio é obtido por interpolação de Lagrange.

------------------------------------------------------------------------

# 15. Outro exemplo: coluna do x

Agora pegue a coluna de `x`:

``` text
A:

[0 1 0 0 0 0]
[0 0 0 1 0 0]
[0 1 0 0 1 0]
[5 0 0 0 0 1]
    ↑
    x
```

Os valores são:

``` text
constraint 1 → 1
constraint 2 → 0
constraint 3 → 1
constraint 4 → 0
```

Portanto queremos um polinômio `A₁(x)` tal que:

``` text
A₁(1) = 1
A₁(2) = 0
A₁(3) = 1
A₁(4) = 0
```

Observe novamente:

``` text
1, 2, 3, 4
```

são posições das constraints.

Enquanto:

``` text
1, 0, 1, 0
```

são os coeficientes daquela coluna.

------------------------------------------------------------------------

# 16. Visualização completa da interpolação

A matriz:

``` text
A

             variável
          one x out s1 y s2

gate 1     0   1  0  0  0  0
gate 2     0   0  0  1  0  0
gate 3     0   1  0  0  1  0
gate 4     5   0  0  0  0  1
```

vira:

``` mermaid
flowchart TD
    M["Matriz A<br/>4 constraints × 6 variáveis"]

    C0["coluna one<br/>[0,0,0,5]"]
    C1["coluna x<br/>[1,0,1,0]"]
    C2["coluna out<br/>[0,0,0,0]"]
    C3["coluna sym_1<br/>[0,1,0,0]"]
    C4["coluna y<br/>[0,0,1,0]"]
    C5["coluna sym_2<br/>[0,0,0,1]"]

    P0["polinômio A₀(x)"]
    P1["polinômio A₁(x)"]
    P2["polinômio A₂(x)"]
    P3["polinômio A₃(x)"]
    P4["polinômio A₄(x)"]
    P5["polinômio A₅(x)"]

    M --> C0 --> P0
    M --> C1 --> P1
    M --> C2 --> P2
    M --> C3 --> P3
    M --> C4 --> P4
    M --> C5 --> P5
```

O mesmo processo é executado para `B` e `C`.

Portanto:

``` text
A matrix → A₀(x), A₁(x), ..., A₅(x)

B matrix → B₀(x), B₁(x), ..., B₅(x)

C matrix → C₀(x), C₁(x), ..., C₅(x)
```

O texto original diz explicitamente que se pega "o primeiro valor de
cada vetor", interpola-se, depois o segundo valor de cada vetor, e assim
por diante. fileciteturn0file0L174-L204

------------------------------------------------------------------------

# 17. Lagrange: o mecanismo

Para quatro pontos:

``` text
x = 1, 2, 3, 4
```

definimos quatro polinômios base.

Para o ponto `1`:

``` text
L₁(x) =
    (x-2)(x-3)(x-4)
    -----------------
    (1-2)(1-3)(1-4)
```

Para o ponto `2`:

``` text
L₂(x) =
    (x-1)(x-3)(x-4)
    -----------------
    (2-1)(2-3)(2-4)
```

Para o ponto `3`:

``` text
L₃(x) =
    (x-1)(x-2)(x-4)
    -----------------
    (3-1)(3-2)(3-4)
```

Para o ponto `4`:

``` text
L₄(x) =
    (x-1)(x-2)(x-3)
    -----------------
    (4-1)(4-2)(4-3)
```

Essas bases possuem a propriedade:

``` text
Lᵢ(j) = 1  se i = j
Lᵢ(j) = 0  se i ≠ j
```

Ou seja, cada uma "acende" em apenas um ponto.

------------------------------------------------------------------------

# 18. Por que isso é útil?

Suponha que queremos representar:

``` text
[1, 0, 1, 0]
```

nos pontos:

``` text
1, 2, 3, 4
```

Podemos escrever:

``` text
P(x) = 1·L₁(x)
     + 0·L₂(x)
     + 1·L₃(x)
     + 0·L₄(x)
```

Então:

``` text
P(1) = 1
P(2) = 0
P(3) = 1
P(4) = 0
```

É exatamente a coluna que queríamos reproduzir.

Portanto, a interpolação não está criando informação nova.

Ela está criando uma função polinomial que **codifica a mesma coluna**.

------------------------------------------------------------------------

# 19. O QAP preserva o R1CS

Podemos pensar assim:

``` text
R1CS

constraint 1 → vetor
constraint 2 → vetor
constraint 3 → vetor
constraint 4 → vetor
```

Depois:

``` text
QAP

x = 1 → valores da constraint 1
x = 2 → valores da constraint 2
x = 3 → valores da constraint 3
x = 4 → valores da constraint 4
```

Então:

``` text
                  MESMA INFORMAÇÃO

R1CS                                      QAP

A₁ = [0,1,0,0,0,0]        ←→        A₀(1), A₁(1), ..., A₅(1)
A₂ = [0,0,0,1,0,0]        ←→        A₀(2), A₁(2), ..., A₅(2)
A₃ = [0,1,0,0,1,0]        ←→        A₀(3), A₁(3), ..., A₅(3)
A₄ = [5,0,0,0,0,1]        ←→        A₀(4), A₁(4), ..., A₅(4)
```

A grande vantagem é que agora podemos fazer álgebra polinomial em vez de
verificar quatro constraints separadamente.

------------------------------------------------------------------------

# 20. De onde vêm os polinômios mostrados no artigo?

O texto fornece:

``` text
A polynomials

[-5.0, 9.166, -5.0, 0.833]
[ 8.0,-11.333,  5.0,-0.666]
[ 0.0, 0.0,     0.0, 0.0]
[-6.0, 9.5,    -4.0, 0.5]
[ 4.0,-7.0,     3.5,-0.5]
[-1.0, 1.833,  -1.0, 0.166]
```

Os coeficientes estão em ordem crescente:

``` text
[a₀, a₁, a₂, a₃]
```

significa:

``` text
a₀ + a₁x + a₂x² + a₃x³
```

Por exemplo:

``` text
A₀(x)
=
-5
+ 9.166x
- 5x²
+ 0.833x³
```

Esse é o polinômio correspondente à primeira coluna de `A`, isto é:

``` text
A₀(1) = 0
A₀(2) = 0
A₀(3) = 0
A₀(4) = 5
```

O artigo lista os coeficientes desses polinômios diretamente após
explicar o processo de interpolação. fileciteturn0file0L176-L204

------------------------------------------------------------------------

# 21. Por que cada polinômio tem grau 3?

Temos quatro pontos:

``` text
1, 2, 3, 4
```

Um polinômio de grau no máximo:

``` text
4 - 1 = 3
```

é suficiente para passar pelos quatro pontos.

Logo:

``` text
4 constraints
        ↓
polinômios de grau ≤ 3
```

Se tivéssemos:

``` text
n constraints
```

teríamos, em geral:

``` text
polinômios de grau ≤ n-1
```

------------------------------------------------------------------------

# 22. Avaliar o QAP recupera o R1CS

Considere `x = 1`.

Pegamos todos os polinômios de `A` e avaliamos:

``` text
A₀(1)
A₁(1)
A₂(1)
A₃(1)
A₄(1)
A₅(1)
```

O resultado é:

``` text
[0, 1, 0, 0, 0, 0]
```

que é exatamente:

``` text
A₁
```

a primeira linha da matriz `A`.

Em `x = 2`:

``` text
[A₀(2), A₁(2), ..., A₅(2)]
=
[0,0,0,1,0,0]
```

que é a segunda constraint.

Em geral:

``` text
[A₀(k), A₁(k), ..., A₅(k)]
=
A_k
```

com a indexação conceitual `k = constraint`.

O mesmo vale para `B` e `C`.

O próprio artigo faz essa verificação para `x = 1`.
fileciteturn0file0L204-L234

------------------------------------------------------------------------

# 23. Agora vem o passo mais importante do QAP

No R1CS tínhamos:

``` text
(A₁ · s)(B₁ · s) = C₁ · s

(A₂ · s)(B₂ · s) = C₂ · s

(A₃ · s)(B₃ · s) = C₃ · s

(A₄ · s)(B₄ · s) = C₄ · s
```

Quatro equações.

No QAP construímos:

``` text
A(x) = Σ Aᵢ(x)sᵢ

B(x) = Σ Bᵢ(x)sᵢ

C(x) = Σ Cᵢ(x)sᵢ
```

Aqui o índice `i` percorre as **variáveis do witness**.

Então:

``` text
A(x) = A₀(x)·s₀
     + A₁(x)·s₁
     + ...
     + A₅(x)·s₅
```

e analogamente para `B(x)` e `C(x)`.

Essa é a versão polinomial do produto matriz-vetor.

------------------------------------------------------------------------

# 24. A conexão exata com A · s

No R1CS:

``` text
A · s
```

produz quatro valores:

``` text
[
  A₁·s,
  A₂·s,
  A₃·s,
  A₄·s
]
```

No QAP:

``` text
A(x) = Σ Aᵢ(x)sᵢ
```

é um polinômio tal que:

``` text
A(1) = A₁·s
A(2) = A₂·s
A(3) = A₃·s
A(4) = A₄·s
```

Portanto:

``` text
             R1CS                  QAP

constraint 1   A₁·s       ←→       A(1)
constraint 2   A₂·s       ←→       A(2)
constraint 3   A₃·s       ←→       A(3)
constraint 4   A₄·s       ←→       A(4)
```

E isso vale para `B` e `C`.

------------------------------------------------------------------------

# 25. O teste QAP

No R1CS, queremos:

``` text
(A·s) ⊙ (B·s) = C·s
```

No QAP, construímos:

``` text
t(x) = A(x)B(x) - C(x)
```

Nos pontos dos gates:

``` text
t(1) = 0
t(2) = 0
t(3) = 0
t(4) = 0
```

porque nesses pontos o QAP reproduz exatamente as quatro constraints do
R1CS.

Portanto:

``` text
R1CS satisfeito
      ↓
t(1)=t(2)=t(3)=t(4)=0
```

------------------------------------------------------------------------

# 26. Por que aparece Z(x)?

Queremos um polinômio que tenha exatamente esses pontos como raízes:

``` text
1, 2, 3, 4
```

Construímos:

``` text
Z(x) = (x-1)(x-2)(x-3)(x-4)
```

Expandindo:

``` text
Z(x) = x⁴ - 10x³ + 35x² - 50x + 24
```

Em coeficientes crescentes:

``` text
Z = [24, -50, 35, -10, 1]
```

que é exatamente o `Z` apresentado no texto.
fileciteturn0file0L260-L272

Visualmente:

``` text
Z(1) = 0
Z(2) = 0
Z(3) = 0
Z(4) = 0
```

------------------------------------------------------------------------

# 27. A condição final

Se:

``` text
t(1)=t(2)=t(3)=t(4)=0
```

então `t(x)` possui todas essas raízes.

Logo:

``` text
Z(x) | t(x)
```

ou seja:

``` text
t(x) = h(x) Z(x)
```

para algum polinômio `h(x)`.

Portanto a verificação do QAP pode ser expressa como:

``` text
A(x)B(x) - C(x)
-------------------- = h(x)
       Z(x)
```

com divisão sem resto.

O texto original descreve justamente essa equivalência entre zerar nos
pontos dos gates e ser múltiplo de `Z(x)`.
fileciteturn0file0L236-L277

------------------------------------------------------------------------

# 28. Fluxo completo, sem pular etapas

``` mermaid
flowchart TD
    P["Programa<br/>y = x³<br/>out = x + y + 5"]

    F["Flattening<br/><br/>sym₁ = x·x<br/>y = sym₁·x<br/>sym₂ = y+x<br/>out = sym₂+5"]

    V["Variáveis globais<br/><br/>s = [one, x, out, sym₁, y, sym₂]"]

    W["Witness<br/><br/>s = [1, 3, 35, 9, 27, 30]"]

    R1["Gate 1<br/>x·x = sym₁"]
    R2["Gate 2<br/>sym₁·x = y"]
    R3["Gate 3<br/>(y+x)·1 = sym₂"]
    R4["Gate 4<br/>(sym₂+5)·1 = out"]

    R["R1CS<br/><br/>(A₁·s)(B₁·s)=C₁·s<br/>...<br/>(A₄·s)(B₄·s)=C₄·s"]

    M["Matrizes A, B, C<br/>4 × 6"]

    I["Interpolar cada coluna<br/>nos pontos 1,2,3,4"]

    Q["Polinômios<br/>Aᵢ(x), Bᵢ(x), Cᵢ(x)"]

    AS["A(x)=Σ Aᵢ(x)sᵢ<br/>B(x)=Σ Bᵢ(x)sᵢ<br/>C(x)=Σ Cᵢ(x)sᵢ"]

    T["t(x)=A(x)B(x)-C(x)"]

    Z["Z(x)=(x-1)(x-2)(x-3)(x-4)"]

    H["t(x)=h(x)Z(x)<br/>divisão sem resto"]

    P --> F
    F --> V
    F --> R1
    F --> R2
    F --> R3
    F --> R4

    V --> W
    R1 --> R
    R2 --> R
    R3 --> R
    R4 --> R

    R --> M --> I --> Q --> AS --> T
    T --> H
    Z --> H
    W --> AS
```

------------------------------------------------------------------------

# 29. O ponto que costuma causar confusão

Existem **dois tipos diferentes de índice** acontecendo.

## Índice das variáveis

No witness:

``` text
s = [
  s₀, s₁, s₂, s₃, s₄, s₅
]
```

representando:

``` text
s₀ = one
s₁ = x
s₂ = out
s₃ = sym₁
s₄ = y
s₅ = sym₂
```

Os polinômios:

``` text
A₀(x), A₁(x), ..., A₅(x)
```

correspondem a essas variáveis.

------------------------------------------------------------------------

## Índice das constraints

Os pontos:

``` text
x = 1
x = 2
x = 3
x = 4
```

correspondem às quatro constraints.

Assim:

``` text
Aᵢ(1)
```

significa o coeficiente da variável `i` na constraint 1.

Enquanto:

``` text
Aᵢ(3)
```

significa o coeficiente da variável `i` na constraint 3.

Essa distinção resolve grande parte da confusão do QAP.

------------------------------------------------------------------------

# 30. Uma tabela que junta tudo

  ----------------------------------------------------------------------------------------------------
  Gate        Operação               A                 B                 C                 Ponto QAP
  ----------- ---------------------- ----------------- ----------------- ----------------- -----------
  1           `x × x = sym₁`         `[0,1,0,0,0,0]`   `[0,1,0,0,0,0]`   `[0,0,0,1,0,0]`   `1`

  2           `sym₁ × x = y`         `[0,0,0,1,0,0]`   `[0,1,0,0,0,0]`   `[0,0,0,0,1,0]`   `2`

  3           `(x+y) × 1 = sym₂`     `[0,1,0,0,1,0]`   `[1,0,0,0,0,0]`   `[0,0,0,0,0,1]`   `3`

  4           `(sym₂+5) × 1 = out`   `[5,0,0,0,0,1]`   `[1,0,0,0,0,0]`   `[0,0,1,0,0,0]`   `4`
  ----------------------------------------------------------------------------------------------------

A coluna "Ponto QAP" é a ponte entre R1CS e QAP.

------------------------------------------------------------------------

# 31. O que está acontecendo conceitualmente

O R1CS diz:

``` text
"Tenho 4 regras que precisam ser verdade."

Regra 1: x·x = sym₁
Regra 2: sym₁·x = y
Regra 3: (x+y)·1 = sym₂
Regra 4: (sym₂+5)·1 = out
```

O QAP diz:

``` text
"Vou colocar essas 4 regras em 4 posições
de uma função polinomial."

posição 1 → regra 1
posição 2 → regra 2
posição 3 → regra 3
posição 4 → regra 4
```

E depois:

``` text
"Se a expressão polinomial t(x)
for zero em todas essas posições,
então todas as regras são satisfeitas."
```

Finalmente:

``` text
t(x) zero em 1,2,3,4
          ↓
t(x) tem raízes 1,2,3,4
          ↓
Z(x) divide t(x)
```

------------------------------------------------------------------------

# 32. O que o artigo original comprime

O texto original é correto, mas algumas transições são muito rápidas
para quem está aprendendo pela primeira vez.

A principal sequência implícita é:

``` text
flattened statement
        ↓
identificar cada operação como gate
        ↓
escolher uma ordem global para as variáveis
        ↓
construir o witness
        ↓
expressar cada gate como
(A·s)(B·s)=C·s
        ↓
obter um vetor A,B,C por gate
        ↓
empilhar os vetores em matrizes A,B,C
        ↓
atribuir um ponto x a cada constraint
        ↓
pegar cada coluna das matrizes
        ↓
interpolar a coluna
        ↓
obter um polinômio
        ↓
repetir para todas as colunas
        ↓
Aᵢ(x), Bᵢ(x), Cᵢ(x)
        ↓
combinar esses polinômios usando o witness
        ↓
A(x), B(x), C(x)
        ↓
t(x)=A(x)B(x)-C(x)
        ↓
verificar divisibilidade por Z(x)
```

Esse é o pipeline que fica escondido quando o texto passa diretamente de
"gates" para `A`, `B`, `C`, e depois de `A`, `B`, `C` para Lagrange.

------------------------------------------------------------------------

# 33. Uma regra mental útil

Para não se perder:

``` text
GATE
  ↓
"qual equação quero impor?"

R1CS
  ↓
"quais variáveis participam dessa equação?"

A, B, C
  ↓
"onde estão esses coeficientes na matriz?"

LAGRANGE
  ↓
"qual polinômio reproduz cada coluna?"

QAP
  ↓
"consigo testar todas as constraints
ao mesmo tempo?"

Z(x)
  ↓
"o polinômio realmente zera
em todos os pontos dos gates?"
```

------------------------------------------------------------------------

# 34. Resumo em uma única figura

``` text
                         PROGRAMA
                            │
                            ▼
                    ┌───────────────┐
                    │   FLATTENING  │
                    └───────┬───────┘
                            │
                operações simples
                            │
                            ▼
                    ┌───────────────┐
                    │     GATES     │
                    └───────┬───────┘
                            │
                 cada gate vira
              uma equação R1CS
                            │
                            ▼
                 ┌─────────────────┐
                 │  A, B, C / R1CS │
                 └────────┬────────┘
                          │
               4 constraints ×
                 6 variáveis
                          │
             ┌────────────┴────────────┐
             │                         │
       linhas = gates            colunas = variáveis
             │                         │
             │                         ▼
             │                  LAGRANGE
             │                         │
             │                         ▼
             │              A₀(x)...A₅(x)
             │              B₀(x)...B₅(x)
             │              C₀(x)...C₅(x)
             │                         │
             └──────────────┬──────────┘
                            │
                     usando witness s
                            │
                            ▼
                 A(x), B(x), C(x)
                            │
                            ▼
                t(x)=A(x)B(x)-C(x)
                            │
                            ▼
                  t(1)=t(2)=t(3)=t(4)=0
                            │
                            ▼
             Z(x)=(x-1)(x-2)(x-3)(x-4)
                            │
                            ▼
                     Z(x) | t(x)
                            │
                            ▼
                    QAP SATISFEITO
```

------------------------------------------------------------------------

# 35. A frase mais importante

Se você quiser guardar apenas uma coisa sobre essa transformação:

> **O QAP não recebe uma informação nova depois do R1CS. Ele pega as
> matrizes `A`, `B` e `C` do R1CS, interpreta cada linha como uma
> constraint em um ponto `x`, e usa interpolação de Lagrange para
> transformar cada coluna dessas matrizes em um polinômio.**

Então a relação é:

``` text
R1CS                         QAP

linha 1 ───────────────────→ avaliação em x=1
linha 2 ───────────────────→ avaliação em x=2
linha 3 ───────────────────→ avaliação em x=3
linha 4 ───────────────────→ avaliação em x=4

coluna 1 ──────────────────→ polinômio 1
coluna 2 ──────────────────→ polinômio 2
...
coluna 6 ──────────────────→ polinômio 6
```

E o witness `s` é o elemento que combina esses polinômios:

``` text
A(x) = Σ Aᵢ(x)sᵢ
B(x) = Σ Bᵢ(x)sᵢ
C(x) = Σ Cᵢ(x)sᵢ
```

para finalmente produzir:

``` text
t(x) = A(x)B(x) - C(x)
```

e testar:

``` text
Z(x) | t(x)
```

Esse é o elo completo entre **gate → R1CS → Lagrange → QAP**.

========================================================================

# PARTE 2 --- zkSNARKs in a Nutshell (Reitwießner), seção 4 em diante

Até aqui você sabe transformar **programa → polinômios**. Falta a outra
metade: como o verificador checa esses polinômios **sem ver o witness**.

O artigo "zkSNARKs in a Nutshell" cobre essa metade. Ele trava na seção
4 por **três motivos**, e nenhum deles é matemática nova:

1.  o autor reusa a letra `E` para **duas coisas diferentes**;
2.  ele chama `E(x) = g^x` de "encriptação", mas isso **não desencripta**;
3.  ele despeja o CRS inteiro de uma vez, sem dizer **para que serve cada
    linha**.

Vamos resolver os três, nessa ordem.

------------------------------------------------------------------------

# 36. QAP vs QSP: mesma forma, outro nome

O texto do Vitalik usa **QAP** (Quadratic Arithmetic Program). O texto do
Reitwießner usa **QSP** (Quadratic Span Program). São primos, não rivais.

``` text
QAP (Vitalik)
    A(x)·B(x) - C(x) = h(x)·Z(x)
    três combinações lineares, uma subtração

QSP (Reitwießner)
    (v₀ + Σ aₖvₖ(x))·(w₀ + Σ bₖwₖ(x)) = h(x)·t(x)
    duas combinações lineares, sem subtração
```

A forma que importa é só esta:

``` text
(combinação linear do witness)
    ×
(combinação linear do witness)
    =
h(x) · (polinômio alvo)
```

Ou seja: **produto de dois "lados" = múltiplo do polinômio alvo**.

No QAP os coeficientes dos dois lados vêm do **mesmo** witness
(`A(x)` e `B(x)` usam o mesmo `s`). No QSP, os lados têm coeficientes
separados (`aₖ` e `bₖ`), e a restrição do input é codificada por uma
função `f(i, j)` que **força** certos `aₖ`, `bₖ` a valer 0 ou 1.

Diferença de contabilidade. Não de ideia.

> **O grau é 2 nos dois casos. Guarde isso. A seção 4.1 explica por quê.**

------------------------------------------------------------------------

# 37. `E(x) = g^x` não é encriptação. É esconder no expoente

Esqueça RSA por um instante. Aqui o objeto é:

``` text
grupo cíclico G de ordem n, gerador g
E(x) := g^x
```

Traduzindo:

``` text
x  →  o número que você quer esconder
g  →  base pública, fixa
g^x →  o valor publicado
```

Recuperar `x` a partir de `g^x` é o **problema do logaritmo discreto**.
Ninguém sabe fazer em curva elíptica. Então:

> **`E` é de mão única. Não existe `D(c)`. O verificador nunca "lê" `x`.**

Ele só **compara** coisas do tipo `g^a` com `g^b`. Se forem iguais, aposta
que `a = b`.

As duas únicas contas que dá para fazer com `g^x` sem saber `x`:

``` text
1) soma:      E(a)·E(b) = g^a·g^b = g^(a+b) = E(a+b)
2) escalar:   E(a)^k    = g^(ak)   = E(a·k)     (k público)
```

O que **não** dá:

``` text
E(a)·E(b) = E(a·b)   ← FALSO
```

Grave essa linha. Ela é a razão de existir de tudo que vem a seguir.

------------------------------------------------------------------------

# 38. A armadilha: o artigo troca de homomorfismo no meio

Esse é o ponto que mais derruba gente.

``` text
Seção 1  (RSA):   E(x) = x^e mod n
                  E(x)·E(y) = E(x·y)     MULTIPLICATIVO

Seção 4  (curva): E(x) = g^x
                  E(x)·E(y) = E(x+y)     ADITIVO
```

Mesma letra `E`. Comportamento oposto.

``` mermaid
flowchart LR
    subgraph S1["Seção 1 — RSA"]
        A1["E(x)·E(y)"] --> B1["E(x·y)<br/>multiplicação"]
    end
    subgraph S4["Seção 4 — Curva elíptica"]
        A2["E(x)·E(y)"] --> B2["E(x+y)<br/>adição"]
    end
```

Consequência prática, e é ela que o autor usa sem dizer:

> **Multiplicar dois valores codificados vira SOMAR os expoentes.**
> `E(v(s))·E(w(s)) = E(v(s) + w(s))` --- você somou os dois valores,
> não multiplicou. E multiplicar **não** dá.

Então como o verificador checa `v(s)·w(s) = h(s)·t(s)`? Com **pairing**.

------------------------------------------------------------------------

# 39. Avaliar um polinômio num ponto secreto, sem saber o ponto

Setup publica:

``` text
E(s⁰), E(s¹), E(s²), ..., E(sᵈ)
```

`s` é secreto e depois é destruído ("toxic waste"). Ninguém mais vê `s`.

Agora o provador quer `E(f(s))` para `f(x) = 4x² + 2x + 4`. Ele faz:

``` text
E(f(s)) = E(4s² + 2s + 4)
        = E(s²)⁴ · E(s¹)² · E(s⁰)⁴
        = (g^(s²))⁴ · (g^s)² · g⁴
        = g^(4s² + 2s + 4)
        = E(f(s))   ✓
```

Ele combinou os ingredientes publicados. **Nunca soube `s`.**

Analogia: a cozinha publica os ingredientes já cortados. Você monta o
prato sem saber a receita.

``` text
E(s⁰), E(s¹), ..., E(sᵈ)   →  para polinômios que o PROVADOR inventa
                              (é o caso de h)

E(vₖ(s)), E(wₖ(s))         →  para polinômios FIXOS do circuito
                              (já vêm avaliados, é mais rápido)
```

------------------------------------------------------------------------

# 40. Por que `E(s^i)` sozinho não basta → entra o α

Problema: o verificador recebe `A = g^z`. Ele não sabe se `z = f(s)` ou se
`z` é um número aleatório que o provador inventou.

Solução: **pedir o mesmo número duas vezes, uma delas multiplicada por α.**

``` text
prover envia:   A = E(f(s))       = g^f(s)
                B = E(α·f(s))     = g^(α·f(s))

verifier checa: e(A, g^α) = e(B, g)
```

Onde `g^α` é público (é `E(α·s⁰)`, e `s⁰ = 1`).

Por que funciona:

``` text
e(A, g^α) = e(g^f(s), g^α) = e(g,g)^(α·f(s))
e(B, g)   = e(g^αf(s), g)  = e(g,g)^(α·f(s))   ✓
```

A ideia em uma frase:

> **B é "o mesmo número de A, vezes α". Se o provador trapacear em A, ele
> precisa acertar o α correspondente em B --- e ele não sabe α.**

Isso tem nome: **d-power knowledge of exponent assumption**. E o autor é
sincero sobre o status dela:

``` text
"we hope not" — ninguém provou, ninguém quebrou.
Mesmo tipo de aposta que sustenta RSA.
```

------------------------------------------------------------------------

# 41. Pairing: a única multiplicação que existe

``` text
e(g^x, g^y) = e(g,g)^(xy)
```

Bilinear nos dois argumentos. O que isso compra:

``` text
adições      →  quantas quiser  (vem de E(a)E(b) = E(a+b))
multiplicação →  EXATAMENTE UMA  (vem do pairing)
```

E é aqui que o "Quadratic" de QSP/QAP ganha significado real:

``` text
t(x)·h(x) = v(x)·w(x)
 ↑___↑       ↑___↑
  um produto   um produto
  → um pairing resolve
```

> **Se a equação do circuito fosse cúbica, não existiria zkSNARK desse
> tipo. O pairing só faz uma multiplicação. O sistema inteiro é moldado
> por essa limitação.**

Essa é a frase que falta no artigo.

------------------------------------------------------------------------

# 42. O CRS não é uma lista. É 4 blocos de "poderes"

Ler o CRS como tabela decorada não funciona. Ler como **"que contas o
provador passa a conseguir fazer"** funciona.

Cada bloco: o que ele **libera** e o que ele **não libera**. O "não
libera" é a parte que o artigo omite --- e é onde mora a segurança.

``` text
segredos destruídos no setup:  s, α, βv, βw, γ
```

### Bloco 1 --- poderes de `s`

``` text
E(s⁰), E(s¹), ..., E(sᵈ)
```

- **Libera:** `E(f(s))` para **qualquer** polinômio `f` de grau ≤ `d`.
- **Não libera:** nada. Isso é poder demais. Veja o problema abaixo.
- **Para que serve:** o provador avaliar `h`, o polinômio que ele mesmo
  inventa.

### Bloco 2 --- polinômios fixos, já avaliados

``` text
E(t(s)),   E(αt(s))
E(v₀(s)), ..., E(vₘ(s))      e as versões × α
E(w₀(s)), ..., E(wₘ(s))      e as versões × α
```

- **Libera:** qualquer **combinação linear** dos polinômios do circuito.
- **Não libera:** avaliar algo que não seja combinação desses.
- **Para que serve:** o provador montar `V_free`, `W` sem saber `s`.

### Bloco 3 --- as cópias × `α`

``` text
E(αs⁰), ..., E(αsᵈ)
E(αvₖ(s)), E(αwₖ(s)), E(αt(s))
```

- **Libera:** produzir a "versão multiplicada por α" de tudo acima.
- **Não libera:** `α` em si. `g^α` é público, `α` não.
- **Para que serve:** viabilizar a **verificação 1** (§43).

### Bloco 4 --- `βv`, `βw`, `γ`

``` text
E(γ),  E(βvγ),  E(βwγ)
E(βv·v₁(s)), ..., E(βv·vₘ(s)),  E(βv·t(s))
E(βw·w₁(s)), ..., E(βw·wₘ(s)),  E(βw·t(s))
```

- **Libera:** `E(βv·P(s) + βw·Q(s))` --- mas **só** se:

  ``` text
  P ∈ span{ v₁, ..., vₘ, t }
  Q ∈ span{ w₁, ..., wₘ, t }
  ```

- **Não libera:** `βv`, `βw` ou `γ` isolados. E nada fora desses spans.
- **Para que serve:** viabilizar a **verificação 2** (§43).

Repare: `v₀` e `w₀` **ficam de fora** do bloco 4. Eles são os offsets
constantes, e o verificador os usa direto na verificação 3.

------------------------------------------------------------------------

## 42.1 O conceito que faltava: o "span permitido"

Defina os dois espaços onde o provador pode colocar as coisas:

``` text
S_v = span{ v₁, ..., vₘ, t }     ← onde V_free precisa viver
S_w = span{ w₁, ..., wₘ, t }     ← onde W precisa viver
```

> **Toda a segurança do bloco 4 se resume a isto: o provador só consegue
> produzir um `Y` válido se `V_free ∈ S_v` e `W ∈ S_w`.**

E é aqui que o Bloco 1 vira um problema:

``` text
Com só os poderes E(s⁰)...E(sᵈ), o provador consegue
produzir E(g(s)) para g ARBITRÁRIO de grau ≤ d.

Ele poderia mandar V_free = E(lixo) e a verificação 1
passaria sem reclamar.
```

A verificação 2 existe **exatamente** para fechar esse buraco.

------------------------------------------------------------------------

## 42.5 Onde entra o Powers of Tau

O artigo diz, em uma linha:

> *"the verifier chooses a secret field element `s` and publishes
> `E(s⁰), E(s¹), ..., E(sᵈ)`"*

Isso aí é o **Powers of Tau**. Só que escrito de um jeito que esconde o
problema: **quem é "o verificador"?**

``` text
Reitwießner chama de   s
Literatura de cerimônia chama de   τ  (tau)
Groth16 / BGM17         chama de   τ  (tau)
                                   ↓
                              é o mesmo número
```

### O problema que o Powers of Tau resolve

``` text
se UMA pessoa escolhe s e publica E(s⁰)...E(sᵈ):

  ✓ funciona
  ✗ essa pessoa sabe s
  ✗ quem sabe s forja prova de qualquer mentira
```

O `s` é o **toxic waste** que o artigo menciona. Precisa ser gerado sem
que **ninguém** saiba o valor final.

### A mecânica: uma rodada

Cada participante pega as potências do anterior e **aplica o próprio
segredo por cima**. Sem nunca ver o `τ`.

Exemplo com número pequeno, `d = 3`:

``` text
ROUND 1 — Alice escolhe τ₁ = 5
    publica:  [1], [5], [25], [125]
    destrói:  5

ROUND 2 — Bob escolhe τ₂ = 3
    recebe:   [1], [5], [25], [125]
    eleva cada um à sua potência:
              [1·1], [3·5], [9·25], [27·125]
            = [1], [15], [225], [3375]
    publica:  potências de 15
    destrói:  3
```

O `τ` final virou `15 = 5 × 3`.

``` text
Alice sabe:  τ₁ = 5        (um fator)
Bob sabe:    τ₂ = 3        (outro fator)
Ninguém sabe: τ = 15       ← ninguém tem os dois
```

E o pulo do gato: **Bob nunca precisou saber τ₁ para multiplicar.** Ele
só elevou o que recebeu. Só isso.

### A propriedade que importa

``` text
τ_final = τ₁ · τ₂ · τ₃ · ... · τ_N
```

> **`τ` só é conhecido se TODOS os participantes coludirem. Basta UM ter
> destruído o segredo dele para o sistema estar seguro.**

Não é "maioria honesta". É **1 de N**. Essa frase é a alma da cerimônia.

### Duas fases

Essa distinção responde uma coisa que o artigo diz de passagem na seção 6
("some parts can be re-used, but not all"):

| Fase                | Produz                          | Serve para           | Reuso                    |
| ------------------- | ------------------------------- | -------------------- | ------------------------ |
| **1 — Powers of Tau** | `E(τⁱ)`, `E(ατⁱ)` — Blocos 1 e 3 | grau máximo          | **universal**: todo circuito até aquele grau |
| **2 — específica**    | `E(vₖ(τ))`, `E(wₖ(τ))`, `E(t(τ))`, β, γ — Blocos 2 e 4 | os polinômios do circuito | **por circuito**: refaz toda vez |

Por quê?

``` text
τ⁰, τ¹, ..., τᵈ   → não sabem nada sobre o circuito.
                    só dizem "até que grau dá".
                    → reusável

vₖ(τ), wₖ(τ)      → são OS polinômios do SEU circuito.
                    → não reusável
```

> **Fase 1 é cara e pública (qualquer um pode entrar, e quanto mais
> gente, melhor). Fase 2 é por aplicação.** Cerimônias reais tipo a
> Perpetual Powers of Tau e a do KZG da Ethereum acumularam centenas de
> milhares de contribuições na Fase 1.

### Por que "perpetual"

Não precisa saber a lista de participantes de antemão. Alguém novo pode
chegar **depois**, multiplicar por mais um fator e devolver.

``` text
τ_final = τ₁ · τ₂ · ... · τ_N · τ_N+1 · ...
                                  ↑
                        chegou depois, ainda conta
```

Cada nova contribuição **só melhora** a segurança. Nunca piora.

### O que acontece se `τ` vazar

Exatamente o que o artigo avisa na seção 4.1:

> *"if someone can recover this and the other secret values chosen later,
> they can arbitrarily spoof proofs by finding zeros in the polynomials"*

Traduzindo para a linguagem da Parte 1: quem sabe `τ` consegue escolher
`h` de forma que `v(τ)·w(τ) = h(τ)·t(τ)` feche **mesmo para uma conta
errada**. Volta à §43: a verificação é só em um ponto. Conhecer o ponto
é conhecer o atalho.

``` text
sabe τ  →  escolhe h que zera justo em τ  →  forja prova
não sabe τ  → (chance ~ grau / |campo|)   →  Schwartz-Zippel segura
```

------------------------------------------------------------------------

# 43. As três verificações: o que pega e o que escapa

A prova tem 7 elementos de grupo:

``` text
V_free, W, H                (valores)
V'_free, W', H'             (os mesmos, × α)
Y                           (amarração β/γ)
```

A ordem não é arbitrária. **Cada verificação tapa um buraco da
anterior.**

``` mermaid
flowchart TD
    V1["Verificação 1 — α<br/>expoente consistente"]
    V1 -.->|"buraco:<br/>qualquer polinômio serve"| V2["Verificação 2 — β,γ<br/>obriga estar em S_v e S_w"]
    V2 -.->|"buraco:<br/>a conta ainda não foi feita"| V3["Verificação 3 — pairing<br/>v·w = h·t em s"]
```

### Verificação 1 --- "o expoente é consistente"

``` text
e(V'_free, g)    = e(V_free, g^α)
e(W',      E(1)) = e(W,      E(α))
e(H',      E(1)) = e(H,      E(α))
```

O que pega: `V'_free` carrega o **mesmo** expoente de `V_free`, vezes `α`.

``` text
e(V'_free, g) = e(g^(α·v_free(s)), g) = e(g,g)^(α·v_free(s))
e(V_free, g^α) = e(g^(v_free(s)), g^α) = e(g,g)^(α·v_free(s))   ✓
```

**O que escapa:**

> **Isso NÃO diz *qual* polinômio foi avaliado. Diz só que *algum* foi,
> de forma consistente.** Com os poderes `E(s⁰)...E(sᵈ)` o provador
> consegue `E(g(s))` para `g` arbitrário, e o α-check passa igual.

### Verificação 2 --- "está no span certo"

``` text
e(E(γ), Y) = e(E(βvγ), V_free) · e(E(βwγ), W)
```

Agora o raciocínio **completo**, que é o que eu tinha errado antes.

**Passo 1 --- o que o provador consegue montar.**

Com β, o CRS só oferece `E(βv·vₖ(s))`, `E(βv·t(s))`, `E(βw·wₖ(s))`,
`E(βw·t(s))`. Então, necessariamente:

``` text
Y = E( βv·P(s) + βw·Q(s) )
        com P ∈ S_v  e  Q ∈ S_w
```

Ele **não consegue** colocar em `Y` nada fora desses spans.

**Passo 2 --- o que o verificador exige.**

Expandindo os dois lados:

``` text
esquerda:  e(g,g)^( γ · Y_exp )
direita:   e(g,g)^( βv·γ·V_exp + βw·γ·W_exp )
```

O `γ` aparece nos dois lados, então a igualdade exige:

``` text
Y_exp = βv·V_exp + βw·W_exp
```

**Passo 3 --- a conclusão.**

Juntando 1 e 2:

``` text
βv·P(s) + βw·Q(s) = βv·V_exp + βw·W_exp
```

Como `βv` e `βw` são secretos e independentes, a única forma de isso
fechar é:

``` text
V_exp = P(s)   →   V_free ∈ S_v
W_exp = Q(s)   →   W      ∈ S_w
```

> **Buraco fechado: `V_free` e `W` não podem mais ser polinômios
> arbitrários. Estão presos ao span dos polinômios do circuito.**

**Honestidade intelectual:** esse "a única forma de fechar" repousa na
**knowledge-of-exponent assumption** (§40). Ninguém provou. Ninguém
quebrou. O autor diz "we hope not" e é isso.

### Verificação 3 --- "a conta do QSP fecha"

``` text
e( E(v₀(s))·E(v_in(s))·V_free ,  E(w₀(s))·W )  =  e( H, E(t(s)) )
```

Dentro de cada argumento do pairing, multiplicar = somar expoentes:

``` text
argumento 1:  E(v₀(s))·E(v_in(s))·V_free
            = E(v₀(s) + v_in(s) + v_free(s))
            = E(v(s))

argumento 2:  E(w₀(s))·W = E(w₀(s) + w(s)) = E(w(s))
```

Então:

``` text
esquerda:  e(E(v(s)), E(w(s))) = e(g,g)^(v(s)·w(s))
direita:   e(E(h(s)), E(t(s))) = e(g,g)^(h(s)·t(s))
```

Igualdade ⟺ `v(s)·w(s) = h(s)·t(s)`. **É o QSP, avaliado em `s`.**

Repare no que o `v_in` está fazendo aqui: os coeficientes dos índices
"não-livres" são determinados pelo input público `u`, então o verificador
mesmo consegue calcular `E(v_in(s))`. O provador só esconde a parte
livre, que é onde mora o witness.

### O que NENHUMA das três faz

Isso aqui é o elo com o item "B) Succinctness by random sampling" do
resumo do artigo, e passa batido:

``` text
ninguém verifica que  t(x) | v(x)·w(x)  como POLINÔMIO.
só verifica a igualdade no ponto s.
```

A aposta é o lema de **Schwartz-Zippel**:

``` text
se  v·w - h·t  NÃO é o polinômio zero,
ele tem no máximo "grau" raízes.

grau ≈ 100 × (nº de gates)        → tipo 10⁶
tamanho do campo                  → tipo 2²⁵⁴

chance de o provador sortear justo uma raiz: ~ 10⁶ / 2²⁵⁴
```

> **É isso que compra a "sucintidão". Não é mágica. É que um ponto é
> sempre um ponto, e o campo é gigante.**

------------------------------------------------------------------------

# 44. Zero-knowledge: duas razões, e a segunda é a boa

O provador escolhe `δ_free`, `δ_w` aleatórios e troca:

``` text
v_free(s)  →  v_free(s) + δ_free·t(s)
w(s)       →  w(s)      + δ_w·t(s)
```

Por que **múltiplo de `t`**? Por dois motivos. O artigo só dá o primeiro.

### Razão 1 --- algébrica: o `h` absorve

``` text
v' = v + δ_free·t        onde v = v₀ + v_in + v_free
w' = w + δ_w·t           onde w = w₀ + w

v'·w' = v·w + δ_free·t·w + δ_w·t·v + δ_free·δ_w·t²
      = t·( h + δ_free·w + δ_w·v + δ_free·δ_w·t )
        └──────────────── h' ────────────────────┘
```

A conta continua fechando. Verificação 3 passa.

### Razão 2 --- estrutural: é o ÚNICO lugar para onde dá para ir

Lembra do span permitido (§42.1)?

``` text
S_v = span{ v₁, ..., vₘ, t }
S_w = span{ w₁, ..., wₘ, t }
```

O verificador 2 **obriga** `V_free ∈ S_v` e `W ∈ S_w`. Então:

``` text
somar δ·t(s)      → continua em S_v   ✓
somar δ·(qualquer outro polinômio)  → SAI de S_v, check 2 quebra  ✗
```

> ** Esta é a razão que o artigo não escreve.** Não basta o `h` absorver.
> O `t` é a única direção livre que não derruba a verificação 2.

E é por isso que as entradas `E(βv·t(s))` e `E(βw·t(s))` existem no
Bloco 4: são a "permissão de movimento" do provador dentro do span.

------------------------------------------------------------------------

## 44.1 Os 7 elementos, atualizados

O artigo mostra a correção do `h` e para por aí. A prova tem 7 elementos e
**todos** precisam ser recalculados. Fazer a conta completa é o que
realmente faz o CRS fazer sentido.

Escreva `V = E(v(s))` e `W_tot = E(w(s))` (com os offsets `v₀`, `w₀`).

``` text
h' = h + δ_free·w + δ_w·v + δ_free·δ_w·t
```

| Elemento    | Como fica                                                                  |
| ----------- | -------------------------------------------------------------------------- |
| `V_free'`   | `V_free · E(t(s))^(δ_free)`                                                |
| `W'`        | `W · E(t(s))^(δ_w)`                                                        |
| `H'`        | `H · W_tot^(δ_free) · V^(δ_w) · E(t(s))^(δ_free·δ_w)`                      |
| `Y'`        | `Y · E(βv·t(s))^(δ_free) · E(βw·t(s))^(δ_w)`                               |
| `V_free''`  | `V'_free · E(αt(s))^(δ_free)`                                              |
| `W''`       | `W' · E(αt(s))^(δ_w)`                                                      |
| `H''`       | `H' · E(αw(s))^(δ_free) · E(αv(s))^(δ_w) · E(αt(s))^(δ_free·δ_w)`         |

Cada termo usa **só** o que está no CRS. Nenhum segredo.

### O detalhe que fecha o círculo

Olhe a última linha, o termo `E(αt(s))^(δ_free·δ_w)`.

> **`E(αt(s))` está no CRS por causa daquele `t²` que aparece quando você
> expande `(v + δ_free·t)(w + δ_w·t)`.** Sem essa entrada, a prova
> embaralhada não seria construível. O artigo lista e não explica.

E o provador consegue `E(w(s))`, `E(v(s))` e suas versões `α` porque tem
`E(vₖ(s))`, `E(wₖ(s))`, `E(αvₖ(s))`, `E(αwₖ(s))` para todo `k` --- e
conhece os coeficientes `aₖ`, `bₖ`, já que são o witness dele.

------------------------------------------------------------------------

## 44.2 O paralelo com a Parte 1

``` text
QAP (Parte 1)
    múltiplos de Z(x) são livres
    → é onde o h(x) vive
    → usado para CALCULAR

zkSNARK (Parte 2)
    múltiplos de t(x) são livres
    → é onde o embaralhamento vive
    → usado para ESCONDER
```

Mesma folga algébrica, dois usos diferentes.

------------------------------------------------------------------------

## 44.3 Perguntas que sobram (e as respostas)

**"Por que não embaralhar `h` também?"**

`h` não é livre. `h = (v·w)/t`. Mexer em `h` quebra a verificação 3.

**"Por que o verificador não desfaz o δ?"**

Ele não sabe `δ`, e `V_free'` é indistinguível de aleatório. Para ele,
`v_free(s) + δ·t(s)` poderia ser qualquer valor do campo.

**"Isso esconde tudo?"**

Esconde `v_free` e `w`, que é onde está o witness. `v_in` continua
visível --- mas `v_in` é determinado pelo input público `u`, então não
tem o que esconder ali.

------------------------------------------------------------------------

# 45. Por que só 7 elementos? (seção 5)

O verificador faz:

``` text
1.  ~3 pairings para os α-shifts
2.  ~3 pairings para o β/γ
3.  ~1 pairing para a conta principal
4.  E(v_in(s)) — linear no tamanho do INPUT
```

O que **não** aparece na conta:

``` text
tamanho do witness        → não importa
complexidade do circuito  → não importa
```

Motivo, em uma linha:

> **Polinômio pode ser gigantesco. Ponto é sempre ponto. Avaliamos em
> `s`, e `s` é um elemento só.**

E se o input for grande demais? O autor joga o input para dentro do
witness:

``` text
antes:  f(u, w)              u público, cresce o custo
depois: f'(H, (u, w)) = f(u, w) ∧ hash(u) = H
```

Agora o input público é só `H`. Custo constante. O `u` virou witness.

------------------------------------------------------------------------

# 46. A frase mais importante da Parte 2

Se você quiser guardar uma coisa:

> **Tudo é escondido no expoente. Com expoente você soma à vontade, mas
> só multiplica uma vez --- e essa única multiplicação vem do pairing.
> A equação do circuito é quadrática porque o pairing só faz uma
> multiplicação. As três verificações se encadeiam: (1) o α prova que o
> expoente é consistente, mas deixa passar polinômio arbitrário; (2) o
> β/γ fecha esse buraco prendendo `V_free` e `W` ao span dos polinômios
> do circuito; (3) o pairing final prova que `v·w = h·t` no ponto `s` ---
> só em `s`, e isso basta por Schwartz-Zippel. O zero-knowledge vem de
> somar múltiplos de `t`: é a única direção livre que não derruba a
> verificação 2.**

------------------------------------------------------------------------

# 47. Mapa de leitura: o que você pode pular

``` text
Seção 1 (RSA)      → ler só pelo homomorfismo. Depois esquecer.
Seções 2 e 3 (NP)  → teoria da computação. Não trava a seção 4.
Seção 4 (setup)    → o "verificador escolhe s" é o Powers of Tau. §42.5.
Seção 4.1          → O CORAÇÃO. α + pairing.
Seção 4.2          → o CRS e as 3 verificações. Mecânico depois da 4.1.
Seção 6            → "some parts can be re-used" = Fase 1 vs Fase 2. §42.5.
Seção 4.3          → zero-knowledge. É o truque do Z(x) de novo.
Seção 5            → custo constante. Curto, vale ler.
```

Ordem que eu recomendo reler o artigo:

``` mermaid
flowchart LR
    A["4.1<br/>E(x)=g^x<br/>+ α<br/>+ pairing"] --> B["4.2<br/>CRS<br/>+ 3 checks"]
    B --> C["4.3<br/>shift = ZK"]
    C --> D["5<br/>custo constante"]
```

Se a 4.1 não entrar, **nada** depois entra. Gasta o tempo lá.
