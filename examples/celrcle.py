from math import sqrt

def haut_de_cercle(prec, tuple_1, tuple_2):
    delta_x = (tuple_2[0]-tuple_1[0]) / prec

    rayon_2 = sqrt((tuple_2[0]-50)**2 + (tuple_2[1] -50 )**2)
    rayon_1 = sqrt((tuple_1[0]-50)**2 + (tuple_1[1] -50 )**2)

    if rayon_1 != rayon_2:
        raise ValueError("fuccckkk")
    
    pos_dict = {}
    pos_liste = []

    for i in range(prec+1):
        pos_dict[i] = (tuple_1[0] + delta_x*i, 50 + sqrt(rayon_1**2 - (tuple_1[0] + delta_x*i - 50)**2))
        pos_liste.append((tuple_1[0]+delta_x*i, 50 + sqrt(rayon_1**2 - (tuple_1[0]+delta_x*i - 50)**2)))

    return pos_dict

def bas_de_cercle(prec, tuple_1, tuple_2):
    delta_x = (tuple_2[0]-tuple_1[0]) / prec

    rayon_2 = sqrt((tuple_2[0]-50)**2 + (tuple_2[1] -50 )**2)
    rayon_1 = sqrt((tuple_1[0]-50)**2 + (tuple_1[1] -50 )**2)

    if rayon_1 != rayon_2:
        raise ValueError("fuccckkk")
    
    pos_dict = {}
    pos_liste = []

    for i in range(prec+1):
        pos_dict[i] = (tuple_1[0] + delta_x*i, 50 - sqrt(rayon_1**2 - (tuple_1[0] + delta_x*i - 50)**2))
        pos_liste.append((tuple_1[0]+delta_x*i, 50 - sqrt(rayon_1**2 - (tuple_1[0]+delta_x*i - 50)**2)))

    return pos_liste


def cercle_complet(prec, tuple_d):
    pos_dict = haut_de_cercle(prec, tuple_d, (100-tuple_d[0], 100-tuple_d[1]))
    for i in range(prec+1):
        pos_dict[i+prec] = bas_de_cercle(prec, (100-tuple_d[0], 100-tuple_d[1]), tuple_d)[i]
    return pos_dict






