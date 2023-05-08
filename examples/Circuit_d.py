import env_examples  # Modifies path, DO NOT REMOVE
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    polaire_variables = Symbol("r"), Symbol("theta")
    r, theta = polaire_variables

    r_expression_angular = 0 * r
    theta_expression_angular = theta
    angular_eqs = (r_expression_angular, theta_expression_angular)

    r_expression_radial = r
    theta_expression_radial = 0 * theta
    radial_eqs = (r_expression_radial, theta_expression_radial)

    wires = [
        Wire((50, 45), (50, 76), angular_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((50, 76), (70, 76), radial_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((70, 76), (70, 50), angular_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((70, 50), (70, 39), angular_eqs, polaire_variables, HIGH_WIRE_RESISTANCE),
        Wire((70, 39), (70, 14), angular_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((70, 14), (50, 14), radial_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((50, 14), (50, 43), angular_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((50, 43), (50, 45), angular_eqs, polaire_variables, BATTERY_VOLTAGE),
    ]
    ground_position = (50, 43)


    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (50, 45), 1:(50, 76), 2:(70, 76), 3: (70, 50), 4: (70, 39), 5: (70, 14), 6: (50, 14), 7: (50, 43)}
    )
    world.compute()
    world.show_all()