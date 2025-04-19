---
title: "Generalized Fourier Transform: Schwartz Space"
---

# Generalized Fourier Transform: Schwartz Space

The Schwartz space $\mathcal{S}$ is the topological vector space of
functions $f : \mathbb{R}_n \to \mathbb{C}$ such that:

- $f(x)$ infinitely differentiable

- any derivitive tends to zero fast than any power of x:

  $$
  \forall m, n \ge 0
  \implies
  \lim_{x \to \infty} |x|^n | f^{(m)} (x) | = 0
  $$

Properties without proof:

- the Schwartz space is closed under **differentiation** and
  **multiplication by polynomials**.
- Schwartz class functions are bounded and decay faster than any
  polynomial
- Schwartz class functions are integrable

## Lemma

Fourier transform of Schwartz class is bounded

Proof:

$$
\because
| \int_{-\infty}^{+\infty} e^{-2 \pi i s x} f(x) dx| & \le
  \int_{-\infty}^{+\infty} | e^{-2 \pi i s x} | \cdot | f(x) | dx
  \\ & =
  \int_{-\infty}^{+\infty} | f(x) | dx
  \\ & =
  \| f \|_1
$$

$$
\therefore
| \mathcal{F} f (s) | \le \| f \|_1
$$

(ref-ft-diff-formula-proof)=

## Differentiation Formulas

First statement:

$$
f \in \mathcal{S}
\implies
\mathcal{F} f^{(n)} =
(2 \pi i s)^n \cdot \mathcal{F} f
$$

Second statement

$$
f \in \mathcal{S}
\implies
\frac{\partial^n \mathcal{F} f}{\partial s^n} =
\mathcal{F} ((-2 \pi i x)^n f(x))
$$

Proof of first statement:

$$
& \because
f \in \mathcal{S}
\\
& \therefore
f' \in \mathcal{S}
$$

$$
\therefore
(\mathcal{F} f') (s) & =
  \int_{-\infty}^{+\infty}
    e^{-2 \pi i s x} f' (x) dx
  \\ & =
  e^{-2 \pi i s x} \cdot f(x) |_{-\infty}^{+\infty} -
    \int_{-\infty}^{+\infty} f(x) d e^{-2 \pi i s x}
  \\ & =
  - \int_{-\infty}^{+\infty}
    (-2 \pi i s) \cdot e^{-2 \pi i s x} f(x) dx
  \\ & =
  2 \pi i s \cdot \mathcal{F} f (s)
$$

By induction it follows that:

$$
\mathcal{F} f^{(n)} =
(2 \pi i s)^n \cdot \mathcal{F} f
$$

Proof of first statement:

$$
& \because
f \in \mathcal{S}
\\
& \therefore
x f(x) \in \mathcal{S}
$$

$$
\therefore
-2 \pi i \cdot (\mathcal{F} (x f(x))) (s) & =
  \int_{-\infty}^{+\infty}
    -2 \pi i \cdot e^{-2 \pi i s x} \cdot x f(x) dx
  \\ & =
  \int_{-\infty}^{+\infty}
    \frac{\partial}{\partial s} e^{-2 \pi i s x} \cdot f(x) dx
  \\ & =
  \frac{\partial \mathcal{F} f (s)}{\partial s}
$$

By induction it follows that:

$$
\frac{\partial^n \mathcal{F} f}{\partial s^n} =
\mathcal{F} ((-2 \pi i x)^n f(x))
$$

$$\tag*{$\blacksquare$}$$

## Closure under Fourier Transform

$$f \in \mathcal{S} \implies \mathcal{F} f \in \mathcal{S}$$

Proof:

$$
(2 \pi i s)^n \cdot \frac{\partial^m}{\partial s^m} \mathcal{F} f(s) & =
  (2 \pi i s)^n \cdot \mathcal{F} ((-2 \pi i x)^m f(x)) (s)
  \\ & =
  \mathcal{F} (\frac{\partial^n}{\partial x^n} (-2 \pi i x)^m f(x)) (s)
  \\ & =
  (-2 \pi i)^m \cdot \mathcal{F} (\frac{\partial^n}{\partial x^n} x^m f(x)) (s)
$$

$$
\therefore
|(2 \pi s)^n| \cdot |\frac{\partial^m}{\partial s^m} \mathcal{F} f(s)| =
  |(-2 \pi)^m| \cdot |\mathcal{F} (\frac{\partial^n}{\partial x^n} x^m f(x)) (s)|
$$

$$
\therefore
|s^n| \cdot |\frac{\partial^m}{\partial s^m} \mathcal{F} f(s)| =
  (2 \pi)^{m - n} \cdot |\mathcal{F} (\frac{\partial^n}{\partial x^n} x^m f(x)) (s)|
$$

$$
\because
f \in \mathcal{S}
$$

$$
\therefore
\frac{\partial^n}{\partial x^n} x^m f(x) \in \mathcal{S}
$$

$$
\therefore
|s^n| \cdot |\frac{\partial^m}{\partial s^m} \mathcal{F} f(s)| \le
  (2 \pi)^{m - n} \cdot \| \frac{\partial^n}{\partial x^n} x^m f \|
$$

$$
\therefore
\mathcal{F} f \in \mathcal{S}
$$

also:

$$\mathcal{F}^{-1} f \in \mathcal{S}$$

## Parseval's Theorem of Fourier Transform

$$
f, g \in \mathcal{S}
\implies
\int_{-\infty}^{+\infty} F (s) \bar{G} (s) ds =
\int_{-\infty}^{+\infty} f (x) \bar{g} (x) dx =
$$

where

$$F = \mathcal{F} f, G = \mathcal{F} g$$

Proof:

$$
\because
g(x) = \int_{-\infty}^{+\infty} e^{2 \pi i s x} G(s) ds
$$

$$
\therefore
\bar{g}(x) = \int_{-\infty}^{+\infty} e^{-2 \pi i s x} \bar{G}(s) ds
$$

$$
\therefore
\int_{-\infty}^{+\infty} f (x) \bar{g} (x) dx & =
\int_{-\infty}^{+\infty} \left(
  f (x)
  \int_{-\infty}^{+\infty} e^{-2 \pi i s x} \bar{G}(s) ds \right) dx
\\ & =
\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty}
  e^{-2 \pi i s x} f(x) \bar{G} (s) ds dx
$$

Since everything converges, integrations above are interchangeable.

$$
\therefore
\int_{-\infty}^{+\infty} f (x) \bar{g} (x) dx & =
\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty}
  e^{-2 \pi i s x} f(x) \bar{G} (s) dx ds
\\ & =
\int_{-\infty}^{+\infty} \left(
  \int_{-\infty}^{+\infty}
    e^{-2 \pi i s x} f(x) dx
  \right)
  \bar{G} (s) ds
\\ & =
\int_{-\infty}^{+\infty} F(x) \bar{G} (s) ds
$$

Inference:

$$
f, g \in \mathcal{S}
\implies
\int_{-\infty}^{+\infty} | F (s) |^2 ds =
\int_{-\infty}^{+\infty} | f (x) |^2 dx
$$

---

Back to {doc}`index`.

```{disqus}

```
