r1 : float = None
r2 : float = None
type : str = None
result : float = None

print("Kérem adja meg az első ellenállás értékét: ")
r1 = float(input())

print("Kérem adja meg az első ellenállás értékét: ")
r2 = float(input())

print("Kérem adja meg a kapcsolás típusát: ")
type = str(input())

match type:
    case "p" | "P":
        result = r1*r2




