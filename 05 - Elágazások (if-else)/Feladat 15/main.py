zoldsegleves: bool = False
husleves: bool = False
gyumolcsleves: bool = False
sultcsirkecomb: bool = False
sultCsirkemell: bool = False
rakottzoldseg: bool = False
spagetti: bool = False
pizza: bool = False
rizs: bool = False
paroltzoldseg: bool = False
gyumolcs: bool = False
sultkrumpli: bool = False
salata: bool = False
kola: bool = False
eloetel: int = None
foetel: int = None
koret: int = None
ertekeles: str = None

menu : str = "A mai menü tartalma: "
ertekeles = ""



print("Előétel\n1-Zöldségleves\n2-Húsleves\n3-Gyümölcsleves\nMit választ: ")
eloetel = int(input())
print("Főétel\n1-Sültcsirkecomb\n2-Sült csirkemell\n3-Rakottzöldség\n4-Spagetti\n5-Pizza\nMit választ: ")
foetel = int(input())
print("Köret\n1-Rizs\n2-Pároltzöldség\n3-Gyümölcs\n4-Sültkrumpli\n5-Saláta\n6-Kóla\nMit választ: ")
koret = int(input())

if(eloetel == 1):
    menu += "Zöldségleves, "
    zoldsegleves = True
elif(eloetel == 2):
    menu += "Húsleves, "
    husleves = True
else:
    menu += "Gyümölcsleves, "
    gyumolcsleves = True



if(foetel == 1):
    menu += "Sültcsirkecomb, "
    sultcsirkecomb = True
elif(foetel == 2):
    menu += "Sült csirkemell, "
    sultCsirkemell = True
elif(foetel == 3):
    menu += "Rakottzöldség, "
    rakottzoldseg = True
elif(foetel == 4):
    menu += "Spagetti, "
    spagetti = True
else:
    menu += "Pizza, "
    pizza = True

if(koret == 1):
    menu += "Rizs"
    rizs = True
elif(koret == 2):
    menu += "Pároltzöldség"
    paroltzoldseg = True
elif(koret == 3):
    menu += "Gyümölcs"
    gyumolcs = True
elif(koret == 4):
    menu += "Sültkrumpli"
    sultkrumpli = True
elif(koret == 5):
    menu += "Saláta"
    salata = True
else:
    menu += "Kóla"
    kola = True


if((eloetel != None and foetel != None and koret != None) and zoldsegleves and spagetti and (gyumolcs or salata) and (not pizza and not rakottzoldseg)):
    ertekeles = "A mai menü értékelése: kiváló"
elif(zoldsegleves and sultCsirkemell and rizs and not sultkrumpli):
    ertekeles = "A mai menü értékelése: fitnesz menü"
elif(husleves and sultcsirkecomb and (sultkrumpli or salata) and not (rakottzoldseg or pizza)):
    ertekeles = "A mai menü értékelése: vasárnapi menü"
elif(pizza or spagetti) and gyumolcs and kola and not (rakottzoldseg or paroltzoldseg):
    ertekeles = "A mai menü értékelése: napi menü"


print(menu)
print(ertekeles)









