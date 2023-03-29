from consoleIO import getCoord
from mathfunctions import calculateDistance

x1: int = getCoord("x")
y1: int = getCoord("y")

x2: int = getCoord("x")
y2: int = getCoord("y")

distance: float = calculateDistance(x1, y1, x2, y2)

print(f"A két koordináta távolsága: {distance}")
