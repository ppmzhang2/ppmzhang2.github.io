---
title: Policy Gradient
---

# Policy Gradient

## Trust Region Policy Optimization (TRPO)

$$max_{\theta} E [\frac{p(x | \theta)}{p(x | \theta_{old})} A]$$

which is subject to:

$$E[ KL [p_{old}, p] ] \le \delta$$

## Proximal Policy Optimization (PPO)

$$r = \frac{p(x | \theta)}{p(x | \theta_{old})}$$

$$max_{\theta} E [min[r A, clip[r, 1-\epsilon, 1+\epsilon]A]]$$

---

Back to {doc}`index`.

```{disqus}

```
