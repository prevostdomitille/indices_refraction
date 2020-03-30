import numpy as np


class Angle:

    def __init__(self, degree):
        if degree > 360:
            print("Warning, angle de valeur supérieure a 360")
        degree = degree % 360
        self.degree = degree  # between 0 and 360
        self.radiant = self.degree * np.pi / 180  # between 0 and 2 * np.pi

    def rad(self):
        return self.radiant

    def deg(self):
        return self.degree

    def setRad(self, value):
        self.radiant = value % (2 * np.pi)
        self.degree = self.radiant * 180 / np.pi

    def setDeg(self, value):
        self.degree = value % 360
        self.radiant = self.degree / np.pi * 360

    def __eq__(self, other):
        return (self.degree - other.deg()) < 0.01

    def __sub__(self, other):
        return DegreeAngle(self.degree - other.deg() % 360)

    def __add__(self, other):
        return DegreeAngle(self.degree + other.deg() % 360)

    def __neg__(self):
        return DegreeAngle(-self.degree)

    def sinus(self):
        return np.sin(self.radiant)

    def cosinus(self):
        return np.cos(self.radiant)


class RadiantAngle(Angle):

    def __init__(self, value):
        if value > 2 * np.pi:
            print("Warning, angle de valeur supérieure a 2 pi")
        value = value % (2 * np.pi)
        self.radiant = value
        self.degree = self.radiant * 180 / np.pi


class DegreeAngle(Angle):

    def __init__(self, value):
        super().__init__(value)
