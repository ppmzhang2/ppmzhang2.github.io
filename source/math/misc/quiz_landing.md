---
title: "Spacecraft Landing Problem"
---

# Spacecraft Landing Problem

## Quiz

Consider a spacecraft **100 km** above the surface of some planet.
It has just been released from the mother-ship and needs to descend to the
surface carrying two astronauts.
The spacecraft weighs **2000 kg** and has **1000 kg** of fuel onboard.
The gravitational acceleration of the planet is **6 $\text{m/s}^{-2}$**
(on Earth it is 9.8 $\text{m/s}^{-2}$).
Burning **1 kg** of fuel in one second generates **6000 N** of upward thrust.
Your job is to write some python code that decides how much fuel to burn, every
second, so that the spacecraft lands on the surface under the following
constraints:

- The upward acceleration must never be more than **3g** otherwise the astronauts will pass out.

- The vertical velocity must be less than **2 $\text{m/s}$** when the spacecraft lands otherwise you destroy it.

The goal is to land on the surface, under these constraints, with as much fuel in the tank as possible.

## Proof

The solution is trivial if we can recognize that the most fuel-efficient way is
"suicide burn", i.e. free-fall until the last moment (coastal) and burn till
landing.
Yet we need to prove mathematically.

### Constrains

Let **upward** be positive.

- Altitude $x(t)\ge 0$, with $x'(t) = v(t)$.

- Speed $v(t) \le 0$ (downward), with

  $$
  v' (t) = a(t) + g
  $$

  where $g=-6$ and $a(t) \in [0,a_{\max}]$ is the upward acceleration generated
  by thrust, where $a_{\max} = 3 \cdot 9.8 = 29.4$

- Fuel / mass: total mass

  $$
  m(t) &= m_{\text{s}}+m_{\text{f}}(t) \\
  m' (t) &= m_{\text{f}}' (t) = u(t) < 0 \\
  m(0) &= m_{\text{s}} + m_{\text{f}}(0) = 2000 + 1000 = 3000
  $$

  Thrust force is $F = -k \cdot u(t)$ with $k=6000$, so

  $$
  a(t) = \frac{F}{m(t)} = \frac{-k \cdot u(t)}{m(t)} \in [0,a_{\max}].
  $$

  $$
  \therefore
  u(t) \in \left[ -\frac{m(t) \cdot a_{\max}}{k}, 0 \right].
  $$

### Lemma

**Fuel minimization is equivalent to time minimization.**

The objective is to minimize fuel consumption i.e.:

$$
\max m(T) \quad \text{s.t.} \quad
\begin{cases}
x'(t) = v(t)
\\ v'(t) = a(t) + g
\\ x(0) = x_0 = 100000
\\ v(0) = 0
\\ x(T) = 0
\\ v(T) \ge v_{\max} = -2
\\ 0 \le a(t) \le a_{\max} = 29.4
\end{cases}
$$

where $T$ is the landing time.

Note that if $v(T) > -2$, we can always decrease fuel consumption further i.e.
increase $m(T)$ to make $v(T) = -2$ and save more fuel.

$$
\therefore
v(T) = v_{\max} = -2
$$

$$
\because
m' (t) = u(t) = -\frac{m(t) \cdot a(t)}{k}
$$

