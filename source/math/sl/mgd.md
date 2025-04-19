---
title: Multivariate Gaussian Distribution
---

# Multivariate Gaussian Distribution

Suppose random vector $\mathbf{X} = (X_1, \ldots, X_p)^T$ has a
multivariate Gaussian distribution:

$$\mathbf{X} \sim \mathcal{N} (\mathbf{\mu}, \mathbf{\Sigma})$$

with probability density function:

$$
f (\mathbf{x}) =
  \frac{1}{\sqrt{(2 \pi)^p \lvert \mathbf{\Sigma} \rvert}}
  \exp \left(
    - \frac{1}{2} (\mathbf{x} - \mathbf{\mu})^T
      \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{\mu})
  \right)
$$

where:

- $\mathbf{\mu} = (\mu_1, \ldots, \mu_p)^T$ is the mean vector
- $\mathbf{\Sigma}$ is the covariance matrix
- $\lvert \mathbf{\Sigma} \rvert$ is the determinant of
  $\mathbf{\Sigma}$.

## Parameter Estimation

Suppose we have a dataset:

$$\mathcal{D} = \{ \mathbf{x}_i \}_{i = 1}^n$$

where each sample $\mathbf{x}_i$ is a $p$-dimensional vector.

The mean vector is calculated by averaging the samples:

$$
\mathbf{\mu} =
  \frac{1}{n} \sum_{i = 1}^n \mathbf{x}_i
$$

where $n$ is the number of samples.

The covariance matrix is estimated by **summing the outer products of
the centered samples**:

$$
\mathbf{\Sigma} =
  \frac{1}{n - 1} \sum_{i = 1}^n
  (\mathbf{x}_i - \mathbf{\mu}) (\mathbf{x}_i - \mathbf{\mu})^T
$$

### Matrix Form

Let $\mathbf{X} = (\mathbf{x}_1, \ldots, \mathbf{x}_n)^T$ be the design
matrix with each row being a sample.

The centered design matrix is computed as:

$$
\tilde{\mathbf{X}} = \left(
  \mathbf{x}_1 - \mathbf{\mu}, \ldots, \mathbf{x}_n - \mathbf{\mu}
\right)^T
$$

The covariance matrix can be written as:

$$
\mathbf{\Sigma} =
  \frac{1}{n - 1} \tilde{\mathbf{X}}^T \tilde{\mathbf{X}}
$$

(ref-sl-mgd-cov)=

## Properties of the Covariance Matrix

```{admonition} Theorem
Covariance matrix $\mathbf{\Sigma}$ is always **symmetric** and
**positive semi-definite**.
```

**Proof:**

$\mathbf{\Sigma}$ is symmetric because:

$$
\mathbf{\Sigma}^T =
  \left(
    \frac{1}{n - 1} \tilde{\mathbf{X}}^T \tilde{\mathbf{X}}
  \right)^T =
  \frac{1}{n - 1} \tilde{\mathbf{X}}^T \tilde{\mathbf{X}} =
  \mathbf{\Sigma}
$$

$\mathbf{\Sigma}$ is positive semi-definite, because for any vector
$\mathbf{v} \in \mathbb{R}^p$:

$$
\mathbf{v}^T \mathbf{\Sigma} \mathbf{v} =
  \mathbf{v}^T \left(
    \frac{1}{n - 1} \tilde{\mathbf{X}}^T \tilde{\mathbf{X}}
  \right) \mathbf{v} =
  \frac{1}{n - 1} (\tilde{\mathbf{X}} \mathbf{v})^T
    (\tilde{\mathbf{X}} \mathbf{v}) =
  \frac{1}{n - 1} \lVert \tilde{\mathbf{X}} \mathbf{v} \rVert^2 \ge 0
$$

Therefore, $\mathbf{\Sigma}$ is symmetric and positive semi-definite.

$$\tag*{$\blacksquare$}$$

### Eigenvalue Interpretation

Without giving a formal proof, an equivalent condition to symmetric and
positive semi-definite property is that **all eigenvalues of the
covariance matrix are non-negative** {cite}`wiki_definite_matrix_`.

- An eigenvalues of the covariance matrix can be interpreted as the
  amount of variance explained by the corresponding eigenvector, which
  cannot be negative.
- A zero eigenvalue indicates that one or more variables can be
  expressed as a linear combination of other variables, which
  effectively makes the covariance matrix **singular and not
  invertible**. Also, along the direction represented by the
  corresponding eigenvector, there is no variability in the data.
- In case of a singular covariance matrix:
  - Apply Tikhonov regularization by adding a small multiple of the
    identity matrix to the covariance matrix {cite}`wiki_ridge_`.
  - Use the pseudo-inverse of the covariance matrix.
  - Perform dimensionality reduction.

---

Back to {doc}`index`.

```{disqus}

```
