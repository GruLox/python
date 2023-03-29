HOURLYWAGE: int = 1000
OVERTIMEWAGE: int = 1500

def calculateWage(hours: int):
    salary: int = None
    if (hours < 40):
        salary = hours * HOURLYWAGE
    else:
        salary = 40 * HOURLYWAGE + (hours - 40) * OVERTIMEWAGE
    
    return salary