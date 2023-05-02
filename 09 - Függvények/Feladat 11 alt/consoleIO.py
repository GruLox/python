from worker import Worker
from functions import *

def getWorkers(count: int) -> list():
    workers: list(Worker) = []
    for i in range(count):
        name = getName(i + 1)
        hoursWorked = getHours(i + 1)
        wage = calculateWage(hoursWorked)
        workers.append(Worker(name, hoursWorked, wage))
    
    return workers


def getName(index: int) -> str:
    name: str = None
    while (name == None or len(name) < 2):
        print(f"Kérem adja meg a {index}. dolgozó nevét: ", end="")
        name = input().strip().capitalize()
    
    return name


def getHours(index: int) -> int:
    hours: int = None
    while (hours == None):
        print(f"Kérem adja meg a {index}. dolgozó ledolgozott óráit: ", end="")
        temp: str = input().strip()
        if (temp.isnumeric()):
            hours = int(temp)
        
    return hours


