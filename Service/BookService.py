from utils.Exceptions import NotFoundError
from Model.Book import Book


BOOK_FILE = "books.txt"

class BookService:
    def __init__(self) -> None:
        self.books: list[Book]=[]

        try:
            with open(BOOK_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    bookToAdd= Book.fromString(line)
                    self.books.append(bookToAdd)
        except FileNotFoundError:
            print("No se encontro el archivo, se creará uno vacio")
            with open(BOOK_FILE, "x", encoding="utf-8") as f:
                pass

    def getAllBooks(self):
        for book in self.books:
            print(book)
    def getAllBooksAvaliable(self):
        for book in self.books:
            if book.getStatus() == "Disponible":
                print(book)
    def getBookByIsbn(self, isbn):
        for book in self.books:
            if(book.getIsbn() == isbn):
                return book
        raise NotFoundError("No se encontro el libro con el isbn:" + isbn)
    
    def getBookByTitle(self, title):
        for book in self.books:
            if book.getTitle() == title:
                return book
        raise NotFoundError("No se encontro el libro con el titulo:" + title)
    
    def addBook(self, book:Book):
        try:
            self.getBookByIsbn(book.getIsbn())
            print("El isbn ya se encuentra registrado")
        except NotFoundError:
            self.books.append(book)
            self.saveBooks()
            print("Libro agregado exitosamente")
    def deleteBookByTitle(self, title):
        try:
            bookToDelete= self.getBookByTitle(title)
            self.books.remove(bookToDelete)
            self.saveBooks()
            print("Operacion exitosa")
        except NotFoundError:
            print("No se encontró un libro con ese titulo")

    def saveBooks(self):
        try:
            with open(BOOK_FILE, "w", encoding="utf-8") as f:
                for book in self.books:
                  f.write(
                  f"{book.getIsbn()},{book.getTitle()},{book.getAuthor()},{book.getGenre()},{book.getStatus()}\n")
        except Exception as e:
            print("Ha ocurrido un error al guardar: " + str(e))
    def saveBookAfterAdd(self, book:Book):
        try:
            with open(BOOK_FILE, "a", encoding="utf-8") as f:
                 f.write(
                    f"{book.getIsbn()},{book.getTitle()},{book.getAuthor()},{book.getGenre()},{book.getStatus()}\n")
        except Exception as e:
            print("Ha ocurrido un error al guardar: " + str(e))
    