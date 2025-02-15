import numpy as np
import matplotlib.pyplot as plt

# Beam properties
L = 1.0  # Length of the beam (m)
E = 2.1e11  # Young's modulus (Pa)
I = 1e-6  # Moment of inertia (m^4)
n_elements = 10  # Number of elements
n_nodes = n_elements + 1

# Load and boundary conditions
F = -1000  # Applied force at the free end (N)

# Element length
dl = L / n_elements

# Global stiffness matrix initialization
K = np.zeros((2 * n_nodes, 2 * n_nodes))
F_vector = np.zeros(2 * n_nodes)

# Beam element stiffness matrix
k_local = (E * I / dl**3) * np.array([
    [12, 6 * dl, -12, 6 * dl],
    [6 * dl, 4 * dl**2, -6 * dl, 2 * dl**2],
    [-12, -6 * dl, 12, -6 * dl],
    [6 * dl, 2 * dl**2, -6 * dl, 4 * dl**2]
])

# Assembly of the global stiffness matrix
for i in range(n_elements):
    dof = [2 * i, 2 * i + 1, 2 * i + 2, 2 * i + 3]
    for a in range(4):
        for b in range(4):
            K[dof[a], dof[b]] += k_local[a, b]

# Apply boundary conditions (fixed at node 0)
K_mod = K[2:, 2:]
F_vector[-2] = F  # Apply force at the last node
F_mod = F_vector[2:]

# Solve for displacements
u = np.linalg.solve(K_mod, F_mod)

displacements = np.zeros(2 * n_nodes)
displacements[2:] = u

# Extract vertical displacements for plotting
y_displacement = displacements[1::2]
nodal_positions = np.linspace(0, L, n_nodes)

# Plot deformed shape
plt.figure(figsize=(8, 4))
plt.plot(nodal_positions, y_displacement, '-o', label='Deformed Shape')
plt.xlabel('Beam Length (m)')
plt.ylabel('Deflection (m)')
plt.title('FEA Cantilever Beam Deflection')
plt.legend()
plt.grid()
plt.show()
