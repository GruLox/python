from book import Book
from bookIO import importBooks, exportBooks, exportBooksByTopic
from services import filterCompSciBooks, filter1900sBooks, sortBooks, sortIntoDictByTopic


books: list[Book] = importBooks()

for book in books:
    print(book)


# Keressük ki az informatika témajú könyveket és mentsük el őket az informatika.txt állömányba
compSciBooks = filterCompSciBooks(books)
exportBooks(compSciBooks, "informatika.txt")


# Az 1900.txt állományba mentsük el azokat a könyveket amelyek az 1900-as években íródtak
booksFromThe1900s = filter1900sBooks(books)
exportBooks(booksFromThe1900s, "1900.txt")

# Rendezzük az adatokat a könyvek oldalainak száma szerint csökkenő sorrendbe és a sorbarakott.txt állományba mentsük el.
sortedBooks = sortBooks(books)
exportBooks(sortedBooks, "sorbarakott.txt")

"""„kategoriak.txt” állományba mentse el a könyveket téma szerint. Például:
Thriller:
	- könnyv1
	- könnyv2
Krimi:
	- könnyv1
	- könnyv2
"""

booksDict = sortIntoDictByTopic(books)
exportBooksByTopic(booksDict, "kategoriak.txt")
