Put into bald mathematical language, this boils down to:

For a set $S$ of $n$ elements, what is the number of derangements of $S$ divided by the number of permutations of $S$?

The answer is: approximately $\dfrac {1}e$, which can be demonstrated as follows.


Let $D_n$ be the number of derangements of a set of size $n$.

We have that:
The Number of Permutations of a set of size $n$ is $n!$.

The Closed Form for Number of Derangements on Finite Set of size $n$ is:
$$D_n = n! \left( {1 - \dfrac {1}{1!} + \dfrac {1}{2!} - \dfrac {1}{3!} + \cdots + \left( {-1}\right)^n \dfrac {1}{n!} }\right)$$


So:

$$ p_n = \dfrac {D_n} {n!}$$
$$ = \dfrac {!n} {n!}\text{\quad Closed Form for Number of Derangements on Finite Set}$$
$$ = \dfrac {n! \mathrm{} \sum_{k  = 0}^n \frac {\left( {-1}\right)^k} {k!} } {n!}\text{\quad Definition of Subfactorial}$$
$$ = \sum_{k  = 0}^n \frac {\left( {-1}\right)^k} {k!}$$
$$ = 1 - \dfrac {1}{1!} + \dfrac {1}{2!} - \dfrac {1}{3!} + \cdots + \left( {-1}\right)^n \dfrac {1}{n!}$$


Finally:
$$1 - \dfrac {1}{1!} + \dfrac {1}{2!} - \dfrac {1}{3!} + \cdots$$
converges to $\dfrac {1}e$ by Taylor Series Expansion for Exponential Function.

$\blacksquare$