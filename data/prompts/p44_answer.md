=== Existence ===

Define:
$$\mathbb E = \{\mathcal{T} \subseteq \mathcal{P}(X): \mathcal{S} \subseteq \mathcal{T} \text{ and } \mathcal{T} \text{ is a topology on X}\}$$


Since Discrete Topology is Topology, $\mathcal{P}(X)$ is a topology on $X$, it follows that $\mathbb E$ is non-empty.

Hence, we can define:
$$\mathrm{} \tau \left(\mathcal{S}\right) = \bigcap \mathbb E$$

It follows that Intersection of Topologies is Topology, $\tau \left(\mathcal{S}\right)$ is a topology on $X$.


By Intersection is Largest Subset/General Result and Intersection is Largest Subset, it follows that $\mathcal{S} \subseteq \tau \left(\mathcal{S}\right)$.


By Intersection is Subset/General Result and Intersection is Subset, it follows that if $\mathcal{S} \subseteq \mathcal{T}$ and $\mathcal{T}$ is a topology on $X$, then $\tau \left(\mathcal{S}\right) \subseteq \mathcal{T}$.

$\square$

=== Uniqueness ===

Suppose that $\mathcal{T}_1$ and $\mathcal{T}_2$ are both topologies on $X$ satisfying conditions $(1)$ and $(2)$.


By condition $(1)$, we have $\mathcal{S} \subseteq \mathcal{T}_2$; hence, we can apply condition $(2)$ to conclude that:
$$\mathcal{T}_1 \subseteq \mathcal{T}_2$$

Similarly:
$$\mathcal{T}_2 \subseteq \mathcal{T}_1$$


By definition of set equality:
$$\mathcal{T}_1 = \mathcal{T}_2$$

$\blacksquare$