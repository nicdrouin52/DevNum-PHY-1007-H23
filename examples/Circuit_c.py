import env_examples  # Modifies path, DO NOT REMOVE
import numpy as np
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World
from celrcle import haut_de_cercle, bas_de_cercle, cercle_complet



if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    prec = 30
    BATTERY_VOLTAGE = 1.0/prec
    HIGH_WIRE_RESISTANCE = 1.0/prec
    LOW_WIRE_RESISTANCE = 0.01/prec

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables


    # Notre essaie pour paramétriser le cercle
    # (ne fonctionne pas, nous ne sommes pas assez outillé pour réusssir, surtout que le cours de programmation n'est pas un prérecquis)
#    x_expression = (625- (y+25)**2)**0.5 
#    y_expression = y
#    droite_eqs = (x_expression, y_expression)

#    x_expression_gauche = -(625- (y-25)**2)**0.5  
#    y_expression_gauche = y
#    gauche_eqs = (x_expression_gauche, y_expression_gauche)


#    x_expression_vertical = 0 * x
#    y_expression_vertical = y
#    vertical_eqs = (x_expression_vertical, y_expression_vertical)

#    x_expression_horizontal = x
#    y_expression_horizontal = 0 * y
#    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

#    wires = [
#        Wire((48,25),(48,75), gauche_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        Wire((48,75),(52,75), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
#        Wire((52, 75),(52, 25), droite_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
#        VoltageSource((52, 25), (48, 25), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
#    ]


    x_expr = x
    y_expr = y
    cerc_eqs = (x_expr, y_expr)

    # Liste vide pour les fils
    wires = []


    for i in range(prec):
        wires.append(Wire(haut_de_cercle(prec, (35,70),(65,70))[i], haut_de_cercle(prec, (35,70),(65,70))[i+1],
                          cerc_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE))

    for i in range(prec):
        wires.append(Wire(haut_de_cercle(prec, (65,70),(75,50))[i], haut_de_cercle(prec, (65,70),(75,50))[i+1],
                          cerc_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))

    for i in range(prec):
        wires.append(Wire(bas_de_cercle(prec, (75,50),(65,30))[i], bas_de_cercle(prec, (75,50),(65,30))[i+1],
                          cerc_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))

    for i in range(prec):
        wires.append(VoltageSource(bas_de_cercle(prec, (65,30),(35,30))[i], bas_de_cercle(prec, (65,30),(35,30))[i+1],
                          cerc_eqs, cartesian_variables, BATTERY_VOLTAGE))

    for i in range(prec):
        wires.append(Wire(bas_de_cercle(prec, (35,30),(25,50))[i], bas_de_cercle(prec, (35,30),(25,50))[i+1],
                          cerc_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))

    for i in range(prec):
        wires.append(Wire(haut_de_cercle(prec, (25,50),(35,70))[i], haut_de_cercle(prec, (25,50),(35,70))[i+1],
                          cerc_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))


    ground_position = (25, 50)
    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        cercle_complet(3*prec, (25,50))
    )

    world.compute()
    world.show_all()