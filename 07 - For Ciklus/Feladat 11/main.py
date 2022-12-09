start: int = None
end : int = None
sumOfEvens : int = 0
productOfOdds : int = 0

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range(start, end + 1, 1):
    if (i % 2 == 2):
        sumOfEvens += i
    else:
        productOfOdds *= i



