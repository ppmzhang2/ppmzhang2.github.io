#############
Loss Function
#############

.. default-role:: code

Notation
========

.. default-role:: math

The YOLO algorithm assumes that the model divides an input image into an
`S \times S` grid.
Each grid cell is responsible to predict `B` bounding boxes, performing both
localization and classification (totally `K` classes).

This implementation [#f01]_ assumes for labels that each cell has **only one**
ground truth box.

- Predictions of each **bounding box**:

  .. math::

     \mathbf{y}^{(box)} = ( x, y, w, h, p^{(obj)} )^T

  - `x` and `y`: coordinates of the object center. `x, y \in (0, 1)`

  - `w` and `h`: width and height of the object `w, h > 0`

  - `p^{(obj)}`: confidence that the box contains an object.
    Its label value can only be either `1` or `0`. Yet the target value for
    training could be different. According to the paper [#f02]_:

        If no pred object exists in that cell, the confidence scores should be
        zero.
        Otherwise we want the confidence score to equal the intersection over
        union (IOU) between the predicted box and the ground truth.

    Thus the target confidence could only be either `0` (no object in that
    cell) or the `IoU` value.
    Suppose `x_{i}`, `y_{i}`, `w_{i}`, `h_{i}` are the ground truth coordinates
    of the `i` th grid cell, the `IoU` of the `j` th predicted bounding box of
    the `i` th cell is:

    .. math::

       IoU_{ij} =
       \frac
         { Area(x_{i}, y_{i}, w_{i}, h_{i}) \cap
           Area(\hat{x}_{ij}, \hat{y}_{ij}, \hat{w}_{ij}, \hat{h}_{ij})
         }
         { Area(x_{i}, y_{i}, w_{i}, h_{i}) \cup
           Area(\hat{x}_{ij}, \hat{y}_{ij}, \hat{w}_{ij}, \hat{h}_{ij})
         }

- Classification of each **cell** (regardless of the number of boxes `B`)

  .. math::

     \mathbf{y}^{(cls)} =
       ( p^{(cls | obj)} (1),
         p^{(cls | obj)} (2),
         \ldots,
         p^{(cls | obj)} (K)
       )^T


- Output / label:

  .. math::

     \mathbf{y}_i =
       ( \mathbf{y}_{i1}^{(box)},
         \mathbf{y}_{i2}^{(box)},
         \ldots,
         \mathbf{y}_{iB}^{(box)},
         \mathbf{y}_i^{(cls)}
       )

  where `i \in \mathbb{N}, i < S^2`.

Formula
========

Original loss function:

.. math::

    L(\mathbf{y}, \mathbf{\hat{y}}) =
      \lambda_{coord} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{obj}
      [ (x_{i} - \hat{x}_{i})^2 + (y_{i} - \hat{y}_{i})^2
      ]
    \\
    + \lambda_{coord} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{obj}
      [ (\sqrt{w_{i}} - \sqrt{\hat{w}_{i}})^2 +
        (\sqrt{h_{i}} - \sqrt{\hat{h}_{i}})^2
      ]
    \\
    + \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{obj}
      (C_{i} - \hat{C}_{i})^2
    \\
    + \lambda_{noobj} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{noobj}
      (C_{i} - \hat{C}_{i})^2
    \\
    + \sum_{i=0}^{S^2} \mathbb{1}_{i}^{obj} \sum_{c \in classes}
      (p_i (c) - \hat{p}_i (c))^2

can be re-written as:

.. math::

    L(\mathbf{y}, \mathbf{\hat{y}}) =
      \lambda_{coord} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{obj}
      [ (x_{i} - \hat{x}_{ij})^2 +
        (y_{i} - \hat{y}_{ij})^2
      ]
    \\
    + \lambda_{coord} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{obj}
      [ (\sqrt{w_{i}} - \sqrt{\hat{w}_{ij}})^2 +
        (\sqrt{h_{i}} - \sqrt{\hat{h}_{ij}})^2
      ]
    \\
    + \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{obj}
      (IoU_{ij} - \hat{p}_{ij}^{(obj)})^2
    \\
    + \lambda_{noobj} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{i}^{noobj}
      (0 - \hat{p}_{ij}^{(obj)})^2
    \\
    + \sum_{i=0}^{S^2} \mathbb{1}_{i}^{obj} \sum_{k=1}^{K}
      (p_i^{(cls | obj)} (k) - \hat{p}_i^{(cls | obj)} (k))^2

where

- `\mathbb{1}_{i}^{obj}` is label determined:

  .. math::

     \mathbb{1}_{i}^{obj} = 
     \begin{cases}
       1 & p_i^{(obj)} = 1
       \\
       0 & otherwise
     \end{cases},

- `\mathbb{1}_{i}^{noobj}` is label determined:

  .. math::

     \mathbb{1}_{i}^{noobj} = 
     \begin{cases}
       1 & p_i^{(obj)} = 0
       \\
       0 & otherwise
     \end{cases},

- `\mathbb{1}_{ij}^{obj}` is a bit complicated. According to the paper [#f02]_:
      
      ... denotes that the `j` th bounding box predictor in cell `i` is
      "responsible" for that prediction.

  that is to say, is `1` if there is an object in cell `i` and confidence of
  the `j` th bounding box has the highest `IoU` with the cell's ground truth.

- `\lambda_{coord} = 5` to increase the localization prediction error

- `\lambda_{noobj} = 0.5` to decrease the loss from confidence predictions
  containing no object

Reference
=========

.. [#f01] https://github.com/motokimura/yolo_v1_pytorch
.. [#f02] https://arxiv.org/abs/1506.02640
