---
title: Important Examples
---

# Important Examples

## General Tips

- Integration techniques
  - integration by substitution
  - integration by parts

## Rectangular Function

$$
\DeclareMathOperator{\sinc}{sinc}
\pi (t) =
\begin{cases}
  1 & -0.5 \le t \le 0.5
  \\
  0 & t < -0.5 \lor t > 0.5
\end{cases}
\implies
\mathcal{F} \pi (s) = \sinc (s)
$$

Proof:

$$
\mathcal{F} \pi (s) & =
  \int_{-\infty}^{+\infty} e^{-2 \pi i s t} \pi(t) dt
  \\ & =
  \int_{-0.5}^{0.5} e^{-2 \pi i s t} dt
  \\ & =
  -\frac{1}{2 \pi i s} \cdot e^{-2 \pi i s t} |_{-0.5}^{0.5}
  \\ & =
  -\frac{1}{2 \pi i s} (e^{- \pi i s} - e^{\pi i s})
  \\ & =
  -\frac{1}{2 \pi i s}
    (\cos (\pi s) - i \cdot \sin (\pi s) - \cos (\pi s) - i \cdot \sin (\pi s))
  \\ & =
  -\frac{- 2 i \cdot \sin (\pi s)}{2 \pi i s}
  \\ & =
  \frac{\sin (\pi s)}{\pi s}
  \\ & =
  \sinc(x)
$$

$$\tag*{$\blacksquare$}$$

## Triangle Function

$$
\Lambda (t) =
\begin{cases}
  t + 1 & -1 \le t \lt 0
  \\
  -t + 1 & 0 \le t \le 1
  \\
  0 & t < -1 \lor t > 1
\end{cases}
\implies
\mathcal{F} \Lambda (s) = \sinc^2 (s)
$$

Proof:

$$
\mathcal{F} \Lambda (s) & =
  \int_{-\infty}^{\infty} e^{-2 \pi i s t} \Lambda (t) dt
  \\ & =
  \int_{-1}^0 e^{-2 \pi i s t} (t + 1) dt +
  \int_0^1 e^{-2 \pi i s t} (-t + 1) dt
  \\ & =
  \int_{-1}^0 e^{-2 \pi i s t} t dt +
  \int_{-1}^0 e^{-2 \pi i s t} dt -
  \int_0^1 e^{-2 \pi i s t} t dt +
  \int_0^1 e^{-2 \pi i s t} dt
  \\ & =
  \int_{-1}^0 e^{-2 \pi i s t} t dt -
  \int_0^1 e^{-2 \pi i s t} t dt +
  \int_{-1}^1 e^{-2 \pi i s t} dt
$$

$$
\because
\int_{-1}^0 e^{-2 \pi i s t} t dt -
\int_0^1 e^{-2 \pi i s t} t dt & =
  \int_{-1}^0 e^{-2 \pi i s t} t dt +
  \int_1^0 e^{-2 \pi i s t} t dt
  \\ & =
  \int_{-1}^0 e^{-2 \pi i s t} t dt +
  \int_{-1}^0 e^{-2 \pi i s (-u)} (-u) d(-u)
  \\ & =
  \int_{-1}^0 e^{-2 \pi i s t} t dt +
  \int_{-1}^0 e^{2 \pi i s u} u du
  \\ & =
  \int_{-1}^0 (e^{-2 \pi i s t} + e^{2 \pi i s t}) t dt
  \\ & =
  \int_{-1}^0 (
    \cos (2 \pi s t) -
    i \cdot \sin (2 \pi s t) +
    \cos (2 \pi s t) +
    i \cdot \sin (2 \pi s t)) t dt
  \\ & =
  2 \int_{-1}^0 \cos (2 \pi s t) t dt
  \\ & =
  2 \frac{1}{2 \pi s} \int_{-1}^0 t d \sin (2 \pi s t)
  \\ & =
  \frac{1}{\pi s} (t \cdot \sin (2 \pi s t) |_{-1}^0 -
  \int_{-1}^0 \sin (2 \pi s t) dt)
  \\ & =
  - \frac{-1 \cdot \sin (2 \pi s \cdot (-1))}{\pi s} -
  \frac{1}{-2 \pi^2 s^2} \cos (2 \pi s t) |_{-1}^0
  \\ & =
  - \frac{\sin (2 \pi s)}{\pi s} +
  \frac{1}{2 \pi^2 s^2} (1 - \cos (2 \pi s))
  \\ & =
  - \frac{\sin (2 \pi s)}{\pi s} +
  \frac{\sin^2 (\pi s)}{\pi^2 s^2}
  ,
$$

