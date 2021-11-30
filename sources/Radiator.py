##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## Radiator
##

from sources.Matrix import Matrix


class Radiator:
    def __init__(self, args: list) -> None:
        self.roomSize = args[0]
        self.radiatorCoordinates = (args[1], args[2])
        if len(args) == 5:
            self.pointCoordinates = (args[3], args[4])

        self.room = [[0 for _ in range(self.roomSize)] for _ in range(self.roomSize)]
        self.matrixes = Matrix(self.roomSize)
        pass


