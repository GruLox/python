from mathfuctions import *
from consoleIO import *


a: float = None
b: float = None
result: float = None

a = getNumberFromConsole()
b = getNumberFromConsole()

result = addition(a, b)

printToConsole(a, b, result, "+")

result = subtraction(a, b)
printToConsole(a, b, result, "-")

result = multiplication(a, b)
printToConsole(a, b, result, "*")

result = division(a, b)
printToConsole(a, b, result, "/")







