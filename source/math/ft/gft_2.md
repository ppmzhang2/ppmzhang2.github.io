---
title: "Generalized Fourier Transform: Tempered Distribution"
---

# Generalized Fourier Transform: Tempered Distribution

A tempered distribution is a **linear functional**:

$$
\DeclareMathOperator{\sgn}{sgn}
f: \mathcal{S} \to \mathbb{C}
$$

- The space of all tempered distributions denoted $\mathcal{S}'$, is the
  dual space of $\mathcal{S}$.

- The value in $\mathbb{C}$ that the distribution $f \in \mathcal{S}'$
  assigns to $\phi \in \mathcal{S}$ is usually denoted by:

  $$\langle f, \phi \rangle$$

Properties without proof:

- Linearity

  $$
  a \langle f, \phi \rangle + b \langle f, \psi \rangle =
  \langle f, a \phi + b \psi \rangle
  $$

- Continuity

  $$
  \lim_{n \to \infty} \phi_n = \phi
  \implies
  \lim_{n \to \infty} \langle f, \phi_n \rangle = \langle f, \phi \rangle
  $$

## Delta Distribution

The $\delta$ distribution, aka the **unit impulse**, is a generalized
function or distribution.

Operationally, the effect of $\delta$ is to evalute the function at the
origin (i.e. pull out the value of origin).

### Classical Interpretation

$$
\delta (x) =
\begin{cases}
  \infty & x = 0
  \\
  0 & x \ne 0
\end{cases}
$$

$$\int_{-\infty}^{+\infty} \delta (x) dx = 1$$

It can be viewed as a sequence of bump functions:

> That is really operationally how it appear: by limiting process you
> were concentrating things and you were just pulling out the value at
> the origin.

$$\delta(x) = \lim_{b \to 0} \frac{1}{|b| \sqrt{\pi}} e^{-(\frac{x}{b})^2}$$

$$\int_{-\infty}^{+\infty} \delta (x) \phi (x) dx = \phi(0)$$

### Distribution Interpretation

> It is a mathematical modus operandi by turning the solution of a
> problem into a definiation

**We define** that $\delta$ distribution maps every continuous function
to its value at zero of its domain:

$$\langle \delta, \phi \rangle = \phi(0)$$

$\delta$ is also linear and continuous:

$$
a \langle \delta, \phi \rangle + b \langle \delta, \psi \rangle =
\langle \delta, a \phi + b \psi \rangle
$$

$$
\lim_{n \to \infty} \phi_n = \phi
\implies
\lim_{n \to \infty} \langle \delta, \phi_n \rangle =
\langle \delta, \phi \rangle
$$

Define a new distribution $\delta_a$

$$
\delta_a: \phi \in \mathcal{S} \mapsto
  \langle \delta_a, \phi \rangle = \phi(a)
$$

## Function Induced Distribution

> you give me a (test) function, I have to tell you how a distribution
> (generalized function) operates on it (by integraion for Fourier
> transform).

**Lemma**: if $f : \mathbb{R}^n \to \mathbb{C}$:

- polynomially bounded
- Riemann integrable on $[−M, M]$ for each $M > 0$.

Then:

$$
f: \phi \in \mathcal{S} \mapsto
  \langle f, \phi \rangle = \int_{-\infty}^{+\infty} f(x) \phi(x) dx
$$

is a tempered distribution (generalized function) induced by $f$.

As the rapidly decreasing functions are "good enough", **most weird
functions** can be considered generalized functions (aka distributions)
by defining the pairing as:

$$\langle f, \phi \rangle = \int_{-\infty}^{+\infty} f(x) \phi(x) dx$$

For example, the integral of $sin(2 \pi x)$ does not make any sense, but
$\int_{-\infty}^{+\infty} sin(2 \pi x) \phi(x) dx$ will converge as
$\phi$ is a rapidly decreasing function. Thus $sin(2 \pi x)$ can be
considered as a generalized function as I can tell you how it can
operate on test functions (i.e. by integraion).

$$
\langle sin(2 \pi x), \phi \rangle =
\int_{-\infty}^{+\infty} sin(2 \pi x) \cdot \phi (x) dx
$$

Similarly:

$$
\langle 1, \phi \rangle =
\int_{-\infty}^{+\infty} 1 \cdot \phi (x) dx
$$

$$
\langle \Pi, \phi \rangle =
\int_{-\infty}^{+\infty} \Pi(x) \cdot \phi (x) dx
$$

## Fourier Transform of Distribution

Properties:

$$
T \in \mathcal{S}' \implies
  \mathcal{F} T \in \mathcal{S}'
$$

$$
T \in \mathcal{S}' \implies
  \mathcal{F}^{-1} T \in \mathcal{S}'
$$

### Theorem

$$
\phi \in \mathcal{S}, T \in \mathcal{S}' \implies
\langle \mathcal{F} T, \phi \rangle =
  \langle T, \mathcal{F} \phi \rangle
$$

Proof:

