---
title: "Linear Regression: Ordinary Least Squares"
---

# Linear Regression: Ordinary Least Squares

## TL;DR

- OLS estimator is unbiased if:
  - No Collinearity
  - $\mathrm{E} \left[ \epsilon_i \right] = 0,$
    $\forall i \in \left[ 1, n \right]$
- OLS estimator is the Best Linear Unbiased Estimator (BLUE) if:
  - No Collinearity
  - $\mathrm{E} \left[ \epsilon_i \right] = 0,$
    $\forall i \in \left[ 1, n \right]$
  - $\mathrm{Var} \left[ \epsilon_i \right] = \sigma^2,$
    $\forall i \in \left[ 1, n \right]$
  - $\mathrm{Cov} \left[ \epsilon_i, \epsilon_j \right] = 0,$
    $\forall i \ne j$
- OLS estimator is equivalent to MLE (generalized linear model) if:
  - No Collinearity
  - $\mathrm{E} \left[ \epsilon_i \right] = 0,$
    $\forall i \in \left[ 1, n \right]$
  - $\mathrm{Var} \left[ \epsilon_i \right] = \sigma^2,$
    $\forall i \in \left[ 1, n \right]$
  - $\mathrm{Cov} \left[ \epsilon_i, \epsilon_j \right] = 0,$
    $\forall i \ne j$
  - random errors are **identically** and **independently** drawn from a
    **normal distribution**.

## Hypothesis

