---
title: Duality
---

# Duality

## Exploration

By exploring the similarity in the formulas for the Fourier transform
and its inverse:

$$
\mathcal{F} f(s) =
  \int_{-\infty}^{+\infty} e^{-2 \pi i s t} f(t) dt
$$

$$
\mathcal{F}^{-1} f(t) =
\int_{-\infty}^{+\infty} e^{2 \pi i s t} f(s) ds
$$

$$
\text{Let } f^- (x) = f(-x)
$$

$$
\therefore
(\mathcal{F} f)^- (x) & =
\int_{-\infty}^{+\infty} e^{-2 \pi i \cdot (-x) \cdot t} f(t) dt
\\ & =
\int_{-\infty}^{+\infty} e^{2 \pi i x t} f(t) dt
\\ & =
\mathcal{F}^{-1} f(x)
$$

$$
\mathcal{F} f^- (x) =
\int_{-\infty}^{+\infty} e^{-2 \pi i s t} f(-t) dt
$$

$$
\text{Let } u = -t \implies t = -u
$$

$$
\therefore
\mathcal{F} f^- (x) & =
\int_{+\infty}^{-\infty} e^{-2 \pi i s \cdot (-u)} f(u) d(-u)
\\ & =
\int_{-\infty}^{+\infty} e^{2 \pi i s u} f(u) du
\\ & =
\mathcal{F}^{-1} f (x)
$$

## Formulas

$$
(\mathcal{F} f)^- = \mathcal{F}^{-1} f
$$

$$
\mathcal{F} f^- = \mathcal{F}^{-1} f
$$

$$
\therefore
(\mathcal{F} f)^- = \mathcal{F} f^-
$$

$$
\text{Let } g^- = f \iff g = f^-
$$

$$
\therefore
\mathcal{F} \mathcal{F} f & =
  \mathcal{F} \mathcal{F} g^-
  \\ & =
  \mathcal{F} \mathcal{F}^{-1} g
  \\ & =
  g
  \\ & =
  f^-
$$

## Application

$$
\DeclareMathOperator{\sinc}{sinc}
\mathcal{F} \sinc = \pi
$$

Proof

$$
\because
\mathcal{F} \pi (x) = \sinc (x)
$$

$$
\therefore
\mathcal{F} \sinc & =
  \mathcal{F} \mathcal{F} \pi
  \\ & =
  \pi^-
  \\ & =
  \pi
$$

$$
\tag*{$\blacksquare$}
$$

---

Back to {doc}`index`.

```{disqus}

```
