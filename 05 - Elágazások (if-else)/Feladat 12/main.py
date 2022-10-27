from os import system

num1: int = None

print("Adja meg a számot! ", end='')
num1 = int(input())

if(num1 >= -20 and num1 <= -10):
    print("A szám -20 és -10 között van.")
elif(num1 >= 20 and num1 <= 10):
    print("A szám 20 és 10 között van.")
else:
    print("A szám nincs egyik intervallumban sem.")