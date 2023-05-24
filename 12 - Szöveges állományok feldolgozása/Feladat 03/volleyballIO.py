import os
from volleyballer import Volleyballer
from typing import *

def importVolleyballers():
    fileName = "data/adatok.txt"
    basepath = os.path.dirname(os.path.abspath(__file__))
    fileFullPath = os.path.join(basepath, fileName)

    volleyballers: List[Volleyballer] = []

    try:
        with open(fileFullPath, encoding="utf-8", mode="r") as file:
            for line in file:
                volleyballer = Volleyballer()
                oneLine = line.strip()

                name, height, position, nationality, team, countryOfTeam = oneLine.split("\t")

                volleyballer.name = name
                volleyballer.height = height
                volleyballer.position = position
                volleyballer.nationality = nationality
                volleyballer.team = team
                volleyballer.countryOfTeam = countryOfTeam

                volleyballers.append(volleyballer)
    
    except FileNotFoundError:
        print("File not found!")



