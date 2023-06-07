import os
from car import Car
from typing import *

def importCars(filePath: str) -> List[Car]:
    basepath = os.path.dirname(os.path.abspath(__file__))
    fullFilePath = os.path.join(basepath, filePath)

    with open(fullFilePath, "r", encoding="uft-8") as file:
        for line in file:
            car = Car()
            auto, mpg, hengerekSzama, nyomatek, loero, suly, gyorsulas, megjelenesiEv, eredet = line.split(";")

            car.auto = auto

