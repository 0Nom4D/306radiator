##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## Radiator
##

from sources.Matrix import AdjacencyMatrix


class Radiator:
    def __init__(self, args: list) -> None:
        self.roomSize = args[0]
        self.radiatorCoordinates = (args[1], args[2])
        self.adjacency = AdjacencyMatrix(self.roomSize)
        if len(args) == 5:
            self.pointCoordinates = (args[3], args[4])
        else:
            self.adjacency.display()
        pass


