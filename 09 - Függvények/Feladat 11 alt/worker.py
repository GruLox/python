class Worker:
    def __init__(self, name, hoursWorked, wage) -> None:
        self.name = name
        self.hoursWorked = hoursWorked
        self.wage = wage

    def __str__(self) -> str:
        return f"{self.name} dolgozó {self.hoursWorked} órát dolgozott ezen a héten, és {self.wage} forintot keresett."
