start: int = None
end : int = None
divisibleByFive: int = 0
divisibleBySeven: int = 0
result: str = None

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(start, end + 1, 1):
    if (i % 5 == 0):
        divisibleByFive += 1
    elif ( i % 7 == 0):
        divisibleBySeven += 1

if (divisibleByFive > divisibleBySeven):
    result = "öttel"
elif (divisibleByFive < divisibleBySeven):
    result = "héttel"
else:
    print("Az öttel és 7-tel osztható számok mennyisége megegyezik")

print(f"Az intervallumban nagyobb a {result} osztható számok mennyisége.")


