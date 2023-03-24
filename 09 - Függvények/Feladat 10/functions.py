def game(solution: int) -> int:
    guess: str = None
    while (guess != solution):
        print(f"Próbálja meg kitalálni a megoldást: ", end="")
        if (not guess.isnumeric()):
            print("Nem számot adott meg!")
            continue
        guess = int(guess)
        if (guess < solution):
            print("A megoldás nagyobb")
        elif (guess > solution):
            print("A megoldás kisebb")
        else:
            print("Talált!")