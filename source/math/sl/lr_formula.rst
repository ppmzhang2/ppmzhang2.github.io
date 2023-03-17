#####################################
Linear Regression: Formula Derivation
#####################################

.. default-role:: math

Simple Linear Regression Formula
================================

Suppose variable `x` and `y` follows a straight-line relationship, which can be
described as:

.. math::

   y = \beta_0 + \beta_1 x

We aim to find the slope (`\beta_1`) that minimizes the residual sum of
squares (**RSS**):

.. math::

   \mathrm{RSS} =
   \sum_{i=1}^n (y_i - \beta_1 x_i - \beta_0)^2

where `\{ (x_i, y_i) \}_{i=1}^n` is the dataset.

To find the minimum value of `\mathrm{RSS}`, we take the derivative
w.r.t `\beta_0` and `\beta_1` and set to `0`:

.. math::

   \begin{cases}
   \frac{\partial}{\partial \beta_0} \mathrm{RSS} =
   \sum_{i=1}^n -2 (y_i - \beta_1 x_i - \beta_0) = 0
   \\
   \frac{\partial}{\partial \beta_1} \mathrm{RSS} =
   \sum_{i=1}^n 2 (y_i - \beta_1 x_i - \beta_0) (-x_i) = 0
   \end{cases}

Find the value of `\beta_0`:

.. math::

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

.. math::

   \therefore
   \beta_0 = \bar{y} - \beta_1 \bar{x}

.. math::

   \tag*{$\blacksquare$}

Find the value of `\beta_1`:

.. math::

   0 &=
   \sum_{i=1}^n (- x_i y_i + \beta_1 x_i^2 + \beta_0 x_i)
   \\ &=
   \sum_{i=1}^n (- x_i y_i + \beta_1 x_i^2 + \bar{y} x_i - \beta_1 \bar{x} x_i)

.. math::

   \therefore
   \beta_1 &= \frac{\sum_{i=1}^n (x_i y_i - \bar{y} x_i)}
     {\sum_{i=1}^n (x_i^2 - \bar{x} x_i)}
   \\ &=
   \frac{\sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i}
     {\sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i}
   \\ &=
   \frac{ \sum_{i=1}^n x_i y_i - n \bar{x} \bar{y} }
     { \sum_{i=1}^n x_i^2 - n \bar{x}^2 }

which is the formula for the slope of the linear regression line.

.. math::

   \tag*{$\blacksquare$}

Another Form
============

Starting with the formula:

.. math::

   \beta_1 = \frac{\sum_{i=1}^n x_i y_i - n \bar{y} \bar{x}}
   {\sum_{i=1}^n x_i^2 - n \bar{x}^2}

Note that:

.. math::

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


and that:

.. math::

   \sum_{i=1}^n x_i^2 - n \bar{x}^2 &=
   \sum_{i=1}^n (x_i - \bar{x} + \bar{x})^2 - n \bar{x}^2
   \\ &=
   \sum_{i=1}^n (x_i - \bar{x})^2 +
     2\bar{x} \sum_{i=1}^n (x_i - \bar{x}) +
     n \bar{x}^2 - n \bar{x}^2
   \\ &=
   \sum_{i=1}^n (x_i - \bar{x})^2

.. math::

   \therefore
   \beta_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}
     {\sum_{i=1}^n (x_i - \bar{x})^2}

.. math::

   \tag*{$\blacksquare$}

Yet Another Form
================

Starting with the formula :cite:p:`wiki_slr_`:

.. math::

   \beta_1 &= \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}
     {\sum_{i=1}^n (x_i - \bar{x})^2}
   \\ &=
   \frac{\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}
     {\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2}
   \\ &=
   \frac{\mathrm{Cov} (x, y)}{\sigma_x^2}

Note the formula of correlation coefficient:

.. math::

   r = \frac{\mathrm{Cov} (x, y)}{\sigma_x \sigma_y}

.. math::

   \beta_1 = r \frac{\sigma_y}{\sigma_x}

where `\sigma_x` and `\sigma_y` are the standard deviation of `x` and `y`
respectively.

.. math::

   \tag*{$\blacksquare$}

Back to :doc:`index`.

.. disqus::
