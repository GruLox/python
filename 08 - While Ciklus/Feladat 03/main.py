from random import randint

number: int = None
solution: int = None
temp: str= None
tries = 0

solution = randint(1, 9)

while(tries < 5):
    print("Tippeljen: ")
    temp = input()
    if (temp.isnumeric()):
        number = int(temp)
    else:
        continue

    if (number == solution):
        print("Talált!")
        break
    else:
        tries += 1
        
if (tries==5):
    print("Nem nyert!")