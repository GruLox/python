from os import system

height: float = float(input("Kérem adja meg a magasságát: "))
name: str = input("Kérem adja meg a nevét: ")

system('cls')

print(f"{name} az ön magassága {height}m!")