class Car:
    def __init__(self) -> None:
        self.auto: str = None
        self.mpg: float = None
        self.hengerekSzama: int = None
        self.nyomatek: float = None
        self.loero: float = None
        self.suly: int = None
        self.gyorsulas: float = None
        self.megjelenesiEv: int = None
        self.eredet: str = None

    def __str__(self) -> str:
        return f"{self.auto} - {self.loero} ({self.megjelenesiEv}, {self.eredet})"
