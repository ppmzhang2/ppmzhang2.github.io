---
title: Operations
---

# Operations

- the most fundamental question of signal processing
  - how to use one signal (function) to modify another
  - most often: to modify the spectrum of the signal
- convolution is probably the most important operation in signal
  processing

## Linear Combination

$$
\mathcal{F}(a \cdot f + b \cdot g) =
  a \cdot \mathcal{F}f + b \cdot \mathcal{F}g
$$

Can be proved by applying definition directly.

## Shift

- Shift in time (signal) corresponds to phase shift in frequency (FT)

$$
(\mathcal{F} f(t - b))(s) = e^{-2 \pi i s b} \cdot \mathcal{F} f (s)
$$

Proof:

$$
(\mathcal{F} f(t - b))(s) =
  \int_{-\infty}^{+\infty}
    e^{-2 \pi i s t} f(t - b) dt
$$

$$
Let: u = t - b \implies t = u + b
$$

$$
(\mathcal{F} f(t - b))(s) & =
  \int_{-\infty}^{+\infty}
    e^{-2 \pi i s \cdot (u + b)} f(u) du
  \\ & =
  e^{-2 \pi i s b}
  \int_{-\infty}^{+\infty}
    e^{-2 \pi i s u} f(u) du
  \\ & =
  e^{-2 \pi i s b} \cdot \mathcal{F} f (s)
$$

$$
\tag*{$\blacksquare$}
$$

## Stretch

- **squashed** in time (signal) corresponds to stretched in phase and
  squashed in magnitude
- **stretched** in time (signal) corresponds to squeezed in phase and
  stretched in magnitude
- a signal **cannot** be both localized in time and frequency

$$(\mathcal{F} f(a t))(s) = |\frac{1}{a}| F(\frac{s}{a})$$

Proof:

$$
(\mathcal{F} f(a t))(s) =
  \int_{-\infty}^{+\infty} e^{-2 \pi i s t} f(at) dt
$$

$$
Let: u = a t \implies t = \frac{1}{a} u
$$

$$
(\mathcal{F} f(a t))(s) & =
  \int_{-\infty}^{+\infty}
    e^{-2 \pi i s \cdot \frac{u}{a}} f(u) dt
  \\ & =
  \int_{-\infty}^{+\infty}
    e^{-2 \pi i \cdot \frac{s}{a} \cdot u} f(u) dt
  \\ & =
  |\frac{1}{a}| \int_{-\infty}^{+\infty}
    e^{-2 \pi i \cdot \frac{s}{a} \cdot u} f(u) du
  \\ & =
  |\frac{1}{a}| F(\frac{s}{a})
$$

$$
\tag*{$\blacksquare$}
$$

## Differentiation

> Fourier transform turns differentiation into multiplication.

**The Derivitive Theorem of Fourier Transform**:

$$
\mathcal{F} f^{(n)} =
(2 \pi i s)^n \cdot \mathcal{F} f
$$

$$
\frac{\partial^n \mathcal{F} f}{\partial s^n} =
\mathcal{F} ((-2 \pi i x)^n f(x))
$$

Rigorous proof can be found in
[Differentiation Formulas](#ref-ft-diff-formula-proof).

```{warning}
These formulas hold only if function $f$ satisfies some specific
conditions e.g. **vanish at infinity**
```

(ref-ft-conv-proof)=

## Convolution

**Convolution Theorem of Fourier Transform**:

First statement:

$$\mathcal{F} f \cdot \mathcal{F} g = \mathcal{F}(f * g)$$

$$\mathcal{F}^{-1} F \cdot \mathcal{F}^{-1} G = \mathcal{F}^{-1} (F * G)$$

Second statement:

$$\mathcal{F} (f \cdot g) = \mathcal{F} f * \mathcal{F} g$$

$$\mathcal{F}^{-1} (F \cdot G) = \mathcal{F}^{-1} F * \mathcal{F}^{-1} G$$

Proof:

$$
\mathcal{F} g(s) \cdot \mathcal{F} f(s) & =
  \int_{-\infty}^{+\infty} e^{-2 \pi i s t} g(t) dt \cdot
  \int_{-\infty}^{+\infty} e^{-2 \pi i s t} f(t) dt
  \\ & =
  \int_{-\infty}^{+\infty} e^{-2 \pi i s t} g(t) dt \cdot
  \int_{-\infty}^{+\infty} e^{-2 \pi i s x} f(x) dx
  \\ & =
  \int_{-\infty}^{+\infty}
  \int_{-\infty}^{+\infty}
  e^{-2 \pi i s t} \cdot e^{-2 \pi i s x} \cdot g(t) \cdot f(x) dt dx
  \\ & =
  \int_{-\infty}^{+\infty}
  \int_{-\infty}^{+\infty}
  e^{-2 \pi i s (t + x)} \cdot g(t) \cdot f(x) dt dx
  \\ & =
  \int_{-\infty}^{+\infty} (
    \int_{-\infty}^{+\infty}
    e^{-2 \pi i s (t + x)} \cdot g(t) dt
  ) f(x) dx
$$

$$Let: u = t + x \implies t = u - x$$

$$
\mathcal{F} g(s) \cdot \mathcal{F} f(s) & =
  \int_{-\infty}^{+\infty} (
    \int_{-\infty}^{+\infty}
    e^{-2 \pi i s (t + x)} \cdot g(t) dt
  ) f(x) dx
  \\ & =
  \int_{-\infty}^{+\infty} (
    \int_{-\infty}^{+\infty}
    e^{-2 \pi i s u} \cdot g(u - x) du
  ) f(x) dx
  \\ & =
  \int_{-\infty}^{+\infty} e^{-2 \pi i s u} (
    \int_{-\infty}^{+\infty}
    g(u - x) \cdot f(x) dx
  ) du
$$

$$Let: (f * g)(u) = \int_{-\infty}^{+\infty} g(u - x) \cdot f(x) dx$$

$$
\mathcal{F} g(s) \cdot \mathcal{F} f(s) & =
  \int_{-\infty}^{+\infty} e^{-2 \pi i s u} (
    \int_{-\infty}^{+\infty}
    g(u - x) \cdot f(x) dx
  ) du
  \\ & =
  \mathcal{F}(f * g)(s)
$$

similarly:

$$
\mathcal{F}^{-1} F \cdot \mathcal{F}^{-1} G = \mathcal{F}^{-1} (F * G)
$$

To prove the second statement we start with the first statement of the
inverse Fourier transform:

$$
\mathcal{F}^{-1} F \cdot \mathcal{F}^{-1} G = \mathcal{F}^{-1} (F * G)
$$

$$
\therefore
f \cdot g =
  \mathcal{F}^{-1} \left( \mathcal{F} f * \mathcal{F} g \right)
$$

$$
\therefore
\mathcal{F} \left( f \cdot g \right) =
  \mathcal{F} f * \mathcal{F} g
$$

Similarly:

$$
\mathcal{F}^{-1} (F \cdot G) = \mathcal{F}^{-1} F * \mathcal{F}^{-1} G
$$

$$\tag*{$\blacksquare$}$$

---

Back to {doc}`index`.

```{disqus}

```
