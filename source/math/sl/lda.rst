###################
LDA: Classification
###################

Linear Discriminant Analysis (LDA) assumes:

- Normality: the class-conditional PDF follows a multivariate Gaussian
  distribution with class-specific mean vectors.

- Homoscedasticity: all class-conditional covariance matrices are equal

.. default-role:: math

Probability Density Function
============================

Suppose we have a set of samples `\mathcal{D}` with `K` classes:

.. math::

   \mathcal{D} = \{ (\mathbf{x}_1, y_1), \ldots, (\mathbf{x}_N, y_N) \}

where `\mathbf{x}_i \in \mathbb{R}^p` is a `p`-dimensional sample and
`y_i \in \{ 1, \ldots, K \}` is the class label for sample `\mathbf{x}_i`.

According to the LDA assumption, `\mathbf{x}` is sampled from a random vector
`\mathbf{X} = (X_1, \ldots, X_p)^T` with a conditional multivariate Gaussian
distribution:

.. math::

   \mathbf{X} \mid k \sim \mathcal{N} (\mathbf{\mu}_k, \mathbf{\Sigma})

where:

- `\mathbf{\mu}_k` is the mean vector for class `k`

- `\mathbf{\Sigma}` is the shared covariance matrix.

The probability density function:

.. math::

   f (\mathbf{x} \mid k) =
     \frac
     {1}
     {\sqrt{(2 \pi)^p \lvert \mathbf{\Sigma} \rvert}}
     \exp
     \left(
       -\frac{1}{2}
       (\mathbf{x} - \mathbf{\mu}_k)^T
       \mathbf{\Sigma}^{-1}
       (\mathbf{x} - \mathbf{\mu}_k)
     \right)

The mean vector for each class `k` is:

.. math::

   \mathbf{\mu}_k =
     \frac{1}{n_k}
     \sum_{\mathbf{x} \in \mathcal{D}_k}
     \mathbf{x}

where `n_k` is the number of samples in class `k` and `\mathcal{D}_k` is the
set of samples in class `k`.

The shared covariance matrix is derived from the concept of pooled variance
:cite:p:`wiki_pooled_`.
The covariance matrix for class `k` is:

.. math::

   \mathbf{\Sigma}_k =
     \frac{1}{n_k - 1}
     \sum_{\mathbf{x} \in \mathcal{D}_k}
     (\mathbf{x} - \mathbf{\mu}_k)
     (\mathbf{x} - \mathbf{\mu}_k)^T

The pooled variance can be calculated by weighted averaging the covariance
matrices for each class, using weights `n_k - 1`:

.. math::

   \mathbf{\Sigma} &=
     \frac{\sum_{k = 1}^K (n_k - 1) \mathbf{\Sigma}_k}
       {\sum_{k = 1}^K (n_k - 1)}
     \\ &=
     \frac{1}{N - K}
     \sum_{k = 1}^K (n_k - 1) \mathbf{\Sigma}_k
     \\ &=
     \frac{1}{N - K}
     \sum_{k = 1}^K
     \sum_{\mathbf{x} \in \mathcal{D}_k}
     (\mathbf{x} - \mathbf{\mu}_k)
     (\mathbf{x} - \mathbf{\mu}_k)^T

where `N` is the total number of samples.

Decision Boundary
=================

According to Bayes' theorem, the posterior probability of class `k` given
sample `\mathbf{x}` is:

.. math::

   f (k \mid \mathbf{x}) =
     \frac
       {f (\mathbf{x} \mid k) \cdot \pi_k}
       {\sum_{i = 1}^K f (\mathbf{x} \mid i) \cdot \pi_i}

Ignoring the denominator which does not depend on `k`, we have:

.. math::

   f (k \mid \mathbf{x}) \propto
     f (\mathbf{x} \mid k) \cdot \pi_k

where `\pi_k` is the prior probability of class `k`.

Taking the logarithm of both sides, we have:

.. math::

   \ln f (k \mid \mathbf{x}) \propto
     \ln f (\mathbf{x} \mid k) + \ln \pi_k

.. math::

   \therefore
   \hat{y} = \arg \max_{k}
     \left(
       - \frac{1}{2} p \ln {2 \pi}
       - \frac{1}{2} \ln \lvert \mathbf{\Sigma} \rvert
       - \frac{1}{2} (\mathbf{x} - \mathbf{\mu}_k)^T
         \mathbf{\Sigma}^{-1}
         (\mathbf{x} - \mathbf{\mu}_k)
       + \ln \pi_k
     \right)

According to :ref:`ref-sl-mgd-cov` of previous page, `\mathbf{\Sigma}_k` is
symmetric and positive semi-definite.
Therefore, `\mathbf{\Sigma}` and `\mathbf{\Sigma}^{-1}` are also symmetric and
positive semi-definite.

.. math::

   \therefore
   - \frac{1}{2} (\mathbf{x} - \mathbf{\mu}_k)^T
   \mathbf{\Sigma}^{-1}
   (\mathbf{x} - \mathbf{\mu}_k) &=
   - \frac{1}{2} \mathbf{x}^T \mathbf{\Sigma}^{-1} \mathbf{x} +
   \frac{1}{2} \mathbf{x}^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_k +
   \frac{1}{2} \mathbf{\mu}_k^T \mathbf{\Sigma}^{-1} \mathbf{x} -
   \frac{1}{2} \mathbf{\mu}_k^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_k
   \\ &=
   - \frac{1}{2} \mathbf{x}^T \mathbf{\Sigma}^{-1} \mathbf{x} +
   \mathbf{x}^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_k -
   \frac{1}{2} \mathbf{\mu}_k^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_k

By removing the terms that do not depend on `k`, we have:

.. math::

   \hat{y} &= \arg \max_{k}
     \left(
       - \frac{1}{2} (\mathbf{x}
       - \mathbf{\mu}_k)^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{\mu}_k)
       + \ln \pi_k
     \right)
   \\ &=
   \arg \max_{k}
     \left(
       \mathbf{x}^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_k -
       \frac{1}{2} \mathbf{\mu}_k^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_k +
       \ln \pi_k
     \right)

The decision boundary is the set of points where the posterior probabilities of
two classes are equal:

.. math::

   f (i \mid \mathbf{x}) - f (j \mid \mathbf{x}) = 0

.. math::

   \therefore
   \mathbf{x}^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_i -
   \frac{1}{2} \mathbf{\mu}_i^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_i +
   \ln \pi_i -
   \mathbf{x}^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_j +
   \frac{1}{2} \mathbf{\mu}_j^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_j -
   \ln \pi_j = 0

.. math::

   \therefore
   \mathbf{x}^T \mathbf{\Sigma}^{-1} (\mathbf{\mu}_i - \mathbf{\mu}_j) -
   \frac{1}{2} (
     \mathbf{\mu}_i^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_i -
     \mathbf{\mu}_j^T \mathbf{\Sigma}^{-1} \mathbf{\mu}_j
   ) + \ln \frac{\pi_i}{\pi_j} = 0

Obviously, the decision boundary is a **linear function** of `\mathbf{x}`.

Back to :doc:`index`.

.. disqus::
