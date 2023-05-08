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

    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((20, 20), (20, 48), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((20, 48), (20, 52), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((20, 52), (20, 80), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),

        Wire((20, 80), (80, 80), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),

        Wire((80, 80), (80, 52), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((80, 52), (80, 48), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((80, 48), (80, 20), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),

        Wire((80, 20), (20, 20), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),

        Wire((40, 20), (40, 45), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((40, 45), (40, 55), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((40, 55), (40, 80), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),

        Wire((60, 20), (60, 45), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 45), (60, 55), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((60, 55), (60, 80), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
    ]
    ground_position = (80, 48)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (48, 80), 1: (80, 20), 2: (60, 20), 3: (40, 20), 4: (20, 20), 5: (20, 48), 6: (20, 80), 7: (40, 80), 8: (60, 80), 9: (80, 80)}
    )
    world.compute()
    world.show_potential() # à la fin, on va avoir show_all. Je l'ai remplacé temporairement
