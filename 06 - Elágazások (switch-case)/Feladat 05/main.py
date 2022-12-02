r1 : float = None
r2 : float = None
type : str = None
result : float = None

print("Kérem adja meg az első ellenállás értékét: ")
r1 = float(input())

print("Kérem adja meg az első ellenállás értékét: ")
r2 = float(input())

print("Kérem adja meg a kapcsolás típusát: ")
type = str(input()).lower().strip()

match type:
    case "p":
        result = (r1*r2) / (r1 +r2)
    case "s":
        result = r1 + r2
    case _:
        print("Ilyen kötés nem létezik!")
    
if(result != None):
    print(f"Az eredő ellenállás: {result}")






