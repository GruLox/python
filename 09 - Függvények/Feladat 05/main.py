def main() -> None:
    word1: str = None
    word2: str = None
    matchCount: int = None

    word1 = get_str()
    word2 = get_str()

    matchCount = count_matches(word1, word2)

    print(matchCount)


def get_str() -> str:
    print(f"Kérem adjon meg egy karakterláncot: ", end="")
    return input()


def count_matches(s1: str, s2: str) -> int:
    counter: int = 0
    matches: str = ""
    for i in s1:
        for j in s2:
            if (i == j and  j not in matches):
                counter += 1
                matches += j
    
    return counter


if (__name__ == "__main__"):
    main()