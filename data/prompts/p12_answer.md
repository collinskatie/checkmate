Let $G$ be a group and let $a \in G$.

Consider the left regular representation $\lambda_a: G \to G$ defined as:

$${\lambda_a} \left(x\right) = a \cdot x$$

From Regular Representations in Group are Permutations we have that $\lambda_a$ is a permutation.

Now let $b \in G$ and consider $\lambda_b: G \to G$ defined as:

$${\lambda_b} \left(x\right) = b \cdot x$$

From the Cancellation Laws it follows that $\lambda_a \ne \lambda_b \leftrightarrow a \ne b$.


Let $H = \{\lambda_x: x \in G\}$.

Consider the mapping $\Phi: G \to H$ defined as:
$$\forall a \in G: \Phi  \left(b\right) = \lambda_a$$

From the above we have that $\Phi$ is a bijection.


Let $a, b \in G$.

From Composition of Regular Representations we have that:
$$\lambda_a \circ \lambda_b = \lambda_{a \cdot b}$$
where $\circ$ denotes composition of mappings.

That is, $\Phi$ has the morphism property.

Thus $\Phi$ is seen to be a group isomorphism.


We also have that:
$$\left({\lambda_a}\right)^{-1} = \lambda_{\left({a^{-1} }\right)}$$
because:
$$\lambda_a \circ \left( {\lambda_a}\right)^{-1} = \lambda_{\left({a \cdot a^{-1} }\right)}$$


Hence the set of left regular representations $\{\lambda_x: x \in G\}$ is a group which is isomorphic to $G$.

$\blacksquare$