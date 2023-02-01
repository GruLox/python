choice: int = None
temp: str  = None
drink: int = None

print("1 - 7UP\n2 - Kinley\n3 - Fanta\n4 - Sió\n5 - Kubu")

while (choice == None or not (choice > 0 and choice <= 5)):
    print("Válasszon egy üdítőt: ")
    temp = input()
    if (temp.isnumeric()):
        choice = int(temp)
    
match choice:
    case 1:
        drink = "7UP"
    case 2:
        drink = "Kinley"
    case 3:
        drink = "Fanta"
    case 4:
        drink = "Sió"
    case 5:
        drink = "Kubu"

print(f"A választott üdítő a {drink}")
    
