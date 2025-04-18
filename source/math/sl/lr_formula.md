---
title: "Linear Regression: Formula Derivation"
---

# Linear Regression: Formula Derivation

## Originally Derived Formula

Suppose variable $x$ and $y$ follows a straight-line relationship, which
can be described as:

$$y = \beta_0^* + \beta_1^* x + \epsilon$$

where zero-mean random variable $\epsilon$ has a constant variance:

$$
\mathrm{E} \left[ \epsilon \right] &= 0
\\
\mathrm{Var} \left[ \epsilon \right] &= \sigma_{\epsilon}^2
$$

We use the hypothesis model to get the prediction $\hat{y}$:

$$\hat{y} = \beta_0 + \beta_1 x$$

We aim to find the slope ($\beta_1$) that minimizes the residual sum of
squares (**RSS**):

$$
\mathrm{RSS} &=
  \sum_{i=1}^n (y_i - \hat{y}_i)^2
\\ &=
  \sum_{i=1}^n (y_i - \beta_1 x_i - \beta_0)^2
$$

where $\{ (x_i, y_i) \}_{i=1}^n$ is the dataset.

To find the minimum value of $\mathrm{RSS}$, we take the derivative
w.r.t $\beta_0$ and $\beta_1$ and set to $0$:

$$
\begin{cases}
\frac{\partial}{\partial \beta_0} \mathrm{RSS} =
\sum_{i=1}^n -2 (y_i - \beta_1 x_i - \beta_0) = 0
\\
\frac{\partial}{\partial \beta_1} \mathrm{RSS} =
\sum_{i=1}^n 2 (y_i - \beta_1 x_i - \beta_0) (-x_i) = 0
\end{cases}
$$

Find the value of $\beta_0$:

$$
0 &=
\sum_{i=1}^n -2 (y_i - \beta_1 x_i - \beta_0)
\\ &=
\sum_{i=1}^n (y_i - \beta_1 x_i - \beta_0)
\\ &=
\sum_{i=1}^n y_i - \sum_{i=1}^n \beta_1 x_i - \sum_{i=1}^n \beta_0
\\ &=
n \bar{y} - n \beta_1 \bar{x} - n \beta_0
\\ &=
\bar{y} - \beta_1 \bar{x} - \beta_0
$$

$$
\therefore
\beta_0 = \bar{y} - \beta_1 \bar{x}
$$

$$\tag*{$\blacksquare$}$$

Find the value of $\beta_1$:

$$
0 &=
\sum_{i=1}^n (- x_i y_i + \beta_1 x_i^2 + \beta_0 x_i)
\\ &=
\sum_{i=1}^n (- x_i y_i + \beta_1 x_i^2 + \bar{y} x_i - \beta_1 \bar{x} x_i)
$$

$$
\therefore
\beta_1 &= \frac{\sum_{i=1}^n (x_i y_i - \bar{y} x_i)}
  {\sum_{i=1}^n (x_i^2 - \bar{x} x_i)}
\\ &=
\frac{\sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i}
  {\sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i}
\\ &=
\frac{ \sum_{i=1}^n x_i y_i - n \bar{x} \bar{y} }
  { \sum_{i=1}^n x_i^2 - n \bar{x}^2 }
$$

which is the formula for the slope of the linear regression line.

$$\tag*{$\blacksquare$}$$

## Factored Form

Starting with the formula:

$$
\beta_1 = \frac{\sum_{i=1}^n x_i y_i - n \bar{y} \bar{x}}
{\sum_{i=1}^n x_i^2 - n \bar{x}^2}
$$

Note that:

$$
\sum_{i=1}^n x_i y_i - n \bar{y} \bar{x} &=
\sum_{i=1}^n (x_i - \bar{x} + \bar{x})(y_i - \bar{y} + \bar{y}) -
  n \bar{y} \bar{x}
\\ &=
\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) +
  \bar{y} \sum_{i=1}^n (x_i - \bar{x}) +
  \bar{x} \sum_{i=1}^n (y_i - \bar{y}) +
  n \bar{x} \bar{y} - n \bar{x} \bar{y}
\\ &=
\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
$$

and that:

$$
\sum_{i=1}^n x_i^2 - n \bar{x}^2 &=
\sum_{i=1}^n (x_i - \bar{x} + \bar{x})^2 - n \bar{x}^2
\\ &=
\sum_{i=1}^n (x_i - \bar{x})^2 +
  2\bar{x} \sum_{i=1}^n (x_i - \bar{x}) +
  n \bar{x}^2 - n \bar{x}^2
