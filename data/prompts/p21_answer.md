Aiming for a contradiction, suppose there is a solution.

Then:
$$ a^n  = 2^m - 1$$
$$ \equiv -1 \mathrm{\ mod \ } 4 \text{\quad as } m > 1$$

$a$ is immediately seen to be odd.

By Square Modulo 4, $n$ must also be odd.


Now:
$$ 2^m = a^n + 1$$
$$ = \left( {a + 1}\right) \sum_{k  = 0}^{n - 1} \left( {-1}\right)^k a^{n - k - 1}\text{\quad Sum of Two Odd Powers}$$

The latter sum has $n$ powers of $a$, which sums to an odd number.

The only odd divisor of $2^m$ is $1$.

However, if the sum is $1$, we have:
$$a^n + 1 = a + 1$$

giving $n = 1$, contradicting our constraint $n > 1$.

Hence the result by Proof by Contradiction.

$\blacksquare$