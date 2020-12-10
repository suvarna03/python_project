from BookItem import BookItem


class Book:
    itemList = []
    def __init__(self, name, author, publish_date, pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []


    def addBookItem(self, isbn, rack):
        b = BookItem(self, isbn, rack)
        self.book_item.append(b)
        Book.itemList.append(b)
        self.total_count += 1
    def printBook(self):
        print('Book name:',self.name,'\n','Author name:',self.author)
        print("{:<8} {:<15} ".format('ISBN', 'RACK'))
        for book_item in self.book_item:
            print("{:<8} {:<15} ".format(book_item.isbn,book_item.rack))

    def searchBookItem(self, isbn):
        for book_item in self.book_item:
            if isbn.strip() == book_item.isbn:
                return book_item
    def removeBookItem(self, book_item):
        if book_item in self.book_item:
            self.book_item.remove(book_item)
            self.total_count -= 1
        else:
            print("you entred wrong isbn")


    def __repr__(self):
        return self.name + ' ' + self.author
