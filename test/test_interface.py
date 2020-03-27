from interface import interface, calcul_reflexion
import numpy as np
from unittest import mock

def test_interface_angle_incidence_0():
    assert interface(0, 1, 1) == (1, 0, 0, 0)


def interface_n1_smaller(angle_incidence, angle_1, angle_2):
    indice_ch_39 = 1.5
    indice_BI = 1.35
    transmission, reflexion, angle_transmit, angle_reflechi = interface(angle_incidence, angle_1, angle_2)
    assert transmission + reflexion - 1 < 0.01
    assert reflexion == 0.7
    assert angle_transmit < 45
    assert angle_transmit > 0
    assert angle_reflechi == - angle_incidence


@mock.patch("interface.calcul_reflexion")
def test_interface_n1_smaller(calcul_reflexion_mock):
    calcul_reflexion_mock.return_value = 0.7
    n1 = 1  # indice de l'air
    n2 = 1.5  # indice du CH 39
    n3 = 1.55  # indice HI
    n4 = 1.35  # indice BI
    n5 = 1.5  # indice CR39

    interface_n1_smaller(-52, n2, n1)
    interface_n2_smaller(42, n2, n1)
    interface_n2_smaller(np.arcsin(n1/n3) * 180 / np.pi + 1, n3, n1)
    interface_n1_smaller(30, n1, n3)
    interface_n1_smaller(30, n1, n4)
    interface_n1_smaller(30, n4, n3)


def interface_n2_smaller(angle_incidence, angle_1, angle_2):
    transmission, reflexion, angle_transmit, angle_reflechi = interface(angle_incidence, angle_1, angle_2)
    assert transmission == 0
    assert reflexion == 1
    assert angle_transmit == angle_incidence
    assert angle_reflechi == - angle_incidence


#difficile a tester, il faudrait des valeurs connues
def test_calcul_reflexion():
    assert calcul_reflexion(1, 1) == 0
    assert calcul_reflexion(1, 0) == 1
    assert calcul_reflexion(0, 1) == 1
