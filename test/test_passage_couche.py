from unittest import mock
from passage_couche import passage_couche


@mock.patch("interface.interface")
def test_passage_couche(mock_interface):
    mock_interface.side_effect = [(0, 0, 38, 0), (10, 1, 34, 1), (1, 2, 0, 0)]
    transmission, angle_interne = passage_couche(0, 0, 0, 0, 2)  # the values are not important as we mock everything
    assert transmission == 10 * (1 - 4) / (1 - 2)
    assert angle_interne == 38
