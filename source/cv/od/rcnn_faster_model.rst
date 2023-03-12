##########################
Faster R-CNN: Model Design
##########################

.. default-role:: code

Architecture
============

.. code-block:: none

   Faster R-CNN Model Structure:

           +-------------------------------+
           |          Input Image          |
           +-------------------------------+
                           |
                           |
                           |
                           |
                           |
           +-------------------------------+
           |    Convolutional Backbone     |------------------|
           +-------------------------------+                  |
                           |                                  |
                           |                                  |
                           |                                  |
                           |                                  |
                           |                                  |
           +-------------------------------+                  |
           | Region Proposal Network (RPN) |                  |
           +-------------------------------+                  |
                           |                                  |
                           |                                  |
                           |----------------------------------|
                           |
                           |
           +-------------------------------+
           |       RoI Pooling Layer       |
           +-------------------------------+
                           |
                           |
                           |
                           |
                           |
           +-------------------------------+
           |     Fully Connected Layers    |------------------|
           +-------------------------------+                  |
                           |                                  |
                           |                                  |
                           |                                  |
                           |                                  |
                           |                                  |
           +-------------------------------+  +-------------------------------+
           |        Classification         |  |          Localization         |
           +-------------------------------+  +-------------------------------+


where:

- both the RoI pooling layer and its following-up FC layers constitute the
  Fast R-CNN detector :cite:p:`rcnn_fast_`

- the backbone convolutional network adapts `ZF` or `VGG` :cite:p:`rcnn_faster_`

Back to :doc:`index`.

.. disqus::
