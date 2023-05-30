from volleyballer import Volleyballer
from typing import *
from volleyballIO import importVolleyballers, exportPlayers, exportPlayersByTeams, exportNations
from services import filterHitters, sortIntoDictByTeams, sortPlayersByHeight, toDictByNations, filterAboveAverage

volleyballers: List[Volleyballer] = importVolleyballers()

# Írjuk ki a képernyőre az össz adatot
for volleyballer in volleyballers:
    print(volleyballer)

# Keressük ki az ütő játékosokat az utok.txt állömányba
hitters: List[Volleyballer] = filterHitters(volleyballers)
exportPlayers(hitters, "utok.txt")


""""A csapattagok.txt állományba mentsük a csapatokat és a hozzájuk tartozó játékosokat a következő formában:
  Telekom Baku: Yelizaveta Mammadova,Yekaterina Gamova,"""
teamsDict: dict[str, List[Volleyballer]] = sortIntoDictByTeams(volleyballers)
exportPlayersByTeams(teamsDict, "csapattagok.txt")

# Rendezzük a játékosokat magasság szerint növekvő sorrendbe és a magaslatok.txt állományba mentsük el.
sortedVolleyballers: List[Volleyballer] = sortPlayersByHeight(volleyballers)
exportPlayers(sortedVolleyballers, "magaslatok.txt")

# Mutassuk be a nemzetisegek.txt állományba, hogy mely nemzetiségek képviseltetik magukat a röplabdavilágban mint játékosok és milyen számban.
nationsDict: dict[str, int] = toDictByNations(volleyballers)
exportNations(nationsDict, "nemzetisegek.txt")


# atlagnalmagasabbak.txt állományba keressük azon játékosok nevét és magasságát akik magasabbak mint az „adatbázisban” szereplő játékosok átlagos magasságánál.
aboveAverage: List[Volleyballer] = filterAboveAverage(volleyballers)
exportPlayers(aboveAverage, "atlagnalmagasabbak.txt")