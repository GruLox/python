def getName(index: int) -> str:
    name: str = None
    while (name == None or len(name) < 2):
        print(f"Kérem adja meg a {index}. dolgozó nevét: ", end="")
        name = input().strip().capitalize()
    
    return name


def getHours(index: int) -> int:
    hours: int = None
    while (hours == None):
        print(f"Kérem adja meg a {index}. dolgozó ledolgozott óráit: ", end="")
        temp: str = input().strip()
        if (temp.isnumeric()):
            hours = int(temp)
        
    return hours


def printToConsole(name: str, hours: int, wage: int):
    print(f"{name} dolgozó {hours} órát dolgozott ezen a héten, és {wage} forintot keresett.")
    
