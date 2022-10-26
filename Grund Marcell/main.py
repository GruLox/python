name:str= None
brand:str= None
model:str= None
releaseYear:int= None
budget:int=None

print("Hogy hívják? ", end='')
name = str(input())

print("Milyen márkájú járművet szeretne? ", end='')
brand = str(input())

print("Milyen modellt szeretne? ", end='')
model = str(input())

print("Milyen évjáratú járművet szeretne? ", end='')
releaseYear = str(input())

print("Hány millió forintot szánna rá? ", end='')
budget = str(input())

print(f"{name}.\nJó napot kedves {name}. Miben segíthetek?\nEngem érdekelne egy: {brand}.\nÉrtem, egy {brand}. Melyik modell?\n{model}\nÉvjárat?\n{releaseYear}\nHány milliót szánna rá?\n{budget}")

print(f"Sajnálom kedves {name}, de jelenleg {releaseYear}-es évjáratú és {brand}s {model} nincs a kínálatunkban ami beleférne a {budget} millió forintba.")