from book import Book
from typing import *

def filterCompSciBooks(books: List[Book]) -> List[Book]:
    compSciBooks: List[Book] = []

    for book  in books:
        if (book.topic == "informatika"):
            compSciBooks.append(book)

    return compSciBooks


def filter1900sBooks(books: List[Book]) -> List[Book]:
    books1900s: List[Book] = []

    for book in books:
        if (book.releaseYear >= 1900 and book.releaseYear <= 1999):
            books1900s.append(book)

    return books1900s


def sortBooks(books: List[Book]) -> List[Book]:
    for i in range(len(books) - 1):
        for j in range(len(books) - i - 1):
            if (books[j].releaseYear < books[j + 1].releaseYear):
                books[j], books[j + 1] = books[j + 1], books[j]
        
    return books


def sortIntoDictByTopic(books: List[Book]):
    booksDict = {}

    for book in books:
        pass