num1 : int = None
num2 : int = None
operator : str = ""
result : float = None

print("Kérem adja meg az első számot: ")
num1 = int(input())

print("Kérem adja meg a második számot: ")
num2 = int(input())

print("Kérem a műveleti jelet")
operator = input()

match operator:
    case "+":
        result = round(num1 + num2, 2)
    case "-":
        result = round(num1 - num2, 2)
    case "/":
        result = round(num1 / num2, 2)
    case "*":
        result = round(num1 * num2, 2)
    case _:
        print("Nincs ilyen művelet!")

if(result != None):
    print(f"Az eredmény: {result}")


    
