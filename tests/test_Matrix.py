##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## test_Matrix
##

from sources.Matrix import Matrix


class TestMatrix:
    def test_Properties(self):
        mChecker = Matrix(2)
        assert mChecker.size == 4
        assert mChecker.adjacencyMatrix == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
