##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## test_Matrix
##

from sources.Radiator import Radiator


class TestRadiator:
    def test_Properties(self):
        rChecker = Radiator([3, 1, 1])
        assert rChecker.roomSize == 3
        assert rChecker.radiatorCoordinates == (1, 1)
        assert rChecker.room == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert rChecker.matrixes.size == 9

    def test_5ArgsProperties(self):
        rChecker = Radiator([3, 1, 1, 1, 1])
        assert rChecker.roomSize == 3
        assert rChecker.radiatorCoordinates == (1, 1)
        assert rChecker.pointCoordinates == (1, 1)
        assert rChecker.room == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert rChecker.matrixes.size == 9
