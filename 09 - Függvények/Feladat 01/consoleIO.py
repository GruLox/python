def getNumberFromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (number == None):
        print("Adjon meg egy számot: ", end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg.")

    return number


def printToConsole(x: float, y: float, result: float, operator: str) -> None:
    print(f"{x} {operator} {y} = {result}")


