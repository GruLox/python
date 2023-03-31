import math
from coordinate import Coordinate

def calculateDistance(coord1: Coordinate, coord2: Coordinate) -> float:
    return math.sqrt(math.pow((coord2.x - coord1.x), 2) + math.pow((coord2.y - coord1.y), 2))