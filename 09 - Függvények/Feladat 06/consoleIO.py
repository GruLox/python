<<<<<<< HEAD
def get_temp() -> str: 
    temperature: float = None
=======
def get_temperature() -> str:
    number: float = None
>>>>>>> b6b1d8220aa2939cd4dd0a8b5ef1dcd819793770
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

<<<<<<< HEAD
    while (temperature == None):
        print("Kérem adja meg a hőfokot Celsiusban: ", end="")
=======
    while (number == None):
        print("Adja meg a hőmérsékletet Celsiusban: ", end="")
>>>>>>> b6b1d8220aa2939cd4dd0a8b5ef1dcd819793770
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg.")

    return number
<<<<<<< HEAD
=======


def get_unit() -> str:
    print("Kérem adja meg a cél mértékegységet (F - Fahrenheit, K - Kelvin): ", end="")
    return input()

>>>>>>> b6b1d8220aa2939cd4dd0a8b5ef1dcd819793770
