##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## test_Matrixes
##

from sources.Matrix import AdjacencyMatrix, RadiatorMatrix


class TestAdjacencyMatrix:

    checkedOutput = "1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n0\t1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0" \
                    "\n0\t0\t1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n0\t0\t0\t1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0" \
                    "\n0\t0\t0\t0\t1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n0\t4\t0\t0\t4\t-16\t4\t0\t0\t4\t0\t0\t0\t0\t0" \
                    "\t0\n0\t0\t4\t0\t0\t4\t-16\t4\t0\t0\t4\t0\t0\t0\t0\t0\n0\t0\t0\t0\t0\t0\t0\t1\t0\t0\t0\t0\t0\t0" \
                    "\t0\t0\n0\t0\t0\t0\t0\t0\t0\t0\t1\t0\t0\t0\t0\t0\t0\t0\n0\t0\t0\t0\t0\t4\t0\t0\t4\t-16\t4\t0\t0" \
                    "\t4\t0\t0\n0\t0\t0\t0\t0\t0\t4\t0\t0\t4\t-16\t4\t0\t0\t4\t0\n0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t1" \
                    "\t0\t0\t0\t0\n0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t1\t0\t0\t0\n0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0" \
                    "\t0\t1\t0\t0\n0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t1\t0\n0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0" \
                    "\t0\t0\t0\t1\n\n"

    def test_Construction(self):
        rChecker = AdjacencyMatrix(4)
        assert rChecker.normalizeSize == 4
        assert rChecker.size == 16
        assert rChecker.adjacencyMatrix is not None

    def test_displayMatrix(self, capsys):
        rChecker = AdjacencyMatrix(4)
        assert rChecker.normalizeSize == 4
        assert rChecker.size == 16
        assert rChecker.adjacencyMatrix is not None
        rChecker.display()
        stdout = capsys.readouterr()[0]
        assert stdout == self.checkedOutput


class TestRadiatorMatrix:

    checkedOutput = "0.0\n0.0\n0.0\n0.0\n0.0\n-300.0\n0.0\n0.0\n0.0\n0.0\n0.0\n0.0\n0.0\n0.0\n0.0\n0.0\n"

    def test_Construction(self):
        rChecker = RadiatorMatrix(4, (1, 1))
        assert rChecker.normalizeSize == 4
        assert rChecker.size == 16
        assert rChecker.getAtPosition((1, 1)) == -300

    def test_displayRawMatrix(self, capsys):
        rChecker = RadiatorMatrix(4, (1, 1))
        assert rChecker.normalizeSize == 4
        assert rChecker.size == 16
        assert rChecker.getAtPosition((1, 1)) == -300
        rChecker.display()
        stdout = capsys.readouterr()[0]
        assert stdout == self.checkedOutput
