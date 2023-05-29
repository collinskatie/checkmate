Let $x, y, z \in X$:

We will show that $\left({X, *}\right)$ satisfies each of the [[Axiom:Group Axioms|group axioms]] in turn:


=== Group Axiom G0: Closure ===

By definition of $*$, we have:

$$x * y = x \circ \left( {0 \circ y}\right)$$

By Axiom $(AC)$ for $B$-algebras:

$$x \circ \left( {0 \circ y}\right) \in X$$


Whence $x * y \in X$, and so $\left( {X, *}\right)$ is a closed structure.

$\square$


=== Group Axiom G1: Associativity ===

$$\left( {x * y}\right) * z = \left( {x \circ \left( {0 \circ y}\right) }\right) \circ \left( {0 \circ z}\right) \text{\quad Definition of } *$$
$$ = x \circ \left( {\left( {0 \circ z}\right) \circ \left( {0 \circ \left( {0 \circ y}\right) }\right) }\right)\text{\quad Axiom } (A3) \text{ for } B\text{-algebras}$$
$$ = x \circ \left( {\left( {0 \circ z}\right) \circ y}\right) \text{\quad Identity: } 0 \circ \left( {0 \circ x}\right) = x$$
$$ = x \circ \left( {0 \circ \left( {y \circ \left( {0 \circ z}\right) }\right) }\right)\text{\quad Axiom } (A3) \text{ for } B\text{-algebras}$$
$$ = x * \left( {y * z}\right)\text{\quad Definition of }*$$

Thus it is seen that $*$ is associative.

$\square$


=== Group Axiom G2: Existence of Identity Element ===

Let $e := 0$; we will show that it is an identity element of $\left({X, *}\right)$.

$$x * e = x \circ \left( {0 \circ 0}\right)\text{\quad Definition of } * \text{ and } e$$
$$ = x \circ 0\text{\quad Axiom } (A1) \text{ for } B\text{-algebras}$$
$$ = x\text{\quad Axiom } (A2) \text{ for } B\text{-algebras}$$


$$ e * x = 0 \circ \left( {0 \circ x}\right)\text{\quad Definition of } * \text{ and } e$$
$$ = x\text{\quad Identity: } 0 \circ \left( {0 \circ x}\right) = x$$


Hence $0$ is an identity for $*$.

$\square$


=== Group Axiom G3: Existence of Inverse Element ===

Let us prove that for all $x \in X$, $0 \circ x$ is an inverse element to $x$.

$$ x * \left( {0 \circ x}\right) = x \circ \left( {0 \circ \left( {0 \circ x}\right) }\right)\text{\quad Definition of } *$$
$$ = x \circ x\text{\quad Identity: } 0 \circ \left( {0 \circ x}\right) = x$$
$$ = 0\text{\quad Axiom } (A1) \text{ for } B\text{-algebras}$$


$$ \left( {0 \circ x}\right) * x = \left( {0 \circ x}\right) \circ \left( {0 \circ x}\right)\text{\quad Definition of } *$$
$$ = 0\text{\quad Axiom } (A1) \text{ for } B\text{-algebras}$$


That is, each $x \in X$ has a unique inverse element $x^{-1}$ under $*$.

This inverse element is $0 \circ x$.

$\square$


It follows that:

$$ a * b^{-1} = a \circ \left( {0 \circ b^{-1} }\right)\text{\quad Definition of } *$$
$$ = a \circ \left( {0 \circ \left( {0 \circ b}\right) }\right)\text{\quad Definition of } b^{-1}$$
$$ a \circ b\text{\quad Identity: }0 \circ \left( {0 \circ x}\right) = x$$

$\square$


All the axioms have been shown to hold and the result follows.

$\blacksquare$