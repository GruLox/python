num1: int = None
num2: int = None
num3: int = None

print("Adja meg az első számot! ", end='')
num1 = int(input())

print("Adja meg a második számot! ", end='')
num2 = int(input())

print("Adja meg a harmadik számot! ", end='')
num3 = int(input())

if(num1 > num2 and num1 > num3 and num2 > num3):
    print(f"A számok sorrendje: {num3} < {num2} < {num1}")
elif(num1 > num2 and num1 > num3 and num2 < num3):
    print(f"A számok sorrendje: {num2} < {num3} < {num1}")
elif(num2 > num1 and num2 > num3 and num1 > num3):
    print(f"A számok sorrendje: {num3} < {num1} < {num2}")
elif(num2 > num1 and num2 > num3 and num1 < num3):
    print(f"A számok sorrendje: {num1} < {num3} < {num2}")
elif(num3 > num1 and num3 > num2 and num2 < num1):
    print(f"A számok sorrendje: {num2} < {num1} < {num3}")
elif(num3 > num1 and num3 > num2 and num2 > num1):
    print(f"A számok sorrendje: {num1} < {num2} < {num3}")



