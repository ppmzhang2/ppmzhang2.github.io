---
title: "Convolution: Central Limit Theorem"
---

# Convolution: Central Limit Theorem

## Gaussian Curve

> Everybody believes the normal (Gaussian) distribution: the
> mathematicians think it is an experimental fact, while the
> experimentalists think it is a mathematical theorem.

- The central limit theorem (CLT) explains the universal appearance of
  the bell-shape (Gaussian) curve in probability.
- Most probabilities are calculated / approximated (in the average
  sense) by a Gaussian curve
- Convoluting **any** signal / function infinite number of times gets a
  Gaussian curve

## Sum of Random Variables

**Lemma**: The probability density function (PDF) of the sum of random
variables is the convolution of each random variable's PDF.

Suppose the probability density function (PDF) for random variable $X_1$
and $X_2$ is $p_1 (x)$ and $p_2 (x)$ respectively.

Prove: the PDF of random variable $X = X_1 + X_2$ is $p_1 * p_2$.

**Proof**:

Suppose $p(x)$ is the PDF of $X$:

$$
Pr (X \le t) & =
  \int_{-\infty}^{t} p(x) dx
  \\ & =
  \iint_{x_1 + x_2 \le t} p_1 (x_1) p_2 (x_2) d x_1 d x_2
$$

Let:

$$
\begin{cases}
  u = x_1
  \\
  v = x_1 + x_2
\end{cases}
$$

$$
\therefore
\begin{cases}
  x_1 = u
  \\
  x_2 = v - u
\end{cases}
$$

$$
\therefore
Pr (X \le t) & =
  \iint_{x_1 + x_2 \le t} p_1 (x_1) p_2 (x_2) d x_1 d x_2
  \\ & =
  \int_{-\infty}^{\infty} \int_{-\infty}^{t} p_1 (u) p_2 (v - u) d v d u
  \\ & =
  \int_{-\infty}^{t} \int_{-\infty}^{\infty} p_2 (v - u) p_1 (u) d u d v
  \\ & =
  \int_{-\infty}^{t} (\int_{-\infty}^{\infty} p_2 (v - u) p_1 (u) d u) d v
  \\ & =
  \int_{-\infty}^{t} (p_1 * p_2)(v) d v
  \\ & =
  \int_{-\infty}^{t} (p_1 * p_2)(x) d x
$$

$$
\therefore
p(x) = (p_1 * p_2) (x)
\space
$$

$$\tag*{$\blacksquare$}$$

## Central Limit Theorem

Random Variables $X_1, X_2, \dots, X_n$ are independently and
identically distributed (i.i.d.) with their PDF equals $p(x)$ and CDF
equals $P(x)$:

$$
\int_{-\infty}^{+\infty} p(x) dx = 1
\\
\int_{-\infty}^{+\infty} x p(x) dx = 0
\\
\int_{-\infty}^{+\infty} x^2 p(x) dx = 1
$$

Let:

$$S_n = \frac{1}{\sqrt{n}} \sum_{i=1}^n X_i$$

Prove:

$$
\lim_{n \to \infty} Pr (a \le S_n \le b) =
  \frac{1}{\sqrt{2 \pi}} \int_a^b e^{-\frac{x^2}{2}} dx
$$

**Proof**

Let $S_n$\'s PDF equals $p_n (x)$ and its CDF equals $P_n (x)$. The
unproven conclusion is equivalent to:

$$\lim_{n \to \infty} p_n (x) = \frac{1}{\sqrt{2 \pi}} e^{- \frac{x^2}{2}}$$

Let the PDF and CDF of $\sqrt{n} S_n = \sum_{i=1}^n X_i$ be $f(x)$ and
$F(x)$ respectively. From the lemma we have:

$$f(x) = p^{(*n)} (x) = \overbrace{p * p * \dots * p}^{n} (x)$$

$$
\therefore
P_n (x) & =
  Pr (S_n \le x)
  \\ & =
  Pr (\sqrt{n} S_n \le \sqrt{n} x)
  \\ & =
  F (\sqrt{n} x)
