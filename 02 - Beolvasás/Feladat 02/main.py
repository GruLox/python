from os import system


name : str = input("Kérem adja meg a nevét: ")
birthYear : int = int(input("Kérem adja meg a születési évét: "))

system('cls')

print(f"{name} ön {birthYear}-ben született!")


