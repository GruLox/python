def get_cord(axis: str) -> int:
    temp: str = None
    coord: int = None
    while (temp == None):
        print(f"Kérem adja meg a {axis} koordinátát: ", end="")
        temp = input()
        if (temp.isnumeric()):
            coord = int(temp)
    
    return coord