$$

$$
\therefore
p_n (x) & =
  \frac{d}{dx} P_n (x)
  \\ & =
  \frac{d}{dx} F (\sqrt{n} x)
  \\ & =
  f(\sqrt{n} x) \cdot \sqrt{n}
  \\ & =
  \sqrt{n} \cdot p^{(*n)} (\sqrt{n} x)
$$

$$
\\
\therefore
\mathcal{F} p_n (s) & =
  \mathcal{F} (\sqrt{n} \cdot p^{(*n)} (\sqrt{n} x)) (s)
  \\ & =
  \sqrt{n} \cdot \mathcal{F} (p^{(*n)} (\sqrt{n} x)) (s)
  \\ & =
  \sqrt{n} \cdot \frac{1}{\sqrt{n}} \cdot \mathcal{F} p^{(*n)} (\frac{s}{\sqrt{n}})
  \\ & =
  \mathcal{F} p^{(*n)} (\frac{s}{\sqrt{n}})
  \\ & =
  (\mathcal{F} p)^n (\frac{s}{\sqrt{n}})
$$

$$
\because
\mathcal{F} p (\frac{s}{\sqrt{n}}) & =
  \int_{-\infty}^{+\infty} e^{-2 \pi i x \frac{s}{\sqrt{n}}} p(x) dx
  \\ & =
  \int_{-\infty}^{+\infty} (
    1 - \frac{2 \pi i s x}{\sqrt{n}} + \frac{(2 \pi i s x)^2}{2 n} + R_3(x))
    p(x) dx
  \\ & =
  \int_{-\infty}^{+\infty} p(x) dx -
    \int_{-\infty}^{+\infty} \frac{2 \pi i s x}{\sqrt{n}} p(x) dx -
    \int_{-\infty}^{+\infty} \frac{2 \pi^2 s^2 x^2}{n} p(x) dx +
    \int_{-\infty}^{+\infty} R_3(x) p(x) dx
  \\ & =
  \int_{-\infty}^{+\infty} p(x) dx -
    \frac{2 \pi i s}{\sqrt{n}} \int_{-\infty}^{+\infty} x p(x) dx -
    \frac{2 \pi^2 s^2}{n} \int_{-\infty}^{+\infty} x^2 p(x) dx +
    \int_{-\infty}^{+\infty} R_3(x) p(x) dx
  \\ & =
  1 - 0 - \frac{2 \pi^2 s^2}{n} + \int_{-\infty}^{+\infty} R_3(x) p(x) dx
  \\ & \approx
  1 - \frac{2 \pi^2 s^2}{n}
$$

$$
\therefore
\lim_{n \to \infty} \mathcal{F} p_n (s) & =
  \lim_{n \to \infty} (\mathcal{F} p)^n (\frac{s}{\sqrt{n}})
  \\ & \approx
  \lim_{n \to \infty} (1 - \frac{2 \pi^2 s^2}{n})^n
  \\ & =
  e^{-2 \pi^2 s^2}
$$

Let $g(x)$ be the gaussian function $e^{- \pi x^2}$. Obviously:

$$
\mathcal{F} (\frac{1}{\sqrt{2 \pi}} g(\frac{x}{\sqrt{2 \pi}})) & =
  \frac{1}{\sqrt{2 \pi}} \sqrt{2 \pi} \mathcal{F} g ({\sqrt{2 \pi}} s)
  \\ & =
  g ({\sqrt{2 \pi}} s)
  \\ & =
  e^{-2 \pi^2 s^2}
$$

$$
\therefore
\lim_{n \to \infty} p_n (x) & =
  \mathcal{F}^{-1} (e^{-2 \pi^2 s^2}) (x)
  \\ & =
  \frac{1}{\sqrt{2 \pi}} g(\frac{x}{\sqrt{2 \pi}})
  \\ & =
  \frac{1}{\sqrt{2 \pi}} e^{- \frac{x^2}{2}}
$$

$$
\tag*{$\blacksquare$}
$$

---

Back to {doc}`index`.

```{disqus}

```
