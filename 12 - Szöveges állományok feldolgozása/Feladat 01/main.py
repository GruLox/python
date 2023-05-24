from typing import *
from io import *
from studentIO import *
from student import Student
from services import calculateStudentAverage, studentsAboveAverage, isExcellent, countGrades, getBestStudent




students: List[Student] = importStudents()

#1 - Írjuk ki minden diák adatát a képernyőre!
for student in students:
    print(student)

# 2 - Hány diák jár az osztályba?
print(f"{len(students)} tanuló jár az osztályba")

# 3 - Mennyi az osztály átlaga?
average = calculateStudentAverage(students)
print(f"Az osztály átlaga: {average}")

# 4 - Keressük a legtöbb pontot elért érettségizőt és írjuk ki az adatait a képernyőre.
# sortedStudents = students.copy()
# sortedStudents.sort(key=lambda student: student.gradeAverage, reverse=True)
bestStudent: Student = getBestStudent(students)
print(f"Legjobb tanuló: {bestStudent}")

# 5 - atlagfelett.txt allományba keressük ki azon tanulókat kiknek pontjai meghaladják az átlagot!
aboveAverageStudents = studentsAboveAverage(students, average)
exportAboveAverage(aboveAverageStudents, "atlagfelett.txt")

# 6 - Van e kitünő tanulónk?
print("Volt kitűnő") if bestStudent.gradeAverage >= 5 else print("Nem volt kítűnő")


"""7 - Hány elégtelen, elégséges, jó, jeles és kitünő tanuló van az osztályban?
    Értékhatárok:
	- elégtelen, ha: 0.00 - 1.99
	- elégséges, ha: 2.00 - 2.99
	- jó, ha: 3.00 - 3.99
	- jeles, ha: 4.00 - 4.99
	- kitünő, ha: 5.00
"""

gradeCounts = countGrades(students)
print(gradeCounts)



