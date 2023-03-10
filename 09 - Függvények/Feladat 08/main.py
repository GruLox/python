from consoleIO import get_cord
from mathfunctions import calculate_distance

x1: int = get_cord("x")
y1: int = get_cord("y")

x2: int = get_cord("x")
y2: int = get_cord("y")

distance: float = calculate_distance(x1, y1, x2, y2)

print(f"A két koordináta távolsága: {distance}")