By [previous derivation](#ref-sl-lr-functional) we conclude that the linear
predictor $f : \mathbb{R}^p \mapsto \mathbb{R}$ is a linear functional:

$$
f (x) = x^\top \beta
$$

where $x \in \mathbb{R}^p$ as the input vector, $\beta \in \mathbb{R}^p$ as the
linear coefficients.

We suppose that there is a **underlying non-random unobservable coefficients**
$\beta^{\ast} \in \mathbb{R}^p$ such that for every data point
$\{ x, y \} \in \mathbb{R}^p \times \mathbb{R}$:

$$
y = x^\top \beta^{\ast} + \varepsilon
$$

where $\varepsilon$ is a random error term, which is assumed to be independent
of the input vector $x$.

Also from [previous chapter](#ref-sl-formula-ls), the Ordinary Least Squares
(OLS) solution can be expressed as:

$$
\beta_{\text{ols}} = (X^\top X)^{-1} X^\top y
$$

If **no collinearity** holds i.e. $X^\top X$ is invertible.

$$
\therefore
\beta_{\text{ols}}
&= (X^\top X)^{-1} X^\top (X \beta^{\ast} + \epsilon) \\
&= (X^\top X)^{-1} X^\top X \beta^{\ast} +
   (X^\top X)^{-1} X^\top \epsilon \\
&= \beta^{\ast} + (X^\top X)^{-1} X^\top \epsilon
$$

where $\epsilon$ is the vector of random errors
$\varepsilon_1, \ldots, \varepsilon_n$.

## Zero Mean Error and Unbiased Estimator

$$
\mathrm{E} \left[ \epsilon \right] = 0
\implies
\mathrm{E} \left[ \beta_{\text{ols}} \right] = \beta^{\ast}
$$

Proof:

$$
\mathrm{E} \left[
  \beta_{\text{ols}}
\right]
&= \mathrm{E} \left[
  \beta^{\ast} + (X^\top X)^{-1} X^\top \epsilon
\right] \\
&= \beta^{\ast} + X^\top (X^\top X)^{-1} \mathrm{E} \left[ \epsilon \right] \\
&= \beta^{\ast}
$$

$$\tag*{$\blacksquare$}$$

## Homoscedasticity and BLUE

The OLS estimator is the Best Linear Unbiased Estimator (BLUE) if:

$$
\forall i \in \left[ 0, n \right] &:
\mathrm{E} \left[ \epsilon \right] = 0,
\mathrm{Var} \left[ \epsilon \right] = \sigma^2 \\
\forall i \ne j &:
\mathrm{Cov} \left[ \epsilon \right] = 0
$$

Proof{cite}`medium_ols_` {cite}`wiki_gmt_`:

$$
\epsilon \epsilon^T &=
\begin{bmatrix}
  \varepsilon_1 \\ \varepsilon_2 \\ \vdots \\ \varepsilon_n
\end{bmatrix}
\cdot
\begin{bmatrix}
  \varepsilon_1 & \varepsilon_2 & \cdots & \varepsilon_n
\end{bmatrix} \\
&= \begin{bmatrix}
  \varepsilon_1 \varepsilon_1 & \varepsilon_1 \varepsilon_2 & \cdots &
    \varepsilon_1 \varepsilon_n \\
  \varepsilon_2 \varepsilon_1 & \varepsilon_2 \varepsilon_2 & \cdots &
    \varepsilon_2 \varepsilon_n \\
  \vdots & \vdots & \ddots & \vdots \\
  \varepsilon_n \varepsilon_1 & \varepsilon_n \varepsilon_2 & \cdots &
    \varepsilon_n \varepsilon_n
\end{bmatrix} \\
&= \begin{bmatrix}
  (\varepsilon_1 - 0) (\varepsilon_1 - 0) &
  (\varepsilon_1 - 0) (\varepsilon_2 - 0) & \cdots &
  (\varepsilon_1 - 0) (\varepsilon_n - 0) \\
  (\varepsilon_2 - 0) (\varepsilon_1 - 0) &
  (\varepsilon_2 - 0) (\varepsilon_2 - 0) & \cdots &
  (\varepsilon_2 - 0) (\varepsilon_n - 0) \\
  \vdots & \vdots & \ddots & \vdots \\
  (\varepsilon_n - 0) (\varepsilon_1 - 0) &
  (\varepsilon_n - 0) (\varepsilon_2 - 0) & \cdots &
  (\epsilon_n - 0) (\epsilon_n - 0)
\end{bmatrix}
$$

$$
\therefore
\mathrm{E} \left[
  \epsilon \epsilon^T
\right] &=
\begin{bmatrix}
  \mathrm{E} \left[
    (\varepsilon_1 - 0) (\varepsilon_1 - 0)
  \right] &
  \mathrm{E} \left[
    (\varepsilon_1 - 0) (\varepsilon_2 - 0)
  \right] &
  \cdots &
  \mathrm{E} \left[
    (\varepsilon_1 - 0) (\varepsilon_n - 0)
  \right] \\
  \mathrm{E} \left[
    (\varepsilon_2 - 0) (\varepsilon_1 - 0)
  \right] &
  \mathrm{E} \left[
    (\varepsilon_2 - 0) (\varepsilon_2 - 0)
  \right] &
  \cdots &
  \mathrm{E} \left[
    (\varepsilon_2 - 0) (\varepsilon_n - 0)
  \right] \\
  \vdots & \vdots & \ddots & \vdots \\
  \mathrm{E} \left[
    (\varepsilon_n - 0) (\varepsilon_1 - 0)
  \right] &
  \mathrm{E} \left[
    (\varepsilon_n - 0) (\varepsilon_2 - 0)
  \right] &
  \cdots &
  \mathrm{E} \left[
    (\varepsilon_n - 0) (\varepsilon_n - 0)
  \right]
\end{bmatrix}
\\ &=
\begin{bmatrix}
  \mathrm{Var} \left[ \varepsilon_1 \right] &
  \mathrm{Cov} \left[ \varepsilon_1, \varepsilon_2 \right] &
  \cdots &
  \mathrm{Cov} \left[ \varepsilon_1, \varepsilon_n \right] \\
  \mathrm{Cov} \left[ \varepsilon_2, \varepsilon_1 \right] &
  \mathrm{Var} \left[ \varepsilon_2 \right] &
  \cdots &
  \mathrm{Cov} \left[ \varepsilon_2, \varepsilon_n \right] \\
  \vdots & \vdots & \ddots & \vdots \\
  \mathrm{Cov} \left[ \varepsilon_n, \varepsilon_1 \right] &
  \mathrm{Cov} \left[ \varepsilon_n, \varepsilon_2 \right] &
  \cdots &
  \mathrm{Var} \left[ \varepsilon_n \right]
\end{bmatrix} \\
&= \sigma^2 I
$$

$$
\therefore
\mathrm{Var} \left[ \beta_{\text{ols}} \right]
&= \mathrm{E} \left[
  (\beta_{\text{ols}} - \mathrm{E} \left[ \beta_{\text{ols}} \right])
  (\beta_{\text{ols}} - \mathrm{E} \left[ \beta_{\text{ols}} \right])^T
\right] \\
&= \mathrm{E} \left[
  ((X^\top X)^{-1} X^\top \epsilon)
  ((X^\top X)^{-1} X^\top \epsilon)^T
\right] \\
&= \mathrm{E} \left[
  (X^\top X)^{-1} X^\top \epsilon
  \epsilon^\top X (X^\top X)^{-1}
\right] \\
&= (X^\top X)^{-1} X^\top
  \mathrm{E} \left[
    \epsilon \epsilon^\top
  \right]
  X (X^\top X)^{-1} \\
&= \sigma^2 (X^\top X)^{-1}
  X^\top X (X^\top X)^{-1} \\
&= \sigma^2 (X^\top X)^{-1}
$$

Let $\tilde{\beta} = \tilde{C} y$ be another
**unbiased linear estimator** of $\beta^\ast$ with
$\tilde{C} = (X^\top X)^{-1} X^\top + D$
where $D$ is a $p \times n$ non-zero matrix.

$$
\therefore
\mathrm{E} \left[ \tilde{\beta} \right]
&= \mathrm{E} \left[ \tilde{C} y \right] \\
&= \mathrm{E} \left[
  ((X^\top X)^{-1} X^\top + D)
  (X \beta^\ast + \epsilon)
\right] \\
&= ((X^\top X)^{-1} X^\top + D) X \beta^\ast +
   ((X^\top X)^{-1} X^\top + D)
   \mathrm{E} \left[ \epsilon \right] \\
&= ((X^\top X)^{-1} X^\top + D) X \beta^\ast \\
&= \beta^\ast + D X \beta^\ast
$$

Since $\tilde{\beta}$ is unbiased:

$$
\therefore
D X = 0
$$

$$
\therefore
\mathrm{Var} \left[ \tilde{\beta} \right]
&= \mathrm{Var} \left[ \tilde{C} y \right] \\
&= \tilde{C} \mathrm{Var} \left[ y \right] \tilde{C}^\top \\
&= \sigma^2 \tilde{C} \tilde{C}^T \\
&= \sigma^2 ((X^\top X)^{-1} X^\top + D) ((X^\top X)^{-1} X^\top + D)^T \\
&= \sigma^2 ((X^\top X)^{-1} X^\top + D) (X (X^\top X)^{-1} + D^T) \\
&= \sigma^2 ((X^\top X)^{-1} + (X^\top X)^{-1} X^\top D^\top +
              D X (X^\top X)^{-1} + D D^\top) \\
&= \sigma^2 (X^\top X)^{-1} + \sigma^2 (X^\top X)^{-1} (D X)^\top +
   \sigma^2 D X (X^\top X)^{-1} + \sigma^2 D D^\top
$$

$$
\because
D X = 0
$$

$$
\therefore
\mathrm{Var} \left[ \tilde{\beta} \right]
&= \sigma^2 (X^\top X)^{-1} + \sigma^2 D D^T \\
&= \mathrm{Var} \left[ \beta_{\text{ols}} \right] + \sigma^2 D D^\top
$$

Since $D D^\top$ is positive semidefinite matrix:

$$
\therefore
\mathrm{Var} \left[ \tilde{\beta} \right] >
\mathrm{Var} \left[ \beta_{\text{ols}} \right]
$$

$$\tag*{$\blacksquare$}$$

## Normally Distributed Error and MLE

The OLS is mathematically equivalent to Maximum Likelihood Estimation if
the error term $\varepsilon_1, \ldots, \varepsilon_n$ are identically and
independently distributed from a normal distribution of zero mean.

Proof:

$$
\because
\varepsilon_i =
y_i - \hat{y}_i =
y_i - x_i \beta
\sim
N(\mu, 0)
$$

$$
\therefore
\mathcal{L} (\beta \mid X) &=
\prod_{i=1}^{n} \frac{1}{\sigma \sqrt{2 \pi}}
e^{-\frac{(y_i - x_i \beta)^2}{2 \sigma^2}}
\\ &=
(\frac{1}{\sigma \sqrt{2 \pi}})^n
\prod_{i=1}^{n}
e^{-\frac{(y_i - x_i \beta)^2}{2 \sigma^2}}
\\ &=
(2 \pi \sigma^2)^{-\frac{n}{2}}
\prod_{i=1}^{n}
e^{-\frac{(y_i - x_i \beta)^2}{2 \sigma^2}}
$$

$$
\therefore
\ln \mathcal{L} (\beta \mid X)
&= -\frac{n}{2} \ln (2 \pi \sigma^2) +
   \sum_{i=1}^n -\frac{(y_i - x_i \beta)^2}{2 \sigma^2} \\
&= -\frac{n}{2} \ln (2 \pi \sigma^2) -
   \frac{1}{2 \sigma^2} \sum_{i=1}^n (y_i - x_i \beta)^2 \\
&= -\frac{n}{2} \ln (2 \pi \sigma^2) -
   \frac{1}{2 \sigma^2} (y - X \beta)^\top (y - X \beta)
$$

To minimize $\ln \mathcal{L}$:

$$
\nabla_{\beta} \ln \mathcal{L} (\beta \mid X) = 0
\\
\implies
(y - X \beta)^T
(y - X \beta) = 0
$$

$$
\therefore
\beta_{\text{mle}}
= (X^\top X)^{-1} X^\top y
= \beta_{\text{ols}}
$$

$$\tag*{$\blacksquare$}$$

---

Back to {doc}`index`.

```{disqus}

```
