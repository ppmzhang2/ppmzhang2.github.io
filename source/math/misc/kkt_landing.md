---
title: "Spacecraft Landing Problem"
---

# KKT Example - Spacecraft Landing Problem

We demonstrate with a
[spacecraft landing problem](https://www.bodekerscientific.com/other/python-programming-challenge/dunstan-high-school-python-programming-challenge):

> Consider a spacecraft **100 km** above the surface of some planet.
> It has just been released from the mother-ship and needs to descend to the
> surface carrying two astronauts.
> The spacecraft weighs **2000 kg** and has **1000 kg** of fuel onboard.
> The gravitational acceleration of the planet is **6 $\text{m/s}^{-2}$**
> (on Earth it is 9.8 $\text{m/s}^{-2}$).
> Burning **1 kg** of fuel in one second generates **6000 N** of upward thrust.
> Your job is to write some python code that decides how much fuel to burn,
> every second, so that the spacecraft lands on the surface under the following
> constraints:
> 
> - The upward acceleration must never be more than **3g** otherwise the
>   astronauts will pass out.
> 
> - The vertical velocity must be less than **2 $\text{m/s}$** when the
>   spacecraft lands otherwise you destroy it.
> 
> The goal is to land on the surface, under these constraints, with as much
> fuel in the tank as possible.

## Proof

The solution is trivial if we can recognize that the most fuel-efficient way is
"suicide burn", i.e. free-fall until the last moment then burn till landing.
Yet as we always assume that the rigorous police is around we need to prove it.

### Constraint

Formalize the constraints (let upwards be positive):

- Altitude $x(t)\ge 0$:

  $$
  x'(t) = v(t)
  $$

- Speed $v(t) \le 0$ (downward):

  $$
  v' (t) = a(t) + g
  $$

  where $g=-6$ and $a(t) \in [0,a_{\max}]$ is the upward acceleration generated
  by thrust, where $a_{\max} = 3 \cdot 9.8 = 29.4$

Let $T$ be the landing time. The boundary data:

$$
\begin{cases}
x(0) = x_0 = 100000
\\ x(T) = 0
\\ v(0) = 0
\\ v(T) \ge v_{\max} = -2
\end{cases}
$$

Note that if $v(T) > -2$, we can always decrease fuel consumption further i.e.
increase $m(T)$ to make $v(T) = -2$ and save more fuel.

$$
\therefore
v(T) = v_{\max} = -2
$$

### Objective

The objective is about minimizing the usage of fuel i.e.:

$$
\max m(T)
$$

Total mass is the sum of spacecraft and fuel:

$$
m(t) &= m_{\text{s}}+m_{\text{f}}(t) \\
m' (t) &= m_{\text{f}}' (t) = u(t) < 0 \\
m(0) &= m_{\text{s}} + m_{\text{f}}(0) = 2000 + 1000 = 3000
$$

Thrust force is $F = -k \cdot u(t)$ with $k=6000$, so

$$
a(t) = \frac{F}{m(t)} = \frac{-k \cdot u(t)}{m(t)} \in [0,a_{\max}]
$$

$$
\therefore
m' (t) = u(t) = -\frac{m(t) \cdot a(t)}{k}
$$

$$
\therefore
m(t) = m(0) \exp \left(
  -\frac{1}{k} \int_0^t a(s) ds
\right)
$$

$$
\therefore
m(T) = m(0) \exp \left(
  -\frac{1}{k} \int_0^T a(t) dt
\right)
$$

Now the objective is equivalent to:

$$
\min \int_0^T a(t) dt
$$

The knowns include two integrals: one is about speed, the other is about position.
First, let's look at speed $v(t)$:

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
\tag{1}
$$

This means the integral is totally determined by $T$.
We denote it as $A(T)$:

$$
\therefore
A(T) = - g \cdot T + v_{\max}
$$

Also, $A(T)$ is monotonically increasing in $T$.

$$
\therefore
\min \int_0^T a(t) dt \Longleftrightarrow \min T
\tag{2}
$$

Now look at position $x(t)$:

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
\tag{3}
$$

Note that (3) is also monotonically increasing in $T$.

$$
\therefore
\min T \Longleftrightarrow \min \int_0^T (T-t) a(t) dt
\tag{4}
$$

Combining (1), (2) and (4) and the bound constraints, we have the new
objective:

$$
\min_{a} \int_0^T (T-t) a(t) dt \quad \text{s.t.} \quad
\int_0^T a(t) dt = A(T); \,
0 \le a(t) \le a_{\max}
$$

### KKT Conditions

By fixing $T$, the current problem is a perfect setup for KKT.
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

which is exactly the "suicide burn" strategy.

$$
\tag*{$\blacksquare$}
$$

---

Back to {doc}`index`.

```{disqus}

```
