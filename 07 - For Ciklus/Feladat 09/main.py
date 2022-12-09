start: int = None
end : int = None

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(end, start - 1, -1):
    if(i % 2 == 0):
        print(i)

