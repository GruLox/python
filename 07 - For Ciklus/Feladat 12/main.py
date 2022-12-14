start: int = None
end : int = None
counter: int = 0

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(start, end + 1, 1):
    if (i % 3 == 0):
        counter += 1

print(f"A 3-mal osztható számok mennyisége: {counter}")