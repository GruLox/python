age: int = None

while  age == None or not (age >= 0 and age <= 99):
    print("Adja meg az életkorát!")
    temp = input()
    if (temp.isnumeric()):
        age = int(temp)

if (age >= 0 and age <= 6):
    print("gyerek")
elif(age >= 7 and age <= 18):
    print("iskolás")
elif(age >= 19 and age <= 65):
    print("dolgozó")
else:
    print("nyugdíjas")