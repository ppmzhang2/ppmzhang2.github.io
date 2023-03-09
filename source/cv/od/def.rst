##################
Problem Definition
##################

.. default-role:: math

A General Problem
=================

Suppose an object detection dataset `S` contains `K` different kinds of
objects; each image contains `M_i` objects `o_1, \ldots, o_{M_i}`:

.. math::

   S = \{ \mathbf{z}_i \}_{i=1}^n
     = \{ I_i, \mathbf{y}_{o_1}, \ldots, \mathbf{y}_{o_{M_i}} \}_{i=1}^n

where

.. math::

   I_i \in \mathbb{W} \times \mathbb{H}\ \times \mathbb{C}

.. math::

   \mathbf{y}_{o_j} =
   \{ c_{o_j}, x_{o_j}, y_{o_j}, w_{o_j}, h_{o_j} \}
   \in \mathbb{K} \times \mathbb{Z}^4

where `c` denotes object category, `x` and `y` are the bounding box center
coordinates, `w` and `h` represent width and height of the bounding box
respectively [#f01]_.

Notes
=====

.. [#f01] `\mathbb{W} \subseteq \mathbb{Z},`
   `\mathbb{H} \subseteq \mathbb{Z},`
   `\mathbb{C} = \{ 1, 2, 3 \},`
   `\mathbb{K} = \{1, \ldots, K\}`.

Back to :doc:`index`.

.. disqus::
