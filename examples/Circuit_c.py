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

    x_expression = (625- (y+25)**2)**0.5 
    y_expression = y
    droite_eqs = (x_expression, y_expression)

    x_expression_gauche = -(625- (y-25)**2)**0.5  
    y_expression_gauche = y
    gauche_eqs = (x_expression_gauche, y_expression_gauche)



    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((48,25),(48,75), gauche_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((48,75),(52,75), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((52, 75),(52, 25), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((52, 25), (48, 25), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
    ]
    ground_position = (52, 25)


    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (48, 25), 1:(48,75), 2: (52, 75), 3: (52,25)}
    )
    
    world.compute()
    world.show_potential() # à la fin, on va avoir show_all. Je l'ai remplacé temporairement