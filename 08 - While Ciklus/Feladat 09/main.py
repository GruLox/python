number: int = None
temp: str = None

while (number == None or  not (number >= 100 and number <= 999)):
    print("Háromjegyű szám: ")
    temp = input()
    if (temp.isnumeric()):
        number = int(temp)
    
if (number % 7 == 0):
    print("A szám osztható 7-tel")
else:
    print("A szám NEM osztható 7-tel")