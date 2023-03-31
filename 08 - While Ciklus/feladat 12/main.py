sum: float = None
temp: str = None
counter: int = 0

while (sum == None):
    print("Megtakarított pénz: ", end="")
    temp = input()
    if (temp.isnumeric()):
        sum = float(temp)

while (sum < 100000):
    sum *= 1.02
    counter += 1

print(f"{counter} hónap alatt fogja a megtakarítás elérni a 100 000 Ft-ot")

