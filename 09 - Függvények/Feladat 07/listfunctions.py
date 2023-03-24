from random import randint


def populateWithRandom() -> list:
    nums = []
    n = None
    for _ in range(10):
        n = randint(1, 10)
        nums.append(n)
    return nums


def printOutList(name:str, arr: list) -> None:
    print(f"{name} tartalma: ", end="")
    for element in arr:
        print(f"{element}, ", end="")
    print()


def sumOfList(arr: list) -> int:
    sum: int = 0
    for element in arr:
        sum += element
    
    return sum


def decideWinner(listSum1: int, listSum2: int) -> int:
    if (listSum1 > listSum2):
        return listSum1
    else:
        return listSum2


