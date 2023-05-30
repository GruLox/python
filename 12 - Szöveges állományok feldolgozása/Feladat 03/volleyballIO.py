import os
from volleyballer import Volleyballer
from typing import *

def importVolleyballers() -> List[Volleyballer]:
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
                volleyballer.height = int(height)
                volleyballer.position = position
                volleyballer.nationality = nationality
                volleyballer.team = team
                volleyballer.countryOfTeam = countryOfTeam

                volleyballers.append(volleyballer)

            return volleyballers
    
    except FileNotFoundError:
        print("File not found!")


def exportPlayers(players: List[Volleyballer], fileName: str) -> None:
    basepath = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output/"
    fileFullPath = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, encoding="utf-8", mode="w") as file:
            for player in players:
                file.write(f"{player}\n")

    except FileNotFoundError:
        print("File not found")


def exportPlayersByTeams(teamsDict: dict[str, List[Volleyballer]], fileName: str) -> None:
    basepath = os.path.dirname(os.path.abspath(__file__))
    basepath  += "/output/"
    fileFullPath = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, "w", encoding="utf-8") as file:
            for team, players in teamsDict.items():
                file.write(f"{team}: ")
                for player in players:
                    file.write(f"{player.name}, ")
                file.write("\n")

    except FileNotFoundError:
        print("File not found")


def exportNations(nationsDict: dict[str, int], fileName) -> None:
    basepath = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output/"
    fileFullPath = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, "w", encoding="utf-8") as file:
            for nation, playercount in nationsDict.items():
                file.write(f"{nation}: {playercount}\n")


    except IOError:
        print("Exception occured")


    



