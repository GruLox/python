def get_temperature() -> str:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (number == None):
        print("Adja meg a hőmérsékletet Celsiusban: ", end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg.")

    return number


def get_unit() -> str:
    print("Kérem adja meg a cél mértékegységet (F - Fahrenheit, K - Kelvin): ", end="")
    return input()

