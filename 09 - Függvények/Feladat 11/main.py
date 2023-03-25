from consoleIO import *
from functions import calculateWage

worker1Name: str = getName(1)
worker1Hours: int = getHours(1)
worker2Name: str = getName(2)
worker2Hours: int = getHours(2)
worker3Name: str = getName(3)
worker3Hours: int = getHours(3)
worker4Name: str = getName(4)
worker4Hours: int = getHours(4)
worker5Name: str = getName(5)
worker5Hours: int = getHours(5)

worker1Wage: int = calculateWage(worker1Hours)
worker2Wage: int = calculateWage(worker2Hours)
worker3Wage: int = calculateWage(worker3Hours)
worker4Wage: int = calculateWage(worker4Hours)
worker5Wage: int = calculateWage(worker5Hours)

printToConsole(worker1Name, worker1Hours, worker1Wage)
printToConsole(worker2Name, worker2Hours, worker2Wage)
printToConsole(worker3Name, worker3Hours, worker3Wage)
printToConsole(worker4Name, worker4Hours, worker4Wage)
printToConsole(worker5Name, worker5Hours, worker5Wage)


