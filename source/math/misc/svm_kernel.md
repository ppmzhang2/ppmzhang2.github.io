---
title: "SVM: Kernel Method"
---

# SVM: Kernel Method

The goal is to find an optimal real-valued function:

$$
f : \mathcal{X} \to \mathbb{R}, \quad
\mathcal{X} \subseteq \mathbb{R}^d
$$

which in a **Reproducing Kernel Hilbert Space** (**RKHS**) $\mathcal{H}$.

```{note}
There is no "dimensionality increase" from the perspective of the RKHS;
only an abstract (but well-defined) space of functions with a kernel-defined
inner product.
```

By the definition of RKHS, the evaluation over $\mathcal{H}$ at each point
$x \in \mathcal{X}$

$$
L_x : f \mapsto f(x)
$$

is a **continuous linear functional** for all $f \in \mathcal{H}$.

By the **Riesz Representation Theorem**:

$$
\forall x \in \mathcal{X}: \quad
\exists k_x \in \mathcal{H}
\quad S.T. \quad
f(x) = L_x (f) = \langle f, k_x \rangle_{\mathcal{H}} \quad
\forall f \in \mathcal{H}
$$

Specifically, we take $f = k_x$:

$$
k_x (y) = L_y (k_x) = \langle k_x, k_y \rangle_{\mathcal{H}}
$$

We define the **reproducing kernel** as a function
$k : \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ such that:

$$
k(x, y) = \langle k_x, k_y \rangle_{\mathcal{H}}
$$

## Empirical Risk

To find the optimal function $f^*$, we need to minimize the empirical risk:

$$
f^* =
\min_{f \in \mathcal{H}} \; R(\|f\|_{\mathcal{H}}^2) + E(f(x_1), \ldots, f(x_n))
$$

Where:

- $(x_i, y_i) \in \mathcal{X} \times \mathbb{R}$ are the training data,
- $R$ is a non-decreasing regularizer (e.g., $R(u) = \lambda u$),
- $E$ is a empirical loss function (e.g., squared loss, hinge loss).

By **representer theorem**, any minimizer of the above problem admits the form:

$$
f^* = \sum_{i=1}^n \alpha_i k_{x_i}
$$

where $\alpha_i \in \mathbb{R}$.

We will use it to compute the empirical risk.
First, we compute the norm:

$$
\|f\|_{\mathcal{H}}^2 =
\left\langle
  \sum_{i=1}^n \alpha_i k_{x_i}, \sum_{j=1}^n \alpha_j k_{x_j}
\right\rangle_{\mathcal{H}} =
\sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j
\langle k_{x_i}, k_{x_j} \rangle_{\mathcal{H}} =
\sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j k(x_i, x_j)
$$

$$
\therefore
\|f\|_{\mathcal{H}}^2 = \alpha^\top K \alpha
$$

where

- $K \in \mathbb{R}^{n \times n}$ is the **Gram matrix** with entries $K_{ij} = k(x_i, x_j)$.

- $\alpha \in \mathbb{R}^n$ is the vector of coefficients $\alpha_i$.

The empirical risk depends on the predictions on the training data, which is a vector:

$$
\mathbf{f} =
\begin{bmatrix}
f(x_1) \\
f(x_2) \\
\vdots \\
f(x_n)
\end{bmatrix} =
\begin{bmatrix}
\sum_{i=1}^n \alpha_i k(x_1, x_i) \\
\sum_{i=1}^n \alpha_i k(x_2, x_i) \\
\vdots \\
\sum_{i=1}^n \alpha_i k(x_n, x_i)
\end{bmatrix}
$$

Expanded as a matrix-vector product:

$$
\mathbf{f} =
\begin{bmatrix}
k(x_1, x_1) & \cdots & k(x_1, x_n) \\
k(x_2, x_1) & \cdots & k(x_2, x_n) \\
\vdots & \ddots & \vdots \\
k(x_n, x_1) & \cdots & k(x_n, x_n)
\end{bmatrix}
\begin{bmatrix}
\alpha_1 \\
\alpha_2 \\
\vdots \\
\alpha_n
\end{bmatrix}
$$

Which is precisely the definition of a matrix-vector product:

$$
\mathbf{f} = K \alpha
$$

## Derivation of Solution

Now the empirical risk can be expressed as
(for simplicity, we will use squared loss):

$$
\min_{\alpha \in \mathbb{R}^n} \; \frac{\lambda}{2} \alpha^\top K \alpha + \frac{1}{2} \|K \alpha - y\|^2
$$

To minimize, take the gradient w.r.t. $\alpha$:

$$
\nabla_\alpha \left( \frac{\lambda}{2} \alpha^\top K \alpha + \frac{1}{2} \|K \alpha - y\|^2 \right)
= \lambda K \alpha + K (K \alpha - y)
= K (\lambda \alpha + K \alpha - y)
$$

Set gradient to zero:

$$
K (\lambda \alpha + K \alpha - y) = 0
$$

Assuming $K$ is positive definite (or at least invertible), this implies:

$$
(\lambda I + K) \alpha = y
$$

**Solution**:

$$
\boxed{
\alpha = (\lambda I + K)^{-1} y
}
$$

Back to {doc}`index`.

```{disqus}

```
