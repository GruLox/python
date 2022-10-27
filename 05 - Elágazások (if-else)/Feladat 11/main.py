num1: int = None

print("Adja meg a számot! ", end='')
num1 = int(input())

if(num1 % 2 == 0 and num1 > 0 and num1 % 5 == 0):
    print("A szám páros, pozitív és osztható 5-tel")
elif(num1 % 2 == 0 and num1 > 0 and num1 % 5 != 0):
    print("A szám páros, pozitív de nem osztható 5-tel")
elif(num1 % 2 == 0 and num1 < 0 and num1 % 5 == 0):
    print("A szám páros, negatív és osztható 5-tel")
elif(num1 % 2 == 0 and num1 < 0 and num1 % 5 != 0):
    print("A szám páros, negatív de nem osztható 5-tel")

elif(num1 % 2 != 0 and num1 > 0 and num1 % 5 == 0):
    print("A szám páratlan, pozitív és osztható 5-tel")
elif(num1 % 2 != 0 and num1 > 0 and num1 % 5 != 0):
    print("A szám páratlan, pozitív de nem osztható 5-tel")
elif(num1 % 2 != 0 and num1 < 0 and num1 % 5 == 0):
    print("A szám páratlan, negatív és osztható 5-tel")
elif(num1 % 2 != 0 and num1 < 0 and num1 % 5 != 0):
    print("A szám páratlan, negatív de nem osztható 5-tel")
else:
    print("A szám 0")   


