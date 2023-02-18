#############
Bayes Theorem
#############

- What does likelihood mean?

- how is "likelihood" different than "probability"?

.. default-role:: math

.. math::

   \DeclareMathOperator{\diff}{d}

Likelihood vs. Joint Distributions
==================================

For `n` jointly random variables `X_1, \ldots, X_n` the joint PDF is defined
as:

.. math::

   f_{X_1 \ldots X_n} (x_1, \ldots, x_n) =
   f_{X_1} (x_1 \mid x_2, \ldots, x_n)
   f_{X_2} (x_2 \mid x_3, \ldots, x_n)
   \cdots
   f_{X_n} (x_n)

where `f_{X_i}` is the marginal PMF / PDF of random variable `X_i`.

In the case of discrete distributions, likelihood is a synonym for the joint
probability of your data.
In the case of continuous distribution, likelihood refers to the joint
probability density of your data.
It is defined, however, as a function of the **model parameters** (`\theta`),
rather than the data themselves (`\mathbf{x}`).

.. math::

   \mathcal{L}(\theta \mid \mathbf{x}) =
   f_{X_1} (x_1 \mid x_2, \ldots, x_n, \theta)
   f_{X_2} (x_2 \mid x_3, \ldots, x_n, \theta)
   \cdots
   f_{X_n} (x_n \mid \theta)

Particularly, when `X_1, X_2, \ldots, X_n` are independent:

.. math::

   \mathcal{L}(\theta \mid \mathbf{x}) =
   \prod_{i=1}^{n} f_{X_i} (x_i \mid \theta)

More particularly, when `X_1, X_2, \ldots, X_n` are independently and
identically distributed (i.i.d.):

.. math::

   \mathcal{L}(\theta \mid \mathbf{x}) =
   \prod_{i=1}^{n} f_{X} (x_i \mid \theta)

This is the core assumption of naive Bayes classifier, where the random
variables `X_1, X_2, \ldots, X_n` are interpreted as `n` mutually independent
features.

Bayes Theorem
=============

The Bayes theorem is to calculate the posterior probability (density) function
of variable `\theta`.

The probability density function form (`\theta` is continuous):

.. math::

   f(\theta \mid \mathbf{x}) =
     \frac{\mathcal{L}(\theta \mid \mathbf{x}) \cdot f(\theta)}
     {\int_{-\infty}^{+\infty}
       L(\theta \mid \mathbf{x}) \cdot f(\theta) \diff \theta}

The probability of `\theta = \theta_i` (`\theta` is discrete):

.. math::

   p_{\Theta} (\theta_i \mid \mathbf{x}) =
     \frac{\mathcal{L}(\theta \mid \mathbf{x}) \cdot p_{\Theta} (\theta_i)}
     {\sum_{i=1}^n
       \mathcal{L}(\theta \mid \mathbf{x}) \cdot p_{\Theta} (\theta_i)}

Back to :doc:`index`.

.. disqus::
