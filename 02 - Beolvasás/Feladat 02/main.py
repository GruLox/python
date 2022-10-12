from os import system

print("Kérem adja meg a nevét: ", end='')
name : str = input()

print("Kérem adja meg a születési évét: ", end='')
birthYear : int = int(input())

system('cls')

print(f"{name} ön {birthYear}-ben született!")


