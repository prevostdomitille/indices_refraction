import numpy as np

from Angle import DegreeAngle
from transmission import transmission

if __name__ == "__main__":
    T = np.zeros(shape=(1801, 2))
    angle = DegreeAngle(30)
    delta_n = 0.0

    i = 0
    for angle_interface in np.arange(-90, 90, 0.1, float):
        transmiss = transmission(angle, delta_n, DegreeAngle(angle_interface))
        T[i] = [transmiss, angle_interface]
        i = i + 1

    exit()


