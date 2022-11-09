num1: int = None

print("Adja meg a számot! ", end='')
num1 = int(input())

if(num1 % 2 == 0):
    print("A szám páros")
else:
    print("A szám páratlan")

if(num1==0):
    print("A szám 0")
elif(num1 < 0):
    print("A szám negatív")
else:
    print("A szám pozitív")

if(num1 % 5 == 0):
    print("A szám osztható 5-tel")
else:
    print("A szám nem osztható 5-tel")



