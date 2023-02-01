limit: str= None
temp: str = None
numberToAdd: int = 0
stepCount: int = 0
sum: int = 0

while(limit == None or not limit.isistance(limit, int)):
    print("Limit: ", end="")
    limit = input().strip()

if(limit.isnumeric()):
    limit = int(limit)

while (sum < limit):
    print("Kérem írjon be egy számot, hogy az összeghez hozzáadjam: ", end="")
    temp = input().strip()
    if (temp.isnumeric()):
        stepCount = stepCount + 1
        numberToAdd = int(temp)
        sum = sum + numberToAdd
        print(f"Az összeg: {sum}")
    else:
        print("Nem számot adott meg!")
        continue
    if (sum > limit):
        print(f"Elérte a limitet, ennyi lépés alatt: {stepCount}")