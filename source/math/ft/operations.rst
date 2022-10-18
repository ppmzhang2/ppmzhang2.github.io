##########
Operations
##########

.. default-role:: math

- the most fundamental question of signal processing

  - how to use one signal (function) to modify another

  - most often: to modify the spectrum of the signal

- convolution is probably the most important operation in signal processing


Shift
=====

- Shift in time (signal) corresponds to phase shift in frequency (FT)

.. math::

   (\mathcal{F} f(t - b))(s) = e^{-2 \pi i s b} \cdot \mathcal{F} f (s)

Proof

.. math::

   (\mathcal{F} f(t - b))(s) =
     \int_{-\infty}^{+\infty}
       e^{-2 \pi i s t} f(t - b) dt

   \\

   Let: u = t - b \implies t = u + b

   \\

   (\mathcal{F} f(t - b))(s) & =
     \int_{-\infty}^{+\infty}
       e^{-2 \pi i s \cdot (u + b)} f(u) du
     \\ & =
     e^{-2 \pi i s b}
     \int_{-\infty}^{+\infty}
       e^{-2 \pi i s u} f(u) du
     \\ & =
     e^{-2 \pi i s b} \cdot \mathcal{F} f (s)

   \square

Stretch
=======

- **squashed** in time (signal) corresponds to stretched in phase and squashed
  in magnitude

- **stretched** in time (signal) corresponds to squeezed in phase and stretched
  in magnitude

- a signal **cannot** be both localized in time and frequency

.. math::

   (\mathcal{F} f(a t))(s) = |\frac{1}{a}| F(\frac{s}{a})

Proof

.. math::

   (\mathcal{F} f(a t))(s) =
     \int_{-\infty}^{+\infty} e^{-2 \pi i s t} f(at) dt

   \\

   Let: u = a t \implies t = \frac{1}{a} u

   \\

   (\mathcal{F} f(a t))(s) & =
     \int_{-\infty}^{+\infty}
       e^{-2 \pi i s \cdot \frac{u}{a}} f(u) dt
     \\ & =
     \int_{-\infty}^{+\infty}
       e^{-2 \pi i \cdot \frac{s}{a} \cdot u} f(u) dt
     \\ & =
     |\frac{1}{a}| \int_{-\infty}^{+\infty}
       e^{-2 \pi i \cdot \frac{s}{a} \cdot u} f(u) du
     \\ & =
     |\frac{1}{a}| F(\frac{s}{a})

   \square


Addition
========

.. math::

   \mathcal{F}(f + g) = \mathcal{F}f + \mathcal{F}g

Can be proved by applying definition directly.

Convolution
===========

.. math::

   \mathcal{F} g \cdot \mathcal{F} f = \mathcal{F}(f * g)

Proof

.. math::

   \mathcal{F} g(s) \cdot \mathcal{F} f(s) & =
     \int_{-\infty}^{+\infty} e^{-2 \pi i s t} g(t) dt \cdot
     \int_{-\infty}^{+\infty} e^{-2 \pi i s t} f(t) dt
     \\ & =
     \int_{-\infty}^{+\infty} e^{-2 \pi i s t} g(t) dt \cdot
     \int_{-\infty}^{+\infty} e^{-2 \pi i s x} f(x) dx
     \\ & =
     \int_{-\infty}^{+\infty}
     \int_{-\infty}^{+\infty}
     e^{-2 \pi i s t} \cdot e^{-2 \pi i s x} \cdot g(t) \cdot f(x) dt dx
     \\ & =
     \int_{-\infty}^{+\infty}
     \int_{-\infty}^{+\infty}
     e^{-2 \pi i s (t + x)} \cdot g(t) \cdot f(x) dt dx
     \\ & =
     \int_{-\infty}^{+\infty} (
       \int_{-\infty}^{+\infty}
       e^{-2 \pi i s (t + x)} \cdot g(t) dt
     ) f(x) dx

   \\

   Let: u = t + x \implies t = u - x

   \\

   \mathcal{F} g(s) \cdot \mathcal{F} f(s) & =
     \int_{-\infty}^{+\infty} (
       \int_{-\infty}^{+\infty}
       e^{-2 \pi i s (t + x)} \cdot g(t) dt
     ) f(x) dx
     \\ & =
     \int_{-\infty}^{+\infty} (
       \int_{-\infty}^{+\infty}
       e^{-2 \pi i s u} \cdot g(u - x) du
     ) f(x) dx
     \\ & =
     \int_{-\infty}^{+\infty} e^{-2 \pi i s u} (
       \int_{-\infty}^{+\infty}
       g(u - x) \cdot f(x) dx
     ) du

   \\

   Let: (f * g)(u) = \int_{-\infty}^{+\infty} g(u - x) \cdot f(x) dx

   \\

   \mathcal{F} g(s) \cdot \mathcal{F} f(s) & =
     \int_{-\infty}^{+\infty} e^{-2 \pi i s u} (
       \int_{-\infty}^{+\infty}
       g(u - x) \cdot f(x) dx
     ) du
     \\ & =
     \mathcal{F}(f * g)(s)

   \square

Back to :doc:`index`.

.. disqus::
