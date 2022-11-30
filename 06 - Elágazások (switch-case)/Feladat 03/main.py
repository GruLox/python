choice: int = 0

print("Kérem válasszon üdítőt: \n1 - Coca Cola\n2 - Pepsi\n3 - Fanta\n4 - Sprite")

choice = int(input())

match choice:
    case 1:
        print("A választott üdítő a Coca Cola")
    case 2:
        print("A választott üdítő a Pepsi")
    case 3:
        print("A választott üdítő a Fanta")
    case 4:
        print("A választott üdítő a Sprite")