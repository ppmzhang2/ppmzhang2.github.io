---
title: "Bayes Example: Biased Coin"
---

# Bayes Example: Biased Coin

Consider a Bernoulli trial of flipping a coin. What is probability of
head if we got $k$ heads in $n$ trials?

## Maximum Likelihood Estimate

Let $\theta$ be the probability of head. We represent $n$ Bernoulli
trial results with $n$ random variables $X_1, \ldots, X_n$:

$$
X_i =
\begin{cases}
  0, & \text{Tail}
  \\
  1, & \text{Head}
\end{cases}
$$

where $i \in [1, n]$.

Since $X_1, \ldots, X_n$ are independently and identically distributed
(i.i.d.), their conditional probability of head given $\theta$ is fixed:

$$
f_{X_i} (x \mid \theta) =
\begin{cases}
  \theta, & x = 1
  \\
  1 - \theta, & x = 0
\end{cases}
$$

where $i \in [1, n]$.

$$
\therefore
\mathcal{L}(\theta \mid \mathbf{x}) =
\prod_{i=1}^{n} f_{X_i} (x_i \mid \theta) =
\theta^{k} (1 - \theta)^{n - k}
$$

$$
\therefore
\ln \mathcal{L}(\theta \mid \mathbf{x}) =
k \ln \theta + (n - k) \ln (1 - \theta)
$$

Finding Maxima using derivatives:

$$
\frac{d \ln \mathcal{L} (\theta \mid \mathbf{x})}{d \theta} =
\frac{k}{\theta} - \frac{n - k}{1 - \theta} = 0
$$

$$
\therefore
\theta = \frac{k}{n}
$$

## Bayes Estimate

The Maximum Likelihood Estimate (MLE) only gives the **most probable**
result, which cannot exclude the possibility of other values. In fact,
**the probability being estimated is also a random variable**, which has
its only distribution and expectation, and the Bayes Estimate will give
the expectation.

### Preliminary Knowledge

To calculate the posterior probability of a coin head, we need to know
the [Beta Function](https://en.wikipedia.org/wiki/Beta_function):

$$
B(x, y) &=
\int_0^1 t^{x-1} (1-t)^{y-1} \mathrm{d} t
\\ &=
\frac{(x - 1)! (y - 1)!}{(x + y - 1)!}
$$

### Bayes Formula

Before trial, we believe that all values of $\theta$ are equally likely,
therefore:

$$
f(\theta) =
\begin{cases}
  1, & x \in [0, 1]
  \\
  0, & \text{otherwise}
\end{cases}
$$

$$
\therefore
f (\theta \mid \mathbf{x}) &=
  \frac{\mathcal{L}(\theta \mid \mathbf{x}) \cdot f(\theta)}
  {\int\limits_{\mathbb{R}}
    \mathcal{L} (\theta \mid \mathbf{x}) \cdot f(\theta) \mathrm{d} \theta}
  \\ &=
  \frac{\theta^{k} (1 - \theta)^{n - k}}
  {\int_0^{1} \theta^{k} (1 - \theta)^{n - k} \mathrm{d} \theta}
  \\ &=
  \frac{\theta^{k} (1 - \theta)^{n - k}}{B(k+1, n-k+1)}
$$

$$
\therefore
E(\theta) & =
\int_0^1 \theta f(\theta \mid \mathbf{x}) \mathrm{d} \theta
\\ &=
\frac{1}{B(k+1, n-k+1)}
\int_0^1 \theta^{k+1} (1 - \theta)^{n-k} \mathrm{d} \theta
\\ &=
\frac{B(k+2, n-k+1)}{B(k+1, n-k+1)}
\\ &=
\frac{k + 1}{n + 2}
$$

Suppose we got all heads in 100 trials. The expected value of head
probability is $\frac{101}{102} = 99.02\%$.

---

Back to {doc}`index`.

```{disqus}

```
