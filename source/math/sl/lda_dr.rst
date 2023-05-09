#############################
LDA: Dimensionality Reduction
#############################

Linear Discriminant Analysis (LDA) is widely considered as a dimensionality
reduction technique with a goal of finding a linear projection
:math:`\mathbf{w}` that maximizes the ratio of between-class variance to
within-class variance.

.. default-role:: math

Within / Between Class Variance
===============================

Suppose we have a :math:`p`-dimensional dataset
:math:`\mathcal{D} = \{\mathbf{x}_i\}_{i=1}^N` with :math:`N` samples and
:math:`K` classes.
The mean vector of each class :math:`\mathbf{\mu}_k` is defined as:

.. math::

   \mathbf{\mu}_k =
   \frac{1}{N_k} \sum_{\mathbf{x} \in \mathcal{D}_k} \mathbf{x}

where :math:`N_k` is the number of samples in class :math:`k` and
:math:`\mathcal{D}_k` is the set of samples in class :math:`k`.

The within-class scatter matrix for class :math:`k` is defined as:

.. math::

   \mathbf{S}_{W_k} =
   \sum_{\mathbf{x} \in \mathcal{D}_k}
   (\mathbf{x} - \mathbf{\mu}_k) (\mathbf{x} - \mathbf{\mu}_k)^T

The within-class scatter matrix for the entire dataset is defined as:

.. math::

   \mathbf{S}_W = \sum_{k=1}^K \mathbf{S}_{W_k}

The between-class scatter matrix is defined as:

.. math::

   \mathbf{S}_B =
   \sum_{k=1}^K
   N_k (\mathbf{\mu}_k - \mathbf{\mu}) (\mathbf{\mu}_k - \mathbf{\mu})^T

where :math:`\mathbf{\mu}` is the mean vector of the entire dataset:

.. math::

   \mathbf{\mu} = \frac{1}{N} \sum_{\mathbf{x} \in \mathcal{D}} \mathbf{x}

Optimal Projection
==================

Suppose the optimal projection is :math:`\mathbf{w}`.
The original dataset can be projected onto :math:`\mathbf{w}` to obtain a
one-dimensional dataset :math:`\mathcal{D}' = \{y_i\}_{i=1}^N` where
:math:`y_i = \mathbf{w}^T \mathbf{x}_i`.

The projected mean of each class :math:`\mu_k'` is defined as:

.. math::

   \mu_k' &= \frac{1}{N_k} \sum_{y \in \mathcal{D}'_k} y
   \\ &=
   \frac{1}{N_k} \sum_{\mathbf{x} \in \mathcal{D}_k} \mathbf{w}^T \mathbf{x}
   \\ &=
   \mathbf{w}^T \mathbf{\mu}_k

The projected mean of the entire projected dataset is defined as:

.. math::

   \mu' &= \frac{1}{N} \sum_{y \in \mathcal{D}'} y
   \\ &=
   \frac{1}{N} \sum_{\mathbf{x} \in \mathcal{D}} \mathbf{w}^T \mathbf{x}
   \\ &=
   \mathbf{w}^T \mathbf{\mu}

The within-class scatter matrix for the projected dataset is defined as:

