####################################################
Generalized Fourier Transform: Tempered Distribution
####################################################

.. default-role:: math

A tempered distribution is a **linear functional**:

.. math::

   f: \mathcal{S} \to \mathbb{C}

- The space of all tempered distributions denoted `\mathcal{S}'`, is the dual
  space of `\mathcal{S}`.

- The value in `\mathbb{C}` that the distribution `f \in \mathcal{S}'` assigns to
  `\phi \in \mathcal{S}` is usually denoted by:

  .. math::
  
     \langle f, \phi \rangle

Properties without proof:

- Linearity

  .. math::

     a \langle f, \phi \rangle + b \langle f, \psi \rangle =
     \langle f, a \phi + b \psi \rangle

- Continuity

  .. math::

     \lim_{n \to \infty} \phi_n = \phi
     \implies
     \lim_{n \to \infty} \langle f, \phi_n \rangle = \langle f, \phi \rangle

- Specifically:

  .. math::
  
     f: \phi \in \mathcal{S} \mapsto
       \langle f, \phi \rangle = \int_{-\infty}^{+\infty} f(x) \phi(x) dx

  is a tempered distribution if `f` is polynomially bounded and Riemann
  integrable.

Dirac delta function
====================

The `\delta` distribution, aka the **unit impulse**, is a generalized function
or distribution.

Operationally, the effect of `\delta` is to evalute the function at the origin
(i.e. pull out the value of origin).

Classical Interpretation
------------------------

.. math::

   \delta (x) =
   \begin{cases}
     \infty & x = 0
     \\
     0 & x \ne 0
   \end{cases}

.. math::

   \int_{-\infty}^{+\infty} \delta (x) dx = 1

It can be viewed as a sequence of bump functions:

    That is really operationally how it appear:
    by limiting process you were concentrating things and you were just pulling out
    the value at the origin.

.. math::

   \delta(x) = \lim_{b \to 0} \frac{1}{|b| \sqrt{\pi}} e^{-(\frac{x}{b})^2}

Distribution Interpretation
---------------------------

   It is a mathematical modus operandi by turning the solution of a problem
   into a definiation

`\delta` maps every continuous function to its value at zero of its domain:

.. math::

   \langle \delta, \phi \rangle = \phi(0)

`\delta` is also linear and continuous:

.. math::

   a \langle \delta, \phi \rangle + b \langle \delta, \psi \rangle =
   \langle \delta, a \phi + b \psi \rangle

.. math::

   \lim_{n \to \infty} \phi_n = \phi
   \implies
   \lim_{n \to \infty} \langle \delta, \phi_n \rangle =
   \langle \delta, \phi \rangle

Define a new distribution `\delta_a`

.. math::

   \delta_a: \phi \in \mathcal{S} \mapsto
     \langle \delta_a, \phi \rangle = \phi(a)

Ordinary Functions
==================

    function induced distribution (generalized function):
    you give me a function, I have to tell you how it operates on a test
    function (by integraion for Fourier transform).

Lemma: let `f : \mathbb{R}^n \to \mathbb{C}` be any function that:

- polynomially bounded

- Riemann integrable on `[−M, M]` for each `M > 0`.

Then:

.. math::

   f: \phi \in \mathcal{S} \mapsto
     \langle f, \phi \rangle = \int_{-\infty}^{+\infty} f(x) \phi(x) dx

is a tempered distribution (generalized function) induced by `f`.

As the rapidly decreasing functions are "good enough", **most wild functions**
can be considered generalized functions (aka distributions) by defining the
pairing as:

.. math::

   \langle f, \phi \rangle = \int_{-\infty}^{+\infty} f(x) \phi(x) dx

For example, the integral of `sin(2 \pi x)` does not make any sense,
but `\int_{-\infty}^{+\infty} sin(2 \pi x) \phi(x) dx` will converge as `\phi`
is a rapidly decreasing function. Thus `sin(2 \pi x)` can be considered as a
generalized function as I can tell you how it can operate on test functions
(i.e. by integraion).

.. math::

   \langle sin(2 \pi x), \phi \rangle =
   \int_{-\infty}^{+\infty} sin(2 \pi x) \cdot \phi (x) dx

Similarly:

