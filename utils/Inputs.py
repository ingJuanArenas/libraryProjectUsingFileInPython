from Model.Book import Book
from Model.User import User


class Inputs:

    
    def getIsbnInput(self):
        return input("Ingrese el ISBN del libro: ")
   
    def getTitleInput(self):
        return input("Ingrese el titulo del libro:")

    def getBookToAddInfoInput(self):
        isbn= self.getIsbnInput()
        title= self.getTitleInput()
        author= input("Ingrese el autor del libro: ")
        genre= input("Ingrese el genero del libro: ")

        bookToAdd = Book(isbn,title,author,genre)

        return bookToAdd
    
    def getUserIdInput(self):
        return input("Ingrese el id: ")
    def getPassWordInput(self):
        return input("Ingrese la contraeña: ")
    
    def getUserToAddInput(self):
        name= input("Ingrese el nombre de usuario: ")
        userId= self.getUserIdInput()
        role = "User"
        psw= self.getPassWordInput()

        userToAdd= User(name,role,userId,psw)

        return userToAdd 
        
    
