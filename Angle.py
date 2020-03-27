import numpy as np

class Angle:

    def __init__(self, degree):
        if degree > 360:
            degree = degree % 360
            print("Warning, angle de valeur supérieure a 360")
        self.deg = degree  # between 0 and 360
        self.rad = self.deg * np.pi / 180  # between 0 and 2 * np.pi

    def rad(self):
        return self.rad

    def deg(self):
        return self.deg

    def __eq__(self, other):
        return self.deg - other.deg < 0.01

    def sinus(self):
        return np.sin(self.rad)

    def cosinus(self):
        return np.cos(self.rad)


class RadiantAngle(Angle):

    def __init__(self, value):
        if value > 2 * np.pi:
            print("Warning, angle de valeur supérieure a 2 pi")
            value = value % (2 * np.pi)
        self.rad = value
        self.deg = self.rad * 180 / np.pi


class DegreeAngle(Angle):

    def __init__(self, value):
        if value > 360:
            print("Warning, angle de valeur supérieure a 360")
            value = value % 360
        self.deg = value
        self.rad = self.deg * np.pi / 180

