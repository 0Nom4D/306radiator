##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## Matrix
##

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
                adjacencyMatrix[i - 1][i] = 4
                adjacencyMatrix[i + 1][i] = 4
                adjacencyMatrix[i][i - self.normalizeSize] = 4
                adjacencyMatrix[i][i + self.normalizeSize] = 4
        self.adjacencyMatrix = np.array(adjacencyMatrix)

    def printMatrix(self, matrix: np.ndarray) -> None:
        for i in range(0, self.size):
            for j in range(0, self.size):
                print(matrix[i][j], end='\t') if (j + 1) != self.size else print(matrix[i][j], end='')
            print()
        print()
