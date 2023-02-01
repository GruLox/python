number: int = None
temp: str = None

while (number == None):
    print("Háromjegyű szám: ")
    temp = input()
    if (temp.isnumeric() and len(temp) == 3):
        number = int(temp)
    
if (number % 7 == 0):
    print("A szám osztható 7-tel")
else:
    print("A szám NEM osztható 7-tel")