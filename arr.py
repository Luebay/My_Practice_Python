import numpy as np

# Define the coefficients matrix and the constants vector
coefficients = np.array([
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 0, 0, 1, 0, -1, 0],
    [0, 0, 0, 1, 0, 0, -1, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, -1, 1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 1],
    [12000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [0, 20, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 4, 0, 0, -1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 30, 0, 1, 0, -1, -1, 0, 0, 0],
    [0, 0, 0, 0, 1200, 0, -1, 0, 1, 0, 0, 0],
])

constants = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0])

# Solve the system of equations
solution = np.linalg.solve(coefficients, constants)

# Print the solution
print("Solution:")
print("V1 =", solution[0])
print("I1 =", solution[1])
print("V2 =", solution[2])
print("I2 =", solution[3])
print("V3 =", solution[4])
print("I3 =", solution[5])
print("V4 =", solution[6])
print("I4 =", solution[7])
print("V5 =", solution[8])
print("I5 =", solution[9])
print("V6 =", solution[10])
print("I6 =", solution[11])
