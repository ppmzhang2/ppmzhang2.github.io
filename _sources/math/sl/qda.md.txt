---
title: Quadratic Discriminant Analysis
---

# Quadratic Discriminant Analysis

Quadratic Discriminant Analysis (QDA) assumes:

- Normality: the class-conditional PDF follows a multivariate Gaussian
  distribution with class-specific mean vectors and covariance matrices

## Probability Density Function

Suppose we have a set of samples $\mathcal{D}$ with $K$ classes:

$$\mathcal{D} = \{ (\mathbf{x}_1, y_1), \ldots, (\mathbf{x}_N, y_N) \}$$

where $\mathbf{x}_i \in \mathbb{R}^p$ is a $p$-dimensional sample and
$y_i \in \{ 1, \ldots, K \}$ is the class label for sample
$\mathbf{x}_i$.

According to the QDA assumption, $\mathbf{x}$ is sampled from a random
vector $\mathbf{X} = (X_1, \ldots, X_p)^T$ with a conditional
multivariate Gaussian distribution:

$$\mathbf{X} \mid k \sim \mathcal{N} (\mathbf{\mu}_k, \mathbf{\Sigma}_k)$$

The probability density function:

$$
f (\mathbf{x} \mid k) =
  \frac
  {1}
  {\sqrt{(2 \pi)^p \lvert \mathbf{\Sigma}_k \rvert}}
  \exp
  \left(
    -\frac{1}{2}
    (\mathbf{x} - \mathbf{\mu}_k)^T
    \mathbf{\Sigma}_k^{-1}
    (\mathbf{x} - \mathbf{\mu}_k)
  \right)
$$

where:

- $\mathbf{\mu}_k$ is the mean vector for class $k$

  $$
  \mathbf{\mu}_k =
    \frac{1}{n_k}
    \sum_{\mathbf{x} \in \mathcal{D}_k}
    \mathbf{x}
  $$

  where $n_k$ is the number of samples in class $k$ and $\mathcal{D}_k$
  is the set of samples in class $k$.

- $\mathbf{\Sigma}_k$ is the covariance matrix for class $k$

  $$
  \mathbf{\Sigma}_k =
    \frac{1}{n_k - 1}
    \sum_{\mathbf{x} \in \mathcal{D}_k}
    (\mathbf{x} - \mathbf{\mu}_k)
    (\mathbf{x} - \mathbf{\mu}_k)^T
  $$

## Classification

According to Bayes\' theorem, the posterior probability of class $k$
given sample $\mathbf{x}$ is:

$$
f (k \mid \mathbf{x}) =
  \frac
    {f (\mathbf{x} \mid k) \cdot \pi_k}
    {\sum_{i = 1}^K f (\mathbf{x} \mid i) \cdot \pi_i}
$$

Ignoring the denominator which does not depend on $k$, we have:

$$
f (k \mid \mathbf{x}) \propto
  f (\mathbf{x} \mid k) \cdot \pi_k
$$

where $\pi_k$ is the prior probability of class $k$.

Taking the logarithm of both sides, we have:

$$
\ln f (k \mid \mathbf{x}) \propto
  \ln f (\mathbf{x} \mid k) + \ln \pi_k
$$

$$
\therefore
\hat{y} = \arg \max_{k}
  \left(
    - \frac{1}{2} p \ln {2 \pi}
    - \frac{1}{2} \ln \lvert \mathbf{\Sigma}_k \rvert
    - \frac{1}{2} (\mathbf{x} - \mathbf{\mu}_k)^T
      \mathbf{\Sigma}_k^{-1}
      (\mathbf{x} - \mathbf{\mu}_k)
    + \ln \pi_k
  \right)
$$

By removing the terms that do not depend on $k$, we have:

$$
\hat{y} &= \arg \max_{k}
  \left(
    - \frac{1}{2} (\mathbf{x} - \mathbf{\mu}_k)^T \mathbf{\Sigma}_k^{-1}
      (\mathbf{x} - \mathbf{\mu}_k)
    - \frac{1}{2} \ln \lvert \mathbf{\Sigma}_k \rvert
    + \ln \pi_k
  \right)
\\ &=
\arg \max_{k}
  \left(
    - \frac{1}{2} \mathbf{x}^T \mathbf{\Sigma}_k^{-1} \mathbf{x}
    + \mathbf{x}^T \mathbf{\Sigma}_k^{-1} \mathbf{\mu}_k
    - \frac{1}{2} \mathbf{\mu}_k^T \mathbf{\Sigma}_k^{-1} \mathbf{\mu}_k
    - \frac{1}{2} \ln \lvert \mathbf{\Sigma}_k \rvert
    + \ln \pi_k
  \right)
$$

---

Back to {doc}`index`.

```{disqus}

```
