day: int = 0

print("Adja meg a mai nap sorszámát: ")

day = int(input())

match day:
    case 1:
        print("Hétfő")
    case 2:
        print("Kedd")
    case 3:
        print("Szerda")
    case 4: 
        print("Csütörtök")
    case 5:
        print("Péntek")
    case 6: 
        print("Szombat")
    case 7:
        print("Vasárnap")