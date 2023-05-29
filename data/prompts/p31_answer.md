Let the random variable $k$ have the binomial distribution with parameters $n$ and $p$, that is:
$$k \sim \mathrm{B} (n, p)$$
where $k$ denotes the number of successes of the $n$ independent trials of the event with probability $p$.


From Expectation of Binomial Distribution:
$$\mathrm{E}(k) = n p \leadsto \dfrac {1}n \mathrm{E}(k) = p$$

Expectation is Linear gives:
$$ \mathrm{E}\left({\dfrac k n}\right) = p =: \mu$$


Similarly, from Variance of Binomial Distribution:
$$\mathrm{var} \left(k\right) = n p \left({1 - p}\right) \leadsto \dfrac {1}{n^2} \mathrm{var} \left(k\right) = \dfrac {p \left({1 - p}\right)} n$$

From Variance of Linear Combination of Random Variables:
$$\mathrm{var} \left({\dfrac k n}\right) = \dfrac {p \left( {1 - p}\right) } n =: \sigma^2$$


By applying Chebyshev's Inequality to $\dfrac {k} {n}$, we have for any $l>0$:
$$\Pr \left({\left| {\dfrac k m - \mu}\right| \geq l \sigma}\right) \leq \dfrac {1}{l^2}$$

Now, let $\epsilon > 0$ and choose $l = \dfrac \epsilon \sigma$, to get:
$$\Pr \left({\left| {\dfrac k m - \mu}\right| \geq \dfrac \epsilon \sigma \cdot \sigma}\right) \leq \dfrac {\sigma^2} {\epsilon^2}$$

Simplifying and plugging in the values of $\mu$ and $\sigma^2$ defined above yields:
$$\Pr \left({\left| {\dfrac k n - p}\right| \geq \epsilon}\right) \leq \dfrac {p \left( {1 - p}\right) } {n \epsilon^2}$$

Scaling both sides by $-1$ and adding $1$ to both sides yields:
$$1- \Pr \left({\left| {\dfrac k n - p}\right| \geq \epsilon}\right) \geq 1 - \dfrac {p \left( {1 - p}\right) } {n \epsilon^2}$$

Applying Union of Event with Complement is Certainty to the left hand side:
$$\Pr \left({\left|{\dfrac k n - p}\right| \leq \epsilon}\right) \geq 1 - \dfrac {p \left( {1 - p}\right) } {n\epsilon^2}$$

Taking the limit as $n$ approaches infinity on both sides, we have:
$$\mathrm{} \lim_{n  \to \infty} \Pr \left({\left| {\frac{k}{n} - p}\right| < \epsilon}\right) = 1$$

$\blacksquare$