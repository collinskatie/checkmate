Let $\mathbf{x}= \begin {bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end {bmatrix} \in \mathbb{R}^n$.

$$ \mathbf{x}\in {\operatorname {N^{\leftarrow}} } \left({\mathbf{A}}\right) \leftrightarrow \mathbf{x}\in {\operatorname N} \left({\mathbf{A}^\intercal}\right) \text{\quad Definition of Left Null Space}$$
$$\leftrightarrow \mathbf{A}^\intercal \mathbf{x}= \mathbf 0 \text{\quad Definition of Null Space}$$
$$ \leftrightarrow \left( {\mathbf{A}^\intercal \mathbf x}\right)^\intercal = \mathbf 0^\intercal\text{\quad taking the transpose of both sides}$$
$$ \leftrightarrow \mathbf{x}^\intercal \left( {\mathbf{A}^\intercal}\right)^\intercal = \mathbf 0^\intercal \text{\quad Transpose of Matrix Product}$$
$$ \leftrightarrow \mathbf{x}^\intercal \mathbf{A} = \mathbf 0^\intercal \text{\quad Transpose of Transpose of Matrix}$$

We have that $\mathbf{A}^\intercal \mathbf{x}= \mathbf 0$ is equivalent to $\mathbf{x}^\intercal \mathbf{A} = \mathbf 0^\intercal$.

This implies that $\mathbf{x}\in {\operatorname N} \left({\mathbf{A}^\intercal}\right) \leftrightarrow \mathbf{x}^\intercal \mathbf{A} = \mathbf 0^\intercal$.

Recall that:
$$\mathbf{x}\in {\operatorname N} \left({\mathbf{A}^\intercal}\right) \leftrightarrow \mathbf{x}\in {\operatorname {N^{\leftarrow}} } \left({\mathbf{A}}\right)$$

Hence the result, by definition of set equality.

$\blacksquare$