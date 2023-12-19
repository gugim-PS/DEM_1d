import numpy as np
import matplotlib.pyplot as plt

n = 1		# Number of particles [ea]
dt = 1e-3	# Time step length [sec]
y_loc = 0.1 # initial particle height [m]
grav = 9.8 # Gravity [kg m / s^2]
i=1
time =0
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

  p_y[0]  += dt * p_vy[0] + 0.5 * dt *dt* p_ay[0]
  p_vy[0] += 0.5 * dt * p_ay[0]
  p_ay[0] -= grav
  p_vy[0] += 0.5 * dt * p_ay[0]

print(p_y)# location of single particle [m]
print(time)
