class RandomAccessMemory:
    def __init__(self, manufacturer: str, capacity: int, type: str, price: int) -> None:
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.voltage = type
        self.price = price
    
    def __str__(self) -> str:
        return f"{self.manufacturer} {self.capacity} GB"