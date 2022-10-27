from os import system

num1: int = None

print("Adja meg a számot! ", end='')
num1 = int(input())

if(num1 >= 0 and num1 <= 9):
    print("Egyjegyű szám")
elif(num1 >= 10 and num1 <= 99):
    print("Kétjegyű szám")
elif(num1 >= 100 and num1 <= 999):
    print("Háromjegyű szám.")
else:
    print("A szám vagy több, mint háromjegyű, vagy negatív.")