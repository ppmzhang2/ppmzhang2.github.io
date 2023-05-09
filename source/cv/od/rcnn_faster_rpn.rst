######################################
Faster R-CNN: Region Proposal Networks
######################################

.. default-role:: math

A Region Proposal Network (RPN) takes an image and outputs a set of object
proposals.

- it is a convolutional neural network

- it takes images of any size

Architecture
============

.. code-block:: none

   RPN Model Structure:

           =================================
           =       Input Feature Map       = 
           =================================
                           |
                           |
                           |
                           |
                           |
           +-------------------------------+
           |    3×3 Convolutional Layer    |
           |                               |------------------|
           |       (sliding window)        |                  |
           +-------------------------------+                  |
                           |                                  |
                           |                                  |
                           |                                  |
                           |                                  |
                           |                                  |
           +-------------------------------+  +-------------------------------+
           |    1×1 Convolutional Layer    |  |    1×1 Convolutional Layer    |
           |                               |  |                               |
           |       (K×2 Classifiers)       |  |        (K×4 Regressors)       |
           +-------------------------------+  +-------------------------------+
                           |                                  |
                           |                                  |
                           |                                  |
                           |                                  |
                           |                                  |
           +-------------------------------+                  |
           |         Proposal Layer        |------------------|
           +-------------------------------+
                           |
                           |
                           |
                           |
                           |
           =================================
           =        Region Proposals       = 
           =================================

- The number of filters in the sliding window layer depends upon the backbone
  (`256` for the ZF and `512` for the VGG).

- The two parallel `1 \times 1` convolutional layers are the core of the RPN
  "attention" mechanism.

- `K` is the number of anchors.
  The default value is `9`

  - three scales: `128`, `256`, `512`

  - three ratios `2:1`, `1:1`, `1:2`

Efficiency
==========

Computation Sharing
-------------------

Both the R-CNN and the Fast R-CNN use selective search to generate object
proposals.
While it is a popular region proposal method for object detection algorithms,
selective search does have its drawbacks.
One of these is that it uses a different mechanism than that of the follow-up
networks, such as the Fast R-CNN detector.
This disadvantage is overcome with the RPN:

  ... Because our ultimate goal is to share computation with a Fast R-CNN
  object detection network, we assume that both nets share a common set of
  convolutional layers ...

Essentially it means that the output of the feature extraction layer will be
utilized by both the RPN and the Fast R-CNN detector network.

Pyramid of Anchors
------------------

The RPN has pre-defined anchors based on the size and aspect ratio, and it
simply computes features at different anchor levels.
This is referred as "pyramid of anchors".
It allows the RPN to efficiently generate region proposals
at different scales, without the need for computationally expensive resizing or
cropping operations, as the image / feature pyramids design.

Translation Invariant
---------------------

If an object can be captured by a region proposal, it will be captured anywhere
in any image.
The probable reason is that the anchors are pre-defined and invariant and that
the `K` regressors are also invariant.

Loss Function
=============

- Only a small portion of predictions are passed through loss calculation:
  
  - positive, which has high overlap (`\mathrm{IoU} > 0.7`) with **any** ground
    truth box, or

  - negative, which has low overlap (`\mathrm{IoU} < 0.3`) with **all** ground
    truth boxes

- It is a combination of both classification and localization risk, which
  follows the multi-task loss in Fast R-CNN:

  - classification: log loss

  - localization: smooth `L_1` [#f01]_.
    It is only activated for positive predictions

.. rubric:: Footnotes

.. [#f01] `L_1 =
   \begin{cases} 0.5 x^2 & |x| < 1
   \\
   |x| - 0.5 & |x| \ge 1
   \end{cases}`

Back to :doc:`index`.

.. disqus::
