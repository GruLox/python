from platform import release
from re import S


print("Adja meg kedvenc filmjének címét: ")
title= str(input())

print("Adja meg kedvenc filmjének rendezőjét: ", end='')
director= str(input())

print("Adja meg a főszereplő nevét: ", end='')
lead= str(input())

print("Adja meg a film megjelenési évét: ", end='')
releaseYear = str(input())

print(f"{releaseYear}-ban {director} rendezésében megjelent a/az {title} című film {lead} főszereplésével!")