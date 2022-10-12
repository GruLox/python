print("Adja meg a kedvenc együttesét: ", end='', end='')
band: str = input()

print("Adja meg a kedvenc számának címét: ", end='')
songName: str = input()

print("Adja meg a kedvenc számának hosszát: ", end='')
songLength: float = float(input())

print(f"Az ön kedvenc együttese a/az {band}, a legjobb zeneszámuk a/az {songName} melynek hossza {songLength} perc!")