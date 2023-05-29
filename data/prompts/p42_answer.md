By assumption:
$$P \subseteq \tau$$

Let $U$ be an open subset of $S$.

Define:
$$X := \{V \in P: V \subseteq U\}$$

By definition of subset:
$$X \subseteq P$$

We will prove that:
$$\forall u \in S: u \in U \leftrightarrow \exists Z \in X: u \in Z$$

Let $u \in S$.

We will prove that:
$$u \in U \to \exists Z \in X: u \in Z$$

Assume that:
$$u \in U$$

By assumption:
there exists local basis $B$ at $u: B \subseteq P$.

By definition of local basis:
$$\exists V \in B: V \subseteq U$$

Thus by definitions of subset and $X$:
$$V \in X$$

Thus by definition of local basis:
$$u \in V$$

$\square$


Assume that:
$$\exists Z \in X: u \in Z$$

By definition of $X$:
$$Z \subseteq U$$

Thus by definition of subset:
$$u \in U$$

$\square$


Thus by definition of union:
$$U = \bigcup X$$

Hence $P$ is basis of $L$.

$\blacksquare$