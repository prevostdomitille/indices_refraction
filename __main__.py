import numpy as np

from matplotlib import pyplot
from Angle import DegreeAngle
from transmission import transmission

if __name__ == "__main__":
    angle = DegreeAngle(30)
    delta_n = 0.0

    P = []
    i = 0
    y = np.arange(-90, 90, 0.1, float)
    for angle_interface in y:
        transmiss = transmission(angle, delta_n, DegreeAngle(angle_interface))
        P.append(transmiss)
        i = i + 1
    pyplot.plot(y, np.array(P))
    pyplot.show()
    exit()
