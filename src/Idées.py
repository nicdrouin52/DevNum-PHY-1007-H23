import numpy as np
import sympy as sp

from laplace_equation_solver import LaplaceEquationSolver

for iteration in np.nditer(P): # permet d'itérer sur toutes les cases d'un coup.
    # mais jsp comment aller chercher les cases autour d'une autre.
    