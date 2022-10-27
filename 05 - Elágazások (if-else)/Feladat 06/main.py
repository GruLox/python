num1: int = None
num2: int = None
num3: int = None

print("Adja meg az első számot! ", end='')
num1 = int(input())

print("Adja meg a második számot! ", end='')
num2 = int(input())

print("Adja meg a harmadik számot! ", end='')
num2 = int(input())

if(num1 > num2 and num1 > num3 and num2 > num3):
    print(f"A számok sorrendje: {num3} < {num2} < {num1}")