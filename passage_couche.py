from interface import interface

def passage_couche(angle_incidence, n1, n2, n3, n):

    _ , _ , a_t1, _  = interface(angle_incidence, n1, n2)
    t23, r23, a_t2, _ = interface(a_t1, n2, n3)
    _, r21, _, _ = interface(a_t1, n2, n3)

    transmission = t23 * ((1 - (r23 * r21) ** n) / (1 - (r23 * r21)))
    angle_interne = a_t1
    angle_refracte = a_t2
    return transmission, angle_interne  #degrees