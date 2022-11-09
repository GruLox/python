num1: int = None

print("Adja meg a számot! ", end='')
num1 = int(input())


if(num1 % 2 == 0 and num1 % 3 == 0):
    print("ZIZI")
elif(num1 % 2 == 0):
    print("BIZ")
elif(num1 % 3 == 0):
    print("BAZ")
else:
    print("A szám nem osztható sem 2-vel, sem 3-mal")
