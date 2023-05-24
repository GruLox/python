import datetime

class Book: 
    def __init__(self) -> None:
        self.lastNameOfAuthor: str = None
        self.firstNameOfAuthor: str = None
        self.birthDateOfAuthor: datetime = None
        self.title: str = None
        self.isbn: str = None
        self.publisher: str = None
        self.releaseYear: int = None
        self.price: float = None
        self.topic: str = None
        self.pages: int = None
        self.honorarium: float = None

    def __str__(self) -> str:
        return f"{self.firstNameOfAuthor} {self.lastNameOfAuthor} - {self.title} [{self.releaseYear}]"