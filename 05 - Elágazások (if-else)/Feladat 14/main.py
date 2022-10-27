x: int = None
y: int = None
z: int = None

print("Adja meg az első számot! ", end='')
x = int(input())

print("Adja meg a második számot! ", end='')
y = int(input())

print("Adja meg a harmadik számot! ", end='')
z = int(input())

if(x % y == 0 and x % z == 0):
    print("X osztható mindkét számmal.")
elif(x % y == 0):
    print("X oszthatü y-nal")
elif(x % z == 0):
    print("X oszthatü z-vel")
else:
    print("X nem osztható egyik számmal sem.")
