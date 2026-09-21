# 1D Particle Motion by DEM (Discrete Element Method)

Solution with Python.

This example calculates the vertical motion of a single particle under gravity using a simple time-integration scheme.

##Equation of Motion

Newton's second law:

$$ F = ma $$

For a particle moving only in the vertical direction:

$$ a_y = \frac{F_y}{m} $$

If only gravity is considered:

$$ a_y = -g $$

The position and velocity are updated using:

$$ y_{t+\Delta t}=y_t+v_t\Delta t+\frac{1}{2}a_t(\Delta t)^2 $$

$$ v_{t+\Delta t}=v_t+\frac{1}{2}a_t\Delta t+\frac{1}{2}a_{t+\Delta t}\Delta t $$

Assumptions

One particle

One-dimensional vertical motion

Gravity only

No wall-particle interaction

No particle-particle interaction

No friction

No rotational motion

Python Code

import numpy as np
import matplotlib.pyplot as plt

n = 1        # Number of particles [ea]
dt = 1e-3    # Time step length [sec]
y_loc = 0.1  # Initial particle height [m]
grav = 9.8   # Gravitational acceleration [m/s^2]

i = 1
time = 0
timestep = 10

p_y = np.zeros(n)
p_vy = np.zeros(n)
p_ay = np.zeros(n)
p_fy = np.zeros(n)

p_y[0] = y_loc
p_ay[0] = 0
p_vy[0] = 0

for t in range(timestep):
    time += dt

    p_y[0] += dt * p_vy[0] + 0.5 * dt * dt * p_ay[0]
    p_vy[0] += 0.5 * dt * p_ay[0]
    p_ay[0] -= grav
    p_vy[0] += 0.5 * dt * p_ay[0]

print(p_y)   # Location of single particle [m]
print(time)  # Total simulation time [s]

Variables

p_y : particle position in the y-direction

p_vy : particle velocity in the y-direction

p_ay : particle acceleration in the y-direction

p_fy : particle force in the y-direction

dt : time-step size

grav : gravitational acceleration

Computational Procedure

At each time step:

Update the particle position.

Update the velocity by half a time step.

Update the acceleration.

Complete the velocity update.

Repeat until the final time step.

The total simulation time is:

$$ t_{\mathrm{total}}=N_{\mathrm{step}}\Delta t $$

For this example:

$$ t_{\mathrm{total}}=10\times10^{-3}=0.01\ \mathrm{s} $$

Note

The supplied code uses:

p_ay[0] -= grav

so the acceleration becomes increasingly negative at every time step.

For physically constant gravitational acceleration, the acceleration would normally be assigned as:

p_ay[0] = -grav

or initialized once as -grav, depending on the chosen integration scheme.

Reference

Cundall, Peter A., and Otto D. L. Strack.
"A discrete numerical model for granular assemblies."
Geotechnique 29.1 (1979): 47-65.

<div align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>
</div>
