from random import randint

smallEven: int = None
bigOdd: int = None
randN: int = None
tempEven: str = None
tempOdd: str = None
countOfDivisibleBy4: int = 0

while (smallEven == None or bigOdd == None or smallEven % 2 != 0
    or bigOdd % 2 != 1 or smallEven >= bigOdd):
    print("Kérem adjon meg egy páros számot: ")
    tempEven = input()
    print("Kérem adjon meg egy, az előzőnél nagyobb páratlan számot: ")
    tempOdd = input()

    if (tempEven.isnumeric() and tempOdd.isnumeric()):
        smallEven = int(tempEven)
        bigOdd = int(tempOdd)
    else:
        continue

randN = randint(smallEven, bigOdd)
print(f"A random szám: {randN}")

if (abs(bigOdd - randN) > abs(smallEven - randN)):
    print(f"A {bigOdd} messzebb található a random számtól ({randN})")
else:
    print(f"A {smallEven} messzebb található a random számtól ({randN})")

print(f"A két érték átlaga: {(smallEven + bigOdd) / 2}")

for i in range(smallEven, bigOdd + 1, 1):
    if (i % 4 == 0):
        countOfDivisibleBy4 += 1

print(f"A 4-gyel osztható számok mennyisége az intervallumban: {countOfDivisibleBy4}")

