import datetime

def main():
    name: str = None
    birthyear: int = None

    name = get_name()
    birthyear = get_birth_year()
    age = calculate_age(birthyear)
    print(f"{name} ön az idén {age} éves")


def get_name() -> str:
    print("Kérem adja meg a nevét: ", end="")
    return input()


def get_birth_year() -> int:
    print("Kérem adja meg a születési dátumat")
    date: str = input()
    return int(date[:3])


def calculate_age(year: int):
    return datetime.now().year - year

if (__name__ == "__main__"):
    main()