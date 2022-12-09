start: int = None
end : int = None
sum : int = 0
product: int = 1

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(start, end + 1, 1):
    sum += i

print(f"A számok össszege: {sum}")

for i in range(start, end + 1, 1):
    product *= i

print(f"A számok szorzata: {product}")

