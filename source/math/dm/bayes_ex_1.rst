##########################
Bayes Example: Biased Coin
##########################

.. default-role:: math

.. math::

   \DeclareMathOperator{\diff}{d}

Consider a Bernoulli trial of flipping a coin with random variable `X`

.. math::
   
   X =
   \begin{cases}
     0 & \text{Tail}
     \\
     1 & \text{Head}
   \end{cases}

Let:

.. math::

   \theta = p_X(1)
   \\
   1 - \theta = p_X(0)

We believe that all values of `\theta` are equally likely, therefore:

.. math::

   \forall
   \theta \in [0, 1]:
   f(\theta) = 1

Since random sample `\mathbf{x}` is independent and identically distributed:

.. math::

   f_X (\mathbf{x} \mid \theta) =
   \prod_{i=1}^{n} p_X (x_i \mid \theta) =
   \theta^{k} (1 - \theta)^{n - k}

where `k` and `n` means `k` heads in `n` trails.
Therefore:

.. math::

   f (\theta \mid \mathbf{x}) =
     \frac{1}{\int_0^{1} \theta^{k} (1 - \theta)^{n - k} \diff \theta}
     \theta^{k} (1 - \theta)^{n - k}

Applying Beta Function
======================

.. math::

   \because
   B(x, y) &=
   \int_0^1 t^{x-1} (1-t)^{y-1} \diff t
   \\ &=
   \frac{(x - 1)! (y - 1)!}{(x + y - 1)!}

.. math::

   \therefore
   f(\theta \mid \mathbf{x}) =
     \frac{1}{B(k+1, n-k+1)}
     \theta^{k} (1 - \theta)^{n - k}

.. math::

   \therefore
   E(\theta) & =
   \int_0^1 \theta f(\theta \mid \mathbf{x}) \diff \theta 
   \\ &=
   \frac{1}{B(k+1, n-k+1)}
   \int_0^1 \theta^{k+1} (1 - \theta)^{n-k} \diff \theta
   \\ &=
   \frac{B(k+2, n-k+1)}{B(k+1, n-k+1)}
   \\ &=
   \frac{k + 1}{n + 2}

Real Values
===========

Suppose we got all heads in 100 trials.
The expected value of head probability is `\frac{101}{102} = 99.02\%`.

Back to :doc:`index`.

.. disqus::
