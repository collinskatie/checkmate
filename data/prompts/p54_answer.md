We assume the two hypotheses of the theorem.


We have that:

$$ {\frac {\mathrm{d}} {\mathrm{d} t} } \left({\Phi \left({t + T}\right) }\right) = {\Phi'} \left({t + T}\right)$$
$$ = {\mathbf{A}} \left({t + T}\right) \Phi \left({t + T}\right)$$
$$ = {\mathbf{A}} \left(t\right) \Phi \left({t + T}\right)$$

So the first implication of the theorem holds, that is: that $\Phi \left({t + T}\right)$ is a fundamental matrix.


Because $\Phi \left(t\right)$ and $\Phi \left({t + T}\right)$ are both fundamental matrices, there must exist some matrix $\mathbf C$ such that:
$$\Phi \left({t + T}\right) = \Phi \left(t\right) \mathbf C$$

Hence by the existence of the matrix logarithm, there exists a matrix $\mathbf{B}$ such that:
$$\mathbf C = e^{\mathbf{B}T}$$


Defining ${\mathbf{P}} \left(t\right) = \Phi \left(t\right) e^{-\mathbf{B} t}$, it follows that:

$${\mathbf{P}} \left({t + T}\right) = \Phi \left({t + T}\right) e^{-\mathbf{B} t - \mathbf{B} T}$$
$$ = \Phi \left(t\right) C e^{-\mathbf{B} T} e^{-\mathbf{B} t}$$
$$ = \Phi \left(t\right) e^{-\mathbf{B} t}$$
$$ = {\mathbf{P}} \left(t\right)$$

and hence ${\mathbf{P}} \left(t\right)$ is periodic with period $T$.

As $\Phi \left(t\right) = {\mathbf{P}} \left(t\right) e^{\mathbf{B} t}$, the second implication also holds.

$\blacksquare$