from volleyballer import Volleyballer
from typing import *

def filterHitters(volleyballers: List[Volleyballer]) -> List[Volleyballer]:
    hitters: List[Volleyballer] = []

    for volleyballer in volleyballers:
        if (volleyballer.position == "ütő"):
            hitters.append(volleyballer)
    
    return hitters


def sortIntoDictByTeams(volleyballers: List[Volleyballer]) -> dict[str, List[Volleyballer]]:
    teamsDict = {}

    for volleyballer in volleyballers:
        if (volleyballer.team not in teamsDict):
            teamsDict[volleyballer.team] = [volleyballer]
        else:
            teamsDict[volleyballer.team].append(volleyballer)
        
    return teamsDict


def sortPlayersByHeight(volleyballers: List[Volleyballer]) -> List[Volleyballer]:
    for i in range(len(volleyballers) - 1):
        for j in range(len(volleyballers) - i - 1):
            if (volleyballers[j].height > volleyballers[j + 1].height):
                volleyballers[j + 1], volleyballers[j] = volleyballers[j], volleyballers[j + 1]
    
    return volleyballers


def toDictByNations(volleyballers: List[Volleyballer]) -> dict[str, int]:
    nationsDict: dict[str, int] = {}

    for volleyballer in volleyballers:
        if (volleyballer.nationality not in nationsDict):
            nationsDict[volleyballer.nationality] = 1
        else:
            nationsDict[volleyballer.nationality] += 1

    return nationsDict


def calculateHeightAverage(volleyballers: List[Volleyballer]) -> float:
    sum = 0
    for volleyballer in volleyballers:
        sum += volleyballer.height

    return round(sum / len(volleyballers), 2)


def filterAboveAverage(volleyballers: List[Volleyballer]):
    average = calculateHeightAverage(volleyballers)
    aboveAverage: List[Volleyballer] = []

    for volleyballer in volleyballers:
        if (volleyballer.height >= average):
            aboveAverage.append(volleyballer)
    
    return aboveAverage

        



    

