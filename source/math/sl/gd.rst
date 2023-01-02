################
Gradient Descent
################

.. default-role:: math

Stochastic vs. Batch
====================

..
    TODO: revision on monte carlo

Suppose observation

.. math::

   \mathbf{x}, y

where

.. math::

   \mathbf{x} =
     ( x_1,
       x_2,
       \ldots,
       x_p
     )^T

The underlying join probability density funtion is
`f_{X, Y}(\mathbf{x}, y)`.

Suppose we have a model whose parameter vecter is denoted as `\mathbf{\theta}`.
Its loss of a specific observation can be defined as:

.. math::

   L_{\theta}(\hat{y}(\mathbf{x}), y)

For example, `l` of ordinary least squares is:

.. math::

   L_{\theta}(\hat{y}(\mathbf{x}), y) = \frac{1}{2} (y - \hat{y})^2
     = \frac{1}{2} (y - \mathbf{\theta}^T \mathbf{x})^2

is an observation of `p` features and one label.

The goal of optimization is to minimize the **expected loss**:

.. math::

   E [ L_{\theta} (\hat{y}(\mathbf{x}), y) ] =
     \int_{x} \int_{y} f_{X, Y}(\mathbf{x}, y)
     L_{\theta}(\hat{y}(\mathbf{x}), y) \mathrm{d} y \mathrm{d} \mathbf{x}

Thus the parameters can be calculated by submitting the gradient iteratively:

.. math::

   \mathbf{\theta}^{(t+1)} =
     \mathbf{\theta}^{(t)} - \eta \cdot
       \nabla_{\theta} E [ L_{\theta} (\hat{y}(\mathbf{x}), y) ]

The original loss function `L(\mathbf{\theta})` is hard to calculate as the
joint PDF `f_{X, Y}(\mathbf{x}, y)` is unknown.
However, `L(\mathbf{\theta})` can be simulated with Monte Carlo integration.
Suppose there is a dataset of size `N`:

.. math::

   D = \{ (\mathbf{x}^{(1)}, y^{(1)}), \ldots, (\mathbf{x}^{(N)}, y^{(N)})\}

.. math::

   E [ L_{\theta} (\hat{y}(\mathbf{x}), y) ] =
     \frac{1}{|\Omega|} \sum_{i \in \Omega} L_{\theta} (\hat{y}(\mathbf{x}^{(i)}), y^{(i)})

where

.. math::

   \Omega \subset D

.. math::

   \therefore
   \mathbf{W}_{t+1} & =
     \mathbf{W}_{t+1} -
     \eta \cdot
       \nabla_{\theta} \frac{1}{|\Omega|} \sum_{i \in \Omega}
       L_{\theta} (\hat{y}(\mathbf{x}^{(i)}), y^{(i)})
     \\ & =
     \mathbf{W}_{t+1} -
     \eta \cdot \frac{1}{|\Omega|} \sum_{i \in \Omega}
       \nabla_{\theta} L_{\theta} (\hat{y}(\mathbf{x}^{(i)}), y^{(i)})


- When `|\Omega| = N`: batch gradient descent

- When `|\Omega| = 1`: stochastic gradient descent (SGD)

- When `1 < |\Omega| < N`: mini-batch gradient descent

Back to :doc:`index`.

.. disqus::
