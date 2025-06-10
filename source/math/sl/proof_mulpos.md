---
title: "Multiplying Positives Makes a Positive"
---

# Multiplying Positives Makes a Positive

**Proposition**

$$\forall a > 0, \forall b > 0: \quad ab > 0.$$

## Lemma: Positive Integer Case

**Statement**

$$
\begin{aligned}
& \forall a > 0, \forall b > 0 \quad (b \in \mathbb{N}): \quad ab > 0
\\\\
& \forall a < 0, \forall b > 0 \quad (b \in \mathbb{N}): \quad ab < 0
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

- **Inductive Step**: Assume $\forall a > 0, \exists b = n \in \mathbb{N} \quad S.T. ab > 0$.
  Then for $b = n+1$:

  $$
  a(n+1) = an + a > 0
  \quad
  (\text{Distributive Property})
  $$

  since $an > 0$ (induction hypothesis) and $a > 0$.

By induction, the statement holds for all $b \in \mathbb{N}$.

Similar reasoning applies for $a < 0$ and $b \in \mathbb{N}$, yielding $ab < 0$.

## Theorem 1: Positive Rational Case

$$
\forall a > 0, \forall b > 0 \quad (b \in \mathbb{Q}): \quad ab > 0
$$

**Proof** (by contradiction):

Suppose the theorem is false, i.e.:

$$
\exists a_0 > 0, \exists b_0 > 0 \quad (b_0 \in \mathbb{Q})
\quad S.T. a_0 b_0 < 0
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

## Theorem 2: Positive Irrational Case

$$
\forall a > 0, \forall b > 0 \quad (b \in \mathbb{R} \setminus \mathbb{Q}):
\quad ab > 0
$$

**Proof**:

Let $b \in \mathbb{R} \setminus \mathbb{Q}$, with $b > 0$.
Define a rational approximation of $b$ by truncating to $n$ decimal digits:

$$
r(b, n) = \text{rational approximation of } b \text{ to } n \text{ decimal digits}
$$

Example:

$$
r(\pi,n) = 3. \overbrace{1415926 \cdots}^n
$$

and define the remainder:

$$
\xi(b, n) = b - r(b, n)
$$

Then:

$$
ab = a \cdot r(b, n) + a \cdot \xi(b, n)
\quad
(\text{Distributive Property})
$$

Since $r(b, n) \in \mathbb{Q}$ and $r(b, n) > 0$, by Theorem 1:

$$
a \cdot r(b, n) > 0
$$

Let $\epsilon > 0$ be such that:

$$
0 < \epsilon < \frac{1}{2} a \cdot r(b, n)
$$

$$
\because
\lim_{n \to \infty} \xi(b, n) = 0
$$

$$
\therefore
\lim_{n \to \infty} | a \cdot \xi(b, n) | = 0
\quad
(\text{Zero Property})
$$

$$
\therefore
\exists N \in \mathbb{N} \quad S.T. \forall n > N: \quad
|a \cdot \xi(b, n)| < \epsilon
$$

$$
\therefore
ab = a \cdot r(b, n) + a \cdot \xi(b, n) >
a \cdot r(b, n) - |a \cdot \xi(b, n)| >
\frac{1}{2} a \cdot r(b, n) > 0
$$

## Conclusion

From the lemma and theorems above, the proposition holds.

$$\tag*{$\blacksquare$}$$

---

Back to {doc}`index`.

```{disqus}

```
