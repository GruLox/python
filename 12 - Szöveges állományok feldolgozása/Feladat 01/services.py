from student import Student

def calculateStudentAverage(students: list[Student]) -> float:
    sum: float = 0
    for student in students:
        sum += student.gradeAverage

    return round(sum / len(students), 2)


def getBestStudent(students: list[Student]) -> Student:
    bestStudent: Student = students[0]

    for i in range(1, len(students), 1):
        if (students[i].gradeAverage > bestStudent.gradeAverage):
            bestStudent = students[i]

    return bestStudent


# def exportAboveAverage(students: list[Student], average: float) -> None:
#     with open("./Feladat 01/atlagfelett.txt", "w") as file:
#         for student in students:
#             if (student.gradeAverage > average):
#                 file.write(f"{student.name} {student.gradeAverage}\n")

def studentsAboveAverage(students: list[Student], average: float) -> list[Student]:
    aboveAverage: list[Student] = []

    for student in students:
        if (student.gradeAverage >= average):
            aboveAverage.append(student)

    return aboveAverage

def isExcellent(students: list[Student]) -> bool:
    for student in students:
        if student.gradeAverage >= 4.5:
            return True
        
    return False


def countGrades(students: list[Student]) -> dict[str, int]:
    grades: dict[str, int] = {"elégtelen": 0, "elégséges": 0, "jó": 0,  "jeles": 0, "kitűnő": 0}
    

    for student in students:
        if (student.gradeAverage == 5):
            grades["kitűnő"] += 1
        if (student.gradeAverage >= 4):
            grades["jeles"] += 1
        elif(student.gradeAverage >= 3):
            grades["jó"] += 1
        elif(student.gradeAverage >= 2):
            grades["elégséges"] += 1
        else:
            grades["elégtelen"] += 1

    return grades
                