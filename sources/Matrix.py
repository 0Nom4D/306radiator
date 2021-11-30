##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## Matrix
##

class Matrix:
    def __init__(self, size: int) -> None:
        self.size = size ** 2
        self.adjacencyMatrix = [[0 for _ in range(size ** 2)] for _ in range(size ** 2)]

        self._constructAdjacency()
        self.printMatrix(self.adjacencyMatrix)
        pass

    def _constructAdjacency(self) -> None:
        for i in range(0, self.size):
            for j in range(0, self.size):
                if j == i:
                    self.adjacencyMatrix[i][j] = 1

    def printMatrix(self, matrix: list) -> None:
        for i in range(0, self.size):
            for j in range(0, self.size):
                print(matrix[i][j], end='\t') if (j + 1) != self.size else print(matrix[i][j], end='')
            print()
        print()