$$
\therefore
\frac{m'(t)}{m(t)} = -\frac{a(t)}{k}
$$

$$
\therefore
m(T) = m(0) \exp \left(
  -\frac{1}{k} \int_0^T a(t) dt
\right)
$$

Thus the objective is equivalent to:

$$
\min \int_0^T a(t) dt \quad \text{s.t.} \quad
\begin{cases}
x'(t) = v(t)
\\ v'(t) = a(t) + g
\\ x(0) = x_0
\\ v(0) = 0
\\ x(T) = 0
\\ v(T) = v_{\max}
\\ 0 \le a(t) \le a_{\max}
\end{cases}
$$

$$
\because
v'(t) = g+a(t), \, v(0)=0, \, v(T)=v_{\max}
$$

$$
\therefore
v(t) = g \cdot t + \int_0^t a(s)ds.
$$

$$
\therefore
\int_0^T a(t) dt = - g \cdot T + v_{\max}
$$

$$
\therefore
\min \int_0^T a(t) dt \Longleftrightarrow \min T
\tag{1}
$$

$$
\because
x'(t)=v(t), \, x(0)=x_0, \, x(T)=0
$$

$$
\therefore
0 = x_0 + \int_0^T v(t) dt
$$

$$
\therefore
x_0 &= -\int_0^T v(t) dt \\ &=
- \frac{1}{2} g \cdot T^2 - \int_0^T \int_0^t a(s) ds dt \\ &=
- \frac{1}{2} g \cdot T^2 - \int\int_{0\le s\le t\le T} a(s) ds dt \\ &=
- \frac{1}{2} g \cdot T^2 - \int_0^T (\int_s^T dt) a(s) ds \\ &=
- \frac{1}{2} g \cdot T^2 - \int_0^T (T-t) a(t) dt
$$

$$
\therefore
\int_0^T (T-t) a(t) dt = -\frac{1}{2} g \cdot T^2 - x_0
\tag{2}
$$

Note that the LHS of (2) looks like a "1st order moment" of $a(t)$.
We define it as:

$$
J= \int_0^T (T-t) a(t) dt .
$$

$$
\therefore
J = -\frac{1}{2} g \cdot T^2 - x_0.
\tag{3}
$$

$$
\therefore
\min J \Longleftrightarrow \min T
\tag{4}
$$

Combining (1) and (4), the original problem is equivalent to:

$$
\min J[a] \quad \text{s.t.} \quad
\begin{cases}
x'(t) = v(t)
\\ v'(t) = a(t) + g
\\ x(0) = x_0
\\ v(0) = 0
\\ x(T) = 0
\\ v(T) = v_{\max}
\\ 0 \le a(t) \le a_{\max}
\end{cases}
$$

### KKT

Re-arrange the problem as:

$$
\min_{a} J[a] = \int_0^T (T-t) a(t) dt \quad \text{s.t.} \quad
\int_0^T a(t) dt = A(T); \,
0 \le a(t) \le a_{\max}
$$

where

$$
A(T) = -g \cdot T + v_{\max}
$$

which is a perfect setup for KKT.
With scalar $\lambda$ and functions $\mu_1(t), \mu_2(t) \ge 0$ as
Lagrange multipliers, the Lagrangian is:

$$
\mathcal{L}[a, \lambda, \mu_1, \mu_2] =
\int_0^T (T-t) a dt +
\lambda \left( \int_0^T a dt - A(T) \right) +
\int_0^T \mu_1(t) (-a) dt +
\int_0^T \mu_2(t) (a - a_{\max}) dt
$$

For $\text{a.e.} \, t \in [0,T]$:

- stationarity:

  $$
  (T-t) + \lambda - \mu_1(t) + \mu_2(t) = 0
  $$

- complementary slackness:

  $$
  \mu_1(t) \cdot a(t) = 0 \\
  \mu_2(t) \cdot (a(t) - a_{\max}) = 0
  $$

Define $w (t) = (T-t) + \lambda$, we have three cases:

- When $a(t) = 0$, $\mu_2 (t) = 0$ due to complementary slackness

  $$
  w (t) = \mu_1(t) \ge 0 \implies t \le T + \lambda
  $$

- When $a(t) = a_{\max}$, $\mu_1 (t) = 0$ due to complementary slackness

  $$
  w (t) = -\mu_2(t) \le 0 \implies t \ge T + \lambda
  $$

- When $0 < a(t) < a_{\max}$, $\mu_1 (t) = \mu_2 (t) = 0$ due to complementary

  $$
  w (t) = 0 \implies t = T + \lambda
  $$

Since $w (t)$ is monotonically decreasing in $t$, there exists exactly one
switching time $t^* = T + \lambda$.

$$
\therefore
a(t) =
\begin{cases}
0, & t < t^* \\
a_{\max}, & t > t^*
\end{cases}
$$

---

Back to {doc}`index`.

```{disqus}

```
