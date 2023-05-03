class GraphicsCard:
    def __init__(self, manufacturer: str, model: str, price: float) -> None:
        self.manufacturer =  manufacturer
        self.model = model
        self.price = price

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"