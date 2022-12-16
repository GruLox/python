start: int = None
end : int = None
numSum: int = 0
divisor: int = 0
average: float = None

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(start, end + 1, 1):
    divisor += 1
    numSum += i

average = numSum / divisor

print(f"A számok átlaga: {average}")
