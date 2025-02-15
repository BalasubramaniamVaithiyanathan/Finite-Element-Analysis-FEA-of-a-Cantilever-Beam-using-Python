# Finite-Element-Analysis-FEA-of-a-Cantilever-Beam-using-Python

- Objectives

The goal of this project is to simulate the deflection of a cantilever beam under an external force using the Finite Element Method (FEM). The aim is to understand the structural behavior of the beam and visualize its deformation.

- Software Used

Python (programming language)

NumPy (scientific computing)

Matplotlib (data visualization)

- Methodology

Definition of Beam Properties: Material properties (elastic modulus, moment of inertia) and geometric parameters are defined.

Discretization: The beam is divided into small finite elements for numerical analysis.

Stiffness Matrix Formulation: The stiffness matrix is constructed using the Euler-Bernoulli beam element formulation.

Application of Boundary Conditions: The fixed end of the beam is assigned zero displacement.

Numerical Solution: A linear system of equations is solved to determine nodal displacements.

Visualization: The deformed shape of the beam is plotted to analyze the results.

- Results

The maximum deflection occurs at the free end of the cantilever beam.

The fixed end of the beam remains stationary, as expected.

The plot provides a clear visualization of the bending mode.

The results align with theoretical expectations and confirm the correctness of the FEM implementation.