$$
\langle \mathcal{F} T, \phi \rangle & =
  \int_{-\infty}^{+\infty} \mathcal{F} T (x) \phi (x) dx
  \\ & =
  \int_{-\infty}^{+\infty} \left(
    \int_{-\infty}^{+\infty} e^{-2 \pi i x y} T(y) dy
  \right) \phi (x) dx
  \\ & =
  \int_{-\infty}^{+\infty}
    \int_{-\infty}^{+\infty} e^{-2 \pi i x y} \phi(x) T(y) dy dx
  \\ & =
  \int_{-\infty}^{+\infty} \left(
    \int_{-\infty}^{+\infty} e^{-2 \pi i x y} \phi(x) T(y) dx
  \right) dy
  \\ & =
  \int_{-\infty}^{+\infty}
    T(y) \cdot \mathcal{F} \phi (y) dy
  \\ & =
  \langle T, \mathcal{F} \phi \rangle
$$

Similarly:

$$
\phi \in \mathcal{S}, T \in \mathcal{S}' \implies
\langle \mathcal{F}^{-1} T, \phi \rangle =
  \langle T, \mathcal{F}^{-1} \phi \rangle
$$

### Applications

Fourier Transform of **shifted delta function**:

$$
\langle \mathcal{F} \delta_a, \phi \rangle & =
  \langle \delta_a, \mathcal{F} \phi \rangle
  \\ & =
  \mathcal{F} \phi (a)
  \\ & =
  \int_{-\infty}^{+\infty} e^{-2 \pi i a x} \phi(x) dx
  \\ & =
  \langle e^{-2 \pi i a x}, \phi \rangle
$$

$$
\therefore
\mathcal{F} \delta_a = e^{-2 \pi i a x}
$$

Specifically when $a = 0$:

$$\mathcal{F} \delta = \mathcal{F} \delta_0 = 1$$

$\delta$ is infinitely concentrated, its Fourier transform $F \delta$ is
uniformly spread out

Fourier Transform of **complex exponential function**:

$$
\langle \mathcal{F} e^{2 \pi i a x}, \phi \rangle & =
  \langle e^{2 \pi i a x}, \mathcal{F} \phi \rangle
  \\ & =
  \int_{-\infty}^{+\infty} e^{2 \pi i a x} \mathcal{F} \phi(x) dx
  \\ & =
  \mathcal{F}^{-1} \mathcal{F} \phi(a)
  \\ & =
  \phi(a)
  \\ & =
  \langle \delta_a, \phi \rangle
$$

$$
\therefore
\mathcal{F} e^{2 \pi i a x} = \delta_a
$$

Fourier Transform of **cosine function**:

$$
\mathcal{F} cos(2 \pi a x) & =
  \mathcal{F} (\frac{1}{2} (e^{2 \pi i a x} + e^{-2 \pi i a x}))
  \\ & =
  \frac{1}{2} (\mathcal{F} e^{2 \pi i a x} + \mathcal{F} e^{-2 \pi i a x})
  \\ & =
  \frac{1}{2} (\delta_a + \delta_{-a})
$$

Fourier Transform of **sine function**:

$$
\mathcal{F} sin(2 \pi a x) & =
  \mathcal{F} (\frac{1}{2i} (e^{2 \pi i a x} - e^{-2 \pi i a x}))
  \\ & =
  \frac{1}{2i} (\mathcal{F} e^{2 \pi i a x} - \mathcal{F} e^{-2 \pi i a x})
  \\ & =
  \frac{1}{2i} (\delta_a - \delta_{-a})
$$

## Derivitive of Distribution

Let $T'$ be the derivitive of distribution $T$, then:

$$
\langle T', \phi \rangle & =
  \int_{-\infty}^{+\infty} T' (x) \phi (x) dx
  \\ & =
  T(x) \phi (x) |_{-\infty}^{+\infty} -
    \int_{-\infty}^{+\infty} T(x) \phi' (x) dx
  \\ & =
  - \langle T, \phi' \rangle
$$

Again, **by turning the solution of a problem into a definiation**, we
define:

$$\langle T', \phi \rangle = - \langle T, \phi' \rangle$$

By defining how it operates on test function, the derivitive of a
distribution can be derived, even for many weird function.

### Applications

**Derivative of Heaviside Step Function**

$$
H (x) =
\begin{cases}
  1 & x \gt 0
  \\
  0 & x \le 0
\end{cases}
$$

$$
\langle H', \phi \rangle & =
  - \langle H, \phi' \rangle
  \\ & =
  - \int_{-\infty}^{+\infty} H(x) \phi' (x) dx
  \\ & =
  - \int_{0}^{+\infty} \phi' (x) dx
  \\ & =
  \phi (0)
  \\ & =
  \langle \delta, \phi \rangle
$$

$$
\therefore
H' = \delta
$$

**Derivative of Signum Function**

$$
\sgn (x) =
\begin{cases}
  -1 & x \lt 0
  \\
  0 & x = 0
  \\
  1 & x \gt 0
