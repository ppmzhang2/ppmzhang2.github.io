---
title: Gradient Descent
---

# Gradient Descent

## Empirical Risk Minimization

Suppose a dataset
$S = \{ \mathbf{z}_i \}_{i=1}^n = \{ (\mathbf{x}_i, \mathbf{y}_i) \}_{i=1}^n$
is sampled from a distribution $\mathcal{D}$ over a domain
$\mathcal{Z} = \mathcal{X} \times \mathcal{Y}$, where
$\mathcal{X} \subseteq \mathbb{R}^d$,
$\mathcal{Y} \subseteq \mathbb{R}^{d_o}$.

We model with a functions $f (\mathbf{x}; \mathbf{w})$ parameterized by
a weight vector $\mathbf{w} \in \mathcal{W}$, such that
$f_{\mathbf{w}}: \mathcal{X} \rightarrow \mathcal{Y}$; we also use a
loss function denoted by
$Q: \mathcal{Z} \times \mathcal{W} \rightarrow \mathbb{R}$ to measure
the difference between a prediction and a true label:

$$Q(\mathbf{z}, \mathbf{w}) = \ell (f (\mathbf{x}; \mathbf{w}), \mathbf{y})$$

Our goal is to find the target weight $\mathbf{w}^*$ such that the
expected risk
$R_{\mathcal{D}} = E_{\mathcal{D}} Q (\mathbf{z}, \mathbf{w})$ is
minimized.

$$
R_{\mathcal{D}} (\mathbf{w}) &=
E_{\mathcal{D}} Q (\mathbf{z}, \mathbf{w})
\\ &=
\int_{\mathcal{D}}
  Q(\mathbf{z}, \mathbf{w}) f_Z (\mathbf{z}) \mathrm{d} \mathbf{z}
$$

where $f_Z$ is the joint probability density function.

$R_{\mathcal{D}}$ is hard to calculate as the distribution (i.e. $f_Z$)
is unknown. It can be estimated, however, with the empirical risk
$R_n$:

$$
R_n (\mathbf{w}) =
\frac{1}
{|\Omega|} \sum_{\mathbf{z} \in \Omega} Q(\mathbf{z}, \mathbf{w})
$$

where $\Omega \subset \mathcal{D}$.

Using gradient descent (GD), $R_n$ can be minimized by submitting the
gradient iteratively:

$$
\mathbf{w}^{(t+1)} &=
\mathbf{w}^{(t)} - \eta \cdot
  \nabla_{\mathbf{w}} R_n (\mathbf{w})
\\ &=
\mathbf{w}^{(t)} - \eta \cdot
  \nabla_{\mathbf{w}}
    \frac{1}{|\Omega|}
    \sum_{\mathbf{z} \in \Omega} Q(\mathbf{z}, \mathbf{w})
\\ &=
\mathbf{w}^{(t)} - \eta \cdot
  \frac{1}{|\Omega|}
  \sum_{\mathbf{z} \in \Omega} \nabla_{\mathbf{w}} Q(\mathbf{z}, \mathbf{w})
$$

## Stochastic vs. Batch

Training with the whole training set $\Omega$ for each step is **Batch
Gradient Descent**. When $|\Omega| = 1$ it is **Stochastic Gradient
Descent (SGD)**. A compromised solution is to train for each step a
subset of the training dataset, which is the **Mini-Batch Gradient
Descent**.[^fn1] 

[^fn1]:
    <https://cilvr.cs.nyu.edu/diglib/lsml/bottou-sgd-tricks-2012.pdf>

---

Back to {doc}`index`.

```{disqus}

```
