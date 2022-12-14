start: int = None
end : int = None

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

if (start % 2 != 1):
    start +=1


for i in range(start, end + 1, 2):
        print(i)