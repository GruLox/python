choice: int = None
temp: int  = None

print("1 - 7UP\n2 - Kinley\n3 - Fanta\n4 - Sió\n5 - Kubu")

while (choice == None or not (choice > 0 and choice <= 5)):
    print("Válasszon egy üdítőt: ")
    temp = input()
    
    