.. math::

   \mathbf{S}'_{W} &=
   \sum_{k=1}^K \sum_{y \in \mathcal{D}'_k} (y - \mu_k')^2
   \\ &=
   \sum_{k=1}^K \sum_{y \in \mathcal{D}'_k}
   (y - \mu_k') (y - \mu_k')^T
   \\ &=
   \sum_{k=1}^K \sum_{\mathbf{x} \in \mathcal{D}_k}
   (\mathbf{w}^T \mathbf{x} - \mathbf{w}^T \mathbf{\mu}_k)
   (\mathbf{w}^T \mathbf{x} - \mathbf{w}^T \mathbf{\mu}_k)^T
   \\ &=
   \sum_{k=1}^K \sum_{\mathbf{x} \in \mathcal{D}_k}
   \mathbf{w}^T (\mathbf{x} - \mathbf{\mu}_k)
   (\mathbf{x} - \mathbf{\mu}_k)^T \mathbf{w}
   \\ &=
   \mathbf{w}^T \mathbf{S}_W \mathbf{w}

The between-class scatter matrix for the projected dataset is defined as:

.. math::

   \mathbf{S}'_{B} &=
   \sum_{k=1}^K N_k (\mu_k' - \mu')^2
   \\ &=
   \sum_{k=1}^K N_k (\mu_k' - \mu') (\mu_k' - \mu')^T
   \\ &=
   \sum_{k=1}^K N_k
   (\mathbf{w}^T \mathbf{\mu}_k - \mathbf{w}^T \mathbf{\mu})
   (\mathbf{w}^T \mathbf{\mu}_k - \mathbf{w}^T \mathbf{\mu})^T
   \\ &=
   \sum_{k=1}^K N_k
   \mathbf{w}^T (\mathbf{\mu}_k - \mathbf{\mu})
   (\mathbf{\mu}_k - \mathbf{\mu})^T \mathbf{w}
   \\ &=
   \mathbf{w}^T \mathbf{S}_B \mathbf{w}

The ratio of between-class variance to within-class variance is defined as:

.. math::

   J(\mathbf{w}) &=
   \frac{\mathbf{S}'_{B}}{\mathbf{S}'_{W}}
   \\ &=
   \frac{\mathbf{w}^T \mathbf{S}_B \mathbf{w}} {\mathbf{w}^T \mathbf{S}_W \mathbf{w}}

Lagrangian Function
===================

Our goal is to find the optimal projection :math:`\mathbf{w}` that maximizes
:math:`J(\mathbf{w})`.
However, if we multiply :math:`\mathbf{w}` by a constant, :math:`J(\mathbf{w})`
will not change, i.e: :math:`J(\mathbf{w}) = J(c \mathbf{w})` for any
constant :math:`c \neq 0`.
By introducing the constraint :math:`\mathbf{w}^T \mathbf{S}_W \mathbf{w} = 1`,
we ensure that the solution is unique.

We define the Lagrangian function as:

.. math::

   L(\mathbf{w}, \lambda) =
   \mathbf{w}^T \mathbf{S}_B \mathbf{w} -
   \lambda (\mathbf{w}^T \mathbf{S}_W \mathbf{w} - 1)

The stationary point of :math:`L(\mathbf{w}, \lambda)` can be found by
solving the following equation:

.. math::

   \frac{\partial L}{\partial \mathbf{w}} &=
   2 \mathbf{S}_B \mathbf{w} - 2 \lambda \mathbf{S}_W \mathbf{w}
   \\ &= 0

which is equivalent to:

.. math::

   \mathbf{S}_B \mathbf{w} = \lambda \mathbf{S}_W \mathbf{w}

When :math:`\mathbf{S}_W` is nonsingular [#f01]_, the equation can be further
simplified to:

.. math::

   \mathbf{S}_W^{-1} \mathbf{S}_B \mathbf{w} = \lambda \mathbf{w}


By plugging back into :math:`J(\mathbf{w})`, we get:

.. math::

   J(\mathbf{w}) &=
   \frac{\mathbf{w}^T \mathbf{S}_B \mathbf{w}}
   {\mathbf{w}^T \mathbf{S}_W \mathbf{w}}
   \\ &=
   \frac{\mathbf{w}^T \lambda \mathbf{S}_W \mathbf{w}}
   {\mathbf{w}^T \mathbf{S}_W \mathbf{w}}
   \\ &=
   \lambda

Therefore maximizing :math:`J(\mathbf{w})` is equivalent to
**finding the eigenvectors corresponding to the largest eigenvalues**
of the matrix :math:`\mathbf{S}_W^{-1} \mathbf{S}_B`.

.. rubric:: Footnotes

.. [#f01] if :math:`\mathbf{S}_W` is singular, we can add a small multiple of
   the identity matrix to :math:`\mathbf{S}_W` to make it invertible
   :cite:p:`rolda_`.
   The solution after regularization might not be exactly the same as the
   solution without regularization, but it will be similar, especially when
   the regularization term is small.

Back to :doc:`index`.

.. disqus::
