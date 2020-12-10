
from Catalog import Catalog
from User import Member, Librarian
from Book import Book
catalog = Catalog()
b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '143hg','H1B2')
catalog.addBookItem(b, '123hg','H1B4')
catalog.addBookItem(b, '113hg','H1B5')
# #
b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

catalog.displayAllBooks()

m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
print(m1)

print('******************* after issue ************************')
m1.issueBook('Shoe Dog','143hg',13)
catalog.displayAllBooks()
print('******************* after return *************************')
m1.returnBook('Shoe Dog','143hg','H1B2')
catalog.displayAllBooks()

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101')
print (librarian)
b =librarian.addBook('XYZ','suvarna','1558','150')
librarian.addBookItem(b,'456gy','H2B2')

catalog.displayAllBooks()
print("**************** After removing book item *******************************")
librarian.removeBook('Shoe Dog','123hg')
catalog.displayAllBooks()
librarian.removeBookItemFromCatalog('Shoe Dog')
print("**************** After removing **************************************")

catalog.displayAllBooks()

