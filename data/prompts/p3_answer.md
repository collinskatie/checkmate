Let $P (z) = a_n z^n + \dots + a_1 z + a_0, \ a_n \ne 0$.

Aiming for a contradiction, suppose that $P (z)$ is not zero for any $z \in \mathbb{C}$.

It follows that $1 / P (z)$ must be entire; and is also bounded in the complex plane.

In order to see that it is indeed bounded, we recall that $\exists R \in \mathbb{R}_{>0}$ such that:

$$\left| {\dfrac {1}{P (z)} }\right| < \dfrac 2 {\left| {a_n}\right| R^n}, \text{whenever} \ \left| z\right| > R.$$

Hence, $1 / P (z)$ is bounded in the region outside the disk $\left| z\right| \leq R$.

However, $1 / P (z)$ is continuous on that closed disk, and thus it is bounded there as well. 

Furthermore, we observe that $1 / P(x)$ must be bounded in the whole plane.

Through Liouville's Theorem, $1 / P(x)$, and thus $P(x)$, is constant. 

This is a contradiction.

$\blacksquare$