---
title: "Linear Regression: Formula Derivation"
---

# Linear Regression: Formula Derivation

(ref-sl-lr-functional)=

## Functional Representation

Define a Hilbert space:

$$
\mathcal{H} = \mathbb{R}^p
$$

with inner product:

$$
\langle u, v \rangle = u^\top v = \sum_{j=1}^p u_j v_j
$$

We are given data $\{ (x_i, y_i) \}_{i=1}^N$, with $x_i \in \mathcal{H}$, $y_i \in \mathbb{R}$.

It turns out that the predictor is a linear functional:

$$
f^{\ast}: \mathcal{H} \mapsto \mathbb{R}
$$

By Riesz representation theorem, in a Hilbert space $\mathcal{H}$, for every
continuous linear functional $f \in \mathcal{H}^*$, there exists a **unique**
$\beta \in \mathcal{H}$ such that:

$$
f(x) = \langle x, \beta \rangle
\quad
\forall x \in \mathcal{H}
$$

Thus, fitting the model means finding $\beta^{\ast}$ such that:

$$
\beta^{\ast} = \arg \min_{\beta \in \mathcal{H}}
\ell \left(
  \{\langle x_1, \beta \rangle, y_1\}, \ldots,
  \{\langle x_N, \beta \rangle, y_N\}
\right)
$$

where $\ell$ is the loss function.

(ref-sl-formula-ls)=

## Least Squares Solution

Here we use the squared loss:

$$
\ell (\beta) = \sum_{i=1}^N (y_i - \langle x_i, \beta \rangle)^2
$$

Rewrite in matrix form:

$$
\ell (\beta) = \| y - X \beta \|^2
$$

where $X$ is the $N \times p$ design matrix with $X_{ij} = x_{ij}$, $y$ is the
$N \times 1$ vector of responses.

The most straightforward way to find $\beta^{\ast}$ is to take the gradient
w.r.t. $\beta$ first:

$$
\begin{align*}
\nabla_\beta \ell (\beta) &=
  \nabla_\beta \left(
    y^\top y - 2 \beta^\top X^\top y + \beta^\top X^\top X \beta
  \right) \\
  &= -2 X^\top y + 2 X^\top X \beta
\end{align*}
$$

Setting the gradient to zero gives:

$$
X^\top X \beta^{\ast} = X^\top y
$$

We can solve $\beta^{\ast}$ if $X^\top X$ is invertible i.e. full rank.
This is why the **no collinearity** assumption is needed for linear regression:

$$
\beta^{\ast} = (X^\top X)^{-1} X^\top y
$$

This is the formula for the least squares solution of linear regression.

```{note}
- $X^+ = (X^\top X)^{-1} X^\top$ is known as the Moore--Penrose
  inverse {cite}`wiki_mpi_` of $X$.

- $X^\top X$ is a Gram matrix{cite}`wiki_gram_` over reals, which is symmetric
  and positive semi-definite, and it is invertible if and only if its
  determinant is non-zero, which is equivalent to the condition that $X$ has
  linearly independent columns.
  Particularly, if $X$ is centered, then $X^\top X$ is the scatter matrix of
  $X$, proportional to the covariance matrix $\text{cov} (X)$.

```

A more intuitive way is to note that response vector $y$ is a fixed point in
$\mathbb{R}^N$. We can define:

$$
\mathcal{S} = \text{span} \{ x^{(1)}, \ldots, x^{(p)} \} \subset \mathbb{R}^N
$$

where $x^{(i)}$ is the $i$-th column of $X$.

Thus $X \beta \in \mathcal{S}$.

To minimize $\| y - X \beta \|$ is to make $X \beta$ the orthogonal projection
of $y$ onto $\mathcal{S}$, so that $y - X \beta$ is orthogonal to
$\mathcal{S}$, i.e.:

$$
\langle y - X \beta^{\ast}, x^{(i)} \rangle = 0
\quad \forall i = 1, \ldots, p
$$

Rewrite in matrix form:

$$
X^\top (y - X \beta^{\ast}) = 0
$$

which is equivalent to the previous equation.

---

Back to {doc}`index`.

```{disqus}

```
