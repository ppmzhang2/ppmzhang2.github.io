---
title: "Generalized Fourier Transform: Delta Distribution"
---

# Generalized Fourier Transform: Delta Distribution

## Sampling Property of Delta

> Mathematical meaning of taking samples is multiplying by $\delta$.

$$f \delta_a = f(a) \delta_a$$

Proof:

$$
\langle f \delta_a, \phi \rangle & =
  \langle \delta_a, f \phi \rangle
  \\ & =
  (f \phi) (a)
  \\ & =
  f(a) \phi (a)
  \\ & =
  \langle f(a) \delta_a, \phi \rangle
$$

$$
\therefore
f \delta_a = f(a) \delta_a
$$

$$\tag*{$\blacksquare$}$$

## Convolution Property of Delta

$$f * \delta_a = f(x - a)$$

Proof:

$$
\langle f * \delta_a, \phi \rangle & =
  \langle f, \phi * \delta_a^- \rangle
  \\ & =
  \langle f, \phi * \delta_{-a} \rangle
  \\ & =
  \langle f(x), \int_{-\infty}^{+\infty} \delta_{-a} (x - y) \phi (y) dy \rangle
  \\ & =
  \langle f(x), \int_{-\infty}^{+\infty} \delta_{-a} (u) \phi (x - u) du \rangle
  \\ & =
  \langle f(x), \langle \delta_{-a} (u), \phi(x - u) \rangle \rangle
  \\ & =
  \langle f(x), \phi(x + a) \rangle
  \\ & =
  \int_{-\infty}^{+\infty} f(x) \phi(x + a) dx
  \\ & =
  \int_{-\infty}^{+\infty} f(u - a) \phi(u) du
  \\ & =
  \langle f(x - a), \phi(x) \rangle
$$

$$
\therefore
f * \delta_a = f(x - a)
$$

$$\tag*{$\blacksquare$}$$

Specifically:

$$
f * \delta & = f
\\
\delta * \delta & = \delta
\\
\delta_a * \delta_b & = \delta_{a+b}
$$

## Scaling Property of Delta

$$\delta (ax) = \frac{1}{|a|} \delta$$

Proof:

Suppose $a > 0$:

$$
\langle \delta (ax), \phi(x) \rangle & =
  \int_{-\infty}^{+\infty} \delta (ax) \phi(x) dx
  \\ & =
  \frac{1}{a} \int_{-\infty}^{+\infty} \delta (u) \phi(\frac{u}{a}) du
  \\ & =
  \frac{1}{a} \phi(0)
  \\ & =
  \langle \frac{1}{a} \delta (x), \phi (x) \rangle
$$

$$
\therefore
a \gt 0 \implies \delta (ax) = \frac{1}{a} \delta
$$

Similarly:

$$a \lt 0 \implies \delta (ax) = -\frac{1}{a} \delta$$

$$
\therefore
\delta (ax) = \frac{1}{|a|} \delta
$$

$$\tag*{$\blacksquare$}$$

---

Back to {doc}`index`.

```{disqus}

```
