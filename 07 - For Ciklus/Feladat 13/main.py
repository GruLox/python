start: int = None
end : int = None
evenCount: int = 0
oddCount: int = 0
result: str = None

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(start, end + 1, 1):
    if (i % 2 != 0):
        oddCount += 1
    else:
        evenCount += 1

if (evenCount > oddCount):
    result = "páros"
elif (evenCount < oddCount):
    result = "páratlan"
else:
    print("A páros és páratlan számok mennyisége megegyezik.")

print(f"Az intervallumban nagyobb a {result} számok mennyisége.")
