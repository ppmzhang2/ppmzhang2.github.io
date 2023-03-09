#########################################
Linear Regression: Ordinary Least Squares
#########################################

.. default-role:: math

TL;DR
=====

- OLS estimator is unbiased if:

  - No Collinearity

  - `\mathrm{E} \left[ \epsilon_i \right] = 0,`
    `\forall i \in \left[ 1, n \right]`

- OLS estimator is the Best Linear Unbiased Estimator (BLUE) if:

  - No Collinearity

  - `\mathrm{E} \left[ \epsilon_i \right] = 0,`
    `\forall i \in \left[ 1, n \right]`

  - `\mathrm{Var} \left[ \epsilon_i \right] = \sigma^2,`
    `\forall i \in \left[ 1, n \right]`

  - `\mathrm{Cov} \left[ \epsilon_i, \epsilon_j \right] = 0,`
    `\forall i \ne j`

- OLS estimator is equivalent to MLE (generalized linear model) if:

  - No Collinearity

  - `\mathrm{E} \left[ \epsilon_i \right] = 0,`
    `\forall i \in \left[ 1, n \right]`

  - `\mathrm{Var} \left[ \epsilon_i \right] = \sigma^2,`
    `\forall i \in \left[ 1, n \right]`

  - `\mathrm{Cov} \left[ \epsilon_i, \epsilon_j \right] = 0,`
    `\forall i \ne j`

  - random errors are **identically** and **independently** drawn from a
    **normal distribution**.

Problem and Hypothesis
======================

Suppose:

.. math::

   \mathbf{y} = \mathbf{X} \mathbf{w}^* + \mathbf{\epsilon}

where

- `\mathbf{X}` is the design matrix of `n \times p` non-random, observable
  predictors [#f01]_

- `\mathbf{\epsilon}` is a `n`-dimensional random vector, which makes
  `\mathbf{y}` the `n`-dimensional observable random vector response

- `\mathbf{w}^* = [w_1^*, \ldots, w_p^*]^T` are the **underlying non-random,
  unobservable coefficients**, which is to be estimated.

Our hypothesis is:

.. math::

   \hat{\mathbf{y}} = \mathbf{X} \mathbf{w}

where the linear estimator `\mathbf{w}` can be represented as:

.. math::

   \mathbf{w} = \mathbf{C} \mathbf{y}

where `\mathbf{C}` is a `p \times n` matrix depends on the `n \times p`
predictor `\mathbf{X}` and the `n \times 1` response `\mathbf{y}`.

A natural thought would be that `\mathbf{c}` is the
`pseudoinverse
<https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse>`_
of `\mathbf{X}`, which will be confirmed by the OLS.

Assumptions of the OLS
======================

No Collinearity
---------------

To get the assumption we need to calculate the analytical solution to the OLS
problem.

With Ordinary Least Squares (OLS), the risk can be calculated as:

.. math::

   R (\hat{\mathbf{w}}) =
   \frac{1}{n} \lVert \hat{\mathbf{y}} - \mathbf{y} \rVert_2^2

To minimize `R` :cite:p:`book_dl_` :cite:p:`book_mc_`:

.. math::

   \nabla_{\mathbf{w}} R = 0

.. math::

   \therefore
   \nabla_{\mathbf{w}} R &=
   \nabla_{\mathbf{w}}
   \frac{1}{n} \lVert \hat{\mathbf{y}} - \mathbf{y} \rVert_2^2
   \\ &=
   \nabla_{\mathbf{w}}
     (\hat{\mathbf{y}} - \mathbf{y})^T
     (\hat{\mathbf{y}} - \mathbf{y})
   \\ &=
   \nabla_{\mathbf{w}}
     (\mathbf{X} \mathbf{w} - \mathbf{y})^T
     (\mathbf{X} \mathbf{w} - \mathbf{y})
   \\ &=
   \nabla_{\mathbf{w}}
     (\mathbf{w}^T \mathbf{X}^T - \mathbf{y}^T)
     (\mathbf{X} \mathbf{w} - \mathbf{y})
   \\ &=
   \nabla_{\mathbf{w}}
     (\mathbf{w}^T \mathbf{X}^T \mathbf{X} \mathbf{w} -
      \mathbf{w}^T \mathbf{X}^T \mathbf{y} -
      \mathbf{y}^T \mathbf{X} \mathbf{w} +
     \mathbf{y}^T \mathbf{y})
   \\ &=
   \nabla_{\mathbf{w}}
     (\mathbf{w}^T \mathbf{X}^T \mathbf{X} \mathbf{w} -
      2 \mathbf{w}^T \mathbf{X}^T \mathbf{y} -
      \mathbf{y}^T \mathbf{y})
   \\ &=
   2 \mathbf{X}^T \mathbf{X} \mathbf{w} - 2 \mathbf{X}^T \mathbf{y}
   \\ &= 0

.. math::

   \therefore
   \mathbf{w}_{ols} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}

