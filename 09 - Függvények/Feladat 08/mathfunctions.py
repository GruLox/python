import math

def calculate_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))