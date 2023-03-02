start: int = None
end : int = None

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

if (start % 2 != 0):
    start -= 1

for i in range(end, start - 1, -2):
        print(i)

