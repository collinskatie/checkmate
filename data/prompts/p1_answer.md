We split into three cases. 

=== Case 1: $p > 1$ ===

We first show that $f + g \in {\mathcal{L}^p} \left(\mu\right)$.

Note that from Pointwise Maximum of Measurable Functions is Measurable:

$x \mapsto \max \{f (x), g (x)\}$ is $\Sigma$-measurable.

We then have from Measure is Monotone: 

$$\mathrm{} \int \mid {f + g}\mid^p \mathrm{d} \mu = \int \mid {2 \max \{f (x), g (x)\} }\mid^p {\mathrm{d} \mu} (x)$$

We then have: 

$$\int \mid {2 \max \{f (x), g (x)\}}\mid^p {\mathrm{d} \mu} (x)
= \int 2^p \mid {\max \{f (x), g (x)\}}\mid^p {\mathrm{d} \mu} (x)\quad \text{Integral of Positive Measurable Function is Positive Homogeneous}$$ 
$$= 2^p \int \max \{\mid {f (x)}\mid ^p, \mid  {g (x)}\mid ^p\} {\mathrm{d} \mu} (x)$$
$$\leq 2^p \int \left( {\mid f\mid^p + \mid g\mid^p}\right) \mathrm{d} \mu$$

Since $f, g \in {\mathcal{L}^p} \left(\mu\right)$, we have: 

$$\mathrm{} \int \mid f\mid^p \mathrm{d} \mu < \infty$$

and:

$$\mathrm{} \int \mid g\mid^p \mathrm{d} \mu < \infty$$

so:

$$\mathrm{} \int \mid {f + g}\mid^p \mathrm{d} \mu < \infty$$

so:

$$f + g \in {\mathcal{L}^p} \left(\mu\right)$$

If: 

$$\mathrm{} \int \mid {f + g}\mid^p \mathrm{d} \mu = 0$$

then the desired inequality is immediate.

So, take: 

$$\mathrm{} \int \mid {f + g}\mid^p \mathrm{d} \mu > 0$$

Write: 

$$\mathrm{} \int \mid {f + g}\mid^p \mathrm{d} \mu = \int \mid {f + g}\mid \mid {f + g}\mid^{p - 1} \mathrm{d} \mu$$

From the Triangle Inequality, Integral of Positive Measurable Function is Monotone and Integral of Positive Measurable Function is Additive, we have: 

$$\mathrm{} \int \mid {f + g}\mid \mid {f + g}\mid^{p - 1} \mathrm{d} \mu \leq \int \mid f\mid \mid {f + g}\mid^{p - 1} \mathrm{d} \mu + \int \mid g\mid \mid {f + g}\mid^{p - 1} \mathrm{d} \mu$$

From Hölder's Inequality, we have: 

$$\mathrm{} \int \mid f\mid \mid {f + g}\mid^{p - 1} \mathrm{d} \mu + \int \mid g\mid \mid {f + g}\mid^{p - 1} \mathrm{d} \mu \leq \left( {\int {\mid f\mid}^p \mathrm{d} \mu}\right)^{1/p} \left( {\int \mid {f + g}\mid^{q \left( {p - 1}\right) } \mathrm{d} \mu}\right)^{1/q} + \left( {\int {\mid g\mid}^p \mathrm{d} \mu}\right)^{1/p} \left( {\int \mid {f + g}\mid^{q \left( {p - 1}\right) } \mathrm{d} \mu}\right)^{1/q}$$

where $q$ satisfies: 

$$\mathrm{} \frac {1} p + \frac {1} q = 1$$

Then we have: 

$$p + q = p q$$

so:

$$p = pq - q = q \left( {p - 1}\right)$$

So we have: 

$$\mathrm{} \int \mid {f + g}\mid^p \mathrm{d} \mu \leq \left( {\left( {\int {\mid f\mid}^p \mathrm{d} \mu}\right)^{1/p} + \left( {\int {\mid g\mid}^p \mathrm{d} \mu}\right)^{1/p} }\right) \left( {\int \mid {f + g}\mid^p \mathrm{d} \mu}\right)^{1/q}$$

From the definition of the $p$-seminorm we have:

$$\mathrm{} \int \mid {f + g}\mid^p \mathrm{d} \mu \leq \left( {\| f\|_p + \| g\|_p}\right) \left( {\int \mid {f + g}\mid^p \mathrm{d} \mu}\right)^{1/q}$$

So that: 

$$\mathrm{} \left( {\int \mid {f + g}\mid^p \mathrm{d} \mu}\right)^{1 - 1/q} \leq \| f\|_p + \| g\|_p$$

That is: 

$$\mathrm{} \left( {\int \mid {f + g}\mid^p \mathrm{d} \mu}\right)^{1/p} \leq \| f\|_p + \| g\|_p$$

So from the definition of the $p$-seminorm we have: 

$$\| {f + g}\|_p \leq \| f\|_p + \| g\|_p$$

$\square$

=== Case 2: $p = 1$ ===

From the Triangle Inequality, we have:

$$\mid {f + g}\mid \leq \mid f\mid + \mid g\mid$$

So, from Integral of Positive Measurable Function is Additive and Integral of Positive Measurable Function is Monotone, we have: 

$$\mathrm{} \int \mid {f + g}\mid \mathrm{d} \mu \leq \int \mid f\mid \mathrm{d} \mu + \int \mid g\mid \mathrm{d} \mu$$

So if $f, g \in {\mathcal{L}^1} \left(\mu\right)$ we have $f + g \in {\mathcal{L}^1} \left(\mu\right)$

From the definition of the $1$-seminorm, we also have that: 

$$\| {f + g}\|_1 \leq \| f\|_1 + \| g\|_1$$

immediately.

$\square$


=== Case 3: $p = \infty$ ===

Suppose $f, g \in {\mathcal{L}^\infty} \left(\mu\right)$.

Then from the definition of the $\mathcal{L}^\infty$-space, there exists $\mu$-null sets $N_1$ and $N_2$ such that: 

$$\mid {f (x)}\mid \leq \| f\|_\infty \text{ for } x \not \in N_1$$

and:

$$\mid {g (x)}\mid \leq \| g\|_\infty\text{ for }x \not \in N_2$$

Then, for $x \not \in N_1 \cup N_2$ we have: 

$$\mid {f (x) + g (x)}\mid \leq \| f\|_\infty + \| g\|_\infty$$

by the Triangle Inequality. 

From Null Sets Closed under Countable Union, we have:

$N_1 \cup N_2$ is $\mu$-null.

So:

$$\| {f + g}\|_\infty \leq \| f\|_\infty + \| g\|_\infty$$

as desired.

$\blacksquare$