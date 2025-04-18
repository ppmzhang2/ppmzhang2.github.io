---
title: "Convolution: Cooling of a Rod"
---

# Convolution: Cooling of a Rod

## Problem

Suppose the temperature of a homogeneous rod is determined by function:

$$
u(x, t)
$$

where $x$ denotes the position $t$ denote the time.

The initial temperature distribution $u(x, 0)$ is denoted by function
$f(x)$. Find the temperature function $u$.

## Solution

According to the cooling formula:

$$
\frac{\partial u}{\partial t} = C \cdot \frac{\partial^2 u}{\partial x^2}
$$

Applying Fourier transform for **spacial variable** $x$ on both sides:

$$
\mathcal{F} (\frac{\partial u}{\partial t}) (s) & =
  \int_{-\infty}^{\infty} e^{-2 \pi i s x}
    \frac{\partial}{\partial t} u(x, t) dx
  \\ & =
  \frac{\partial}{\partial t}
    \int_{-\infty}^{\infty} e^{-2 \pi i s x} u(x, t) dx
  \\ & =
  \frac{\partial}{\partial t} U(s, t)
$$

where $U(s, t) = \mathcal{F} u (s, t)$

$$
\mathcal{F} (C \cdot \frac{\partial^2 u}{\partial x^2}) (s) & =
  C \cdot \int_{-\infty}^{\infty} e^{-2 \pi i s x}
    \frac{\partial^2}{\partial x^2} u(x, t) dx
  \\ & =
  C \cdot (2 \pi i s)^2
    \int_{-\infty}^{\infty} e^{-2 \pi i s x} u(x, t) dx
  \\ & =
    -4 C \pi^2 s^2 U(s, t)
$$

Therefore we have a differential equation:

$$
\frac{\partial}{\partial t} U(s, t) = -4 C \pi^2 s^2 U(s, t)
$$

whose solution:

$$
U(s, t) = F(s) \cdot G(s, t)
$$

where $F(s) = \mathcal{F} f(x)$ and $G(s, t) = e^{-4 C \pi^2 s^2 t}$.

Notice that $G(s, t)$ is a Gaussian function of variable $s$, which can
well be denoted as a Fourier transform of another Gaussian function
$g(x, t)$ of variable $x$.

Suppose:

$$
g(x, t) = A(t) e^{(- \pi (a(t) \cdot x)^2)} = A(t) e^{- \pi a^2 (t) x^2}
$$

$$
\therefore
G(s, t) & =
  (\mathcal{F} g) (s, t)
  \\ & =
  (\mathcal{F} (A(t) e^{- \pi a^2 (t) x^2})) (s)
  \\ & =
  A(t) \cdot \frac{1}{|a(t)|} e^{- \pi \frac{s^2}{a^2(t)}}
  \\ & =
  e^{-4 C \pi^2 s^2 t}
$$

By solving the system of equations:

$$
\begin{cases}
-4 C \pi^2 t = \frac{\pi}{a^2 (t)}
\\
A(t) = |a(t)|
\end{cases}
$$

we have:

$$
A(t) = a(t) = \frac{1}{2 \sqrt{C \pi t}}
$$

$$
\therefore
g(x, t) = \frac{1}{2 \sqrt{C \pi t}} e^{- \frac{x^2}{4 C t}}
$$

$$
\therefore
U(s, t) & =
  F(s) \cdot G(s, t)
  \\ & =
  \mathcal{F} f (s) \cdot \mathcal{F} g (s, t)
  \\ & =
  \mathcal{F} (f (x) * g(x, t))
$$

$$
\therefore
u(x, t) & =
  f(x) * g(x, t)
  \\ & =
  f(x) * \frac{1}{2 \sqrt{C \pi t}} e^{- \frac{x^2}{4 C t}}
$$

---

Back to {doc}`index`.

```{disqus}

```
