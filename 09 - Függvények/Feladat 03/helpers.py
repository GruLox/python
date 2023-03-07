from datetime import datetime


def get_birth_year() -> int:
    print("Kérem adja meg a születési dátumát (ÉÉÉÉ-HH-NN): ", end="")
    date: str = input()
    return int(date[:4])


def calculate_age(year: int):
    return datetime.now().year - year