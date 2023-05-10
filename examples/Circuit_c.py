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

    x_expression = (625- (y-25)**2)**0.5 
    y_expression = y
    droite_eqs = (x_expression, y_expression)

    x_expression_gauche = -(625- (y+25)**2)**0.5  
    y_expression_gauche = y
    gauche_eqs = (x_expression_gauche, y_expression_gauche)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((0, 50),(0, 0), gauche_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((0, 0),(1, 0.0200089), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((1, 0.0200089),(2, 0.0801), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((0, 0), (25, 25), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
#        VoltageSource((1, 0.0200089), (2, 0.0801), droite_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((25, 25),(0,50), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
#        Wire((0, 0),(2, 0.0801), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((1, 0.02),(2, 0.0801), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        VoltageSource((2, 0.0801), (0, 50), droite_eqs, cartesian_variables, BATTERY_VOLTAGE),
#        Wire((0, 50),(0, 0), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((0, 50),(0, 0), gauche_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((-2, -0.0801),(0,50), gauche_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((0,50),(0,0), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((48, 80), (50, 80), gauche_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
#        Wire((0, 50),(0, 0), gauche_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((2, 0.0801),(0,50), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
    ]
    ground_position = (0, 0)


    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (0, 0), 1:(25, 25), 3:(0, 50)}
    )
    world.compute()
    world.show_potential() # à la fin, on va avoir show_all. Je l'ai remplacé temporairement