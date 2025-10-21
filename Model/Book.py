class Book:
    def __init__(self, isbn, title, author, genre) -> None:
        self.__isbn= isbn
        self.title= title
        self.author = author
        self.genre= genre
        self.status= "Disponible"

    @classmethod
    def fromString(cls,data ):
        isbn, title, author, genre, status = data.strip().split(",")
        book = cls(isbn, title, author, genre)
        book.setStatus(status)
        return book
    def getIsbn(self):
        return self.__isbn
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getGenre(self):
        return self.genre
    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status= status
    
    def __str__(self) -> str:
        return f"ISBN: {self.__isbn}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Status: {self.status}"
    
        