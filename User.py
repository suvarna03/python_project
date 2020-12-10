from Book import Book
from Catalog import Catalog

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id



class Member(User):
    def __init__(self, name, location, age, aadhar_id, member_id):
        super().__init__(name, location, age, aadhar_id)
        self.member_id = member_id
        self.penalty = 0
    def __repr__(self):
        return '*************Details of members:***********************'+'\n'+'Name of Member: '+self.name + "\n" +'Location: '+ self.location + '\n' + 'Member_id: '+self.member_id
    def issueBook(self,name,isbn,days=10):
        if days > 10:
            self.penalty=((days - 10) * 10)
        for i in Book.itemList:
            if isbn.strip() == i.isbn:
                print(self.name ,"issued book",name)
                Catalog.removeBookItem(self,name,isbn)
                break
            if isbn.strip() != i.isbn:
                print(isbn,"not available in the liabrary")
                break
    def returnBook(self,name,isbn,rack):
        for i in Book.itemList:
            if isbn.strip() == i.isbn:
                book = Catalog.searchByName(name)
                book.addBookItem(isbn, rack)
                print(self.name,'your fine is:',self.penalty)
                break

            if isbn.strip() != i.isbn:
                print("You are returning wrong isbn")
                break




class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def __repr__(self):
        return '*************Details of Librarian:***********************'+'\n'+'Name of Librarian: '+self.name + "\n" +'Location: '+ self.location + '\n' + 'Emp_id: '+self.emp_id

    def addBook(self, name, author, publish_date, pages):
        b = Book(name, author, publish_date, pages)
        Catalog.books.append(b)
        Catalog.different_book_count += 1
        return b

    def addBookItem(self, book, isbn, rack):
        book.addBookItem(isbn, rack,)

    def removeBook(self,name,isbn):
        Catalog.removeBookItem(self, name, isbn)
    def removeBookItemFromCatalog(self, name):

        for book in Catalog.books:
            if name.strip() == book.name:
                Catalog.books.remove(book)
                Catalog.different_book_count -= 1






