x: int = None
y: int = None

print("Adja meg az első számot! ", end='')
x = int(input())

print("Adja meg a második számot! ", end='')
y = int(input())

if(x % y == 0):
    print("Y osztója X-nak")
else:
    print("Y nem osztója X-nek")
