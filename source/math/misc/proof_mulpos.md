---
title: "Multiplying Positives Makes a Positive"
---

# Multiplying Positives Makes a Positive

**Proposition**

$$
\forall a > 0, \forall b > 0
\quad (a, b \in \mathbb{R}):
\quad ab > 0.
$$

## Verifying for Rationals

**Lemma**:

$$
\begin{aligned}
& \forall a > 0, \forall b > 0
\quad (a \in \mathbb{R}, b \in \mathbb{N}):
\quad ab > 0
\\\\
& \forall a < 0, \forall b > 0
\quad (a \in \mathbb{R}, b \in \mathbb{N}):
\quad ab < 0
\end{aligned}
$$

**Proof** (by induction on $b$):

We prove the first part of the lemma. The second part follows similarly.

- **Base Case**: Let $b = 1$. Then:

  $$
  ab = a \cdot 1 = a > 0
  \quad
  (\text{Identity Element})
  $$

- **Inductive Step**: Assume for some $n \in \mathbb{N}$, we have:

  $$
  a n > 0
  $$

  We need to show that $a (n + 1) > 0$.

  $$
  a(n + 1) = a n + a
  \quad
  (\text{Distributive Property})
  $$

  since $an > 0$ and $a > 0$, we have:

  $$
  a n + a > 0
  $$

  Thus, $a(n + 1) > 0$.

By induction, the statement holds for all $b \in \mathbb{N}$.

Similar reasoning applies for $a < 0$ and $b \in \mathbb{N}$, yielding $ab < 0$.

$$\tag*{$\blacksquare$}$$

**Theorem 1**:

$$
\forall a > 0, \forall b > 0
\quad (a \in \mathbb{R}, b \in \mathbb{Q}):
\quad ab > 0
$$

**Proof** (by contradiction):

Suppose the theorem is false, i.e.:

$$
\exists a_0 > 0, \exists b_0 > 0
\quad (a_0 \in \mathbb{R}, b_0 \in \mathbb{Q}):
\quad S.T. \quad
a_0 b_0 < 0
$$

Let $b_0 = \frac{m}{n}$, where $m, n \in \mathbb{N}$.

$$
\therefore
a_0 b_0 = \frac{m a_0}{n}
$$

$$
\therefore
n a_0 b_0 = m a_0
$$

Since $a_0 > 0$ and $m \in \mathbb{N}$, Thus by the lemma:

$$
n a_0 b_0 = m a_0 > 0
$$

However, since $a_0 b_0 < 0$ (assumption) and $n \in \mathbb{N}$, we also have by the lemma:

$$
n a_0 b_0 < 0
$$

This leads to a contradiction.
Therefore, our assumption is false, and the theorem holds.

$$\tag*{$\blacksquare$}$$

## The Proof

Before extending to the real numbers, we need to establish one key points:

- the limit of a bounded sequence of positive rational numbers is strictly positive.

**Theorem 2**:

If a real sequence $S_n \to S$ as $n \to \infty$, then:

$$
S_n > c > 0
\quad (\forall n \ge N)
\implies
S \ge c > 0
$$

**Proof** (by contradiction):

Assume the opposite, i.e.

$$
S < c
$$

$$
\therefore
c - S > 0
$$

Select $\epsilon = c - S$, we have:

$$
\exists M \in \mathbb{N} \quad S.T. \quad
\forall n \ge M:
\quad |S_n - S| < c - S
$$

$$
\therefore
S_n < c - S + S = c
$$

According to the assumption, we also have:

$$
S_n > c
\quad (\forall n \ge N)
$$

Thus $\forall n \ge \max(N, M)$, $S_n$ should be both greater than $c$ and less
than $c$, which is a contradiction.

Therefore, our assumption is false, and the theorem holds.

$$\tag*{$\blacksquare$}$$

Now we can prove the proposition.

**Proof**:

Construct a sequence of rational numbers $b_n \in \mathbb{Q}$ such that:

$$
\begin{aligned}
& \forall n \in \mathbb{N}: b_n > 0
\\\\
& \lim_{n \to \infty} b_n = b
\end{aligned}
$$

This is possible by the density of $\mathbb{Q}$ in $\mathbb{R}$.
For the same reason, we can select:

$$
q \in \mathbb{Q} \quad S.T. \quad 0 < q < b
$$

$$
\because
\lim_{n \to \infty} b_n = b
$$

$$
\therefore
\exists N \in \mathbb{N} \quad
S.T. \quad \forall n \ge N: \quad
b_n > q
$$

$$
\therefore
b_n - q > 0
$$

Since $a > 0$, $b_n - q > 0$, and $b_n - q \in \mathbb{Q}$,
applying **Theorem 1**:

$$
a (b_n - q) > 0
$$

$$
\therefore
a b_n > a q > 0
\quad
\forall n \ge N
$$

Define function:

$$
f(x) = a x
$$

Since $f(x)$ is continuous for $x \in \mathbb{R}$, we have:

$$
\lim_{n \to \infty} f(b_n) = \lim_{n \to \infty} a b_n = ab
$$

Let sequence $S_n = a b_n$.
Then $S_n \to ab$ as $n \to \infty$.
Also since $S_n > a q > 0$ for all $n \ge N$, applying **Theorem 2**:

$$
ab \ge a q > 0
$$

$$\tag*{$\blacksquare$}$$

---

Back to {doc}`index`.

```{disqus}

```
