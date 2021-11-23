##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## test_ArgChecker
##

from sources.main import printUsage, main
import pytest


class TestMain:

    usageResult = "USAGE\n\t./306radiator n ir jr [i j]\n\nDESCRIPTION\n\tn\t\tsize of the room\n\
\t(ir, jr)\tcoordinates of the radiator\n\t(i, j)\t\tcoordinates of a point in the room\n"

    def test_printUsage(self):
        assert not printUsage()

    def test_printUsagePrints(self, capsys):
        printUsage()
        stdout = capsys.readouterr()[0]
        assert stdout == self.usageResult

