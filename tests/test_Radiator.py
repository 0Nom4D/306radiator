##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## test_Matrix
##

from sources.Radiator import Radiator


class TestRadiator:
    def test_Properties(self):
        rChecker = Radiator([4, 1, 1])
        assert rChecker.roomSize == 4
        assert rChecker.radiatorCoordinates == (1, 1)
        assert rChecker.adjacency.size == 16

    def test_5ArgsProperties(self):
        rChecker = Radiator([4, 1, 1, 1, 1])
        assert rChecker.roomSize == 4
        assert rChecker.radiatorCoordinates == (1, 1)
        assert rChecker.pointCoordinates == (1, 1)
        assert rChecker.adjacency.size == 16

    def test_NormalCasePrint(self, capsys):
        rChecker = Radiator([4, 1, 1])
        stdout = capsys.readouterr()[0]
        assert stdout is not None

    def test_5ArgsCasePrint(self, capsys):
        rChecker = Radiator([4, 1, 1, 1, 1])
        stdout = capsys.readouterr()[0]
        assert stdout is not None
