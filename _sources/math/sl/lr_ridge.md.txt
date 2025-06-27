---
title: "Linear Regression: Ridge Regression"
---

(ref-sl-lr-ridge)=

# Linear Regression: Ridge Regression

## Projection Matrix

Given a design matrix $X \in \mathbb{R}^{N \times p}$ and response vector
$y \in \mathbb{R}^N$, by [previous derivation](ref-sl-formula-ls) the OLS
estimator of the coefficients is:

$$
\beta_\text{ols} = (X^\top X)^{-1} X^\top y
$$

The predicted values are:

$$
y_\text{ols} = H y
$$

where $H = X (X^\top X)^{-1} X^\top$

The matrix $H$ is known as the **hat matrix** or **projection matrix** for OLS,
since it is an **orthogonal projection** matrix onto the column space of $X$.
Obviously for the OLS projection matrix $H$:

- $H^2 = H$
- $H^\top = H$
- $\operatorname{rank} (H) = \operatorname{rank} (X)$.

Ridge regression introduces a penalty to stabilize the coefficient estimates:

$$
\beta_\text{ridge} = (X^\top X + \lambda I)^{-1} X^\top y, \quad \lambda > 0
$$

The corresponding fitted values are:

$$
y_\text{ridge} = H_\lambda y
$$

where $H_\lambda = X (X^\top X + \lambda I)^{-1} X^\top$

Note that $H_\lambda$ may not have the properties as an **projection matrix**:

- $H_\lambda^2 \neq H_\lambda$

- $H_\lambda^T \neq H_\lambda$ in general

We will show the deviation from orthogonality is due to the **shrinkage**
effect.

## Shrinkage Factor

Let $X = U D V^\top$ be the singular value decomposition of $X$, where:

- $U \in \mathbb{R}^{N \times p}$; its columns $u_1, \ldots, u_p$ are
  orthonormal vectors in $\mathbb{R}^N$

- $V \in \mathbb{R}^{p \times p}$; its columns $v_1, \ldots, v_p$ are
  orthonormal vectors in $\mathbb{R}^p$

- $D = \operatorname{diag}(d_1, \ldots, d_p)$, where
  $d_1 \geq d_2 \geq \ldots \geq d_p \geq 0$ are the singular values of $X$.

Applying the SVD to the ridge regression estimator, we have:

$$
y_\text{ridge} =
\sum_{j=1}^p \left( \frac{d_j^2}{d_j^2 + \lambda} \right)
\langle y, u_j \rangle u_j
$$

The coefficient

$$
\frac{d_j^2}{d_j^2 + \lambda} \in (0, 1)
$$

is the **shrinkage factor** that depends on the singular value $d_j$ [^1]:

- when $d_j^2 \gg \lambda$, the shrinkage factor is close to 1, meaning minimal
  shrinkage

- when $d_j^2 \ll \lambda$, the shrinkage factor is close to 0, meaning strong
  shrinkage

## Interpretation

From the Principal Component Analysis (PCA) perspective, a small $d_j$ means
**low variance**, and de-emphasizing these components makes the model more
focused on components with more information.

While from the perspective of [SNR](ref-sl-lr-snr-snr), a small $d_j$ also
means low signal-to-noise ratio, and reducing its contribution means
less susceptible to noise and overfitting, thus a more robust model.

[^1]: The trivial case is when $\lambda = 0$, which reduces to OLS.

---

Back to {doc}`index`.

```{disqus}

```
