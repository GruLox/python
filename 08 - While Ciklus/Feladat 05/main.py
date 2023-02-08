limit: int = None
truncatedString: str = None
numberToAdd: int = 0
stepCount: int = 0
sum: int = 0

while(limit == None or not isinstance(limit, int)):
    print("Limit: ", end="")
    truncatedString = input().strip()
    truncatedString = truncatedString.replace(".", "").replace("-", "")
    if (truncatedString.isnumeric()):
        limit = int(truncatedString)


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
        
if (sum > limit):
    print(f"Elérte a limitet, ennyi lépés alatt: {stepCount}")