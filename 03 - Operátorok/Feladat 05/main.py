from ftplib import error_perm
from xml.dom import NoModificationAllowedErr


num1: float = None
num2: float = None
num3: float = None
num4: float = None
eredmeny:float = None

print("Adja meg az első számot!")
num1 = float(input())

print("Adja meg a második számot!")
num2 = float(input())

print("Adja meg a harmadik számot!")
num3 = float(input())

print("Adja meg a negyedik számot!")
num4 = float(input())

eredmeny = (num1 + num2) / (num3 - num4)

print(f"Az eredmeny: {eredmeny}.")