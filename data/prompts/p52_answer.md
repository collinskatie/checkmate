=== Necessary Condition ===

Let $P'$ be a plan given by the equation:
$$\beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 = \delta$$

The Hessian normal vector of $P$ is given by:
$$\mathbf {n_P} = \left({\frac{\alpha_1}{p}, \frac{\alpha_2}{p}, \frac{\alpha_3}{p}}\right), \text{where}$$
$p = \sqrt{\alpha_1^2 + \alpha_2^2 + \alpha_3^2}$. Similarly, the Hessian normal vector of $P'$ is given by:
$$\mathbf {n_{P'}} = \left({\frac{\beta_1}{q}, \frac{\beta_2}{q}, \frac{\beta_3}{q}}\right), \text{where}$$
$q = \sqrt{\beta_1^2 + \beta_2^2 + \beta_3^2}$.

Since $P$ and $P'$ are parallel, we have that $\mathbf {n_P} \times \mathbf {n_{P'}} = \mathbf 0$.

We have:
$$\mathbf {n_P} \times \mathbf {n_{P'}} = \left({\frac{\alpha_1}{p}, \frac{\alpha_2}{p}, \frac{\alpha_3}{p}}\right) \times \left({\frac{\beta_1}{q}, \frac{\beta_2}{q}, \frac{\beta_3}{q}}\right)$$
$$ = \frac{1}{pq} \left({\alpha_2 \beta_3 - \alpha_3 \beta_2, \alpha_3 \beta_1 - \alpha_1 \beta_3, \alpha_1 \beta_2 - \alpha_2 \beta_1}\right)$$
$$ = \mathbf 0$$

Obviously, $pq\ne 0$, so:
$$\alpha_2 \beta_3 - \alpha_3 \beta_2 = 0$$
$$\alpha_3 \beta_1 - \alpha_1 \beta_3 = 0$$
$$\alpha_1 \beta_2 - \alpha_2 \beta_1 = 0$$

This implies that $\exists t \in \mathbb{R} \backslash \{0\}$ such that: $(\beta_1, \beta_2, \beta_3) = t(\alpha_1, \alpha_2, \alpha_3)$.

Putting this back into the equation of $P'$, we have:
$$t\alpha_1 x_1 + t\alpha_2 x_2 + t\alpha_3 x_3 = \delta$$
$$\mathbb{R}ightarrow\alpha_1 x_1 + \alpha_2 x_2 + \alpha_3 x_3 = \frac{\delta}{t}$$

Therefore, setting $\gamma' = \frac{\delta}{t}$, the conclusion follows.

=== Sufficient Condition ===

Let $P' \ne P$ be a plane given by the equation:

$$\alpha_1 x_1 + \alpha_2 x_2 + \alpha_3 x_3 = \gamma'$$

Aiming for contradiction, suppose we have a point:
$$\mathbf{x}= \left({x_1, x_2, x_3}\right) \in P \cap P'$$

Then, as $\mathbf{x}\in P$, it also satisfies:

$$\alpha_1 x_1 + \alpha_2 x_2 + \alpha_3 x_3 = \gamma$$

It follows that $\gamma = \gamma'$, so $P = P'$.

This contradiction shows that $P \cap P' = \varnothing$, that is, $P$ and $P'$ are parallel.

The remaining case is when $P' = P$.

By definition, $P$ is parallel to itself. 

The result follows.

$\blacksquare$