def get_str() -> str:
    print("Kérem adja meg a nevét: ", end="")
    return input()


def greet(s: str) -> None:
    print(f"Hello, {s}")