\end{cases}
$$

$$
\langle \sgn', \phi \rangle & =
  -\langle \sgn, \phi' \rangle
  \\ & =
  -\int_{0}^{+\infty} \phi' dx +
    \int_{-\infty}^0 \phi' dx
  \\ & =
  2 \phi (0)
  \\ & =
  \langle 2 \delta, \phi \rangle
$$

$$
\therefore
\sgn' = 2 \delta
$$

**Fourier Transform of Signum Function**

$$
(\mathcal{F} \sgn) (s) & =
  \frac{1}{2 \pi i s} (\mathcal{F} \sgn') (s)
  \\ & =
  \frac{1}{2 \pi i s} \left(\mathcal{F} (2 \delta) \right) (s)
  \\ & =
  \frac{2}{2 \pi i s}
  \\ & =
  \frac{1}{\pi i s}
$$

**Fourier Transform of Heaviside Step Function**

$$
H (x) & =
\begin{cases}
  1 & x \gt 0
  \\
  0 & x \le 0
\end{cases}
\\ & =
\frac{1}{2}(1 + \sgn(x))
$$

$$
\therefore
\mathcal{F} H (s) & =
  \mathcal{F} (\frac{1}{2} + \frac{\sgn{x}}{2}) (s)
  \\ & =
  \frac{1}{2} \mathcal{F} 1 (s) + \frac{1}{2} \mathcal{F} \sgn (s)
  \\ & =
  \frac{1}{2} \delta + \frac{1}{2 \pi i s}
$$

```{warning}
The following derivation is **WRONG**:
```

$$
\mathcal{F} H (s) & =
  \frac{1}{2 \pi i s} (\mathcal{F} H') (s)
  \\ & =
  \frac{1}{2 \pi i s} \left(\mathcal{F} \delta \right) (s)
  \\ & =
  \frac{1}{2 \pi i s}
$$

As the highest score answer[^1] suggested:

> \... There\'s a family of functions that differ by additive constants
> and all have the same derivative. Their Fourier transforms differ by
> $\delta$ s at the origin (proportional to the additive constants), so
> it can\'t be the case that you get the Fourier transform of all of
> them by dividing the transform of the derivative by $i \omega$

## Multiplication of Distribution

$$
\langle Tf, \phi \rangle =
  \int_{-\infty}^{+\infty} T(x) f(x) \phi(x) dx
  =
  \langle T, f\phi \rangle
$$

```{note}
- Arbitrary distributions $S$ and $T$ can not multiply as $ST$ is
  undefined.
- A distribution multiplied by a function $f$ is valid if
  $f \phi \in \mathcal{S}$
```

## Convolution of Distribution

```{note}
- It is often **invalid** to convolute two arbitrary distributions, as
  well as to convolute with an arbitrary function.
- With the distribution interpretation, convolution $f * T$ is defined
  in terms of **pairing** not integral. It mimics the classical integral
  operation of convolution.
```

$$
f \in \mathcal{S}, \psi \in \mathcal{S}'
\implies
\forall \phi \in \mathcal{S}:
\langle \psi * f, \phi \rangle =
  \langle \psi, \phi * f^- \rangle
$$

Proof:

$$
\langle \psi * f, \phi \rangle & =
  \int_{-\infty}^{+\infty} (\psi * f)(x) \phi (x) dx
  \\ & =
  \int_{-\infty}^{+\infty}
    \left( \int_{-\infty}^{+\infty} f(x - y) \psi (y) dy \right)
    \phi (x) dx
  \\ & =
  \int_{-\infty}^{+\infty} \psi (y)
    \left( \int_{-\infty}^{+\infty} f(x - y) \phi (x) dx \right)
    dy
  \\ & =
  \int_{-\infty}^{+\infty} \psi (y)
    \left( \int_{-\infty}^{+\infty} f^- (y - x) \phi (x) dx \right)
    dy
  \\ & =
  \int_{-\infty}^{+\infty} \psi (y) \left( \phi * f^- \right) (y) dy
  \\ & =
    \langle \psi, \phi * f^- \rangle
$$

$$\tag*{$\blacksquare$}$$

Extending to the general case:

$$\langle S * T, \phi \rangle = \langle S, \phi * T^- \rangle$$

```{note}
This formula holds only if $\phi * T^- \in \mathcal{S}$.
```

**Convolution Theorem of Fourier Transform**:

$$\mathcal{F} (S * T) = \mathcal{F} S \cdot \mathcal{F} T$$

$$\mathcal{F} (S \cdot T) = \mathcal{F} S * \mathcal{F} T$$

```{note}
Again, these formulas hold only if
$\forall \phi \in \mathcal{S}, \phi * T^- \in \mathcal{S}$.
```

Proof can be found at [Convolution](#ref-ft-conv-proof)
of operations section.

[^1]: <https://math.stackexchange.com/questions/73922/fourier-transform-of-unit-step>

---

Back to {doc}`index`.

```{disqus}

```
