name: str = None
temp: str = None

while(name == None):
    print("Kérem írja be a nevét: ", end="")
    temp = input().strip()
    if (len(temp) >= 2 and temp.isalpha()):
        name = temp