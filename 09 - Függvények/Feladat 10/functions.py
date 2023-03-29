def game(solution: int) -> int:
    guess: str = None
    tries: int = 0
    while (guess != solution):
        print(f"Próbálja meg kitalálni a megoldást: ", end="")
        guess = input().strip()

        if (not guess.isnumeric()):
            print("Nem számot adott meg!")
            continue
        
        guess = int(guess)
        if (guess < solution):
            print("A megoldás nagyobb")
        elif (guess > solution):
            print("A megoldás kisebb")
        else:
            return tries

        tries += 1