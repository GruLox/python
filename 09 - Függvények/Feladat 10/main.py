from random import randint
from consoleIO import getNumber
from functions import game

n1: int = getNumber(0, 9)
n2: int = getNumber(40, 50)

print(f"A két megadott szám {n1} és {n2}")

randNum: int = randint(n1, n2) 

tries = game(randNum)

print(f"Talált! {tries} próbálkozásból találta ki a számot.")

