import env_examples  # Modifies path, DO NOT REMOVE
from sympy import Symbol
from scipy.constants import pi
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
        Wire((50, pi/4), (50, 19*pi/45), angular_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((50, 19*pi/45), (70, 19*pi/45), radial_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((70, 19*pi/45), (70, 5*pi/18), angular_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((70, 5*pi/18), (70, 13*pi/60), angular_eqs, polaire_variables, HIGH_WIRE_RESISTANCE),
        Wire((70, 13*pi/60), (70, 7*pi/90), angular_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((70, 7*pi/90), (50, 7*pi/90), radial_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((50, 7*pi/90), (50, 43*pi/180), angular_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((50, 43*pi/180), (50, pi/4), angular_eqs, polaire_variables, BATTERY_VOLTAGE),
    ]
    ground_position = (50, 43*pi/180)


    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (50, pi/4), 1:(50, 19*pi/45), 2:(70, 19*pi/45), 3: (70, 5*pi/18), 4: (70, 13*pi/60), 5: (70, 7*pi/90), 6: (50, 7*pi/90), 7: (50, 43*pi/180)}
    )
    world.compute()
    world.show_all()