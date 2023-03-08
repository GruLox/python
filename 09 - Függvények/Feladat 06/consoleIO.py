def get_temp() -> str: 
    temperature: float = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (temperature == None):
        print("Kérem adja meg a hőfokot Celsiusban: ", end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg.")

    return number
