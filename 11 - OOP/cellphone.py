class Cellphone:
    def __init__(self, brand: str, model: str, price: float) -> None:
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self) -> str:
        return f"A {self.brand} {self.model} {self.price} forintba kerül";