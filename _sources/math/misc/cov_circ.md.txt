---
title: "Calculus of Variations: Circle Minimizing Arc Length"
---

# Calculus of Variations: Circle Minimizing Arc Length

We rephrase the problem as finding a function $f(x)$ that minimizes the arc
length while satisfying a certain area constraint.
Specifically, we seek the function $f(x) \in C^1([a,b])$ that:

1. Satisfies the boundary conditions:

   $$
   f(a) = f(b) = 0
   $$

2. The area under the curve:

   $$
   \int_a^b f(x)\, dx
   $$

   is fixed

The target is to minimize the arc length:

$$
L[f] = \int_a^b \sqrt{1 + (f'(x))^2}\, dx
$$

## The Proof

**Proof:**

To incorporate the integral constraint, introduce a Lagrange multiplier
$\lambda$, and define the augmented functional:

$$
\mathcal{J}[f] = \int_a^b \left[ \sqrt{1 + (f'(x))^2} - \lambda f(x) \right] dx
$$

We now treat this as a standard variational problem with Lagrangian:

$$
\mathcal{L}(x, f, f') = \sqrt{1 + (f')^2} - \lambda f
$$

Since:

$$
\begin{aligned}
\frac{\partial \mathcal{L}}{\partial f'} &= \frac{f'}{\sqrt{1 + (f')^2}} \\
\frac{\partial \mathcal{L}}{\partial f} &= -\lambda
\end{aligned}
$$

By Euler–Lagrange equation

$$
\frac{d}{dx} \left( \frac{\partial \mathcal{L}}{\partial f'} \right) =
\frac{\partial \mathcal{L}}{\partial f}
$$

We have:

$$
\frac{d}{dx} \left( \frac{f'}{\sqrt{1 + (f')^2}} \right) = - \lambda
$$

Define:

$$
u = \frac{f'}{\sqrt{1 + (f')^2}} \Rightarrow
f' = \frac{u}{\sqrt{1 - u^2}}
$$

we have:

$$
f' = \frac{u}{\sqrt{1 - u^2}} \tag{1}
$$

and

$$
u' = -\lambda \tag{2}
$$

Integrating (1) gives:

$$
f(x) = \int_a^x \frac{u(t)}{\sqrt{1 - u^2(t)}}\, dt
$$

By (2), we have:

$$
u(t) = -\lambda t + C_1
$$

$$
f(x) =
\int_{u(a)}^{u(x)} \frac{u}{\sqrt{1 - u^2}} \cdot (-\frac{1}{\lambda})\, du
$$

$$
\therefore
f(x) = \frac{1}{\lambda} \int_{u(x)}^{u(a)} \frac{u}{\sqrt{1 - u^2}}\, du
$$

$$
\because
\int \frac{u}{\sqrt{1 - u^2}}\, du = -\sqrt{1 - u^2} + C
$$

Therefore:

$$
\begin{aligned}
f(x) &=
\frac{1}{\lambda} \left[ -\sqrt{1 - u^2} \right]_{u(x)}^{u(a)} \\ &=
\frac{1}{\lambda} \left[ \sqrt{1 - u^2} \right]_{u(a)}^{u(x)} \\ &=
\frac{1}{\lambda} \left[ \sqrt{1 - (-\lambda x + C_1)^2} - \sqrt{1 - (-\lambda a + C_1)^2} \right]
\end{aligned}
$$

$$
\because
f(b) = 0
$$

$$
\therefore
(-\lambda b + C_1)^2 = (-\lambda a + C_1)^2 \Rightarrow
C_1 = \frac{\lambda(a + b)}{2}
$$

Let $c = \frac{a + b}{2}$ and $R = \frac{1}{\lambda}$, then:

$$
f(x) = \sqrt{R^2 - (x - c)^2} - \sqrt{R^2 - (a - c)^2}
$$

This is indeed a segment of a circle with radius $R$.

$$\tag*{$\blacksquare$}$$

## Interpretation

In fact, the circle is centered at $(c, -\sqrt{R^2 - (a - c)^2})$, which is
below the $x$-axis, and the segment $ab$ is a chord of the circle.

---

Back to {doc}`index`.

```{disqus}

```
