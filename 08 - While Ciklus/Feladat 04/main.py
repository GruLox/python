sum: int= 0
temp: str = 0
numberToAdd: int = 0

while (sum < 100):
    print("Kérem írjon be egy számot, hogy az összeghez hozzáadjam: ", end="")
    temp = input().strip()
    if (temp.isnumeric()):
        numberToAdd = int(temp)
        sum = sum + numberToAdd
        print(f"Az összeg: {sum}")
    else:
        print("Nem számot adott meg!")