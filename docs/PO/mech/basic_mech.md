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


### Slightly Harder Case: $F_D$ proportional to $v^2$

