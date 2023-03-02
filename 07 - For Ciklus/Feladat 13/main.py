start: int = None
end : int = None
evenSum: int = 0
oddSum: int = 0
result: str = None

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(start, end + 1, 1):
    if (i % 2 != 0):
        oddSum += i
    else:
        evenSum += i

if (evenSum > oddSum):
    result = "páros"
elif (evenSum < oddSum):
    result = "páratlan"
else:
    print("A páros és páratlan számok mennyisége megegyezik.")

print(f"Az intervallumban nagyobb a {result} számok mennyisége.")