\\ &=
\sum_{i=1}^n (x_i - \bar{x})^2
$$

$$
\therefore
\beta_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}
  {\sum_{i=1}^n (x_i - \bar{x})^2}
$$

## Slope Weighted Average Form

Starting with the formula:

$$
\beta_1 &=
  \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}
    {\sum_{i=1}^n (x_i - \bar{x})^2}
  \\ &=
  \frac{\sum_{i=1}^n (x_i - \bar{x})^2
        \frac{y_i - \bar{y}}{x_i - \bar{x}}}
    {\sum_{i=1}^n (x_i - \bar{x})^2}
  \\ &=
  \sum_{i=1}^n
    \frac{(x_i - \bar{x})^2}{\sum_{i=1}^n (x_i - \bar{x})^2}
    \frac{y_i - \bar{y}}{x_i - \bar{x}}
$$

This is also the reason why points may have a great influence on the
coefficient if they are far from the mean value.{cite}`wiki_slr_`

## Correlation Coefficient Form

Starting with the formula :

$$
\beta_1 &= \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}
  {\sum_{i=1}^n (x_i - \bar{x})^2}
\\ &=
\frac{\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}
  {\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2}
\\ &=
\frac{\mathrm{Cov} (x, y)}{\sigma_x^2}
$$

Note the formula of correlation coefficient:

$$r = \frac{\mathrm{Cov} (x, y)}{\sigma_x \sigma_y}$$

$$\beta_1 = r \frac{\sigma_y}{\sigma_x}$$

where $\sigma_x$ and $\sigma_y$ are the standard deviation of $x$ and
$y$ respectively.{cite}`wiki_slr_`

## Expectation and Variance

Starting with the formula:

$$
\beta_1 &=
  \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}
    {\sum_{i=1}^n (x_i - \bar{x})^2}
  \\ &=
  \frac{
    \sum_{i=1}^n
    (x_i - \bar{x})
    (\beta_0^* + \beta_1^* x_i + \epsilon - \beta_0^* - \beta_1^* \bar{x})}
    {\sum_{i=1}^n (x_i - \bar{x})^2}
  \\ &=
  \frac{
    \sum_{i=1}^n
    (x_i - \bar{x})
    (\beta_1^* x_i - \beta_1^* \bar{x} + \epsilon)}
    {\sum_{i=1}^n (x_i - \bar{x})^2}
$$

Now we can calculate the expectation and variance of the slope with
properties of these statistics:

$$
\mathrm{E} \left[ \beta_1 \right] &=
  \frac{
    \sum_{i=1}^n
    (x_i - \bar{x})
    \mathrm{E} \left[ \beta_1^* x_i - \beta_1^* \bar{x} + \epsilon \right]
 }
 {\sum_{i=1}^n (x_i - \bar{x})^2}
\\ &=
  \beta_1^*
  \frac{
    \sum_{i=1}^n
    (x_i - \bar{x})^2
  }
  {\sum_{i=1}^n (x_i - \bar{x})^2}
\\ &=
  \beta_1^*
$$

$$
\mathrm{Var} \left[ \beta_1 \right] &=
  \frac{
    \sum_{i=1}^n
    (x_i - \bar{x})^2
    \mathrm{Var} \left[ \beta_1^* x_i - \beta_1^* \bar{x} + \epsilon \right]
 }
 {(\sum_{i=1}^n (x_i - \bar{x})^2)^2}
\\ &=
  \frac{
    \sum_{i=1}^n
    (x_i - \bar{x})^2
    \mathrm{Var} \left[ \epsilon \right]
 }
 {(\sum_{i=1}^n (x_i - \bar{x})^2)^2}
\\ &=
  \frac{
    \mathrm{Var} \left[ \epsilon \right]
 }
 {\sum_{i=1}^n (x_i - \bar{x})^2}
$$

where $\mathrm{Var} \left[ \epsilon \right]$ can be estimated with
residual:

$$
\mathrm{Var} \left[ \epsilon \right] =
  \frac{1}{n-2} \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

which makes it equal to slope\'s standard error of
$\mathrm{SE} \left[ \beta_1 \right]$.

---

Back to {doc}`index`.

```{disqus}

```
