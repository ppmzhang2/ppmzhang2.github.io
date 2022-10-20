#########################
Convolution: Introduction
#########################

.. default-role:: math

Interpreted by Filtering
========================

    `f * h` is (at least) as good as the best properties of `f` and `h`
    separately (as long as `h` is not a delta function)

- Filtering a signal (function) is to eliminate some of its frequency and let
  the others go through, then check the consequences in the time domain.

- Filter is a system that convolves an input (which can vary) with a fixed
  signal (function), a.k.a. **impulse response**

- In the frequency domain, filtering is just multiplication: `G = F \cdot H`

- In the time domain, filtering is synonymous with convolution: `g = f * h`
  where `h` is the **fixed fixed impulse response**, or the inverse Fourier
  transform of the transform function `H`.

- It is easy to understand filtering (convolution) in terms of frequency, not
  so easy in the time domain

- low-pass filter works as a smoother: removing the short-term fluctuations and
  leaving the longer-term trend.

- high-pass filter: e.g. edge detection

- To design a filter is to design `H`

Differentiability
=================

If `f` is differentiable, convolution `f * g` is differentiable:

.. math::

   (f * g)' = f' * g

Back to :doc:`index`.

.. disqus::
