=== Necessary Condition ===

This is proved in Congruence by Divisor of Modulus.

Note that for this result it is not required that $r \perp s$.

$\square$


=== Sufficient Condition ===

Now suppose that $a \equiv b \mathrm{\ mod \ } r$ and $a \equiv b \mathrm{\ mod \ } s$.

We have by definition of congruence:
$$a \equiv b \mathrm{\ mod \ } r \to \exists k \in \mathbb{Z}: a - b = k r$$

From $a \equiv b \mathrm{\ mod \ } s$ we also have that:
$$k r \equiv 0 \mathrm{\ mod \ } s$$

As $r \perp s$, we have from Common Factor Cancelling in Congruence:
$$k \equiv 0 \mathrm{\ mod \ } s$$

So:
$$\exists q \in \mathbb{Z}: a - b = q s r$$

Hence by definition of congruence:
$$a \equiv b \mathrm{\ mod \ } {r s}$$

$\blacksquare$