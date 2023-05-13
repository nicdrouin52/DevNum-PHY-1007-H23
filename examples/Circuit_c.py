import env_examples  # Modifies path, DO NOT REMOVE
import numpy as np
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World
from celrcle import haut_de_cercle, bas_de_cercle, cercle_complet



if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables


    # Paramétrisation de la partie droite du cercle
    x_expression = (np.abs(625 - (y - 25)**2))**0.5
    y_expression = y
    droite_eqs = (x_expression, y_expression)

    # Paramétrisation de la partie gauche du cercle
    x_expression_gauche = -(np.abs(625 - (y + 25)**2))**0.5
    y_expression_gauche = y
    gauche_eqs = (x_expression_gauche, y_expression_gauche)

    # Pour les fils horizontaux (source, résistance)
    x_expression_horizontal = x
    y_expression_horizontal = y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((55, 25),(55, 75), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((55, 75),(45, 75), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((45, 75),(45, 25), gauche_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((45, 25), (55, 25), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE)
    ]

    ground_position = (45, 25)
    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (45, 25), 1: (45, 75), 2: (55, 75), 3: (55, 25)}
    )
    world.compute()
    world.show_all()
