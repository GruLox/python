start: int = None
end : int = None
result: int = 0
changer: int = 1


print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(start, end + 1, 1):
    result += i * changer
    changer *= -1

print(f"A művelet eredménye: {result}")
