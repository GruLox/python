def getAmount() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncatedString: str = None

    while (number == None):
        print("Adja meg a az átváltandó értéket HUF-ban: ", end="")
        temp = input()
        truncatedString = temp.replace(".", "").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg.")

    return number


def getCurrency() -> str:
    currency: str = None

    while (currency == None or currency not in ["EUR", "JPY", "USD", "CHF"]):
        print("Kérem adja meg a cél valutát: ", end="")
        currency = input().upper()
    
    return currency

    
