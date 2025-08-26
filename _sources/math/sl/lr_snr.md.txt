---
title: "Linear Regression: Signal-to-Noise Ratio (SNR)"
---

# Linear Regression: Signal-to-Noise Ratio (SNR)

We are given the model:

$$
y = X\beta + \epsilon
$$

where:

- $X \in \mathbb{R}^{N \times p}$ is the design matrix; and by Singular Value
  Decomposition (SVD), it can be expressed as $X = U D V^\top$
  - $U \in \mathbb{R}^{N \times p}$; its columns $u_1, \ldots, u_p$ are
    orthonormal vectors in $\mathbb{R}^N$
  - $V \in \mathbb{R}^{p \times p}$; its columns $v_1, \ldots, v_p$ are
    orthonormal vectors in $\mathbb{R}^p$
  - $D = \operatorname{diag}(d_1, \ldots, d_p)$, where
    $d_1 \geq d_2 \geq \ldots \geq d_p \geq 0$ are the singular values of $X$.

- $y \in \mathbb{R}^N$ is the response vector
- $\beta \in \mathbb{R}^p$ is the true coefficient vector
- $\epsilon \sim \mathcal{N}(0, \sigma^2 I)$ is the noise vector, with
  independent and identically distributed (i.i.d.) Gaussian entries

Here we interpret the response can be expressed as the sum of the
**true signal** $X\beta$ and the **noise term** $\epsilon$.

## Signal Energy

We introduce the **signal energy** as the $L^2$ norm squared of the signal vector
$s$:

$$
\| s \|^2 = \langle s, s \rangle
$$

and the **signal energy in direction $u_j \in \mathbb{R}^N$** as:

$$
| \langle X\beta, u_j \rangle |^2
$$

To compute the **true signal energy** per direction $u_j$, we substitute
$X = UDV^\top$.
Thus:

$$
\langle X\beta, u_j \rangle = \langle UDV^\top \beta, u_j \rangle
$$

Note that:

$$
UDV^\top \beta = \sum_{k=1}^p d_k \langle \beta, v_k \rangle u_k
$$

$$
\therefore
\langle X\beta, u_j \rangle =
\left\langle \sum_{k=1}^p d_k \langle \beta, v_k \rangle u_k, u_j
\right\rangle =
d_j \langle \beta, v_j \rangle
$$

$$
\therefore
| \langle X\beta, u_j \rangle |^2 =
(d_j \langle \beta, v_j \rangle)^2
$$

The (per-direction) **signal energy** can also be applied to the noise term
$\epsilon$, wi

Since $\epsilon \sim \mathcal{N}(0, \sigma^2 I)$ and $u_j$ is a unit vector:

$$
\langle \epsilon, u_j \rangle \sim \mathcal{N}(0, \sigma^2)
$$

Therefore:

$$
\mathbb{E}[\langle \epsilon, u_j \rangle^2] =
\mathrm{Var}(\langle \epsilon, u_j \rangle) +
\mathbb{E}[\langle \epsilon, u_j \rangle]^2 =
\sigma^2 + 0 = \sigma^2
$$

(ref-sl-lr-snr-snr)=

## Signal-to-Noise Ratio

We define the per-direction signal-to-noise ratio as:

$$
\text{SNR}_j = \frac{(d_j \langle \beta, v_j \rangle)^2}{\sigma^2}
$$

Since $\sigma$ is a constant, $\text{SNR}_j$ is determined by the numerator,
especially the singular value $d_j$:

- a large $d_j$ gives a large SNR, and
- a small $d_j$ gives a small signal energy, thus a small SNR, meaning more
  sensitive to noise.

This conclusion will be useful in the context of **shrinkage** methods, such as
[ridge regression](ref-sl-lr-ridge).

---

Back to {doc}`index`.

```{disqus}

```
