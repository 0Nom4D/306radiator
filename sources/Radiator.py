##
## EPITECH PROJECT, 2021
## 306radiator
## File description:
## Radiator
##


import numpy as np
from sources.Matrix import AdjacencyMatrix, RadiatorMatrix


class Radiator:
    def __init__(self, args: list) -> None:
        self.roomSize = args[0]
        self.radiatorCoordinates = (args[1], args[2])
        self.adjacency = AdjacencyMatrix(self.roomSize)
        self.radiator = RadiatorMatrix(self.roomSize, self.radiatorCoordinates)
        InvAdjacency = np.linalg.inv(self.adjacency.adjacencyMatrix)

        if len(args) == 5:
            self.pointCoordinates = (args[3], args[4])
            self.radiator.radiatorMatrix = self.radiator.multMatrix(InvAdjacency)
            print(round(self.radiator.getAtPosition(self.pointCoordinates), 1))
        else:
            self.adjacency.display()
            self.radiator.radiatorMatrix = self.radiator.multMatrix(InvAdjacency)
            self.radiator.display()
        pass


