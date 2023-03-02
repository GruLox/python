def main() -> None:
    s1: str = None
    s2: str = None
    matchCount: int = None

    s1 = get_str()
    s2 = get_str()

    matchCount = count_matches(s1, s2)




def get_str() -> str:
    print(f"Kérem adjon meg egy karakterláncot: ", end="")
    return input()


def count_matches() -> int:
    pass

if (__name__ == "__main__"):
    main()