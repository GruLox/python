class Processor:
    def __init__(self,  manufacturer: str, model: str , frequency: int, cores: int, cache: int) -> None:
        self.name = manufacturer
        self.model = model
        self.frequency = frequency
        self.cores = cores
        self.cache = cache

    def __str__(self) -> str:
        return f'{self.name} {self.model}'
        