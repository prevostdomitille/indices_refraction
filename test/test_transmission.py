from transmission import transmission

from Angle import Angle


def test_transmission():
    assert transmission(Angle(30), 0, Angle(40)) < 1
