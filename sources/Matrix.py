##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## Matrix
##

from math import floor, ceil
import numpy as np


class AdjacencyMatrix:
    def __init__(self, size: int) -> None:
        self.normalizeSize = size
        self.size = size ** 2
        self.adjacencyMatrix = np.array(0)

        self._constructAdjacency()
        pass

    def _constructAdjacency(self) -> None:
        adjacencyMatrix = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for i in range(0, self.size):
            for j in range(0, self.size):
                if j == i:
                    adjacencyMatrix[i][j] = 1
        for i in range(0, self.size):
            if i % self.normalizeSize and (i + 1) % self.normalizeSize and self.normalizeSize < i < (self.size - self.normalizeSize):
                adjacencyMatrix[i][i] = -16
                adjacencyMatrix[i][i + 1] = 4
                adjacencyMatrix[i][i - 1] = 4
                adjacencyMatrix[i][i - self.normalizeSize] = 4
                adjacencyMatrix[i][i + self.normalizeSize] = 4
        self.adjacencyMatrix = np.array(adjacencyMatrix)

    def display(self) -> None:
        for i in range(0, self.size):
            for j in range(0, self.size):
                print(self.adjacencyMatrix[i][j], end='\t') if (j + 1) != self.size else print(self.adjacencyMatrix[i][j], end='')
            print()
        print()


class RadiatorMatrix:
    def __init__(self, size: int, radiatorCoordinates: (int, int)) -> None:
        self.normalizeSize = size
        self.size = size ** 2
        self.radiatorCoordinates = radiatorCoordinates
        self.radiatorMatrix = np.array(0)

        self._constructMatrix()
        pass

    def _constructMatrix(self) -> None:
        radiatorMatrix = [0 for _ in range(self.size)]

        radiatorMatrix[self.normalizeSize * self.radiatorCoordinates[1] + self.radiatorCoordinates[0]] = -300
        self.radiatorMatrix = np.array(radiatorMatrix)

    def multMatrix(self, matrixToMult: np.ndarray) -> np.ndarray:
        newMultMatrix = np.matmul(matrixToMult, self.radiatorMatrix)
        return newMultMatrix

    def display(self) -> None:
        for i in range(0, self.size):
            if round(self.radiatorMatrix[i], 1) == -0.0:
                print(0.0)
            else:
                nbToRound = self.radiatorMatrix[i] * 10
                if nbToRound - floor(nbToRound) < 0.5:
                    nbToRound = floor(nbToRound)
                else:
                    nbToRound = ceil(nbToRound)
                print('%.1f' % (nbToRound / 10))

    def getAtPosition(self, pointCoordinates: (int, int)):
        return self.radiatorMatrix[self.normalizeSize * pointCoordinates[1] + pointCoordinates[0]]
