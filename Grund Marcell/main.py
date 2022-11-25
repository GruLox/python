#iskolaválasztás
#3 féle kedvezmény, mindet kiszámolni, mindet kiíratni
#legjobb ajánlat if statementtel

choice: int = None
basePrice: int = None
numberOfStudents: int = None
groupDiscount: float = None
schoolDiscount: float = None
studentDiscount: float = None
bestDeal : str = ""
bestPrice: float = None

print("Kérem válassza ki a helyszínt!\n1 - Velencei tó\n2 - Tihany és Balatonfüred")
choice = int(input())

if(choice == 1):
    basePrice = 6000
else: 
    basePrice = 7500

print("Kérem a létszámot: ")
numberOfStudents = int(input())

if(numberOfStudents < 5):
    groupDiscount = basePrice
elif(numberOfStudents >= 5 and numberOfStudents <= 15):
    groupDiscount = basePrice * .95
elif(numberOfStudents >=16 and numberOfStudents <= 25):
    groupDiscount = basePrice * .92
else:
    groupDiscount = basePrice * .85

if(numberOfStudents < 5):
    schoolDiscount = basePrice
elif(numberOfStudents >= 5 and numberOfStudents <= 10):
    schoolDiscount = basePrice * (numberOfStudents - 1) / numberOfStudents
elif(numberOfStudents >= 11 and numberOfStudents <= 20):
    schoolDiscount = basePrice * (numberOfStudents - 2) / numberOfStudents
else:
    schoolDiscount = basePrice * (numberOfStudents - 3) / numberOfStudents

studentDiscount = basePrice * .92

if(groupDiscount < schoolDiscount and groupDiscount < studentDiscount):
    bestDeal = "csoportkedvezmény"
    bestPrice = groupDiscount
elif(schoolDiscount < groupDiscount and schoolDiscount < studentDiscount):
    bestDeal = "intézményi kedvezmény"
    bestPrice = schoolDiscount
elif(studentDiscount < groupDiscount and studentDiscount < schoolDiscount):
    bestDeal = "diákkedvezmény"
    bestPrice = studentDiscount
elif(schoolDiscount == groupDiscount):
    bestDeal = "intézményi vagy csoportkedvezmény ugyanazzal az árral"
    bestPrice = schoolDiscount
elif(schoolDiscount == studentDiscount):
    bestDeal = "intézményi vagy diákkedvezmény ugyanazzal az árral"
    bestPrice = schoolDiscount
elif(groupDiscount == studentDiscount):
    bestDeal = "csoportkedvezmény vagy diákkedvezmény ugyanazzal az árral"
    bestPrice = groupDiscount


print(f"Csoportkedvezményes ár: {groupDiscount}")
print(f"Intézményi kedvezményes ár: {schoolDiscount}")
print(f"Diák kedvezményes ár: {studentDiscount}")
print(f"A legjobb ajánlat a/az {bestDeal}! {numberOfStudents} fő esetén: {bestPrice} Ft.")






