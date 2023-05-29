Let $f$ be the function:

$$f (x) = \begin{cases} k^2 \sigma^2 & : \mid {x - \mu}\mid \geq k \sigma \\
0 & : \text{otherwise} \end{cases}$$

By construction, we see that:
$$f (x)\leq \mid {x - \mu}\mid^2 = \left( {x - \mu}\right)^2$$
for all $x$.

This means that:
$$\mathrm{E}\left( {f (X)}\right) \leq \mathrm{E}\left( {\left( {X - \mu}\right)^2}\right)$$

By definition of variance:

$$\mathrm{E}\left( {\left( {X - \mu}\right)^2}\right) = \mathrm{var}\left(X\right) = \sigma^2$$

By definition of expectation of discrete random variable, we can show that:

$$\mathrm{E}\left( {f (X)}\right) = k^2 \sigma^2 \Pr \left({\mid {X - \mu}\mid \geq k \sigma}\right) + 0 \cdot \Pr \left({\mid {X - \mu}\mid \leq k \sigma}\right)$$
$$ = k^2 \sigma^2 \Pr \left({\mid{X - \mu}\mid \geq k \sigma}\right)$$

Putting this together, we have:

$$\mathrm{E}\left( {f (X)}\right) \leq \mathrm{E}\left( {\left( {X - \mu}\right)^2}\right)$$
$$ \leadsto k^2 \sigma^2 \Pr \left({\mid {X - \mu}\mid \geq k \sigma}\right) \leq \sigma^2$$

By dividing both sides by $k^2 \sigma^2$, we get: 

$$\Pr \left({\mid {X - \mu}\mid \geq k \sigma}\right) \leq \dfrac {1}{k^2}$$

$\blacksquare$