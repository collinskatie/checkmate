Let $\llbracket a \rrbracket_m$ denote the residue class modulo $m$ of $a$.

Since $a \perp m$, it follows by Reduced Residue System under Multiplication forms Abelian Group that $\llbracket a \rrbracket_m$ belongs to the abelian group $\left( {\mathbb{Z}'_m, \times}\right)$.

Let $k = \mid {\llbracket a \rrbracket_m}\mid$ where $\mid {\, \cdot \,}\mid$ denotes the order of a group element.

By Order of Element Divides Order of Finite Group:
$$k \backslash \mid {\mathbb{Z}'_m}\mid$$

By the definition of the Euler $\phi$ function:
$$\mid {\mathbb{Z}'_m}\mid = \phi \left(m\right)$$


Thus:

$$\llbracket a \rrbracket_m^k = \llbracket a \rrbracket_m \text{\quad Definition of Order of Group Element}$$
$$\leadsto \llbracket a \rrbracket_m^{\phi \left(m\right)} = \llbracket {a^{\phi \left(m\right)} }\rrbracket_m \text{\quad Congruence of Powers}$$
$$ = \llbracket 1 \rrbracket_m$$
$$ \leadsto a^{\phi \left(m\right)} \equiv 1 \mathrm{\ mod \ } m \text{\quad Definition of Residue Class}$$

$\blacksquare$