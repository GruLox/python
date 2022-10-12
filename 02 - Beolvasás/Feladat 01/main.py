from os import system

name: str = None

print("Kérem adja meg a nevét: ", end='')
name = str(input())

system('cls')

print(f"Üdvözlöm, {name}")