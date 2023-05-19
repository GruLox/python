from typing import *
from io import *
from studentIO import *
from student import Student
from functions import calculateStudentAverage,  exportAboveAverage, isExcellent, countGrades



students: List[Student] = importStudents()

for student in students:
    print(student)

average = calculateStudentAverage(students)

sortedStudents = students.copy()
sortedStudents.sort(key=lambda student: student.gradeAverage, reverse=True)

exportAboveAverage(students, average)

gradeCounts = countGrades(students)


print("Volt kitűnő") if isExcellent(students) else print("Nem volt kítűnő")
print(f"{len(students)} tanuló jár az osztályba")
print(f"Az osztály átlaga: {average}")
print(f"Legjobb tanuló: {sortedStudents[0]}")
print(gradeCounts)



