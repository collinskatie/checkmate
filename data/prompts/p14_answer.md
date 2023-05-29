=== Existence ===

First, we prove that such a subgroup exists.

Let $\mathbb S$ be the set of all subgroups of $G$ which contain $S$.

$\mathbb S \ne \varnothing$ because $G$ is itself a subgroup of $G$, and thus $G \in \mathbb S$.


Let $H$ be the intersection of all the elements of $\mathbb S$.

By Intersection of Subgroups is Subgroup, $H$ is the largest element of $\mathbb S$ contained in each element of $\mathbb S$.

Thus $H$ is a subgroup of $G$.

Since $\forall x \in \mathbb S: S \subseteq x$, we see that $S \subseteq H$, so $H \in \mathbb S$.


=== Smallest ===

Now to show that $H$ is the smallest such subgroup.

If any $K \leq G: S \subseteq K$, then $K \in \mathbb S$ and therefore $H \subseteq K$.

So $H$ is the smallest subgroup of $G$ containing $S$.


=== Uniqueness ===

Now we show that $H$ is unique.

Suppose $\exists H_1, H_2 \in \mathbb S$ such that $H_1$ and $H_2$ were two such smallest subgroups containing $S$.

Then, by the definition of "smallest", each would be equal in size.

If one is not a subset of the other, then their intersection (by definition containing $S$) would be a smaller subgroup and hence neither $H_1$ nor $H_2$ would be the smallest.

Hence one must be a subset of the other.

By definition of set equality, that means they must be the same set.

So the smallest subgroup, whose existence we have proved above, is unique.

$\blacksquare$