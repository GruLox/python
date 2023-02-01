smallerNumber: int = None
biggerNumber: int = None
smallTemp: str = None
bigTemp: str = None

while ((smallerNumber == None or biggerNumber == None)
      or biggerNumber <= smallerNumber):
      print("Kisebb szám: ")
      smallTemp = input()
      print("Nagyobb szám: ")
      bigTemp = input()
      if ((smallTemp.isnumeric()) and (bigTemp.isnumeric())):
        smallerNumber = int(smallTemp)
        biggerNumber = int(bigTemp)
    
for i in range(biggerNumber, smallerNumber, -1):
    print(f"{i}, ", end="")
