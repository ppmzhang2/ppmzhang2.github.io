---
title: Bayes Theorem
---

# Bayes Theorem

- What does likelihood mean?
- how is "likelihood" different than "probability"?

## Joint, Marginal and Conditional Distributions

For $n$ jointly random variables $X_1, \ldots, X_n$ the joint PDF is
defined as:

$$
f_{X_1 \ldots X_n} (x_1, \ldots, x_n)
$$

Obviously, the probability of $[x_1, \ldots, x_n] \in \mathbb{R}^n$ must
be one. So we must have:

$$
\int \cdots \int\limits_{\mathbb{R}^n} \cdots \int
  f_{X_1 \ldots X_n} (x_1, \ldots, x_n)
  \mathrm{d} x_1 \cdots \mathrm{d} x_n = 1
$$

A marginal PDF is the **integral of the joint PDF**. Let $X$ and $Y$ be
two jointly continuous random variables with joint PDF $f_{XY} (x, y)$.
We have:

$$
f_X (x) =
\int_{-\infty}^{+\infty}
f_{XY} (x, y) \mathrm{d} y
$$

The conditional PDF is the joint PDF over marginal PDF:

$$
f_X (x \mid y) =
\frac{f_{XY} (x, y)}{f_Y (y)}
$$

Alternatively, **a joint PDF is the product of conditional PDF and
marginal PDF**:

$$f_{XY} (x, y) = f_X (x \mid y) \cdot f_Y (y)$$

Therefore the joint PDF of $X_1, \ldots, X_n$ can be transformed as:

$$
f_{X_1 \ldots X_n} (x_1, \ldots, x_n) =
f_{X_1} (x_1 \mid x_2, \ldots, x_n)
f_{X_2} (x_2 \mid x_3, \ldots, x_n)
\cdots
f_{X_n} (x_n)
$$

where $f_{X_i}$ is the marginal PMF / PDF of random variable $X_i$.

## Likelihood

Likelihood is a synonym for the **joint probability (density)** of your
data [^1]. It is defined, however, as a function of the **model
parameters** ($\theta$) as data sampled from $X_1, \ldots, X_n$ is
fixed.

$$
\mathcal{L}(\theta \mid \mathbf{x}^{(0)}) & =
f_{X_1 \ldots X_n} (x_1^{(0)}, \ldots, x_n^{(0)} \mid \theta)
\\ &=
f_{X_1} (x_1^{(0)} \mid x_2^{(0)}, \ldots, x_n^{(0)}, \theta)
f_{X_2} (x_2^{(0)} \mid x_3^{(0)}, \ldots, x_n^{(0)}, \theta)
\cdots
f_{X_n} (x_n^{(0)} \mid \theta)
$$

Particularly, when $X_1, X_2, \ldots, X_n$ are independent. This is the
case when random variables $X_1, X_2, \ldots, X_n$ are $n$ **mutually
independent** features. (core assumption of naive Bayes classifier)

$$
\mathcal{L}(\theta \mid \mathbf{x}^{(0)}) =
\prod_{i=1}^{n} f_{X_i} (x_i^{(0)} \mid \theta)
$$

More particularly, when $X_1, X_2, \ldots, X_n$ are independently and
identically distributed (i.i.d.):

$$
\mathcal{L}(\theta \mid \mathbf{x}^{(0)}) =
\prod_{i=1}^{n} f_{X} (x_i^{(0)} \mid \theta)
$$

(bayes-theorem-1)=

## Bayes Theorem

The Bayes theorem is to calculate the posterior (conditional)
probability (density) function of variable $\theta$.

The probability density function form ($\theta$ is continuous):

$$
f(\theta \mid \mathbf{x}) & =
  \frac{f_{X_1 \ldots X_n \Theta} (x_1, \ldots, x_n, \theta)}
  {f_{X_1 \ldots X_n} (x_1, \ldots, x_n)}
  \\ &=
  \frac{f_{X_1 \ldots X_n \Theta} (x_1, \ldots, x_n, \theta)}
  {\int\limits_{\mathbb{R}}
    f_{X_1 \ldots X_n \Theta} (x_1, \ldots, x_n, \theta) \mathrm{d} \theta}
  \\ &=
  \frac
    {f_{X_1 \ldots X_n} (x_1, \ldots, x_n \mid \theta) \cdot \pi (\theta)}
    {\int\limits_{\mathbb{R}}
      f_{X_1 \ldots X_n} (x_1, \ldots, x_n \mid \theta) \cdot
      \pi (\theta) \mathrm{d} \theta}
  \\ &=
  \frac
    {\mathcal{L}(\theta \mid \mathbf{x}) \cdot \pi (\theta)}
    {\int\limits_{\mathbb{R}}
      \mathcal{L} (\theta \mid \mathbf{x}) \cdot
      \pi (\theta) \mathrm{d} \theta}
$$

where $\pi (\theta)$ is the prior PDF of $\theta$.

[^1]:
    In the case of discrete distributions, likelihood is the joint
    probability; in the case of continuous distribution, likelihood
    refers to the joint probability density

---

Back to {doc}`index`.

```{disqus}

```
