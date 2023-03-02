def main():
    name: str = None

    name = get_str()
    greet(name)


def get_str() -> str:
    print("Kérem adja meg a nevét: ", end="")
    return input()
    

def greet(s: str) -> None:
    print(f"Hello, {s}")


if (__name__ == "__main__"):
    main()


    


