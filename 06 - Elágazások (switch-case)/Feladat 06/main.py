import math

width: int=None
height: int=None
choice: str=None
result: float=None

print("Adja meg a téglalap hosszát: ")
height=int(input())

print("Adja meg a téglalap szélességét: ")
width=int(input())

print("Kérem válasszon kiszámolható műveletek közül: \nt - terület\nk - kerület\na - átló")
choice=input()

match choice:
    case "t":
        result= width * height
    case "k":
        result=2 * (width+height)
    case "a":
        result = math.sqrt(math.pow(width, 2)+ math.pow(height, 2))
    case _:
        print("Nincs ilyen művelet!")

if(result != None):
    print(f"Az eremény: {result}")


