def getNumber(start: int, end: int) -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (number == None or number < start or number > end):
        print(f"Adjon meg egy számot {start} és {end} között: ", end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg.")

    return number