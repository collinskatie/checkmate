Let $x_0 \in A$.

Define $H : A \times [0\ldots 1] \to A$ by:
$$H \left({x, t}\right) = t x_0 + \left( {1 - t}\right) x$$

This yields a homotopy between the identity map $I_A$ and the constant map $x_0$.

Thanks to the assumption of convexity for $A$, $H$ takes values in $A$.

$H$ is a continuous function, since it is polynomial separately in $x, t$, and:
$$H \left({-, 0}\right) = I_A$$
$$H \left({-, 1}\right) \equiv x_0\quad (\text{the constant function on } x_0)$$

This proves that $H: I_A \simeq c_{x_0}$.

$\blacksquare$