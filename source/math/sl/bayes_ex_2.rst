#############################
Bayes Example: Classification
#############################

.. default-role:: math

.. math::

   \DeclareMathOperator{\diff}{d}

Consider a binary classification problem `\theta \in \{0, 1\}`:

.. math::
   
   \theta =
   \begin{cases}
     0, & \text{Tail}
     \\
     1, & \text{Head}
   \end{cases}

The prior probability of `\theta`:

.. math::

   p_{\Theta}(\theta) =
   \begin{cases}
     0.69, & \theta = 0
     \\
     0.31, & \theta = 1
   \end{cases}

.. math::

   \therefore
   \pi (\theta) = 0.69 \cdot \delta_0 (x) + 0.31 \cdot \delta_1 (x)

The probability density function of predictor random variable `X`, given the
condition of `\theta`, is also known:

.. math::

   f_X(x \mid \theta = 0) =
     \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} x^2}

.. math::

   f_X(x \mid \theta = 1) =
     \frac{1}{\sqrt{\pi}} e^{- (x - 1)^2}

.. math::

   \therefore
   \mathcal{L} (\theta \mid x) &= f_X (x \mid \theta)
   \\ &=
   \begin{cases}
     \frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} x^2}, & \theta = 0
     \\
     \frac{1}{\sqrt{\pi}} e^{- (x - 1)^2}, & \theta = 1
     \\
     0, & \text{otherwise}
   \end{cases}

.. math::

   \therefore
   f (\theta \mid x) &=
   \frac
     {\mathcal{L}(\theta \mid \mathbf{x}) \cdot \pi (\theta)}
     {\int\limits_{\mathbb{R}}
       \mathcal{L} (\theta \mid \mathbf{x}) \cdot
       \pi (\theta) \mathrm{d} \theta}
   \\ &=
   \frac
     {\mathcal{L}(\theta \mid \mathbf{x}) \cdot \pi (\theta)}
     {0.69 \cdot f_X(x \mid \theta = 0) + 0.31 \cdot f_X(x \mid \theta = 1)}


Back to :doc:`index`.

.. disqus::
