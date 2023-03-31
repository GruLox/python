from coordinate import Coordinate

def getCoord() -> Coordinate:
    x = getAxis("x")
    y = getAxis("y")
    return Coordinate(x, y)



def getAxis(axis: str) -> int:
    temp: str = None
    coord: int = None
    while (temp == None):
        print(f"Kérem adja meg a {axis} koordinátát: ", end="")
        temp = input()
        if (temp.isnumeric()):
            coord = int(temp)
    
    return coord