$$
\int_{-1}^1 e^{-2 \pi i s t} dt & =
  -\frac{1}{2 \pi i s} \cdot e^{-2 \pi i s t} |_{-1}^{1}
  \\ & =
  -\frac{1}{2 \pi i s} (e^{-2 \pi i s} - e^{2 \pi i s})
  \\ & =
  -\frac{1}{2 \pi i s}
    (\cos (2 \pi s) - i \cdot \sin (2 \pi s) - \cos (2 \pi s) - i \cdot \sin (2 \pi s))
  \\ & =
  -\frac{-2 i \cdot \sin(2 \pi s)}{2 \pi i s}
  \\ & =
  \frac{\sin (2 \pi s)}{\pi s}
$$

$$
\therefore
\mathcal{F} \Lambda (s)
  & =
  \int_{-1}^0 e^{-2 \pi i s t} t dt -
  \int_0^1 e^{-2 \pi i s t} t dt +
  \int_{-1}^1 e^{-2 \pi i s t} dt
  \\ &=
  - \frac{\sin (2 \pi s)}{\pi s} +
  \frac{\sin^2 (\pi s)}{\pi^2 s^2} +
  \frac{\sin (2 \pi s)}{\pi s}
  \\ & =
  \frac{\sin^2 (\pi s)}{\pi^2 s^2}
  \\ & =
  \sinc^2 (s)
$$

$$\tag*{$\blacksquare$}$$

## Gaussian function

$$
f (t) = e^{- \pi t^2}
\implies
\mathcal{F} f (s) = f (s)
$$

Proof:

$$
F(s) = \mathcal{F} f (s)
  =
  \int_{-\infty}^{\infty} e^{-2 \pi i s t} f (t) dt
  =
  \int_{-\infty}^{\infty} e^{-2 \pi i s t} e^{- \pi t^2} dt
$$

$$
F'(s) & = \int_{-\infty}^{\infty}
  \frac{d}{ds} e^{-2 \pi i s t} e^{- \pi t^2} dt
  \\ & =
  \int_{-\infty}^{\infty}
    e^{- \pi t^2} \frac{d}{ds} e^{-2 \pi i s t} dt
  \\ & =
  \int_{-\infty}^{\infty}
    e^{- \pi t^2} \cdot (-2 \pi i t) \cdot e^{-2 \pi i s t} dt
  \\ & =
  i \cdot \int_{-\infty}^{\infty}
    e^{-2 \pi i s t} \cdot (-2 \pi t) \cdot e^{- \pi t^2} dt
  \\ & =
  i \cdot \int_{-\infty}^{\infty}
    e^{-2 \pi i s t} d e^{- \pi t^2}
  \\ & =
  i \cdot e^{-2 \pi i s t} \cdot e^{- \pi t^2} |_{-\infty}^{+\infty} -
  i \cdot \int_{-\infty}^{+\infty}
    e^{- \pi t^2} d e^{-2 \pi i s t}
$$

$$
\because
\lim_{t \to -\infty} e^{-2 \pi i s t} \cdot e^{- \pi t^2} & =
  \lim_{t \to +\infty} e^{2 \pi i s t} \cdot e^{- \pi t^2}
  \\ & =
  \lim_{t \to +\infty} \frac{e^{2 \pi i s t}}{e^{\pi t^2}}
  \\ & =
  \lim_{t \to +\infty}
    \frac{\cos (2 \pi s t) + i \cdot \sin(2 \pi s t)}{e^{\pi t^2}}
  \\ & =
  0,
$$

$$
\lim_{t \to +\infty} e^{-2 \pi i s t} \cdot e^{- \pi t^2} & =
  \lim_{t \to +\infty} e^{-2 \pi i s t} \cdot e^{- \pi t^2}
  \\ & =
  \lim_{t \to +\infty} \frac{e^{-2 \pi i s t}}{e^{\pi t^2}}
  \\ & =
  \lim_{t \to +\infty}
    \frac{\cos (2 \pi s t) - i \cdot \sin(2 \pi s t)}{e^{\pi t^2}}
  \\ & =
  0
$$

$$
\therefore
F'(s) & =
  i \cdot e^{-2 \pi i s t} \cdot e^{- \pi t^2} |_{-\infty}^{+\infty} -
  i \cdot \int_{-\infty}^{+\infty}
    e^{- \pi t^2} d e^{-2 \pi i s t}
  \\ & =
  -i \cdot \int_{-\infty}^{+\infty}
    e^{- \pi t^2} d e^{-2 \pi i s t}
  \\ & =
  -i \cdot \int_{-\infty}^{+\infty}
    (-2 \pi i s) \cdot e^{- \pi t^2} \cdot e^{-2 \pi i s t} dt
  \\ & =
  -2 \pi s \int_{-\infty}^{+\infty}
    e^{-2 \pi i s t} \cdot e^{- \pi t^2} dt
  \\ & =
  -2 \pi s \cdot F(s)
$$

$$
\therefore
\mathcal{F} f(s) & =
  F(s)
  =
  e^{- \pi s^2}
  \\ & =
  f(s)
$$

$$\tag*{$\blacksquare$}$$

---

Back to {doc}`index`.

```{disqus}

```
