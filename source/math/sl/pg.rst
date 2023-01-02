###############
Policy Gradient
###############

.. default-role:: math

Trust Region Policy Optimization (TRPO)
=======================================

.. math::

   max_{\theta} E [\frac{p(x | \theta)}{p(x | \theta_{old})} A]

which is subject to:

.. math::

   E[ KL [p_{old}, p] ] \le \delta


Proximal Policy Optimization (PPO)
==================================

.. math::

   r = \frac{p(x | \theta)}{p(x | \theta_{old})}

.. math::

   max_{\theta} E [min[r A, clip[r, 1-\epsilon, 1+\epsilon]A]]


Back to :doc:`index`.

.. disqus::
