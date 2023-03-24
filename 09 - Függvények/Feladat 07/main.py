from listfunctions import *



list1: list[int] = populateWithRandom()
list2: list[int] = populateWithRandom()

printOutList("1. lista", list1)
printOutList("2. lista", list2)

list1Sum: int = sumOfList(list1)
list2Sum: int = sumOfList(list2)

winner: list = decideWinner(list1Sum, list2Sum)

nameOfWinner: str = "1. lista" if (winner == list1Sum) else "2.lista"

print(f"{nameOfWinner} elemeinek összege a nagyobb.")


