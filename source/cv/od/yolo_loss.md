---
title: "YOLO: Loss Function"
---

# YOLO: Loss Function

## Notation

The YOLO algorithm assumes that the model divides an input image into an
$S \times S$ grid. Each grid cell is responsible to predict $B$ bounding
boxes, performing both localization and classification (totally $K$
classes).

Therefore the bounding box of index $(i, j)$ ($i \in S^2,$ $j \in B$)
is[^fn1]:

$$
\mathbf y_{ij} =
\{ c_{ij}, x_{ij}, y_{ij}, w_{ij}, h_{ij},
   p_{ij}^{(1)}, \ldots, p_{ij}^{(K)} \}
$$

where:

- $c$: object confidence

  - prediction: logit value
  - ground truth: $1$ / $0$ flag

- $x$, $y$, $w$ and $h$: bouding box coordinates

  - YOLO redicts bounding boxes using anchor boxes since YOLO9000
    {cite}`yolov2_`. The predictions correspond to:

  $$
  b_x &= \sigma(x) + c_x
  \\
  b_y &= \sigma(y) + c_y
  \\
  b_w &= p_w e^w
  \\
  b_h &= p_h e^h
  $$

- $p_{ij}^{(1)}, \ldots, p_{ij}^{(K)}$: confidence of $K$ classes

  - prediction: logit values
  - ground truth: one-hot values

## Mask

### IoU Mask

Given a prediction $\hat{\mathbf{y}}$ and label $\mathbf{y}$, the IoU
mask is:

$$
\mathbb{1}_{ij}^{\mathrm{IoU}} =
\begin{cases}
  1 & \mathrm{IoU}_{ij}^{\mathrm{max}} > \mathrm{IoU}_0
  \\
  0 & \mathrm{otherwise}
\end{cases}
$$

where

- $\mathrm{IoU}_{ij}^{\mathrm{max}}$ is the maximum $\mathrm{IoU}$ value
  of $\hat{\mathbf{y}}_{ij}$ compared with all the ground truth bounding
  boxes;
- $\mathrm{IoU}_0$ is the minimum $\mathrm{IoU}$ threshold.

### Ground Truth Mask

Ground truth mask is determined by the **ground truth confidence only**:

$$
\mathbb{1}_{ij}^{\mathrm{gt}} =
\begin{cases}
  1 & o_{ij} = 1
  \\
  0 & \mathrm{otherwise}
\end{cases}
$$

### Confidence Mask

Confidence Mask is determined by the **prediction only**:

$$
\mathbb{1}_{ij}^{\mathrm{conf}} =
\begin{cases}
  1 & \hat{o}_{ij} > o_0
  \\
  0 & \mathrm{otherwise}
\end{cases}
$$

where

- $o_0$ is the minimum object confidence threshold.

### Overall Object / Background Mask

The background mask is a combination of $\mathbb{1}_{ij}^{\mathrm{gt}}$
and $\mathbb{1}_{ij}^{\mathrm{IoU}}$:

$$
\mathbb{1}_{ij}^{\mathrm{bgd}} =
(1 - \mathbb{1}_{ij}^{\mathrm{gt}})
(1 - \mathbb{1}_{ij}^{\mathrm{IoU}})
$$

The object mask is $\mathbb{1}_{ij}^{\mathrm{gt}}$:

$$\mathbb{1}_{ij}^{\mathrm{obj}} = \mathbb{1}_{ij}^{\mathrm{gt}}$$

## Empirical Risk

The YOLO risk is nothing but the sum of the following Risks.

### IoU Risk

$$
\mathcal{L}^{\mathrm{IoU}} (\mathbf{y}, \mathbf{\hat{y}}) =
\sum_{i=0}^{S^2} \sum_{j=0}^{B}
  \gamma_{ij}^{\mathrm{IoU}} \cdot
  \mathbb{1}_{ij}^{\mathrm{obj}} \cdot
  (1 - \mathrm{IoU}_{ij}^{\mathrm{max}})
$$

```{note}
Some implementation[^fn2] will give large weights to small bounding boxes:

$$
\gamma_{ij}^{\mathrm{IoU}} =
2 - \frac{b_w \cdot b_h}{I_w \cdot I_h}
$$

where $I_w$ and $I_h$ are the image width and height respectively.
```

### Confidence Risk

The confidence risk is computed with binary cross entropy:

$$
\mathcal L^{\mathrm conf} (\mathbf y, \mathbf {\hat{y}}) =
\sum_{i=0}^{S^2} \sum_{j=0}^{B}
  c_{ij} \log {\hat c_{ij}} +
  (1 - c_{ij}) \log {\hat c_{ij}}
$$

### Class Risk

YOLOv3 class risk is computed with binary cross entropy as it allows the
model to handle class imbalance more effectively {cite:p}`yolov3_`.

$$
\mathcal{L}^{\mathrm{cls}} (\mathbf{y}, \mathbf{\hat{y}}) =
\frac{1}{K} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \sum_{k=1}^{K}
  p_{ij}^{(k)} \log \hat{p}_{ij}^{(k)} +
  (1 - p_{ij}^{(k)}) \log \hat{p}_{ij}^{(k)}
$$

## Review

### Why no MSE

We adopted the IoU Risk instead of the mean squared error (MSE), as it
does not directly depend on the coordinates or scale of the bounding
boxes, and it could be more robust to data imbalance and various object
scales.

---

Back to {doc}`index`.

[^fn1]:
    assume each bounding box of each grid cell has **only one** ground
    truth box.

[^fn2]: <https://github.com/YunYang1994/TensorFlow2.0-Examples>

```{disqus}
```
