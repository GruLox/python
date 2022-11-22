num1: int = None

print("Adja meg a számot! ", end='')
num1 = int(input())

if(num1 % 4 == 0 and num1 % 6 == 0):
    print("A szám osztható 4-gyel és 6-tal is.")
else:
    print("A szám nem osztható 4-gyel és 6-tal is.")

import math
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague