############
Model Design
############

.. default-role:: code

Notation
========

.. default-role:: math

The YOLO algorithm assumes that the model divides an input image into an
`S \times S` grid.
Each grid cell is responsible to predict `B` bounding boxes, performing both
localization and classification (totally `K` classes).

- Predictions of each **bounding box**:

  .. math::

     \mathbf{y}^{(box)} = ( p^{(obj)}, x, y, w, h )^T

  - `p^{(obj)}`: confidence that the box contains an object; ground truth
    confidence could only be `1` or `0`

  - `x` and `y`: coordinates of the object center. `x, y \in (0, 1)`
  - `w` and `h`: width and height of the object `w, h > 0`

- Classification of each **cell** (regardless of the number of boxes `B`)

  .. math::

     \mathbf{y}^{(cls)} =
       ( p^{(cls | obj)} (1),
         p^{(cls | obj)} (2),
         \ldots,
         p^{(cls | obj)} (K)
       )^T

For `i \in \mathbb{N}, i < S^2`:

- output / label:

  .. math::

     \mathbf{y}_i =
       ( \mathbf{y}_{i1}^{(box)},
         \mathbf{y}_{i2}^{(box)},
         \ldots,
         \mathbf{y}_{iB}^{(box)},
         \mathbf{y}_i^{(cls)}
       )

- Predicted class index of each **cell**:

  .. math::

     k_i^{(max)} = \arg \max_{k} p_i^{(cls|obj)} (k)

- IoU (use both prediction and label)

  .. math::

     IoU =
     \frac
       { Area(x_{ij}, y_{ij}, w_{ij}, h_{ij}) \cap
         Area(\hat{x}_{ij}, \hat{y}_{ij}, \hat{w}_{ij}, \hat{h}_{ij})
       }
       { Area(x_{ij}, y_{ij}, w_{ij}, h_{ij}) \cup
         Area(\hat{x}_{ij}, \hat{y}_{ij}, \hat{w}_{ij}, \hat{h}_{ij})
       }

- Confidence score for each **bounding box** (use both prediction and label):

  .. math::

     C_{ij} = p_{ij}^{(cls)} (k_i^{(max)}) \cdot IoU_{ij}
            = p_i^{(cls | obj)} (k_i^{(max)}) \cdot p_{ij}^{(obj)} \cdot IoU_{ij}

Loss Function
=============

Loss function:

.. math::

    L(\mathbf{y}, \mathbf{\hat{y}}) =
      \lambda_{coord} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{obj}
      [ (x_{ij} - \hat{x}_{ij})^2 + (y_{ij} - \hat{y}_{ij})^2
      ]
    \\
    + \lambda_{coord} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{obj}
      [ (\sqrt{w_{ij}} - \sqrt{\hat{w}_{ij}})^2 +
        (\sqrt{h_{ij}} - \sqrt{\hat{h}_{ij}})^2
      ]
    \\
    + \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{obj}
      (C_{ij} - \hat{C}_{ij})^2
    \\
    + \lambda_{noobj} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{noobj}
      (C_{ij} - \hat{C}_{ij})^2
    \\
    + \sum_{i=0}^{S^2} \mathbb{1}_{i}^{obj} \sum_{k=1}^{K}
      (p_i^{(cls | obj)} (k) - \hat{p}_i^{(cls | obj)} (k))^2

Specifically:

- `\mathbb{1}_{i}^{obj}` is label determined:

  .. math::

     \mathbb{1}_{i}^{obj} = 
     \begin{cases}
       1 & p_i^{(obj)} = 1
       \\
       0 & otherwise
     \end{cases},

- `\mathbb{1}_{ij}^{obj}`: according to the paper [#f01]_:
      
      ... denotes that the `j` th bounding box predictor in cell `i` is
      "responsible" for that prediction.

  that is to say, is `1` if there is an object in cell `i` and confidence of
  the `j` th predictors of this cell is the highest among all the predictors
  of this cell.

- label `C_{ij}` can be either `1` or `0`.

- `\lambda_{coord} = 5` to increase the localization prediction error

- `\lambda_{noobj} = 0.5` to decrease the loss from confidence predictions
  containing no object

- For `B = 1`:

  .. math::
  
     L(\mathbf{y}, \mathbf{\hat{y}}) =
     \lambda_{coord} \sum_{i=0}^{S^2} \mathbb{1}_{i}^{obj}
       [ (x_i - \hat{x}_i)^2 + (y_i - \hat{y}_i)^2 +
         (\sqrt{w_i} - \sqrt{\hat{w}_i})^2 +
         (\sqrt{h_i} - \sqrt{\hat{h}_i})^2
       ]
     \\
     + \sum_{i=0}^{S^2} \mathbb{1}_{i}^{obj} (C_i - \hat{C}_i)^2
     + \lambda_{noobj} \sum_{i=0}^{S^2} \mathbb{1}_{i}^{noobj}
       (C_i - \hat{C}_i)^2
     \\
     + \sum_{i=0}^{S^2} \mathbb{1}_{i}^{obj} \sum_{k=1}^{K}
       (p_i^{(cls)} (k) - \hat{p}_i^{(cls)} (k))^2

Reference
=========

.. [#f01] https://arxiv.org/abs/1506.02640
