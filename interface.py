import numpy as np
from Angle import RadiantAngle, Angle


def calcul_reflexion(a_i_rad, a_t_rad):
    r_t = -np.tan(a_i_rad - a_t_rad) / np.tan(a_i_rad + a_t_rad)
    r_p = -np.sin(a_i_rad - a_t_rad) / np.sin(a_i_rad + a_t_rad)

    R_p = r_p ** 2
    R_t = r_t ** 2
    reflexion = (R_p + R_t) / 2
    return reflexion


def interface(angle_incidence, n1, n2):
    if angle_incidence.deg() == 0:
        reflexion = ((n1 - n2) / (n1 + n2)) ** 2
        angle_transmit = Angle(0)
    else:
        if (n1 >= n2) & (angle_incidence.rad() >= np.arcsin(n2 / n1)):
            reflexion = 1
            angle_transmit = angle_incidence
        else:
            a_t_rad = np.arcsin(min(n1, n2) / max(n1, n2)) * angle_incidence.sinus()
            angle_transmit = RadiantAngle(a_t_rad)
            reflexion = calcul_reflexion(angle_incidence.rad(), angle_transmit.rad())

    transmission = 1 - reflexion
    angle_reflechi = - angle_incidence
    return transmission, reflexion, angle_transmit, angle_reflechi
