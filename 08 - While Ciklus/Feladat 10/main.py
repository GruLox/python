number: int = None
temp: str = None
sumOfDivisibleByFive: int = 0
divisibleByElevenCount: int = 0

while (number == None):
    print("Max kétjegyű szám: ")
    temp = input()
    if (temp.isnumeric() and len(temp) < 3):
        number = int(temp)

print(f"A 0 és {number} közötti páros számok: ", end="")
for i in range(0, number + 1, 1):
    if (i % 2 == 0):
        print(i, end=", ")
    if (i % 5 == 0):
        sumOfDivisibleByFive += i
    if (i % 11 == 0):
        divisibleByElevenCount += 1


print(f"\nSzámok amelyeknek, ha héttel elosztjuk 3 a maradéka: ", end="")
for i in range(0, number + 1, 1):
    if (i % 7 == 3):
        print(i, end=", ")


print(f"\nAz öttel osztható számok összege: {sumOfDivisibleByFive}")
print(f"A 11-el osztható számok mennyisége: {divisibleByElevenCount}")
        

