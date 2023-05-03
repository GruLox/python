class Motherboard:
    def __init__(self, manufacturer: str, model: str, ramSlots: int, cardSlots: int) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.ramSlots = ramSlots
        self.cardSlots = cardSlots

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"
