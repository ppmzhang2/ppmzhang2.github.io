---
title: "Faster R-CNN: Fast R-CNN Detector"
---

# Faster R-CNN: Fast R-CNN Detector

## RoI Pooling

- it converts any variable size tensor into fixed size ones
- why not resizing: max pooling is **differentiable**, while resizing is
  not
- input
  - feature map out of the backbone
  - box coordinates in **relative** format
- output: cropped feature map to feed detector
- max pooling vs. average pooling (TBD)
  - robustness to noise
  - max pooling captures the most important feature in each sliding
    window, while average pooling may dilute the information of
    important features

## FC Layers

TBD

---

Back to {doc}`index`.

```{disqus}

```
