def main():
    name: str = None

    name = get_name()
    name = color(name)
    print(f"Üdvözlöm, {name}")    


def get_name() -> str:
    print("Kérem adja meg a nevét: ", end="")
    return input()


def color(s: str) -> str:
    value: int = len(s)
    return f"\033[38;2;{value};{value};{value}m{s}\033[0m"


if (__name__ == "__main__"):
    main()