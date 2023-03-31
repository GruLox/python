from consoleIO import getCoord
from mathfunctions import calculateDistance
from coordinate import Coordinate

coord1: Coordinate = getCoord()
coord2: Coordinate = getCoord()

distance: float = calculateDistance(coord1, coord2)

print(f"A két koordináta távolsága: {distance}")
