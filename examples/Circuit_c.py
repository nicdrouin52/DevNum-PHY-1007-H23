import env_examples  # Modifies path, DO NOT REMOVE
import numpy as np
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_droite = (30**2 - (y - 30)**2)**(1/2)
    y_expression_droite = y
    droite_eqs = (x_expression_droite, y_expression_droite)

    x_expression_gauche = -(30**2 - (y - 30)**2)**(1/2)
    y_expression_gauche = y
    gauche_eqs = (x_expression_gauche, y_expression_gauche)

    wires = [
#        VoltageSource((0, 0), (0, 20), gauche_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((0, 0), (0, 60), gauche_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((48, 80), (50, 80), gauche_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((0, 60), (0, 0), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
    ]
    ground_position = (0, 0)


    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (0, 0), 1:(0, 60)}
    )
    world.compute()
    world.show_potential() # à la fin, on va avoir show_all. Je l'ai remplacé temporairement