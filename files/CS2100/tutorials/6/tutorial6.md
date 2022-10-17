# Tutorial 6
(why is this before the midterm bruh :|)

### Question 1

`````ad-question
title: Name the essential theorems $\mathcal{A}$, $\mathcal{B}$, $\mathcal{C}$ and $\mathcal{D}$ used in the following derivation:

$$
\begin{align*}
F(j, k, m, p) &= k' \cdot (j' \cdot p \cdot (j' + m'))' + (p + k' + j)' \\
&= k' \cdot (j + p' + j\cdot m) + p'\cdot k \cdot j' \quad [\mathcal{A}\text{; involution}] \\
&= j \cdot k' + k' \cdot p' + j \cdot k' \cdot m + p'\cdot k \cdot j' \quad [\text{distributive; commutative}] \\
&= j \cdot k' + p' \cdot (k' + k\cdot j') + j \cdot k' \cdot m \quad [\text{associative; distributive; commutative}] \\
&= j \cdot k' + k' \cdot p' + j' \cdot p' + j\cdot k' \cdot m \quad [\mathcal{B}\text{; distributive; commutative}] \\
&= j \cdot k' + k' \cdot p' + j' \cdot p' \quad [\text{associative; }\mathcal{C}] \\
&= j \cdot k' + j' \cdot p' \quad [\mathcal{B}]
\end{align*}
$$
`````

#### Solution Notes Taken

| Theorem            | Examples                                                                   |
| ------------------ | -------------------------------------------------------------------------- |
| Identity           | $A + 0 = 0 + A = A$<br>$A \cdot 1 = 1 \cdot A = A$                         |     |
| Inverse/Complement | $A+A' = A' + A = 1$<br>$A\cdot A' = A' \cdot A = 0$                        |     |
| Commutative        | $A+B = B+A$<br>$A\cdot B = B\cdot A$                                       |     |
| Associative        | $A+(B+C) = (A+B)+C$<br> $A\cdot (B\cdot C) = (A\cdot B)\cdot C$            |     |
| Distributive       | $A\cdot (B+C) = (A\cdot B) + (A\cdot C)$<br>$A+(B\cdot C)=(A+B)\cdot(A+C)$ |     |
|    Idempotency                |                                                                            |     |
|                    |                                                                            |     |

### Question 2

Using Boolean algebra, simplify each of the following expressions into simplified **sum-of-products (SOP) expressions**. Indicate the law/theorem used for each step.

1. $F(x,y,z) = (x + y\cdot z')\cdot (y' + y) + x'\cdot (y\cdot z' + y)$
2. $G(p,q,r,s) = \Pi\text{ }M(5, 9, 13)$

*Tip*: For (b), it is simpler to start with the given expression and get done in 5 steps, rather than to expand it into sum-of-products/sum-of-minterms expression first.

#### Part (a)



#### Part (b)





### Question 3









### Question 4

A circuit takes in four inputs, `K`, `L`, `M`, `N` and generates 3 outputs `X`, `Y`, `Z` as follows:
- `X(K, L, M, N) : KL == MN`
- `Y(K, L, M, N) : KL <= MN`
- `Z(K, L, M, N) : KLM < LMN`

(a)








