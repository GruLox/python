from datetime import datetime


def get_birth_year() -> int:
    temp: str = None
    date: int = None

    while (date == None):
        print("Kérem adja meg a születési évét (ÉÉÉÉ): ", end="")
        temp: str = input()
        if (temp.isnumeric() and len(temp) == 4):
            date = int(temp)
        
    return date


def calculate_age(year: int):
    return datetime.now().year - year