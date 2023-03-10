def get_str() -> str:
    name: str = None

    while (name == None or len(name) < 2):
        print("Kérem adja meg a nevét: ", end="")
        name = input()

        if (len(name) < 2):
            print("Nem megefelelő a név.")

    return name.capitalize().strip()


def greet(s: str) -> None:
    print(f"Hello, {s}")