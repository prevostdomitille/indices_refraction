from passage_couche import passage_couche
from interface import interface
import matplotlib.pyplot as plt

def transmission(angle, delta_n, angle_interface):
    n1 = 1  # indice de l'air
    n2 = 1.5  # indice du CH 39
    n3 = 1.55  # indice HI
    n4 = 1.35  # indice BI
    n5 = 1.5  # indice CR39

    nb_iterations = 100000

    T1, _ , angle1, _ = interface(angle, n1, n2)
    T2, angle2 = passage_couche(angle1, n2, n3, n4, nb_iterations)
    T3, _ , angle3, _ = interface(90 - angle_interface - angle2, n3, n3 + delta_n)
    T4, angle4 = passage_couche(angle_interface - angle3, n3 + delta_n, n4, n5, nb_iterations)
    T5, _ = passage_couche(angle4, n4, n5, n1, nb_iterations)

    transmission = T1 * T2 * T3 * T4 * T5

    # Transmission_progressive = [T1, T1 * T2, T1 * T2 * T3, T1 * T2 * T3 * T4, T1 * T2 * T3 * T4 * T5];
    # plt.plot(Transmission_progressive)
    return transmission