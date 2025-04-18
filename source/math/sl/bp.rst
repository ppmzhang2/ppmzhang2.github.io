###########################
Gradient in Backpropagation
###########################

.. default-role:: math

TL;DR
=====

TBD [#f01]_.

.. math::

   \tag*{$\blacksquare$}

Fully Connected Layer
=====================

Suppose:

.. math::

   \mathbf{z} = \mathbf{W} \mathbf{x} + \mathbf{b}

where

.. math::

   \mathbf{x} = (x_1, x_2, \dots, x_n)^T
   \\
   \mathbf{z} = (z_1, z_2, \dots, z_m)^T
   \\
   \mathbf{b} = (b_1, b_2, \dots, b_m)^T

.. math::

   \mathbf{W} = \begin{pmatrix}
     w_{11} & w_{12} & \dots & w_{1n}
     \\
     w_{21} & w_{22} & \dots & w_{2n}
     \\
     \vdots & \vdots & \ddots & \vdots
     \\
     w_{m1} & w_{m2} & \dots & w_{mn}
   \end{pmatrix}

.. math::

   \therefore
   z_i = \sum_{j=1}^n w_{ij} x_j + b_i

.. math::

   \therefore
   \frac{\partial z_i}{\partial w_{ij}} = x_j

.. math::

   \frac{\partial z_i}{\partial b_i} = 1

Gradient
========

We define some kind of "gradient" of the output with respect to each element of
the weight matrix:

.. math::

   \frac{\partial L}{\partial \mathbf{W}} =
     \begin{pmatrix}
       \frac{\partial L}{\partial w_{11}} & \dots & \frac{\partial L}{\partial w_{1n}}
       \\
       \vdots & \ddots & \vdots
       \\
       \frac{\partial L}{\partial w_{m1}} & \dots & \frac{\partial L}{\partial w_{mn}}
     \end{pmatrix}

Note that this is **NOT the Jacobian matrix**, which should be a **3D tensor**.
What we really want is some delta, with which we can update the weight matrix.

.. math::

   \frac{\partial L}{\partial \mathbf{W}} &=
     \begin{pmatrix}
       \frac{\partial L}{\partial y_1} \frac{\partial y_1}{\partial z_1} \frac{\partial z_1}{\partial w_{11}} &
         \dots &
         \frac{\partial L}{\partial y_1} \frac{\partial y_1}{\partial z_1} \frac{\partial z_1}{\partial w_{1n}}
       \\
       \vdots & \ddots & \vdots
       \\
       \frac{\partial L}{\partial y_m} \frac{\partial y_m}{\partial z_m} \frac{\partial z_m}{\partial w_{m1}} &
         \dots &
         \frac{\partial L}{\partial y_m} \frac{\partial y_m}{\partial z_m} \frac{\partial z_m}{\partial w_{mn}}
     \end{pmatrix}
   \\ &=
     \begin{pmatrix}
       \frac{\partial L}{\partial y_1} f' (z_1) x_1 &
         \dots &
         \frac{\partial L}{\partial y_1} f' (z_1) x_n
       \\
       \vdots & \ddots & \vdots
       \\
       \frac{\partial L}{\partial y_m} f' (z_m) x_1 &
         \dots &
         \frac{\partial L}{\partial y_m} f' (z_m) x_n
     \end{pmatrix}
   \\ &=
     (\frac{\partial L}{\partial y_1}, \dots, \frac{\partial L}{\partial y_m})^T 
     \odot
     (f' (z_1), \dots, f' (z_m))^T
     \cdot
     \mathbf{x}^T
   \\ &=
     \nabla_{\mathbf{y}} L \odot \nabla_{\mathbf{z}} f \cdot \mathbf{x}^T



----

.. [#f01] https://www.adityaagrawal.net/blog/deep_learning/bprop_fc

Back to :doc:`index`.

.. disqus::
