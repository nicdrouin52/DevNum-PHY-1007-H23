import env_examples  # Modifies path, DO NOT REMOVE
import numpy as np
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World
from celrcle import haut_de_cercle, bas_de_cercle, cercle_complet
from math import sqrt



if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression = x
    y_expression = y
    ligne_eqs = (x_expression, y_expression)

    # Paramétrisation de la partie du cercle avec un grand rayon
    x_expression_grand = -(np.abs((1/45)**2 - (x - (1/45))**2))**0.5
    y_expression_grand = (np.abs((45)**2 - (y - (45))**2))**0.5
    grand_eqs = (x_expression_grand, y_expression_grand)

    # Paramétrisation de la partie du cercle avec un petit rayon
    x_expression_petit = (np.abs((52.5)**2 - (x - (52.5))**2))**0.5
    y_expression_petit = -(np.abs((-1/52.5)**2 - (y - (-1/52.5))**2))**0.5
    petit_eqs = (x_expression_petit, y_expression_petit)


    wires = [
        Wire((15, 60),(17.5, 70), ligne_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((17.5, 70), (70, 17.5), petit_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((70, 17.5),(60, 15), ligne_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((60, 15), (15, 60), grand_eqs, cartesian_variables, BATTERY_VOLTAGE)
    ]

    ground_position = (60, 15)
    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (15, 60), 1: (17.5, 70), 2: (70, 17.5), 3: (60, 15)}
    )
    world.compute()
    world.show_all()