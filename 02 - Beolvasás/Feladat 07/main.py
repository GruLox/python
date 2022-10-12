brand:str= None
type:str= None
cubicCM:int= None
model:str= None
releaseYear:int= None

print("Adja meg a kedvenc autójának márkáját: ", end='')
brand = str(input())

print("Adja meg a kedvenc autójának típusát: ", end='')
type = str(input())

print("Adja meg a kedvenc autójának köbcentijét: ", end='')
cubicCM = str(input())

print("Adja meg a kedvenc autójának modelljét: ", end='')
model = str(input())

print("Adja meg a kedvenc autójának megjelenési évét: ", end='')
releaseYear = int(input())

print(f"Márka: {brand}\nModell: {model}\nTípus: {type}\nKöbcenti: {cubicCM}\nMegjelenési év: {releaseYear}")