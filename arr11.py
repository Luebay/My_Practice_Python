import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define circuit parameters
R1 = 12000  # ohms
L1 = 20      # henries
L2 = 4       # henries
R2 = 30      # ohms
R3 = 1200    # ohms

# Define time-dependent independent voltage source
def V1(t):
    return 100 * np.cos(314 * t)

# Define the system of differential equations
def circuit_ode(Y, t):
    V2, V3, V4, I2, I3, I4, I5, I6 = Y

    dV2dt = (V1(t) - V2) / R1
    dV3dt = (V2 - V3 - L1 * I3) / L1
    dV4dt = (-L1 * I3 - L2 * I4 + V5 - V4) / L2
    dI2dt = I2
    dI3dt = V3 / L1
    dI4dt = V4 / L2
    dI5dt = I5 / R2
    dI6dt = (V4 - V6) / R3

    return [dV2dt, dV3dt, dV4dt, dI2dt, dI3dt, dI4dt, dI5dt, dI6dt]

# Set initial conditions for inductors and currents
initial_conditions = [0, 0, 0, 0, 0, 0, 0, 0]

# Define time points
t = np.linspace(0, 1, 1000)  # Time vector from 0 to 1 second

# Solve the system of differential equations
solution = odeint(circuit_ode, initial_conditions, t)

# Extract results for each variable
V2_solution, V3_solution, V4_solution, I2_solution, I3_solution, I4_solution, I5_solution, I6_solution = solution.T

# Plot the results
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, V1(t), label='V1')
plt.plot(t, V2_solution, label='V2')
plt.plot(t, V3_solution, label='V3')
plt.plot(t, V4_solution, label='V4')
plt.legend()
plt.title('Voltage Across Components')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')

plt.subplot(2, 1, 2)
plt.plot(t, I2_solution, label='I2')
plt.plot(t, I3_solution, label='I3')
plt.plot(t, I4_solution, label='I4')
plt.plot(t, I5_solution, label='I5')
plt.plot(t, I6_solution, label='I6')
plt.legend()
plt.title('Current Through Components')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')

plt.tight_layout()
plt.show()
