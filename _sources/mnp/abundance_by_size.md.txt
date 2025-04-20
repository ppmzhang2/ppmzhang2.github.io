---
title: Size-Based Prediction of MnP Abundance
---

# Size-Based Prediction of MnP Abundance

Across water, soil, sediment, sludge, and air, there is a strong inverse power-law relationship:

$$
n(x) \propto x^{-\alpha}
$$

Where:

- $x$ is the characteristic size of the particles (e.g., geometric mean of the bin).
- $n(x)$ is the number of MP particles of size $x$ (in $\mu m$)
- the exponent $\alpha$ is a positive constant typically between 1 and 2

The raw power-law distribution is:

$$
n(x) = b \cdot x^{-\alpha}
$$

Taking logarithms of both sides yields a linear form:

$$
\log(n) = -\alpha \log(x) + \log(b)
$$

Based on this study, particles are only observed in a limited size range.
Therefore, both $x$ and $n(x)$ should be normalized to the bin width:

$$
\hat n = \frac{n}{x_{UB} - x_{LB}}
$$

$$
\hat x = \sqrt{x_{UB} \cdot x_{LB}}
$$

Where:

- $n$: number of particles in the bin
- $x_{UB}, x_{LB}$: upper and lower size limits of the bin,
- $\hat n$: density of particles in a specific size range
- $\hat x$: geometric mean of the bin size

After these corrections, the relationship becomes:

$$
\log (\hat n) = -\alpha \log (\hat x) + \log (b)
\tag{1}
$$

Exponentiating both sides:

$$
\hat n = b \cdot \hat x^{-\alpha}
$$

Or equivalently:

$$
n =
  b \cdot (x_{UB} - x_{LB}) \cdot
  \left( \sqrt{x_{UB} \cdot x_{LB}} \right)^{-\alpha}
\tag{2}
$$

Suppose the number of particles $\hat n_{\text{ref}}$ in a reference bin $[x_{LB.\text{ref}}, x_{UB.\text{ref}}]$ is known, to predict the number of particles $\hat n_{\text{pred}}$ in another bin $[x_{LB.\text{pred}}, x_{UB.\text{pred}}]$ with the same constants $\alpha$ and $b$, apply Equation (2) to both bins

$$
n_{\text{pred}} =
  b \cdot (x_{UB.\text{pred}} - x_{LB.\text{pred}}) \cdot
  \left( \sqrt{x_{UB.\text{pred}} \cdot x_{LB.\text{pred}}} \right)^{-\alpha}
$$

$$
n_{\text{ref}} =
  b \cdot (x_{UB.\text{ref}} - x_{LB.\text{ref}}) \cdot
  \left( \sqrt{x_{UB.\text{ref}} \cdot x_{LB.\text{ref}}} \right)^{-\alpha}
$$

Take the ratio:

$$
\frac{n_{\text{pred}}}{n_{\text{ref}}} =
  \frac{(x_{UB.\text{pred}} - x_{LB.\text{pred}}) \cdot
    \left(
      \sqrt{x_{UB.\text{pred}} \cdot x_{LB.\text{pred}}}
    \right)^{-\alpha}
  }
  {(x_{UB.\text{ref}} - x_{LB.\text{ref}}) \cdot
    \left(
      \sqrt{x_{UB.\text{ref}} \cdot x_{LB.\text{ref}}}
    \right)^{-\alpha}
  }
$$

$$
\therefore
n_{\text{pred}} =
n_{\text{ref}} \cdot
\left(
\frac{x_{UB.\text{pred}} - x_{LB.\text{pred}}}{x_{UB.\text{ref}} - x_{LB.\text{ref}}}
\right)
\cdot
\left(
\frac{x_{UB.\text{pred}} \cdot x_{LB.\text{pred}}}{x_{UB.\text{ref}} \cdot x_{LB.\text{ref}}}
\right)^{- \alpha / 2}
$$

Back to {doc}`index`.

```{disqus}

```
