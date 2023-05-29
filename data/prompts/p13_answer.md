Let $x, y, z \in G$.

Suppose that $\neg \left( {\left( {x \circ z}\right)   \mathcal{Q} \left( {y \circ z}\right) }\right)$.

Then by the definition of $\mathcal{Q}$:
$$\left( {x \circ z}\right)   \mathcal{R} \left( {y \circ z}\right)$$

Because $\mathcal{R}$ is compatible with $\circ$:

$$\left( {x \circ z}\right) \circ z^{-1}   \mathcal{R} \left( {y \circ z}\right) \circ z^{-1}$$


By {{GroupAxiom|1}} and the {{GroupAxiom|3}}:

$$x   \mathcal{R} y$$

so by the definition of $\mathcal{Q}$:

$$\neg \left( {x   \mathcal{Q} y}\right)$$


By the Rule of Transposition:
$$\forall x, y, z \in G: x   \mathcal{Q} y \to \left( {x \circ z}\right)   \mathcal{Q} \left( {y \circ z}\right)$$

A similar argument shows that:
$$\forall x, y, z \in G: x   \mathcal{Q} y \to \left( {z \circ x}\right)   \mathcal{Q} \left( {z \circ y}\right)$$

Thus, by definition, $\mathcal{Q}$ is a relation compatible with $\circ$.

$\blacksquare$