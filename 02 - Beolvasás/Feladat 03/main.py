from os import system

print("Kérem adja meg a magasságát: ", end='')
height: float = float(input())

print("Kérem adja meg a nevét: ", end='')
name: str = input()

system('cls')

print(f"{name} az ön magassága {height}m!")