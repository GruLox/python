import os
from book import Book
from datetime import datetime
from typing import *




def importBooks() -> list[Book]:
    fileName = "data/adatok.txt"
    basepath = os.path.dirname(os.path.abspath(__file__))
    fileFullPath = os.path.join(basepath, fileName)

    books: list[Book] = []

    try:            
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                book: Book = Book()
                oneLine = line.strip()
                lastNameOfAuthor, firstNameOfAuthor, birthDateOfAuthor, title, isbn, publisher, releaseYear, price, topic, pages, honorarium = oneLine.split("\t")

                book.lastNameOfAuthor = lastNameOfAuthor
                book.firstNameOfAuthor = firstNameOfAuthor
                book.birthDateOfAuthor = datetime.fromisoformat(birthDateOfAuthor)
                book.title = title
                book.isbn = isbn
                book.publisher = publisher
                book.releaseYear = int(releaseYear)
                book.price = float(price)
                book.topic = topic
                book.pages = int(pages)
                book.honorarium = float(honorarium)

                books.append(book)
            
            return books

    
    except FileNotFoundError as ex:
        print(f"{ex.filename} not found")


def exportBooks(books: List[Book], fileName) -> None:
    basepath = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output/"
    fileFullPath = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath, "w") as file:
            for book in books:    
                file.write(str(book) + "\n")
        
    except FileNotFoundError as ex:
        print(f"{ex.filename} not found")


def exportBooksByTopic(booksDict: Dict[str, List[Book]], fileName) -> None:
    basepath = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output/"
    fileFullPath = os.path.join(basepath, fileName)

    with open(fileFullPath, "w") as file:
        for category, books in booksDict.items():
            file.write(f"{category}: \n")
            for book in books:
                file.write(f"\t- {book}\n")

            file.write("\n")

        




