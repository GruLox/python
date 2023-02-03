smallerNumber: int = None
biggerNumber: int = None
smallTemp: str = None
bigTemp: str = None

while (smallerNumber == None):
    print("Kisebb szám: ")
    smallTemp = input()
    if (smallTemp.isnumeric()):
        smallerNumber = int(smallTemp)

while (biggerNumber == None or biggerNumber <= smallerNumber):
    print("Nagyobb szám: ")
    bigTemp = input()
    if (bigTemp.isnumeric()):
        biggerNumber = int(bigTemp)

for i in range(biggerNumber, smallerNumber, -1):
    print(f"{i}, ", end="")
