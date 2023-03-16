def get_name() -> str:
    name: str = None

    while (name == None or len(name) < 2):
        print("Kérem adja meg a nevét: ", end="")
        name = input()

    return name