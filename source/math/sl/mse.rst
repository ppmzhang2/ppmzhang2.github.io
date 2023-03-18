################################
Mean Squared Error Decomposition
################################

.. default-role:: math

TL;DR
=====

.. math::

   \mathrm{MSR} \left[ f \right] &=
   \mathrm{MSE} \left[ f \right] +
   \mathrm{E} \left[ \epsilon^2 \right]
   \\\\
   \mathrm{MSE} \left[ f \right] &=
     \mathrm{Var} \left[ f \right] +
     \mathrm{Bias}^2 \left[ f \right]

Derivation
==========

Problem Definition
------------------

Suppose predictor `x` and response `y` follows a true relationship `f^*`, which
can be described as:

.. math::

   y = f^* (x) + \epsilon

where zero-mean random variable `\epsilon` has a constant variance:

.. math::

   \mathrm{E} \left[ \epsilon \right] &= 0
   \\
   \mathrm{Var} \left[ \epsilon \right] &= \sigma_{\epsilon}^2

We use the hypothesis model `f` to get the prediction `\hat{y}`:

.. math::

   \hat{y} = f(x)

Now the formulas can be represented as follows:

.. math::

   \mathrm{Var} \left[ f \right] &=
     \mathrm{E} \left[ (f (x) - \mathrm{E} \left[ f(x) \right])^2 \right]
     \\ &=
     \mathrm{E} \left[
       f^2 (x) - 2 f(x) \mathrm{E} \left[ f(x) \right] +
       \mathrm{E}^2 \left[ f(x) \right]
     \right]
     \\ &=
     \mathrm{E} \left[ f^2 (x) \right] -
     2 \mathrm{E} \left[ f(x) \mathrm{E} \left[ f(x) \right] \right] +
     \mathrm{E}^2 \left[ f (x) \right]
     \\ &=
     \mathrm{E} \left[ f^2 (x) \right] -
     \mathrm{E}^2 \left[ f (x) \right]
   \\\\
   \mathrm{Bias} \left[ f \right] &=
     \mathrm{E} \left[ f(x) - f^* (x) \right]
     \\ &=
     \mathrm{E} \left[ f(x) \right] - f^* (x)

Residual vs. Error vs. Noise
----------------------------

Random Noise:

.. math::

   \epsilon

Model `f` prediction error:

.. math::

   e = f^* (x) - f (x)

Residual:

.. math::

   \hat{\epsilon} &=
   y - \hat{y}
   \\ &=
   f^* (x) - f (x) + \epsilon
   \\ &=
   e + \epsilon

Mean Squared Residual (MSR):

.. math::

   \mathrm{MSR} \left[ f \right] &=
   \mathrm{E} \left[ (y - \hat{y})^2 \right]
   \\ &=
   \mathrm{E} \left[ (f^* (x) + \epsilon - f(x))^2 \right]
   \\ &=
   \mathrm{E} \left[ (e + \epsilon)^2 \right]

Mean Squared Error (MSE):

.. math::

   \mathrm{MSE} \left[ f \right] &=
   \mathrm{E} \left[ (f^* (x) - f(x))^2 \right]
   \\ &=
   \mathrm{E} \left[ e^2 \right]

MSR Decomposition
-----------------

The MSR equals the MSE plus an irreducible noise term if the model error and
the noise are independent:

.. math::

   \mathrm{Cov} \left[ e, \epsilon \right] = 0
   \implies
   \mathrm{MSR} \left[ f \right] =
   \mathrm{MSE} \left[ f \right] +
   \mathrm{E} \left[ \epsilon^2 \right]

**Proof**:

.. math::

   \mathrm{MSR} \left[ f \right] &=
   \mathrm{E} \left[
     (e + \epsilon)^2
   \right]
   \\ &=
   \mathrm{E} \left[
     e^2 + 2 \epsilon e + \epsilon^2
   \right]
   \\ &=
   \mathrm{E} \left[ e^2 \right] +
   2 \mathrm{E} \left[ e \epsilon \right] +
   \mathrm{E} \left[ \epsilon^2 \right]

.. math::

   & \because
   \mathrm{Cov} \left[ e, \epsilon \right] = 0
   \\
   & \therefore
   \mathrm{E} \left[ e \epsilon \right] =
   \mathrm{E} \left[ e \right] \mathrm{E} \left[ \epsilon \right] = 0

.. math::

   \therefore
   \mathrm{MSR} \left[ f \right] =
   \mathrm{MSE} \left[ f \right] +
   \mathrm{E} \left[ \epsilon^2 \right]

.. math::

   \tag*{$\blacksquare$}

MSE Decomposition
-----------------

The MSE equals variance plus squared bias:

.. math::

   \mathrm{MSE} \left[ f \right] =
     \mathrm{Var} \left[ f \right] +
     \mathrm{Bias}^2 \left[ f \right]

**Proof**:

.. math::

   \mathrm{Var} \left[ f \right] +
   \mathrm{Bias}^2 \left[ f \right] &=
     \mathrm{E} \left[ f^2 (x) \right] -
     \mathrm{E}^2 \left[ f (x) \right] +
     (\mathrm{E} \left[ f(x) \right] - f^* (x))^2
   \\ &=
     \mathrm{E} \left[ f^2 (x) \right] -
     2 f^* (x) \mathrm{E} \left[ f(x) \right] +
     (f^*)^2 (x)
   \\ &=
     \mathrm{E} \left[
       f^2 (x) - 2 f^* (x) f (x) + (f^*)^2 (x)
     \right]
   \\ &=
     \mathrm{E} \left[ (f (x) - f^* (x))^2 \right]
   \\ &=
     \mathrm{MSE} \left[ f \right]

.. math::

   \tag*{$\blacksquare$}

Comments
========

If **noise term is independent of the model prediction error term**:

.. math::

   \mathrm{MSR} \left[ f \right] =
     \mathrm{Var} \left[ f \right] +
     \mathrm{Bias}^2 \left[ f \right] +
     \mathrm{E} \left[ \epsilon^2 \right]

Specifically, for **unbiased** model `f` (e.g. the OLS estimator):

.. math::

   \mathrm{MSR} \left[ f \right] =
     \mathrm{Var} \left[ f \right] +
     \mathrm{E} \left[ \epsilon^2 \right]

which means the squared residual term can evaluate model performance, i.e.
calculate the variance cannot be explained by the model.

Back to :doc:`index`.

.. disqus::
