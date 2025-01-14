import env_examples  # Modifies path, DO NOT REMOVE
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    # Équations qui permettent de faire des fils verticaux
    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    # Équations qui permettent de faire des fils horizontaux
    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    # Série de fils qui consruisent le circuit
    wires = [
        Wire((26, 26), (26, 74), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((26, 74), (60, 74), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 74), (70, 74), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((70, 74), (74, 74), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((74, 74), (74, 46), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((74, 46), (74, 36), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((74, 36), (74, 26), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((74, 26), (40, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((40, 26), (36, 26), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((36, 26), (26, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
    ]

    # Position de la mise en terre
    ground_position = (40, 26)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)

    # Positionnement des noeuds 
    world.show_circuit(
        {0: (26, 26), 1: (26, 74), 2: (60, 74), 3: (70, 74), 4: (74, 74), 5: (74, 46), 6: (74, 36), 7: (74, 26), 8: (40, 26), 9: (36, 26)}
    )
    world.compute()
    world.show_all()