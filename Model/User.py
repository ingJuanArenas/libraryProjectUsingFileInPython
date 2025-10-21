from os import name


class User:
    def __init__(self,name, role, id, psw) -> None:
        self.name =name
        self.role = role
        self.__id = id
        self.psw = psw
        self.borrowedBooks= []
        self.limitBooks = 3 if role == "User" else 10
        self.borrowedBooksQuantity= 0

    @classmethod
    def fromString(cls, data:str):
        name, role, id, psw, borrowedBooks, limitBooks, borrowedBooksQuantity = data.strip().split(",")
        user= cls(name,role,id,psw)
        user.setBorrowedBooks(borrowedBooks)
        user.setBorrowedBooksQuantity(int(borrowedBooksQuantity))
        user.setLimitBooks(int(limitBooks))
        return user
### getters and setters  all atributes
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getRole(self):
        return self.role

    def setRole(self, role):
        self.role = role

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getPsw(self):
        return self.psw

    def setPsw(self, psw):
        self.psw = psw

    def getBorrowedBooks(self):
        return self.borrowedBooks

    def setBorrowedBooks(self, borrowedBooks):
        self.borrowedBooks = borrowedBooks

    def getLimitBooks(self):
        return self.limitBooks

    def setLimitBooks(self, limitBooks):
        self.limitBooks = limitBooks

    def getBorrowedBooksQuantity(self):
        return self.borrowedBooksQuantity

    def setBorrowedBooksQuantity(self, borrowedBooksQuantity):
        self.borrowedBooksQuantity = borrowedBooksQuantity

    def __str__(self) -> str:
        return f"Name: {self.name}, Role: {self.role}, ID: {self.__id}, Password: {self.psw}, Borrowed Books: {self.borrowedBooks}, Limit Books: {self.limitBooks}, Borrowed Books Quantity: {self.borrowedBooksQuantity}"