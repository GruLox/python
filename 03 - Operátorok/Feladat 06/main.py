num1:float = None
num2: float = None
num3: float = None
eredmeny: float = None

print("Adja meg az első számot!")
num1 = float(input())

print("Adja meg a második számot!")
num2 = float(input())

print("Adja meg a harmadik számot!")
num3 = float(input())

eredmeny = ((num1 + 0.5) * (num2 - 0.7)) % num3

print(f"Az eredmeny: {eredmeny}.")