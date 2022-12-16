start: int = None
end : int = None
evenSum: int = 0
oddSum: int = 0
average: float = 0

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(start, end + 1, 1):
    if (i % 2 == 0):
        evenSum += i
    else:
        oddSum += i

average = (evenSum + oddSum) / 2

print(f"A páros és páratlan számok összegének átlaga: {average}")


    

