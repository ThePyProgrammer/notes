# Basic Mechanics

## Projectile Motion with Drag

### Easy Case: $F_D$ proportional to $v$

We know the following:

$$
\begin{align*}
F_D &= (-\alpha mv)\hat v \\
F_g &= (-mg) \begin{pmatrix}0\\1\end{pmatrix} \\
F_\text{net} = m \frac{d\vec v}{dt} &= F_D + F_g \\
&= -\alpha m\begin{pmatrix}v_x\\v_y\end{pmatrix} -mg \begin{pmatrix}0\\1\end{pmatrix} \\
\frac{d\vec v}{dt} = \begin{pmatrix}\dot v_x \\\dot v_y\end{pmatrix} &= \begin{pmatrix}-\alpha v_x\\-\alpha v_y -g\end{pmatrix}
\end{align*}
$$

We then solve the two ODEs separately (since they're not coupled, thank god)

$$
\begin{align*}
\frac{dv_x}{dt} &= -\alpha v_x \\
\int_{u_x}^{v_x} \frac{dv_x}{v_x} &= -\alpha \int_0^t dt \\
\ln \left( \frac{v_x}{u_x} \right) &= -\alpha t \\
v_x &= u_x e^{-\alpha t}
\end{align*}
$$

$$
\begin{align*}
\frac{dv_y}{dt} &= -\alpha v_y -g \\
\int_{u_y}^{v_y} \frac{dv_y}{v_y + \frac{g}{\alpha}} &= -\alpha \int_0^t dt \\
\ln \left( \frac{v_y + \frac{g}{\alpha}}{u_y + \frac{g}{\alpha}} \right) &= -\alpha t \\
v_y + \frac{g}{\alpha} &= \left(u_y + \frac{g}{\alpha}\right) e^{-\alpha t} \\
v_y &= \left(u_y + \frac{g}{\alpha} \right) e^{-\alpha t} - \frac{g}{\alpha}
\end{align*}
$$


You can then integrate to get $x$ and $y$, assuming you start at the origin $O(x, y)$:

$$
\begin{align*}
x &= \int_0^t v_x \text{ }dt \\
&= u_x \int_0^t e^{-\alpha t}\text{ }dt \\
&= -\frac{u_x}\alpha \left[e^{-\alpha t} \right]_0^t \\
&= \frac{u_x}\alpha \left(1 - e^{-\alpha t} \right)
\end{align*}
$$

As for $y$:

$$
\begin{align*}
y &= \int_0^t v_y \text{ }dt \\
&= \left(u_y + \frac{g}\alpha \right) \int_0^t e^{-\alpha t}\text{ }dt - \frac{g}{\alpha} \int_0^t dt \\
&= -\frac{1}\alpha\left(u_y + \frac{g}\alpha \right) \left[e^{-\alpha t} \right]_0^t - \frac{gt}{\alpha} \\
&= \frac{1}\alpha\left(u_y + \frac{g}\alpha \right) \left(1 - e^{-\alpha t} \right) - \frac{gt}{\alpha}
\end{align*}
$$

When $y = 0$, we can therefore use this very formula to get values:

$$
\begin{align*}
\frac{1}\alpha\left(u_y + \frac{g}\alpha \right) \left(1 - e^{-\alpha t} \right) - \frac{gt}{\alpha} &= 0 \\
\left(u_y + \frac{g}\alpha \right) \left(1 - e^{-\alpha t} \right) &= gt \\
\end{align*}
$$

I won't solve this because I don't know how to do so :).

### Slightly Harder Case: $F_D$ proportional to $v^2$

$$
\begin{align*}
F_D &= (-\alpha mv^2)\hat v \\
F_g &= (-mg) \begin{pmatrix}0\\1\end{pmatrix} \\
F_\text{net} = m \frac{d\vec v}{dt} &= F_D + F_g \\
&= -\alpha m \sqrt{v_x^2 + v_y^2} \begin{pmatrix}v_x\\v_y\end{pmatrix} -mg \begin{pmatrix}0\\1\end{pmatrix} \\
\frac{d\vec v}{dt} = \begin{pmatrix}\dot v_x \\\dot v_y\end{pmatrix} &= \begin{pmatrix}-\alpha v_x\sqrt{v_x^2 + v_y^2}\\-\alpha v_y\sqrt{v_x^2 + v_y^2} -g\end{pmatrix}
\end{align*}
$$


This gives rise to a set of coupled expressions, which does not sound fun to solve, and hence I won't :).

## 



