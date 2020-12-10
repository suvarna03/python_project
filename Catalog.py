from Book import Book

from BookItem import BookItem

class Catalog:

    different_book_count = 0
    books = []
    def addBook(self, name, author, publish_date, pages):
        b = Book(name, author, publish_date, pages)
        Catalog.different_book_count += 1
        Catalog.books.append(b)
        return b
    def addBookItem(self, book, isbn, rack):
        book.addBookItem(isbn, rack)

    def displayAllBooks(self):
        print('Number of different Books Available: ',Catalog.different_book_count)
        c = 0
        for book in Catalog.books:
            c += book.total_count
            book.printBook()
        print('Total Books: ',c)

    @classmethod
    def searchByName(cls,name):
        for book in cls.books:
            if name.strip() == book.name:
                return book
            else:
                print("Currently not available")
                break

    @classmethod
    def searchByAuthor(cls, author):
        for book in cls.books:
            if author.strip() == book.author:
                return book
            else:
                print("Currently not available")
                break



    def removeBookItem(self, name, isbn):
        book = Catalog.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)








