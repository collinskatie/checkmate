Let $\mathbb D^3$ be centered at the origin, and $D^3$ be some other unit ball in $\mathbb{R}^3$ such that $\mathbb D^3 \cap D^3 = \varnothing$.

Let $\mathbb S^2 = \partial \mathbb D^3$.

By the Hausdorff Paradox, there exists a decomposition of $ \mathbb S^2$ into four sets $A, B, C, D$ such that $A, B, C$ and $B \cup C$ are congruent, and $D$ is countable.

For $r \in \mathbb{R}_{>0}$, define a function $r^*: \mathbb{R}^3 \to \mathbb{R}^3$ as ${r^*} \left({\mathbf x}\right) = r \mathbf x$, and define the sets:

$$ W = \bigcup_{0  < r  \leq 1} {r^*} \left(A\right)$$
$$ X = \bigcup_{0  < r  \leq 1} {r^*} \left(B\right)$$
$$ Y = \bigcup_{0  < r  \leq 1} {r^*} \left(C\right)$$
$$ Z = \bigcup_{0  < r  \leq 1} {r^*} \left(D\right)$$


Let $T = W \cup Z \cup \{\mathbf 0\}$.

$W$ and $X \cup Y$ are clearly congruent by the congruency of $A$ with $B \cup C$, hence $W$ and $X \cup Y$ are equidecomposable.

Since $X$ and $Y$ are congruent, and $W$ and $X$ are congruent, $X \cup Y$ and $W \cup X$ are equidecomposable.  

$W$ and $X \cup Y$ as well as $X$ and $W$ are congruent, so $W \cup X$ and $W \cup X \cup Y$ are equidecomposable.  

Hence $W$ and $W \cup X \cup Y$ are equidecomposable, by Equidecomposability is Equivalence Relation.

So $T$ and $\mathbb D^3$ are equidecomposable, from Equidecomposability Unaffected by Union.


Similarly we find $X$, $Y$, and $W \cup X \cup Y$ are equidecomposable.


Since $D$ is only countable, but ${\operatorname {SO} } (3)$ is not, we have:
$$\exists \phi \in {\operatorname {SO} } (3): \phi (D) \subset A \cup B \cup C$$
so that $I = \phi (D) \subset W \cup X \cup Y$.

Since $X$ and $W \cup X \cup Y$ are equidecomposable, by Subsets of Equidecomposable Subsets are Equidecomposable, $\exists H \subseteq X$ such that $H$ and $I$ are equidecomposable.


Finally, let $p \in X - H$ be a point and define $S = Y \cup H \cup \{p\}$.

Since:

- $Y$ and $W \cup X \cup Y$

- $H$ and $Z$

- $\{0\}$ and $\{p\}$

are all equidecomposable in pairs, $S$ and $\mathbb B^3$ are equidecomposable by Equidecomposability Unaffected by Union.

Since $D^3$ and $\mathbb D^3$ are congruent, $D^3$ and $S$ are equidecomposable, from Equidecomposability is Equivalence Relation.  


By Equidecomposability Unaffected by Union, $T \cup S$ and $\mathbb D^3 \cup D^3$ are equidecomposable.

Hence $T \cup S \subseteq \mathbb D^3 \subset \mathbb D^3 \cup D^3$ are equidecomposable and so, by the Equidecomposable Nested Sets|chain property of equidecomposability, $\mathbb D^3$ and $\mathbb D^3 \cup D^3$ are equidecomposable.

$\blacksquare$