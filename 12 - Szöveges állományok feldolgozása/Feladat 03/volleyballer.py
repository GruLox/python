class Volleyballer:
    def __init__(self):
        self.name: str = None
        self.height: int = None
        self.position: str = None
        self.nationality: str = None
        self.team: str = None
        self.countryOfTeam: str = None

    def __str__(self):
        return f"{self.name} ({self.nationality} - {self.team})"

    