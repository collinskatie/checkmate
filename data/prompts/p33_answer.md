It is to be shown that $Q$ is a probability measure on $\left({\Omega, \Sigma}\right)$.


As $\Pr$ is a measure, we have that:

$$\forall A \in \Omega: Q (A) \geq 0$$

Also, we have that:

$$ Q \left(\Omega\right) = \Pr \left(\Omega\mid B\right)$$
$$ = \frac {\Pr \left({\Omega \cap B}\right) } {\Pr \left({B}\right)}$$
$$ = \frac {\Pr \left({B}\right)} {\Pr \left({B}\right)}\text{\quad Intersection with Universe}$$
$$ = 1\text{\quad as } \Pr \left({B}\right) > 0$$


Now, suppose that $A_1, A_2, \ldots$ are disjoint events in $\Sigma$.

Then:

$$Q \left({\bigcup_{i  = 1}^\infty A_i}\right)
      | r = \frac {1} {\Pr(B)} \Pr \left({\left({\bigcup_{i  = 1}^\infty A_i}\right) \cap B}\right)$$
$$ = \frac {1} {\Pr(B)} \Pr \left({\bigcup_{i  = 1}^\infty \left({A_i \cap B}\right) }\right)\text{\quad Intersection Distributes over Union}$$
$$ = \sum_{i  = 1}^\infty \frac {\Pr\left({A_i \cap B}\right)} {\Pr(B)}\text{\quad as }\Pr \text{ is a measure}$$
$$ = \sum_{i  = 1}^\infty Q \left({A_i}\right)$$

$\blacksquare$