.. math::

   \langle 1, \phi \rangle =
   \int_{-\infty}^{+\infty} 1 \cdot \phi (x) dx

   \langle \Pi, \phi \rangle =
   \int_{-\infty}^{+\infty} \Pi(x) \cdot \phi (x) dx

Fourier Transform of Distribution
=================================

Properties:

.. math::

   T \in \mathcal{S}' \implies
     \mathcal{F} T \in \mathcal{S}'

.. math::

   T \in \mathcal{S}' \implies
     \mathcal{F}^{-1} T \in \mathcal{S}'

Theorem
-------

.. math::

   \phi \in \mathcal{S}, T \in \mathcal{S}' \implies
   \langle \mathcal{F} T, \phi \rangle =
     \langle T, \mathcal{F} \phi \rangle

Proof:

.. math::

   \langle \mathcal{F} T, \phi \rangle & =
     \int_{-\infty}^{+\infty} \mathcal{F} T (x) \phi (x) dx
     \\ & =
     \int_{-\infty}^{+\infty} \left(
       \int_{-\infty}^{+\infty} e^{-2 \pi i x y} T(y) dy
     \right) \phi (x) dx
     \\ & =
     \int_{-\infty}^{+\infty}
       \int_{-\infty}^{+\infty} e^{-2 \pi i x y} \phi(x) T(y) dy dx
     \\ & =
     \int_{-\infty}^{+\infty} \left(
       \int_{-\infty}^{+\infty} e^{-2 \pi i x y} \phi(x) T(y) dx
     \right) dy
     \\ & =
     \int_{-\infty}^{+\infty}
       T(y) \cdot \mathcal{F} \phi (y) dy
     \\ & =
     \langle T, \mathcal{F} \phi \rangle

Similarly:

.. math::

   \phi \in \mathcal{S}, T \in \mathcal{S}' \implies
   \langle \mathcal{F}^{-1} T, \phi \rangle =
     \langle T, \mathcal{F}^{-1} \phi \rangle

Applications
------------

Fourier Transform of **shifted delta function**:

.. math::

   \langle \mathcal{F} \delta_a, \phi \rangle & =
     \langle \delta_a, \mathcal{F} \phi \rangle
     \\ & =
     \mathcal{F} \phi (a)
     \\ & =
     \int_{-\infty}^{+\infty} e^{-2 \pi i a x} \phi(x) dx
     \\ & =
     \langle e^{-2 \pi i a x}, \phi \rangle

.. math::

   \therefore
   \mathcal{F} \delta_a = e^{-2 \pi i a x}

Specifically when `a = 0`:

.. math::

   \mathcal{F} \delta = \mathcal{F} \delta_0 = 1

`\delta` is infinitely concentrated, its Fourier transform `F \delta` is
uniformly spread out

Fourier Transform of **complex exponential function**:

.. math::

   \langle \mathcal{F} e^{2 \pi i a x}, \phi \rangle & =
     \langle e^{2 \pi i a x}, \mathcal{F} \phi \rangle
     \\ & =
     \int_{-\infty}^{+\infty} e^{2 \pi i a x} \mathcal{F} \phi(x) dx
     \\ & =
     \mathcal{F}^{-1} \mathcal{F} \phi(a)
     \\ & =
     \phi(a)
     \\ & =
     \langle \delta_a, \phi \rangle
     
.. math::

   \therefore
   \mathcal{F} e^{2 \pi i a x} = \delta_a

Fourier Transform of **cosine function**:

.. math::

   \mathcal{F} cos(2 \pi a x) & =
     \mathcal{F} (\frac{1}{2} (e^{2 \pi i a x} + e^{-2 \pi i a x}))
     \\ & =
     \frac{1}{2} (\mathcal{F} e^{2 \pi i a x} + \mathcal{F} e^{-2 \pi i a x})
     \\ & =
     \frac{1}{2} (\delta_a + \delta_{-a})

Fourier Transform of **sine function**:

.. math::

   \mathcal{F} sin(2 \pi a x) & =
     \mathcal{F} (\frac{1}{2i} (e^{2 \pi i a x} - e^{-2 \pi i a x}))
     \\ & =
     \frac{1}{2i} (\mathcal{F} e^{2 \pi i a x} - \mathcal{F} e^{-2 \pi i a x})
     \\ & =
     \frac{1}{2i} (\delta_a - \delta_{-a})

Back to :doc:`index`.

.. disqus::
