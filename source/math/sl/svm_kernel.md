---
title: "SVM: Kernel Method"
---

# SVM: Kernel Method

We seek $f \in \mathcal{H}$, where $\mathcal{H}$ is a
**Reproducing Kernel Hilbert Space** (**RKHS**) of real-valued functions on
$\mathcal{X} \subseteq \mathbb{R}^d$.

$$
f : \mathcal{X} \to \mathbb{R}, \quad
\mathcal{X} \subseteq \mathbb{R}^d
$$

By the definition of RKHS, the pointwise evaluation in $\mathcal{H}$ for each
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

To confirm the **reproducing property**, take $f = k_x$:

$$
k_x (y) = L_y (k_x) = \langle k_x, k_y \rangle_{\mathcal{H}}
$$

We define the **reproducing kernel** as a function
$k : \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ such that:

$$
k(x, y) = \langle k_x, k_y \rangle_{\mathcal{H}}
$$

```{note}
In the RKHS setting, the concept of "dimensionality increase" is abstract:
functions live in an infinite-dimensional space.
However, the "effective dimension" is governed by the kernel $k$, which defines
the structure of $\mathcal{H}$.
Once a kernel is chosen, the hypothesis space is fixed, and no additional
dimensions are introduced during learning.
Later the representer theorem also shows that the solution is a finite linear
combination of kernel functions evaluated at the training points.
In fact, some people use the notation $\mathcal{H}_k$ to denote the RKHS
associated with kernel $k$.
For simplicity we use $\mathcal{H}$.
```

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

## Appendix: Proof of Riesz Representation Theorem

Let $\mathcal{H}$ be a Hilbert space of real-valued functions on
$\mathcal{X} \subseteq \mathbb{R}^d$, equipped with an inner product
$\langle \cdot, \cdot \rangle_{\mathcal{H}}$.
For any _bounded linear functional_ $L: \mathcal{H} \to \mathbb{R}$,
we want to show that
there _exists a unique_ $g \in \mathcal{H}$ such that

$$
\forall f \in \mathcal{H}: \quad
L(f) = \langle f, g \rangle_{\mathcal{H}}
$$

**Proof**:

For any $f \in \mathcal{H}$, for the trivial case when $L(f) = 0$,
we can always take $g = 0$, which gives $\langle f, 0 \rangle = 0 = L(f)$.

Let us consider the case when $L(f) \ne 0$ for some $f \in \mathcal{H}$.

First, we define the **kernel** and the **orthogonal complement** of the kernel of $L$:

$$
\ker L = \{ f \in \mathcal{H} : L(f) = 0 \}.
$$

$$
(\ker L)^\perp =
\{ g \in \mathcal{H} : \langle g, f \rangle = 0, \quad \forall f \in \ker L \}
$$

Since $L$ is a bounded linear operator, $\ker(L)$ is a _closed subspace_ of
$\mathcal{H}$. Thus we can apply the **orthogonal decomposition theorem**:

$$
\mathcal{H} = \ker(L) \oplus (\ker L)^\perp
$$

and any $f \in \mathcal{H}$ can be uniquely decomposed as:

$$
f = f_0 + g_0
$$

where $f_0 \in \ker(L)$ and $g_0 \in (\ker L)^\perp$.
Note that $g_0 \ne 0$ as $L(f) \ne 0$.

Let:

$$
g = \frac{L(g_0)}{\|g_0\|^2} g_0
$$

$$
\therefore
\langle g_0, g \rangle =
\left\langle g_0, \frac{L(g_0)}{\|g_0\|^2} g_0 \right\rangle =
\frac{\|g_0\|^2}{\|g_0\|^2} L(g_0) = L(g_0).
$$

$$
\because
L(f) = L(f_0 + g_0) = 0 + L(g_0) = L(g_0).
$$

$$
\because
\langle f, g \rangle =
\langle f_0 + g_0, g \rangle = \langle g_0, g \rangle =
L(g_0)
$$

$$
\therefore
L(f) = \langle f, g \rangle_{\mathcal{H}}
$$

To prove the uniqueness of $g$, suppose there are $g_1, g_2 \in \mathcal{H}$
such that

$$
L(f) = \langle f, g_1 \rangle = \langle f, g_2 \rangle
\quad \forall f \in \mathcal{H}.
$$

$$
\therefore
\langle f, g_1 - g_2 \rangle = 0
\quad \forall f \in \mathcal{H}.
$$

Take $f = g_1 - g_2$:

$$
\|g_1 - g_2\|^2 = 0 \Rightarrow g_1 = g_2.
$$

$$
\tag*{$\blacksquare$}
$$

Back to {doc}`index`.

```{disqus}

```
