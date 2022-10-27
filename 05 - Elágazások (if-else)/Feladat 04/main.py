num1: int = None
num2: int = None

print("Adja meg az első számot! ", end='')
num1 = int(input())

print("Adja meg a második számot! ", end='')
num2 = int(input())

if(num1 > num2):
    print(f"A nagyobbik szám a {num1}")
elif(num1 < num2):
    print(f"A nagyobbik szám a {num2}")
else:
    print("A két szám egyenlő.")


