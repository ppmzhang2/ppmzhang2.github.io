---
title: "Faster R-CNN: Training"
---

# Faster R-CNN: Training

## RPN

- Training

  - It randomly sample equal sized positive / negative boxes (totally \~
    $256$)
  - pre-trained backbone are also turned

- normalization not required and could be simplified

- weights initialization: from a normal distribution $N(0, 0.01)$

  $$\mathcal{N}(0, \, 0.01)$$

- pre-trained backbone turning

  : - ZF: all layers - VGG: $conv3_1$ and up

## Overall Process

4-step alternating training

1.  train RPN above
2.  train detector, initialized by
    - pre-trained backbone
    - proposals of RPN trained in step 1
    - backbone not shared between RPN and detector
3.  TBD: fine tune RPN, fix backbone
4.  fine tune detector, fix backbone

---

Back to {doc}`index`.

```{disqus}

```
