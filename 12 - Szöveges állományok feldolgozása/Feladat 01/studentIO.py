from typing import *
from io import open
import os
from student import Student

def importStudents() -> list[Student]:
    fileName: str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    oneLine: str = None
    data: list[str] = []
    students: List[Student] = []

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                student: Student = Student()

                data = oneLine.split("\t")

                student.name = data[0]

                student.gradeAverage = float(data[1].replace(",","."))

                students.append(student)
            
            return students

    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []
    

def exportAboveAverage(aboveAverageStudents: list[Student], filename: str) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output/"
    fileFullPath: str = os.path.join(basepath, filename)

    try:
        with open(fileFullPath, "w") as file:
            for student in aboveAverageStudents:
                file.write(f"{student.name} {student.gradeAverage}\n")

    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        

