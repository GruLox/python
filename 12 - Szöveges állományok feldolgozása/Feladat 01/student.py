class Student:
    def __init__(self) -> None:
        self.name: str = None
        self.gradeAverage: float = 0

    def __str__(self) -> str:
        return f"{self.name} - {self.gradeAverage}"