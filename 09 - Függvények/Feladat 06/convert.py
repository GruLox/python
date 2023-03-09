def convert(unit: str, temp: float):
    if (unit.upper() == "F"):
        return (9 / 5) * temp + 32

    elif(unit.upper() == "K"):
        return temp + 273

    else:
        print("Érvénytelen mértékegység")
        return None