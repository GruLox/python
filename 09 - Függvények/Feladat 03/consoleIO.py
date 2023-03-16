def getName() -> str:
    name: str = None

    while (name == None or len(name) < 2):
        print("Kérem adja meg a nevét: ", end="")
        name = input()

    return name.capitalize()


def getBirthYear() -> int:
    temp: str = None
    date: int = None

    while (date == None):
        print("Kérem adja meg a születési évét (ÉÉÉÉ): ", end="")
        temp: str = input()
        if (temp.isnumeric() and len(temp) == 4):
            date = int(temp)
        
    return date