This is exactly how the Moore–Penrose inverse is computed, if `\mathbf{X}` has
linearly independent columns, which is the origin of the **no
multi-collinearity** assumption.

An alternative form is:

.. math::

   \mathbf{w}_{ols} &=
   (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T
   (\mathbf{X} \mathbf{w}^* + \mathbf{\epsilon})
   \\ &=
   \mathbf{w}^* + (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{\epsilon}

Zero Mean Error and Unbiased Estimator
--------------------------------------

.. math::

   \mathrm{E} \left[ \mathbf{\epsilon} \right] = \mathbf{0}
   \implies
   \mathrm{E} \left[ \mathbf{w}_{ols} \right] = \mathbf{w}^*

Proof:

.. math::

   \mathrm{E} \left[
     \mathbf{w}_{ols}
   \right] &=
   \mathrm{E} \left[
     \mathbf{w}^* +
     (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{\epsilon}
   \right]
   \\ &=
   \mathbf{w}^* +
   (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T
   \mathrm{E} \left[ \mathbf{\epsilon} \right]
   \\ &=
   \mathbf{w}^* +
   (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{0}
   \\ &=
   \mathbf{w}^*

.. math::

   \tag*{$\blacksquare$}

Homoscedasticity and BLUE
-------------------------

The OLS estimator is the Best Linear Unbiased Estimator (BLUE) if:

.. math::

   \forall i \in \left[ 0, n \right] &:
   \mathrm{E} \left[ \mathbf{\epsilon} \right] = 0,
   \mathrm{Var} \left[ \mathbf{\epsilon} \right] = \sigma^2

   \\

   \forall i \ne j &:
   \mathrm{Cov} \left[ \mathbf{\epsilon} \right] = 0

Proof :cite:p:`medium_ols_` :cite:p:`wiki_gmt_`:

.. math::

   \mathbf{\epsilon} \mathbf{\epsilon}^T &=
   \begin{bmatrix}
     \epsilon_1 \\ \epsilon_2 \\ \vdots \\ \epsilon_n
   \end{bmatrix}
   \cdot
   \begin{bmatrix}
     \epsilon_1 & \epsilon_2 & \cdots & \epsilon_n
   \end{bmatrix}
   \\ &=
   \begin{bmatrix}
     \epsilon_1 \epsilon_1 & \epsilon_1 \epsilon_2 & \cdots &
       \epsilon_1 \epsilon_n
     \\
     \epsilon_2 \epsilon_1 & \epsilon_2 \epsilon_2 & \cdots &
       \epsilon_2 \epsilon_n
     \\
     \vdots & \vdots & \ddots & \vdots
     \\
     \epsilon_n \epsilon_1 & \epsilon_n \epsilon_2 & \cdots &
       \epsilon_n \epsilon_n
   \end{bmatrix}
   \\ &=
   \begin{bmatrix}
     (\epsilon_1 - 0) (\epsilon_1 - 0) & (\epsilon_1 - 0) (\epsilon_2 - 0)
       & \cdots & (\epsilon_1 - 0) (\epsilon_n - 0)
     \\
     (\epsilon_2 - 0) (\epsilon_1 - 0) & (\epsilon_2 - 0) (\epsilon_2 - 0)
       & \cdots & (\epsilon_2 - 0) (\epsilon_n - 0)
     \\
     \vdots & \vdots & \ddots & \vdots
     \\
     (\epsilon_n - 0) (\epsilon_1 - 0) & (\epsilon_n - 0) (\epsilon_2 - 0)
       & \cdots & (\epsilon_n - 0) (\epsilon_n - 0)
   \end{bmatrix}

.. math::

   \therefore
   \mathrm{E} \left[
     \mathbf{\epsilon} \mathbf{\epsilon}^T
   \right] &=
   \begin{bmatrix}
     \mathrm{E} \left[
       (\epsilon_1 - 0) (\epsilon_1 - 0)
     \right] &
     \mathrm{E} \left[
       (\epsilon_1 - 0) (\epsilon_2 - 0)
     \right] &
     \cdots &
     \mathrm{E} \left[
       (\epsilon_1 - 0) (\epsilon_n - 0)
     \right]
     \\
     \mathrm{E} \left[
       (\epsilon_2 - 0) (\epsilon_1 - 0)
     \right] &
     \mathrm{E} \left[
       (\epsilon_2 - 0) (\epsilon_2 - 0)
     \right] &
     \cdots &
     \mathrm{E} \left[
       (\epsilon_2 - 0) (\epsilon_n - 0)
     \right]
     \\
     \vdots & \vdots & \ddots & \vdots
     \\
     \mathrm{E} \left[
       (\epsilon_n - 0) (\epsilon_1 - 0)
     \right] &
     \mathrm{E} \left[
       (\epsilon_n - 0) (\epsilon_2 - 0)
     \right] &
     \cdots &
     \mathrm{E} \left[
       (\epsilon_n - 0) (\epsilon_n - 0)
     \right]
   \end{bmatrix}
   \\ &=
   \begin{bmatrix}
     \mathrm{Var} \left[ \epsilon_1 \right] &
     \mathrm{Cov} \left[ \epsilon_1, \epsilon_2 \right] &
     \cdots &
     \mathrm{Cov} \left[ \epsilon_1, \epsilon_n \right]
     \\
     \mathrm{Cov} \left[ \epsilon_2, \epsilon_1 \right] &
     \mathrm{Var} \left[ \epsilon_2 \right] &
     \cdots &
     \mathrm{Cov} \left[ \epsilon_2, \epsilon_n \right]
     \\
     \vdots & \vdots & \ddots & \vdots
     \\
     \mathrm{Cov} \left[ \epsilon_n, \epsilon_1 \right] &
     \mathrm{Cov} \left[ \epsilon_n, \epsilon_2 \right] &
     \cdots &
     \mathrm{Var} \left[ \epsilon_n \right]
   \end{bmatrix}
   \\ &=
   \sigma^2 \mathbf{I}

.. math::

   \therefore
   \mathrm{Var} \left[ \mathbf{w}_{ols} \right] &=
   \mathrm{E} \left[
     (\mathbf{w}_{ols} - \mathrm{E} \left[
       \mathbf{w}_{ols}
     \right])
     (\mathbf{w}_{ols} - \mathrm{E} \left[
       \mathbf{w}_{ols}
     \right])^T
   \right]
   \\ &=
   \mathrm{E} \left[
     ((\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{\epsilon})
     ((\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{\epsilon})^T
   \right]
   \\ &=
   \mathrm{E} \left[
     (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{\epsilon}
     \mathbf{\epsilon}^T \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1}
   \right]
   \\ &=
     (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T
     \mathrm{E} \left[
       \mathbf{\epsilon} \mathbf{\epsilon}^T
     \right]
     \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1}
   \\ &=
     \sigma^2 (\mathbf{X}^T \mathbf{X})^{-1}
     \mathbf{X}^T \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1}
   \\ &=
     \sigma^2 (\mathbf{X}^T \mathbf{X})^{-1}

Let `\tilde{\mathbf{w}} = \tilde{\mathbf{C}} \mathbf{y}` be another **unbiased
linear estimator** of `\mathbf{w}^*` with
`\tilde{\mathbf{C}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T + \mathbf{D}`
where `\mathbf{D}` is a `p \times n` non-zero matrix.

.. math::

   \mathrm{E} \left[ \tilde{\mathbf{w}} \right] &=
   \mathrm{E} \left[ \tilde{\mathbf{C}} \mathbf{y} \right]
   \\ &=
   \mathrm{E} \left[
     ((\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T + \mathbf{D})
     (\mathbf{X} \mathbf{w}^* + \mathbf{\epsilon})
   \right]
   \\ &=
   ((\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T + \mathbf{D})
   \mathbf{X} \mathbf{w}^* +
   ((\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T + \mathbf{D})
   \mathrm{E} \left[ \mathbf{\epsilon} \right]
   \\ &=
   ((\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T + \mathbf{D})
   \mathbf{X} \mathbf{w}^*
   \\ &=
   \mathbf{w}^* + \mathbf{D} \mathbf{X} \mathbf{w}^*

Since `\tilde{\mathbf{w}}` is unbiased:

.. math::

   \therefore
   \mathbf{D} \mathbf{X} = 0

.. math::

   \therefore
   \mathrm{Var} \left[
     \tilde{\mathbf{w}}
   \right] &=
   \mathrm{Var} \left[
     \tilde{\mathbf{C}} \mathbf{y}
   \right]
   \\ &=
   \tilde{\mathbf{C}} \mathrm{Var} \left[ \mathbf{y} \right]
   \tilde{\mathbf{C}}^T
   \\ &=
   \sigma^2 \tilde{\mathbf{C}} \tilde{\mathbf{C}}^T
   \\ &=
   \sigma^2
   ((\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T + \mathbf{D})
   ((\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T + \mathbf{D})^T
   \\ &=
   \sigma^2
   ((\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T + \mathbf{D})
   (\mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1} + \mathbf{D}^T)
   \\ &=
   \sigma^2
   ((\mathbf{X}^T \mathbf{X})^{-1} +
    (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{D}^T +
    \mathbf{D} \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1} +
    \mathbf{D} \mathbf{D}^T)
   \\ &=
   \sigma^2 (\mathbf{X}^T \mathbf{X})^{-1} +
   \sigma^2 (\mathbf{X}^T \mathbf{X})^{-1} (\mathbf{D} \mathbf{X})^T +
   \sigma^2 \mathbf{D} \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1} +
   \sigma^2 \mathbf{D} \mathbf{D}^T

.. math::

   \because
   \mathbf{D} \mathbf{X} = 0

.. math::

   \therefore
   \mathrm{Var} \left[
     \tilde{\mathbf{w}}
   \right] &=
   \sigma^2 (\mathbf{X}^T \mathbf{X})^{-1} +
   \sigma^2 \mathbf{D} \mathbf{D}^T
   \\ &=
   \mathrm{Var} \left[ \mathbf{w}_{ols} \right] +
   \sigma^2 \mathbf{D} \mathbf{D}^T

Since `\mathbf{D} \mathbf{D}^T` is positive semidefinite matrix:

.. math::

   \because
   \mathbf{D} \mathbf{D}^T \text{ is positive semidefinite}

.. math::

   \therefore
   \mathrm{Var} \left[ \tilde{\mathbf{w}} \right] >
   \mathrm{Var} \left[ \mathbf{w}_{ols} \right]

.. math::

   \tag*{$\blacksquare$}

Normally Distributed Error and MLE
----------------------------------

The OLS is mathematically equivalent to Maximum Likelihood Estimation
if the error term `\epsilon_1, \ldots, \epsilon_n` are identically and
independently distributed from a normal distribution of zero mean.

Proof:

.. math::

   \because
   \epsilon_i =
   y_i - \hat{y}_i =
   y_i - \mathbf{x}_i \mathbf{w}
   \sim
   N(\mu, 0)

.. math::

   \therefore
   \mathcal{L} (\mathbf{w} \mid \mathbf{X}) &=
   \prod_{i=1}^{n} \frac{1}{\sigma \sqrt{2 \pi}}
   e^{-\frac{(y_i - \mathbf{x}_i \mathbf{w})^2}{2 \sigma^2}}
   \\ &=
   (\frac{1}{\sigma \sqrt{2 \pi}})^n
   \prod_{i=1}^{n} 
   e^{-\frac{(y_i - \mathbf{x}_i \mathbf{w})^2}{2 \sigma^2}}
   \\ &=
   (2 \pi \sigma^2)^{-\frac{n}{2}}
   \prod_{i=1}^{n} 
   e^{-\frac{(y_i - \mathbf{x}_i \mathbf{w})^2}{2 \sigma^2}}

.. math::

   \therefore
   \ln \mathcal{L} (\mathbf{w} \mid \mathbf{X}) &=
   -\frac{n}{2} \ln (2 \pi \sigma^2) +
   \sum_{i=1}^n
   -\frac{(y_i - \mathbf{x}_i \mathbf{w})^2}{2 \sigma^2}
   \\ &=
   -\frac{n}{2} \ln (2 \pi \sigma^2) - \frac{1}{2 \sigma^2}
   \sum_{i=1}^n
   (y_i - \mathbf{x}_i \mathbf{w})^2
   \\ &=
   -\frac{n}{2} \ln (2 \pi \sigma^2) - \frac{1}{2 \sigma^2}
   (\mathbf{y} - \mathbf{X} \mathbf{w})^T (\mathbf{y} - \mathbf{X} \mathbf{w})

To minimize `\ln \mathcal{L}`:

.. math::

   \nabla_{\mathbf{w}} \ln \mathcal{L} (\mathbf{w} \mid \mathbf{X}) = 0
   \\
   \implies
   (\mathbf{y} - \mathbf{X} \mathbf{w})^T
   (\mathbf{y} - \mathbf{X} \mathbf{w}) = 0

.. math::

   \therefore
   \mathbf{w}_{mle} =
   (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} =
   \mathbf{w}_{ols}

.. math::

   \tag*{$\blacksquare$}

Notes
=====

.. [#f01] `\mathbf{X}_{i1} = 1` for all `i \in [1, n]`

Back to :doc:`index`.

.. disqus::
