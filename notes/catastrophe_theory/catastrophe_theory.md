# Catastrophe Theory --<br> The Seven Elementary Catastrophes

<p class="author">Benjamin Hertzsch</p>


__*Disclaimer:*__ These notes were typed up as a first version for a PhD  seminar I gave in Edinburgh on the 27/02/2025. These notes likely contain numerous typos, are wordy or inaccurate in places, and the there are issues with varying screen sizes. I will update the notes and fix the template soon.

In these notes, I will derive Thom's *seven elementary catastrophes* ([Thom (1972)](https://books.google.co.uk/books/about/Stabilit%C3%A9_structurelle_et_morphog%C3%A9n%C3%A8s.html?id=t7Lbs7x5G9wC&redir_esc=y)), the main elements of catastrophe theory in the four-dimensional universe. Key works on catastrophe theory are [Thom (1972)](https://books.google.co.uk/books/about/Stabilit%C3%A9_structurelle_et_morphog%C3%A9n%C3%A8s.html?id=t7Lbs7x5G9wC&redir_esc=y), [Arnol'd (1972)](https://link.springer.com/article/10.1007/BF01077644) (amongst many of Arnol'd's mathematical works on catastrophe theory) as well as various articles by [Zeeman (1972-1977)](https://books.google.co.uk/books/about/Catastrophe_Theory.html?id=CxuYf2PP2hsC&redir_esc=y). An in-depth and mathematically rigorous survey of catastrophe theory can be found in [Arnold et al. (1985)](https://link.springer.com/book/10.1007/978-0-8176-8340-5). For applications of catastrophe theory, see also [Arnold (1984)](https://link.springer.com/book/10.1007/978-3-642-58124-3); for beautiful illustrations of the various caustics in optics, we refer to [Berry (1980)](https://michaelberryphysics.wordpress.com/wp-content/uploads/2022/02/berry089-1.pdf). In the following, I will closely follow [Saunders (1980)](https://www.cambridge.org/core/books/an-introduction-to-catastrophe-theory/D5ECA839997CD9C2A247C413E69CD2B8) to derive catastrophe theory in the language familiar to physicists.

## Fundamentals and terminology

<p><span class="paragraph">Critical points and Morse's lemma</span>
Consider a multivariate function $f(\mathbf{x})$ of some state variables $\mathbf{x}$. The function has a critical point at $\mathbf{x}_0$ if

$$
\nabla \mathbf{x} \lvert_{\mathbf{x}_0} = 0
$$

The critical point is *non-degenerate* if the Hessian $\mathcal{H}f(\mathbf{x}) = \partial_i \partial_j f(\mathbf{x})$ at the critical point is invertible, i.e. if

$$
\det(\mathcal{H}f(\mathbf{x})) \lvert_{\mathbf{x}_0}  \neq 0
$$

If $\det(\mathcal{H}f(\mathbf{x})) \lvert_{\mathbf{x}_0} = 0$, the critical point is *degenerate*. In the one-dimensional case, $f(x)$, it is customary to call the a critical point *$n$-fold degnerate* for $n$ derivatives higher than first-order vanishing at $x_0$.

**Catastrophe theory is the general classification of degenerate points and thus extends Morse's classication of non-degenerate critical points**. In the following, critical points will always taken to be at the origin $\mathbf{x} = \mathbf{0}$.

<figure>
<img src="./notes/catastrophe_theory/figures/fig-min_max_Morse.jpeg" style="display: block; margin: 0 auto; width: 80%; max-width: 800px; padding: 5px;">
<figcaption>The functions $-x^2$ and $x^2$ have a maximum / minimum respectively as a non-degenerate critical point at the origin.</figcaption>
</figure>

For a function $f(x)$ of a single variable and a non-degenerate critical point at the origin, *Morse's classification* states that the critical point is a minimum if $f''(0) > 0$ and a maximum if $f''(0) < 0$. This classification extends to the multivariate case as follows: Consider a multivariate function $f(\mathbf{x})$ with $n$ state variables $\mathbf{x}$ and a non-degenerate critical point at the origin. *Morse's lemma* states that there exists a diffeomorphism $\psi$ which preservers the origin, $\psi(\mathbf{0}) = \mathbf{0}$, under which the function near the non-degenerate critical point may be written in the quadratic form

$$
f(\psi(\mathbf{x})) = -x_1^2 - x_2^2 - \ldots - x_p^2+1 + x_{p+1}^2 + \ldots + x_{n}^2 \,,
$$

One calls $p$ the (Morse) index of the singularity at $\mathbf{x}={0}$, which counts the directions in which the function assumes a maximum. Written in this quadratic form, it is obvious that the Hessian $\mathcal{H}{f}$ is invertible at a non-degenerate critical point. 


<p><span class="paragraph">Corank</span>
Degenerate critical points were defined above by the condition $\det \mathcal{H} f(\mathbf{x}) = 0$. Consider now a frame in which the Hessian is diagonal, so that diagonal second derivatives coincide with the eigenvalues, of the product of which is equal to the determinant. It is now a priori unclear how many of these eigenvalues vanish, corresponding to the orthogonal directions in which the Hessian is degenerate. The *splitting lemma* now states that to classify all the non-degenerate critical points, one only has to consider the *essential* variables, for which the vanishing of the second derivate cannot be removed by a suitable coordinate transformation. Their number is equal to the number of vanishing eigenvalues of $\mathcal{H} f(\mathbf{x})$. One refers to the number of essential variables as *corank* of the singularity.

In the following, I will assume the number of state variables for a function always to be equal to the number of essential variables, and hence use the terms interchangeably.


<p><span class="paragraph">Structural stability</span>
*Structural stability* refers to the property of a function that the qualitative nature of the function does not change under small perturbations. Consider for example the polynomials in a single variable $x^n$ up to some order $n$. Structural stability requires that the addition of any polynomial $\alpha x^m$ with small $\alpha$ and $m$ a positive integer and does not alter the critical nature of the function near the critical point (i.e. the origin). For $m>n$, this is trivially true; for $m<n$, the situation may change.

<figure>
<img src="./notes/catastrophe_theory/figures/fig-cubic_unfolding.jpeg" style="display: block; margin: 0 auto;  width: 90%; max-width: 900px; padding: 5px;">
<figcaption>The function $x^3 - \alpha x$ with $\alpha = \{-0.15, 0.0, 0.15\}$. Varying $\alpha$ from negative to positive values unfolds the degenerate critical point at the origin to a pair of non-degenerate critical points (maximum and minimum).</figcaption>
</figure>


Consider for instance the function $f(x) = x^3$ which has a degenerate critical point at the origin. This is function not structurally stable, as the addition of the term $-\alpha x$ with $\alpha>0$ would change the function's qualitative nature by unfolding the critical point at the origin into a maximum and a minimum at $x = \{ \pm \sqrt{\frac{\alpha}{3}}\}$. However, the family of functions $f_{\mathbf{u}}(\mathbf{x}) = x^3 + u_2 x^2 + u_1 x^1 + u_0$ is structurally stable, as the addition of any term $x^n$ up to $n=3$ does not change the critical behaviour of the family of functions. The same argument applies to multivariate functions with several state variables $\mathbf{x}$, where the function family $f_{\mathbf{u}}(\mathbf{x})$ addition of any small perturbation in $\alpha h(\mathbf{x})$ with must be "recovered" in the function family.

Throughout these notes, the subcript $\mathbf{u}$ will be generally omitted for simplicity, and "families of functions" will be simply referred to as "functions". It should be clear from the context that parameters may be involved.

At this point, note that we have been discussing polynomials only. This is actually general, as we are interested in the neighborhood of a critical point, where a function may be expanded in a Taylor series. The results we derived are therefore to be understood as classifying the $k$-*jet* $j^k(x)$ (Taylor series truncated at order $k$) of a generic analytic function that can be locally expanded as a polynomial.

<p><span class="paragraph">Unfoldings</span>
The function families discussed above are also called *unfoldings* of the singularities. Consider again the bare singularity $x^n$, for which the unfolding

$$
f_{\mathbf{u}}(x) = x^n + u_{n-1} x^{n-1} + \ldots + u_1 x + u_0
$$

provides a structurally stable family of functions. Similarly, for a singularity in several state variables $\mathbf{x}$, a possible unfolding is obtained by adding all monomials of lower order. For instance, for $x^3 y^2$, all terms $x^k y^l$ with $k <3 \in \mathbb{N}$, $l < 2 \in \mathbb{N}$ could appear in this function family.


An unfolding is said to be *versal* if it is structurally stable. Clearly, this is the case for the unfoldings proposed above. However, not all terms in these function families are actually necessary to ensure structural stability. For instance, for a singularity $x^n$, it is readily seen that the terms $u_{n-1} x^{n-1}$ and $u_0$ do not actually change qualitative behavior of the function, as they may simply be absorbed in a shift of the origin and do not change the critical point. For more than one state variable, it is not so obvious which terms would be relevant, but the same argument applies.

An unfolding is said to be *universal* if it is structurally stable and has the least number of parameters. The term *unfolding* in the literature usually refers to universal unfolding of a caustic. In the univariate case, the singularity a $x^n$ is $n-2$-fold degenerate and takes $n-2$ unfolding parameters:

$$
f_{\mathbf{u}}(x) = x^n + u_{n-2} x^{n-2} + \ldots + u_1 x
$$

For singularities with two state variables, a few universal unfoldings will be derived below. Throughout these notes, the essential (state) variables will always be denoted as $\mathbf{x}$, and the universal unfolding parameteres as $\mathbf{u}$.

Finally, consider again the singularity $x^3$, for which we can now write down the universal unfolding as 

$$
f(x) = x^3 + u x
$$

It is now clear that the term "unfolding" is chosen because the linear term reveals that the degenerate critical point actually is two coincident non-degenerate critical points, which are unfolded by varying $u$. Generally, universal unfoldings unfold $n$-fold degenerate critical points into $n+1$ non-degenerate critical points.


<p><span class="paragraph">Codimension</span>
The unfolding parameters in physical applications of catastrophe theory represent a target space, which is typically the (up to) $4$ dimensions of our space-time. This means that stable geometric objects (rather than unstable transient events) in this target space can be defined by up to $4$ constraint equations. The number of constraint equations is typically called the $codimension$ of an object. 

For the following list of seven elementary catastrophes, it suffices to define the codimension of a singularity as the number of parameters in the universal unfolding. This is because, as we have already seen for the univariate case $f(x)$, the number of unfolding parameters is equal to a singularity's degree of degeneracy. But saying that a critical point is $n$-fold degenerate is the same as saying that there $n$ constraint equations, which constrain $n$ higher derivatives to vanish.

For the case of more than one essential variable, the same argument holds, and the codimension is again equal to the number of unfolding parameters. We will see below that finding the universal unfoldings is more tricky, but we can already make another important observation:
Consider a singularity of corank $l$, with $l$ state variables (all of which are essential). The Hessian is symmetric, thus the vanishing of $\det \mathcal{H} f$ requires that all the $l(l+1)/2$ independent entries of the Hessian are zero. This means that there are $l(l+1)/2$ constraint equations, and the singularity is therefore of codimension at least $l(l+1)/2$. In words, a corank-$l$ singularity is stabilised by at least $l(l+1)$ unfolding parameters. Corank-3 singularities therefore take at least 6 unfolding parameters, and are not stable in the 4-dimensional universe; similarly for higher corank.

The corollary of the above is the following: 

<div class="centered-box">
**In the $4$-dimensional universe, the full classification of stable degenerate critical points is given by the catastrophes of corank up to 2 and codimension up to 4.**
</div>

Is is clear evident that the relevant corank-1 singularities are $x^3$ through $x^6$. It will also be shown the that there are three relevant corank-2 singularities.

<div class="centered-box">
**The seven elementary catastrophes are given by:**

**$x^3 \qquad x^4 \qquad x^5 \qquad x^6 \qquad x^3 + y^3 \qquad x^3 - x y^2 \qquad y^4 + x^2 y$**

These are called the **_fold_**, **_cusp_**, **_swallowtail_**, **_butterfly_** and the **_hyperbolic_**, **_elliptic_** and **_parabolic umbilic_**.
</div>

For completeness, note that our simplistic definition of codimension ceases to be appropriate for catastrophes of higher-order catastrophes, where moduli spaces occur and the geometric and algebraic dimensions of the singularities become different.

<p><span class="paragraph">Critical set, singular set and bifurcation set</span>
The normal forms of the caustics live in the space $(\mathbf{x}, \mathbf{u})$ of essential variables $\mathbf{x}$ and unfolding parameters $\mathbf{u}$. In this space, there are a few objects of interest, which reveal the characteristic geometries of the various caustics in physical applications. The *equilibrium* or *critical set* $\mathcal{M}$ is defined as the set of all points for which the function's gradient vanishes,

$$
\mathcal{M} = \{ \mathbf{x}, \mathbf{u} : \nabla f_{\mathbf{u}}(\mathbf{x}) = 0\} \,
$$

where the subscript $\mathbf{u}$ is again omitted. The *singular set* $\mathcal{S}$ is defined as the set of all points within the critical set for which the Hessian is non-invertable,

$$
\mathcal{S} = \{ \mathbf{x}, \mathbf{u}  \in \mathcal{M}: \det \mathcal{H} f_{\mathbf{u}}(\mathbf{x}) = 0\}
$$

Both $\mathcal{M}$ and $\mathcal{S}$ live in space of essential variables and unfolding parameters $(\mathbf{x},\mathbf{u})$. The *bifurcation set* $\mathcal{B}$ is defined as the projection of the singular set into the space of unfolding parameters

$$
\mathcal{B} = \{\mathbf{u}  \in \mathcal{S}\}
$$

$\mathcal{B}$ i readily obtained by eliminating the state variables $\mathbf{x}$ from $\mathcal{S}$ and $\mathcal{M}$.


<p><span class="paragraph">Physical manifestation of catastrophes</span>
Before deriving the classification of all caustics, it is instructive to attach a physical meaning to the objects defined above. The various catastrophes generally arise in situations that map from a space of initial configurations, *Lagrangian space*, to a space of final configurations, *Eulerian space*. The essential variables $\mathbf{x}$ here take the role of Lagrangian space coordinates, while the unfolding variables $\mathbf{u}$ correspond to the Eulerian space coordinates. The latter usually chart the (up to) $4$-dimensional space-time a physical experiment lives in.

The singularity germs describe the Lagrangian space configuration, e.g. a lensing or gravitational potential $\Phi(\mathbf{x})$. The critical set $\mathcal{M}$ then corresponds the set of solutions to a governing equation (mapping equation, equation of motion, ...) from this initial configuration, i.e. the set of all possible paths from $\mathbf{x}$ to $\mathbf{u}$. This may be, for instance, the ensemble of light rays bent by a lensing potential, matter moving through a gravitational potential, or generic solutions to an initial value problem. The singular set $\mathcal{S}$ then corresponds to the boundaries of those regions in the Eulerian space $\mathbf{u}$ where several solutions coincide; that is, where several Lagrangian positions $\mathbf{x}$ are mapped to the same final configuration $\mathbf{u}$. The Lagrangian space is usually inaccessible, so that an experiment does not observe $\mathcal{M}$ and $\mathcal{S}$, but only the bifurcation set $\mathcal{B}$, which is the projection of $\mathcal{S}$ into the observed Eulerian space $\mathbf{u}$.

These concepts are is nicely illustrated with snapshot of a 2D mesh simulation for cosmological structure formation; for more details, see [my research page](./research.html). An observer would observe the Eulerian space in the right panel, i.e. the density of particles at the final positions at some time $t$. The observer does not a priori know whence these particles came from, as the Lagrangian space is not observable. The bifurcation set in Eulerian space is characterised by (infinite) density spikes. Our knowledge of the simulation allows us to draw the evolving mesh from Lagrangian space, and correctly identify the bifurcation set as the set of Eulerian points bounding the *multistream* regions where several incoming paths overlap.





## The seven elementary catastrophes

Having discussed all the needed fundamental notions, I will discuss the seven elementary catastrophes and their characteristic geometries.

### Corank-1 catastrophes: the cuspoids

We will first discuss the the corank-1 catastrophes, which are known as the _cuspoids_, after the archetypical cusp catastrophe occurring in this family of singularities. 

We have already seen above that the universal unfoldings are given in the form $f(x) = x^n + u_{n-2} x^{n-2} + \ldots + u_1 x$. It is thus straightforward to derive the equilibrium, singular and bifurcation sets and discus their geometries.

#### A<sub>2</sub> fold catastrophe

Some properties of the fold catastrophe $x^3$ were already discussed above. The universal unfolding is

$$
\boxed{f_{A_2}(x) = x^3 + u x}
$$

with a single unfolding parameter $u$. The equilibrium and singular set are readily obtained:


$$
\mathcal{M}_{A_2} = \left\{ (x, u) :  3 x^2 + u = 0 \right\}
$$

$$
\mathcal{S}_{A_2} = \left\{ (x, u) : 6x = 0 \right\}
$$

Elimination of $x$ yields the bifurcation set

$$
\mathcal{B}_{A_2} = \left\{ u: u = 0 \right\}
$$

The bifurcation set in this case is just a single point in the unfolding space. This is exactly what we discussed above regarding the structural stability of the cubic polynomial: As the unfolding parameter $u$ is varied through 0, the qualitative nature changes as the degenerate critical point is unfolded into a pair of non-degenerate critical points (maximum and minimum).


#### A<sub>3</sub> cusp catastrophe

Next in the list of co-dimension-$1$ caustics is the *cusp* catastrophe $x^4$. The cusp has co-dimension $2$, and the universal unfolding is

$$
\boxed{f_{A_3}(x) = x^4 + u x^2 + v x}
$$

with two unfolding parameters $(u,v)$. The equilibrium and singular set are given by

$$
\mathcal{M}_{A_3} = \left\{ (x, u, v) :  4 x^3 + 2 u x + v = 0 \right\}
$$

$$
\mathcal{S}_{A_3} = \left\{ (x, u) : 12 x^2 + 2u = 0\right\}
$$

Eliminating $x$ yields the bifurcation set in the unfolding parameters

$$
\mathcal{B}_{A_3} = \left\{ (u, v) : 8 u^3 + 37 v^2 =0\right\}
$$

The equilibrium set (yellow) and singular set (red) are shown in the left panel of the figure below.  The bifurcation set is the projection into the space of unfolding parameters $(u,v)$ shown on the right-hand side. 

<figure>
<img src="./notes/catastrophe_theory/figures/fig-A3_equilibrium_set.jpeg" style="display: block; margin: 0 auto; width: 90%; max-width: 800px; padding: 5px;">
<figcaption>Equilibrium and singular set (left) and bifurcation set (right) of the $A_3$ catastrophe, revealing the characteristic cusp geometry.
</figure>

For clarity, the following figure also shows a rotating view of the equilbrium surface

<figure>
<img src="./notes/catastrophe_theory/figures/anim-A3_equilibrium_set.gif" style="display: block; margin: 0 auto; width: 50%; max-width: 350px;padding: 5px;">
<figcaption>Rotating view of the $A_3$ equilibrium set.
</figure>

The equilibrium and bifurcation set of the cusp catastrophe reveals a generic geometric property of all the caustics: The equilibrium surface is a smooth surface in the space $(\mathbf{x}, \mathbf{u})$, but the bifurcation set is not a smooth line in the unfolding space $(\mathbf{u})$. More formally, the equilibrium set is always a manifold, whereas the bifurcation set is not. In the case of the cusp, $\mathcal{B}$ is diffeomorphic, but not homeomorphic, to $\mathbb{R}^1$, meaning that $\mathcal{B}$ cannot be smoothly deformed to $\mathbb{R}^1$ without flattening the non-differentiable point at the origin.

As was mentioned above, the equilibrium set typically represent the physical solutions to a boundary problem, with $\mathbf{x}$ being the unobservable Lagrangian space, and $\mathbf{u}$ being the observed Eulerian space. For the cusp, we can see that there are regions of 3 overlapping solutions, which are bounded the by the cusp point and the fold lines emerging from it. These are known as *multi-image regions* in lensing applications, or *multistream regions* is cosmological structure formation and are nicely illustrated in the following physical applications.

<figure style="justify-content: center; width: 100%">
<div>
<img src="./notes/catastrophe_theory/figures/cusp_reflection.jpeg" alt="Description 1" style="width: 25%; min-width: 0px; margin-left: 8%; margin-right: 4%">
<img src="./notes/catastrophe_theory/figures/mirror_plot.jpeg" alt="Description 2" style="width: 25%;min-width: 0px;">
<img src="./notes/catastrophe_theory/figures/anim-A3_mesh.gif" alt="Description 2" style="width: 25%; min-width: 0px; margin-left: 4%; margin-right: 8%">
</div>
<figcaption>Physical realisations of cusp catastrophes: left a reflection in a circular mirror (taken from https://i.sstatic.net/TMJnP.jpg), modelled in the middle panel with a circular mirror and a single reflection (dominant contribution to caustic) of the incident rays. The right panel shows a 2D cosmological mesh simulation (Zel'dovich approximation) for the formation of Zel'dovich pancake, bounded by two fold lines connecting two cusp points.</figcaption>
</figure>



#### A<sub>4</sub> swallowtail catastrophe

The next corank-1 catastrophe is the swallowtail $x^5$, which has co-dimension 3 with the universal unfolding

$$
\boxed{f_{A_4}(x) = x^5 + u x^3 + v x + w}
$$

The equilibrium and singular set are given by

$$
\mathcal{M}_{A_4} = \left\{ (x, u, v, w) :  5 x^4 + 3 u x^2 + 2 v x + w = 0 \right\} 
$$

$$
\mathcal{S}_{A_4} = \left\{ (x, u, v) : 20 x^3 + 6 u x + 2v = 0\right\}
$$

Eliminating $x$ gives the two-dimensional bifurcation surface in the space of unfolding parameters $(u,v,w)$:

$$
\mathcal{B}_{A_4} = \left\{ (u, v, w) : -81 u^4 w+27 u^3 v^2+360 u^2 w^2-540 u v^2 w+135 v^4-400 w^3=0 \right\}
$$

The equilibrium set $\mathcal{M}_{A_4}$ is now a $3$-dimensional volume in the $4$-dimensional space $(x,u,v,w)$. To visualise the characteristic swallowtail geometry, it is instructive to plot slices of the equilibrium set for varying values of $u$, as done in the figure below.

<figure>
<img src="./notes/catastrophe_theory/figures/fig-A4_equilibrium_set.jpeg" style="display: block; margin: 0 auto; max-width: 100%; max-height: 400px; width: auto; padding: 5px;">
<figcaption>Slices of the $A_4$ equilibrium for fixed varying values $u=\{1.5, 0.0, -1.5\}$, revealing the unfolding of the non-degenerate critical point into two cusp points and three fold lines.</figcaption>
</figure>

As in the cusp catastrophe, the equilibrium surface (i.e. the slice for fixed $u$) folds over itself, so that the projection into the $(v, w)$-plane yields a multi-image regions with overlapping pieces of the equilibrium surface. The swallowtail caustic unfolds by forming a pocket in the equilibrium surface, which is bounded by two cusp points and three fold lines. This becomes clearer in the animation below, which visualises the equilibrium set for fixed $u$. The bifurcation set $\mathcal{B}_{A_4}$ is a two-dimensional surface in the $3$-dimensional unfolding space $(u,v,w)$, and can be readily visualised.

<figure>
<div style="display: flex; justify-content: center; gap: 100px; max-width: 100%;">
<img src="./notes/catastrophe_theory/figures/anim-A4_equilibrium_set.gif" alt="Description 1" style="height: 300px; margin-right: 25px">
<img src="./notes/catastrophe_theory/figures/fig-A4_bifurcation_set.jpeg" alt="Description 2" style="height: 300px; margin-left: 25px">
</div>
<figcaption>Left panel: Rotating view of the equilibrium set $\mathcal{M}_{A_4}$ for $u=-1.5$. Right panel: The bifurcation set $\mathcal{B}_{A_4}$ of the $A_4$ catastrophe.</figcaption>
</figure>

In physical applications, the unfolding parameters $(v,w)$ may correspond to the spatial coordinates of a two-dimensional target space, while $u$ corresponds to time coordinate or other control parameter that controls the "strength" or "growth" of the swallowtail caustic. An observer would therefore typically see "growing" slices of $\mathcal{B}_{A_4}$ for varying $u$. This becomes apparent when continuously varying $u$ and plotting the equilibrium set slices along with the corresponding bifurcation set slices:

<figure>
<img src="./notes/catastrophe_theory/figures/anim-A4_equil_bif_set.gif" style="display: block; margin: 0 auto; height: 300px; width: auto; padding: 5px;">
<figcaption>Animation of the $u$-slice of the $A_4$ equilibrium (and corresponding singular) set for varying values of $u$.</figcaption>
</figure>

This is illustrated in the following the figures, where the correspondence with the animation above becomes apparent.

<figure>
<div style="display: flex; justify-content: center; gap: 100px; max-width: 100%;">
<img src="./notes/catastrophe_theory/figures/fig-A4_Berry.jpg" alt="Description 1" style="height: 250px; padding: 20px">
<img src="./notes/catastrophe_theory/figures/swallowtail_optics.jpg" alt="Description 1" style="height: 250px; padding: 20px">
<img src="./notes/catastrophe_theory/figures/anim-A4_mesh.gif" alt="Description 1" style="height: 250px; padding: 20px">
</div>
<figcaption>Left: Swallowtail caustic in an optics experiment, taken from  [Berry (1980)](https://michaelberryphysics.wordpress.com/wp-content/uploads/2022/02/berry089-1.pdf). Middle panel: another optical swallowtail catastrophe, taken from https://www.researchgate.net/figure/Two-simulations-of-optical-diffraction-patterns-near-i-a-swallowtail-ii-a_fig1_365445500. Right panel: 2D cosmological mesh simulation (Zel'dovich approximation) for the formation of a swallowtail cluster.</figcaption>
</figure>


The swallowtail catastrophe in particular has attracted attention not only from scientists, but also in the fine arts. And example is Salvador Dalí's last painting, "The swallow's tail" (1983), which Dalí created in honour of the aesthetics of Thom's theory of catastrophes and their morphogenesis. More recently, engineer and author Allan McRobie has interpreted catastrophe theory as the theory of "beautifully curved" surfaces, which appear ubiquitously in the organic world, and are found to appeal more to the innate human understanding of beauty than the simple shapes of solid geometry possibly could. An example of this is shown in the right panel of the figure below, where a woman's curved torso is aesthetically forming the equilibrium surface of the swallowtail catastrophe.

<figure>
<div style="display: flex; justify-content: center; gap: 100px; max-width: 100%;">
<img src="./notes/catastrophe_theory/figures/Dali_swallowtail.jpg" alt="Description 1" style="height: 250px; padding: 20px">
<img src="./notes/catastrophe_theory/figures/seduction_curves.jpg" alt="Description 1" style="height: 250px; padding: 20px">
</div>
<figcaption>Left: Salvador Dali's "La queue d'aronde" ("The swallow's tail") (1983), an artistic illustration of Thom's catastrophe theory. Taken from https://www.wikiart.org/en/salvador-dali/the-swallow-s-tail. Right: Cover photo of Allan McRobie's "The seduction of curves" (2017), a woman's torso forming the swallowtail equilibrium surface. Taken from https://www.eng.cam.ac.uk/news/seduction-curves-lines-beauty-connect-mathematics-art-and-nude-allan-mcrobie.</figcaption>
</figure>



#### A<sub>5</sub> butterfly catastrophe

The last in the list of the corank-1 cuspoid singularities is the butterfly catastrophe $x^6$ which is of co-dimension $4$ with the universal unfolding

$$
\boxed{f_{A_5}(x) = x^6 + t x^4 + u x^3 + vx^2 + wx}
$$

The equilibrium and singular sets are given by

$$
\mathcal{M}_{A_5} = \left\{ (x, t, u, v, w) :  4 t x^3+3 u x^2+2 v x+w+6 x^5 = 0 \right\}
$$

$$
\mathcal{S}_{A_5} = \left\{ (x, t, u, v, w) : 12 t x^2+6 u x+2 v+30 x^4 = 0\right\} \,,
$$

thus yielding the (somewhat more complicated) bifurcation set

$$
\mathcal{B}_{A_5} = \left\{ (t, u, v, w) : -13824 t^5 w^2+13824 t^4 u v w-4096 t^4 v^3-3456 t^3 u^3 w+1152 t^3 u^2 v^2+86400 t^3 v w^2-89100
t^2 u^2 w^2-80640 t^2 u v^2 w+24576 t^2 v^4+102060 t u^3 v w-31104 t u^2 v^3+202500 t u
w^3-144000 t v^2 w^2-19683 u^5 w+6561 u^4 v^2-182250 u^2 v w^2+172800 u v^3 w-36864 v^5-84375
w^4=0 \right\}
$$

The equilibrium set is now $4$-dimensional in the $5$-dimensional space $(x,t,u,v,w)$. Similarly, the bifurcation set is now a $3$-dimensional volume in the $4$-dimensional unfolding space $(t,u,v,w)$. Visualisations of the full structure are therefore difficult. Yet, intuition about the butterfly geometry can be gained by considering slices for fixed $t,u$.
The following figure shows the equilibrium set slice along with corresponding bifurcation set slice for fixed $(t,u)$.

<figure style="margin-bottom: 20px">
<img src="./notes/catastrophe_theory/figures/fig-A5_equil_set.jpeg" style="display: block; margin: 0 auto; height: 300px; width: auto; padding: 5px;">
<figcaption>Slice of the $A_5$ equilibrium set for $(t,u)=(-1,0)$ seen from different angles.</figcaption>
</figure>


<figure>
<div style="display: flex; justify-content: center; gap: 100px; max-width: 100%;">
<img src="./notes/catastrophe_theory/figures/anim-A5_equil_bif_set.gif" alt="Description 1" style="height: 300px; margin-right: 30px">
<img src="./notes/catastrophe_theory/figures/fig-A5_bif_set.jpeg" alt="Description 2" style="height: 300px; margin-left: 30px">
</div>
<figcaption>Left panel: Rotating view of the $A_5$ equilibrium set slice for $(t,u)=(-1,0)$. Right panel: Corresponding slice of the $A_5$ bifurcation set.</figcaption>
</figure>



Again, more intuition may be gained by smoothly varying the parameters $(t,u)$. This is done in the following animation, where $(t,u)$ are varied along a circle about the origin. Both the equilibrium set slice and the corresponding bifurcation set slice are shown in the middle and right panels. The animation nicely illustrates how the butterfly catastrophe unfolds into lower catastrophes, namely swallowtails, cups and connecting fold lines, at different points in the unfolding space.

<figure>
<img src="./notes/catastrophe_theory/figures/anim-A5_equil_bif_set_variation.gif" style="display: block; margin: 0 auto; height: 300px; width: auto; padding: 5px;">
<figcaption>Slices of the $A_5$ bifurcation set $\mathcal{B}_{D_5}$ for $(t,u)$ varied in a circle of radius of radius $r=1.5$ about the origin.</figcaption>
</figure>


### Corank-2 catastrophes: the umbilics

The corank-1 catastrophes were trivial to derive from the structural stability of the canonical $x^n$ singularity. For the corank-2 catastrophes, more work is needed, and we again follow [Saunders (1980)](https://www.cambridge.org/core/books/an-introduction-to-catastrophe-theory/D5ECA839997CD9C2A247C413E69CD2B8) for the detailed derivation.

To investigate the non-degenerate critical points of corank 2, let us start the derivation from the 3-jet of a function with two variables $(x,y)$ such that the 2-jet identically vanishes:

$$
j^3(x,y) = (a_1 x + b_1 y)(a_2 x + b_2 y)(a_3 x + b_3 y)
$$

Our task now is to find suitable diffeomorphisms to bring this 3-jet into (one possible choice of) the distinct forms for the canonical singularities. The proposed factorised form of the 3-jet is particularly nice, as the 3 corank-2 singularities turn out to correspond to three possible cases for roots the jet polynomial, namely (i) real distinct roots, (ii) complex distinct roots and (iii) one pair of repeated real roots. We now go through these cases and discuss their geometries.


#### D<sub>4</sub><sup>+</sup> hyperbolic umbilic

Consider first the case of complex roots. Because complex roots of a real polynomial appear in pairs, we can conclude w.l.o. generality that $(a_3 = \bar{a}_2, b_3 = \bar{b}_2)$ and write $j^3(x,y) = (a_1 x + b_1 y)\left((\Re(a_2) x + \Re(b_2) y)^2 + (\Im(a_2) x + \Im(b_2) y)^2 \right)$. Using two linear transformations (diffeomorphisms), we can write

$$
j^3(x,y) \sim (a x + b y)(x^2 + y^2) \sim x^3 + x y^2 \sim x^3 + y^3
$$

The first transformation used was $(x \mapsto ax + by, y \mapsto bx -ay)$, and the second diffeomorphism was found by writing $(x+y)^3 + (x-y)^3 = 2x^3 + 6xy^2$.

The form $\eta(x,y) = x^3 + x y^2$ is the one used by [Arnol'd (1972)](https://link.springer.com/article/10.1007/BF01077644), and we will see below that it is parallel to the canonical form of elliptic umbilic. For physical applications, the form $\eta(x,y) = x^3 + y^3$ is generally found to be more useful, and we therefore take the canonical form of the form of the $D_4^+$ singularity to be

$$
\boxed{D_4^+: \quad \eta(x,y) = x^3 + y^3}
$$

We are now interested in the universal unfolding, which we will find using *Siersma's trick*. One starts by considering a versal unfolding $g(x,y)$ of the canonical singularity by adding all possible monomials in $x, y$:

$$
g(x, y) = \eta(x,y) + \sum_{i,j} \alpha_{i,j} x^i x^j
$$

Clearly, this is not the universal unfolding as several of the added terms can be eliminated by a suitable diffeomorphism, just as $x^{n-1}$ was eliminated for the $x^n$-singularities above. Consider now an infinitesimal diffeomorphism $\Psi : \left\{ x \mapsto x + \psi(x,y),  y \mapsto y + \chi(x,y) \right\}$ with some polynomial functions $\psi(x,y), \chi(x,y)$.  This infinitesimal diffeomorphism transforms the canonical singularity to

$$
\Psi :  \eta(x,y) \mapsto \eta(x,y) + \psi(x,y) \frac{\partial \eta(x,y)}{\partial x} + \chi(x,y) \frac{\partial \eta(x,y)}{\partial y}
$$

This implies that a suitable choice of the functions $\psi(x,y), \chi(x,y)$ can reproduce any terms in  $g(x,y)$ that are multiples of either $\frac{\partial \eta}{\partial x}$ or $\frac{\partial \eta}{\partial y}$. These terms can therefore not be part of the universal unfolding, and can be eliminated. The remaining terms may or may not be the terms in the universal unfolding.

This is visually illustrated by arranging all monomials in a triangle such that any term is a multiple of its upper neighbors. One now draws a shadow from the terms $\partial_x \eta$ and $\partial_y \eta$ to exclude their multiples. For the $D_4^+$ singularity, these are $\partial_x \eta\sim x^2$ and $\partial_y \eta\sim y^2$. 

<figure>
<img src="./notes/catastrophe_theory/figures/fig-triangle_D4p.jpg" style="display: block; margin: 0 auto; height: 180px; padding: 5px;">
<figcaption>Siersma's triangle for the $D_4^+$ singularity.</figcaption>
</figure>

Here, we find three unshaded terms $x, y, xy$ which may appear in the universal unfolding. But the $D_4^+$ catastrophe has codimension 3 (the least codimension for corank-2 singularities), and we therefore conclude that we have obtained universal unfolding with these three terms:

$$
\boxed{f_{D_4^+}(x) = x^3 + y^3  + w x y - u x - v y}
$$

From here on, we can proceed as before. The equilibrium set $\mathcal{M}_{D_4^+}$ of the elliptic umbilic caustic is given by the two simultaneous equations

$$
\mathcal{M}_{D_4^+} = \{ (x, y, u, v, w) : -u+w y+3 x^2 = 0 \qquad -v+w x+3 y^2=0\}
$$

and the singular set $\mathcal{S}_{D_4^+}$ is given by 

$$
\mathcal{S}_{D_4^+} =  \{ (x, y, u, v, w) : 36 x y-w^2 = 0 \}
$$

Eliminating the essential variables $(x,y)$ yields the bifurcation set $\mathcal{B}_{D_4^+}$

$$
\mathcal{B}_{D_4^+} = \{ (u, v, w) : -u^4+8 u^3 w^2-2 u^2 v^2-18 u^2 w^4-24 u v^2 w^2-v^4-18 v^2 w^4+27 w^8=0 \}
$$

The bifurcation set $\mathcal{B}_{D_4^+}$ is a 2-dimensional surface in the unfolding space $(u,v,w)$, and may therefore be readily visualised. In physical application, the parameter $w$ typically corresponds to a time or other strength parameter, specifying the growth of the caustic. It is therefore most instructive to also plot a slice of the bifurcation set for fixed $u$, as this is the configuration that may be observed e.g. in optical experiments at a given time.

<figure>
<img src="./notes/catastrophe_theory/figures/fig-D4hyp_bifurcation_set.jpeg" style="display: block; margin: 0 auto; height: 300px; width: auto; padding: 5px;">
<figcaption>Bifurcation set $\mathcal{B}_{D_4^+}$ of the hyperbolic caustic, with a slice for fixed $w=-1$ on the right hand side</figcaption>
</figure>

More intuiton about the arguably beautiful purse-like folding of the bifurctation is obtained by rotating the surface

<figure>
<img src="./notes/catastrophe_theory/figures/anim-D4hyp_bifurcation_set.gif" style="display: block; margin: 0 auto; height: 300px; width: auto; padding: 5px;">
<figcaption>Rotating view of the bifurcation set $\mathcal{B}_{D_4^+}$.</figcaption>
</figure>

While we have now shown the characteristic geometry of the hyperbolic umbilic caustic as may be observed in experiments, it is worthwhile to also investigate the equilibrium set $\mathcal{M}_{D_4^+}$. Here, this is a 3-dimensional volume. If one again considers a slice for fixed $w$ (i.e. physically considers a fixed-time slice), the 2-dimensional $\mathcal{M}_{D_4^+}$-slice may be readily visualised e.g. by eliminating the state variable $x$ (i.e. projecting into the space $(y,u,v)$).

<figure>
<img src="./notes/catastrophe_theory/figures/anim-D4p_equil_bif_set.gif" style="display: block; margin: 0 auto; height: 300px; width: auto; padding: 5px;">
<figcaption>Rotating view of a slice of the equilibrium set $\mathcal{M}_{D_4^+}$ for fixed $w=1$, projected into $(y,u,v)$ by eliminating $x$.</figcaption>
</figure>

The rotating view of the equilibrium surface beautifully illustrates the argument brought forward above, namely that the equilibrium and singular sets of the catastrophes are smooth manifolds, with the singular structure in the bifurcation sets miraculously arising from projections "along the line of sight".



<figure>
<div style="display: flex; justify-content: center; gap: 100px; max-width: 100%;">
<img src="./notes/catastrophe_theory/figures/fig-D4p_Berry.jpg" alt="Description 1" style="height: 250px; margin-right: 25px">
<img src="./notes/catastrophe_theory/figures/anim-D4p_mesh.gif" alt="Description 1" style="height: 250px;  margin-left: 25px">
</div>
<figcaption>Left: hyperbolic umbilic caustic in an optical experiment, taken from [Berry (1980)](https://michaelberryphysics.wordpress.com/wp-content/uploads/2022/02/berry089-1.pdf). Right: Cosmological 2D mesh simulation (Zel'dovich approximation) of a hyperbolic umbilic cluster.</figcaption>
</figure>



#### D<sub>4</sub><sup>-</sup> elliptic umbilic

Consider now the case of three real and distinct root, i.e. the coefficient pairs $(a_i, b_i)$ are distinct. One can then write the 3-jet as

$$
j^3(x,y)  \sim (a x + b y) x y \sim (x + y) x y \sim x (x^2 - y^2) \,,
$$

where we first used the diffeomorphism $(x \mapsto a_2 x + b_2 y, y \mapsto a_2 x + b_2 y)$ and then $(x \mapsto x + y, y \mapsto x- y)$.

We thus take the canonical form of the $D_4^-$ singularity to be

$$
\boxed{D_4^-: \quad \eta(x,y) = x^3 - x y^2}
$$

and the nomenclature $D_4^{\pm}$ in Arnold's form $x^3 \pm x y^2$ is evident.

We now again find the universal unfolding Siersma's trick. The relevant derivatives are $\partial_x \eta\sim x^2 - y^2$ and $\partial_y \eta \sim x y$. While the latter has an obvious place in the diagram, the former does not. One can, however, use these terms to write $x^3 = x(x^2 - y^2) + y(yx)$ and similary for $y^3$, so that both $x^3$ and $y^3$ may be eliminated.



<figure>
<img src="./notes/catastrophe_theory/figures/fig-triangle_D4m.jpg" style="display: block; margin: 0 auto; height: 180px;  padding: 5px;">
<figcaption>Siersma's triangle for the $D_4^-$ singularity.</figcaption>
</figure>

There are 4 unshaded terms, $x, y, x^2$ and $y^2$ left. But the $D_4^-$ singularity again has codimension 3, so one further variable must be eliminated. If one introduces a symmetric unfolding term $x^2 + y^2$, one can easily eliminate both $x^2$ and $y^2$ by writing $2 x^2 = (x^2+y^2) + (x^2-y^2)$ and similarly for $y^2$. Note that one could equivalently use $x^2$ or $y^2$ to eliminate the other respectively, but the symmetric form is generally found more useful. We therefore write the universal unfolding as

$$
\boxed{f_{D_4^-} = 1/3 x^3 - x y^2  + w (x^2 + y^2) - u x + v y}
$$

The equilibrium set $\mathcal{M}_{D_4^-}$ of the elliptic umbilic caustic is given by the two simultaneous equations

$$
\mathcal{M}_{D_4^-} = \{ (x, y, u, v, w) : -u+2 w x+x^2-y^2 = 0 \qquad v+2 w y-2 x y = 0 \}
$$

and the singular set $\mathcal{S}_{D_4^-}$ is given by 

$$
\mathcal{S}_{D_4^-} = \{ (x, y, u, v, w) : 4 w^2 - 4 x^2 - 4 y^2 =0 \}
$$

Eliminating the essential variables $(x,y)$ yields the bifurcation set $\mathcal{B}_{D_4^-}$

$$
\mathcal{B}_{D_4^-} = \{ (u, v, w) : -u^4+8 u^3 w^2-2 u^2 v^2-18 u^2 w^4-24 u v^2 w^2-v^4-18 v^2 w^4+27 w^8=0 \}\,,
$$

which is a two-dimensional surface the three-dimensional unfolding space $(u, v, w)$. The full bifurcation set $\mathcal{B}_{D_4^-}$ may be readily visualised in the figure below

<figure>
<img src="./notes/catastrophe_theory/figures/fig-D4ell_bifurcation_set.jpeg" style="display: block; margin: 0 auto; height: 300px; width: auto; padding: 5px;">
<figcaption>Bifurcation set $\mathcal{B}_{D_4^-}$ of the umbilic catastrophe, and slice for $u=-0.5$.</figcaption>
</figure>

Clearly visible is the characteristic triangular geometry, with the elliptic umbilic point unfolding into three cusp points connected by fold lines. As for the hyperbolic umbilic, it is again instructive to plot a slice of the equilibrium set $\mathcal{M}_{D_4^-}$ for fixed $w$, this time by projecting into $(x,u,v)$. The following animation beautifully illustrates how the equilibrium is a smooth surface, with the triangular structure arising from the projection of the singular set along the line of sight.


<figure>
<img src="./notes/catastrophe_theory/figures/anim-D4m_equil_bif_set.gif" style="display: block; margin: 0 auto; height: 300px; padding: 5px;">
<figcaption>Rotating view of the equilibrium set $\mathcal{M}_{D_4^-}$ of the elliptic umbilic for $w=-0.5$.</figcaption>
</figure>

The characteristic triangular geometry of the elliptic umbilic caustic is readily observed in physical applications.


<figure>
<div style="display: flex; justify-content: center; gap: 100px; max-width: 100%;">
<img src="./notes/catastrophe_theory/figures/fig-D4m_Berry.jpg" alt="Description 1" style="height: 220px; margin-right: 20px">
<img src="./notes/catastrophe_theory/figures/fig-D4m_Berry_2.jpg" alt="Description 1" style="height: 220px; margin-left: 20px;  margin-right: 20px">
<img src="./notes/catastrophe_theory/figures/anim-D4m_mesh.gif" alt="Description 1" style="height: 220px; margin-left: 20px">
</div>
<figcaption>Left and umbilic: elliptic umbilics in optical experiments, both taken from [Berry (1980)](https://michaelberryphysics.wordpress.com/wp-content/uploads/2022/02/berry089-1.pdf). In the middle panel, the wavelength is comparable to the length scale of the caustic, thus resulting in a clear wave interference pattern pattern. Right: Cosmological 2D mesh simulation (Zel'dovich approximation) of an elliptic umbilic cluster.</figcaption>
</figure>


#### D<sub>5</sub> parabolic umbilic

The parabolic umbilic corresponds to the case of a pair of repeated roots. One can write 

$$
j^3(x,y) \sim (a_1 x + b_1 y)^2(a_3 x + a_3 y) \sim x^2 y
$$

The equality of the repeated roots gives an additional constraint equation, thus raising the codimension to 4. One can show that this requires one to consider the 4-jet

$$
j^4(x,y) =  x^2 y+ h(x,y)
$$ 

to obtain the canonical form of the singularity. Writing $h(x,y) = \alpha_1 y^4 + \alpha_2 y^3 x + \alpha_3 y^2 x^2 + \alpha_4 x y^3 + \alpha_5 x^4$, one now wants to find a diffeomorphism $\Psi : \left\{ x \mapsto x + \psi(x,y),  y \mapsto y + \chi(x,y) \right\}$ that does not alter the 3-jet to and simplify the 4-jet. It can be shown that one can choose $\psi(x,y) = -\frac{1}{2} \alpha_2 y^2, \chi(x,y) = -(\alpha_3 y^2 + \alpha_4 x y + \alpha_5 x^2)$ to obtain $j^4(x,y) \sim x^2 y + y^4$, which we take as the canonical form of the $D_5$ singularity:

$$
\boxed{D_5: \quad \eta(x,y) = y^4 + x^2 y }
$$

Note that a further degeneracy in the 3-jet or the requirement of a higher term (e.g. $y^4$) vanishing in the 4-jet would raise the codimension to 4. The $D_5$ singularity is therefore the last in the list of the catastrophes up to codimension 4.

The universal unfolding is again found by considering $\partial_x \eta \sim x y$ and $\partial_y \eta \sim x^2 + y^3$, where the former has a place in the diagram. One can draw further shadows from $x^3 = -y^2(xy) + x(x^2 + y^3)$ and $y^4 = y (x^2 + y^3) - x(xy)$.

<figure>
<img src="./notes/catastrophe_theory/figures/fig-triangle_D5.jpg" style="display: block; margin: 0 auto; height: 180px; padding: 5px;">
<figcaption>Siersma's triangle for the $D_5$ singularity.</figcaption>
</figure>

This leaves 5 unshaded terms $x, y, x^2, y^2, y^3$ of which $y^3$ may be eliminated from a combination of $x^2$ and $x^2 + y^3$. We therefore take the universal unfolding of the $D_5$ singularity to be.

$$
\boxed{f_{D_5} = y^4 + x^2 y + w x^2 + t y^2 - u x - v y}
$$

The equilibrium set $\mathcal{M}_{D_5}$ is given by 

$$
\mathcal{M}_{D_5} = \{ (x, y, t, u, v, w): = -u + 2 w x + 2 x y=0 \qquad -v + x^2 + 2 t y + 4 y^3=0 \}
$$

and the singular set $\mathcal{S}_{D_5}$ is

$$
\mathcal{S}_{D_5} = \{ (x, y, t, u, v, w): 4 t w - 4 x^2 + 4 t y + 24 w y^2 + 24 y^3=0 \}
$$

Finally, the bifurcation set $\mathcal{B}_{D_5}$ is obtained as

$$
\mathcal{B}_{D_5} =  \{ (t, u, v, w): 1889568 u^5 - 524880 u^4 w^2 - 7558272 u^3 v w^2 + 58320 u^3 w^4 + 1259712 u^2 v w^4 + 839808 t u^2 w^5 - 3240 u^2 w^6 - 69984 u v w^6 - 93312 t u w^7 + 90 u w^8 + 1296 v w^8 + 2592 t w^9 - w^10 + 5184 w^11 = 0 \}
$$

The geometry of the parabolic umbilic is arguably the most complicated of all the objects discussed in these notes. Note that the equilibrium set  $\mathcal{M}_{D_5}$ is 4-dimensional hypersurface in the 6-dimensional $(\mathbf{x}, \mathbf{u})$ and the bifurcation set $\mathcal{B}_{D_5}$ is a 3-dimensional volume in the space of unfolding parameters. Intuition may be gained by plotting slices of the bifurcation set for varying $(t,u)$, as in the following figure

<figure>
<img src="./notes/catastrophe_theory/figures/fig-D5_bifurcation_sets.jpg" style="display: block; margin: 0 auto; height: auto; width: 100%; padding: 5px;">
<figcaption>Slices of the $D5$ bifurcation set $\mathcal{B}_{D_5}$ for $(t,u) = \{(-1,0),(0,1),(-0.8,-0.5)\}$.</figcaption>
</figure>

Interestingly, the parabolic umbilic exhibits quite distinct geometries for different parameter values $(t,u)$, some of which are typically displayed in textbooks. More intuition may be gained by plotting the bifurcation sets for smoothly varying values $(t,u), as done in the following animation.

<figure>
<img src="./notes/catastrophe_theory/figures/anim-D5_bifurcation_set_variation.gif" style="display: block; margin: 0 auto; height: 300px; padding: 5px;">
<figcaption>Slices of the $D_5$ bifurcation set $\mathcal{B}_{D_5}$ for $(t,u)$ varied in a unit circle about the origin.</figcaption>
</figure>

Here, one nicely observes the different configurations which [Thom (1972)](https://books.google.co.uk/books/about/Stabilit%C3%A9_structurelle_et_morphog%C3%A9n%C3%A8s.html?id=t7Lbs7x5G9wC&redir_esc=y) already described in his very original work on morphogenesis. As one crosses $(1,0)$, the *beak-to-beak* configuration turns into two swallowtails, which in turn disappear and turn into a *dovetail* configuration. At $(0, -1)$, an isolated bifurcation point at the origin, which grows first into a *lisp* configuration and then a *hyperbolic umbilic focus* of maximal extend at about $(...)$. The triangle then shrinks into an *elliptic focus* which eventually disappears. A *piercing configration*  then forms around $(-0.2, 0.8)$, out of which the *beak-to-beak* emerges again.

It is, however, difficult to go beyond the shown $(t,u)$ slices and understand the morphogenesis of the bifurcation set, and even more the equilibrium set, in the whole unfolding space.


<figure>
<div style="display: flex; justify-content: center; gap: 100px; max-width: 100%;">
<img src="./notes/catastrophe_theory/figures/fig-D5_Berry_1.jpg" alt="Description 1" style="height: 200px; margin-right: 25px">
<img src="./notes/catastrophe_theory/figures/fig-D5_Berry_2.jpg" alt="Description 1" style="height: 200px;  margin-left: 25px">
</div>
<figcaption>Two illustrations of parabolic umbilics in an optical experiments, for different points in the unfolding space, thus resulting in the piercing and hyperbolic focus configuration respectively. Taken from [Berry (1980)](https://michaelberryphysics.wordpress.com/wp-content/uploads/2022/02/berry089-1.pdf)</figcaption>
</figure>


### Summary of the seven elementary catastrophes

The derivation of the seven elementary catastrophes is now complete. The results are summarised below:

<table>
<thead>
  <tr>
    <th>name</th>
    <th>symbol</th>
    <th>singularity</th>
    <th>unfolding</th>
    <th>corank</th>
    <th>codimension</th>
  </tr>
  </thead>
  <tr>
    <td>*fold*</td>
    <td>$A_2$</td>
    <td>$x^3$</td>
    <td>$x^3+\mu_1 x$</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>*cusp*</td>
    <td>$A_3$</td>
    <td>$x^4$</td>
    <td>$x^4+\mu_1 x^2 + \mu_2 x$</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>*swallowtail*</td>
    <td>$A_4$</td>
    <td>$x^5$</td>
    <td>$x^5+\mu_1 x^3 + \mu_2 x^2 + \mu_3 x$</td>
    <td>1</td>
    <td>3</td>
  </tr>
  <tr>
    <td>*butterfly*</td>
    <td>$A_5$</td>
    <td>$x^6$</td>
    <td>$x^6+\mu_1 x^4 + \mu_2 x^3 + \mu_3 x^2 + \mu_4 x$</td>
    <td>1</td>
    <td>4</td>
  </tr>
  <tr>
    <td>*ell. umbilic*</td>
    <td>$D_4^-$</td>
    <td>$x^3 - x y^2$</td>
    <td>$\frac{1}{3} x^3 - x y^2 + \mu_1 (x^2 + y^2) - \mu_2 x + \mu_3 y$</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td>*hyp. umbilic*</td>
    <td>$D_4^+$</td>
    <td>$x^3 + y^3$</td>
    <td>$x^3 + y^3 + \mu_1 x y - \mu_2 x - \mu_3 y$</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td>*par. umbilic*</td>
    <td>$D_5$</td>
    <td>$y^4 + x^2 y$</td>
    <td>$y^4 + x^2 y + \mu_1 x^2 + \mu_2 y^2 - \mu_3 x - \mu_4 y$</td>
    <td>2</td>
    <td>4</td>
  </tr>
</table>

Having discussed the characteristic geometries of the seven elementary catastrophes, I would like to conclude this section with a picture of work. Naum Gabo's intriguing "Linear Construction in Space No. 2" (1958). The sculpture shows a smooth and intricately curved structure made solely from organic shapes. An observer sees the structure as if were projected along their line of sight, and the shapes that are folding over the projected direction are observed as caustic points, thus beautifully illustrating the mathematical and physical concepts we have discussed above.

<figure>
<img src="./notes/catastrophe_theory/figures/Gabo_Linear_construction.jpg" style="display: block; margin: 0 auto; height: 320px;  padding: 5px;">
<figcaption>Naum Gabo's "Linear Construction in Space No. 2" (1958), taken from https://www.guggenheim.org/artwork/1385.</figcaption>
</figure>



## Beyond the seven elementary catastrophes

Having completed the discussion of the seven elementary caustics, the reader may be tempted to continue reading into catastrophe theory by mentioning two interesting properties of higher catastrophes. 

Firstly, we have shown in detail how the unfoldings codimension-4 singularities are derived. The very same methods can be applied to derive the canonical forms and unfoldings of the codimension-5 singularities, which are well known in the literature (e.g. $x^7$ is known as the *wigwam* catastrophe). It is obvious that the corank-1 cuspoids, i.e. the $x^n$ singularities, form an infinite family, of which the universal unfoldings are evident. It is also intuitive that the corank-2 umbilics form an infinite family, even though the canonical forms and unfoldings are much less clear in this case. [Arnol'd](https://link.springer.com/article/10.1007/BF01077644) has demonstrated that these infinite families, along with three "exceptional" higher-codimension catastrophes, can be classified using the Coxeter-Dynkin diagrams; that is, the catastrophes admit an *ADE classification*. This finally motivates the use of the symbols $A_n$ for the cuspoids and $D_n$ for the umbilics, which we had left uncommented above. I will write separate notes on Picard-Lefschetz theory and the ADE classification and of higher catastrophes soon.

The second curious property of higher-codimension catastrophes can be introduced by considering a general 4-jet such that the 3-jet identically vanishes

$$
j^4(x,y) \sim (a_1 x + b_1 y)(a_2 x + b_2 y)(a_3 x + b_3 y)(a_4 x + b_4 y)
$$

Assuming real and non-repeated roots of the quartic polynomial, the singularity is of codimension 8. One can now proceed as above to find a possible canonical form. But if one writes

$$
j^4(x,y) \sim x y(a x + b y)(p x + q y) \sim x y(x + y)(s x + t y) \sim x y(x + y)(x + \lambda y) \,,
$$

there remains a free parameter $\lambda$ that cannot be absorbed by a suitable diffeomorphism. One therefore does not obtain a single canonical form, but a 1-parameter family of castrastrophes that cannot be transformed into each other through diffeomorphisms. These *moduli spaces* are a generic property of higher catastrophes.