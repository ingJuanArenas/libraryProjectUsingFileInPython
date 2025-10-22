from utils.Exceptions import NotFoundError
from Model.User import User


USERS_FILE = "users.txt"
ENCONDING= "utf-8"

class UserService:
    def __init__(self) -> None:
        self.__users:list[User]= []

        try:
            with open(USERS_FILE,"r", encoding= ENCONDING) as f:
                for line in f:
                    userToAdd= User.fromString(line)
                    self.__users.append(userToAdd)
        except FileNotFoundError:
            print("No se ha encontrado el archivo, se creará uno vacio")
            with open(USERS_FILE, "x", encoding= ENCONDING) as f:
                pass
    
    def getAllUsers(self):
        for user in self.__users:
            print(user)

    def getUserById(self, id):
        for user in self.__users:
            if user.getId()== id:
                return user
        raise NotFoundError("Usuario no encontrado")
    
    def addUser(self, user:User):
        try:
            self.getUserById(user.getId())
            print("El id ya se encuentra registrado")
        except NotFoundError:
            self.__users.append(user)
            self.saveUserAfterRegister(user)
            print("Operacion exitosa")

    def deleteUserById(self, id):
        try:
            userToDelete= self.getUserById(id)
            self.__users.remove(userToDelete)
            print("Usuario eliminado exitosamente")
        except NotFoundError:
            print("Usuario no encontrado")

    def saveUsersToFile(self):
        try:
            with open(USERS_FILE,"w", encoding=ENCONDING) as f:
                for user in self.__users:
                    userData= f"{user.getName()},{user.getRole()},{user.getId()},{user.getPsw()},{user.getBorrowedBooksQuantity()},{user.getLimitBooks()},{'|'.join(map(str, user.borrowedBooks))}\n"
                    f.write(userData)
            print("Usuarios guardados exitosamente")
        except Exception as e:
            print("Error al guardar: " + str(e))
    
    def saveUserAfterRegister(self, user:User):
        try:
            with open(USERS_FILE, "a", encoding=ENCONDING) as f:
                userData= f"{user.getName()},{user.getRole()},{user.getId()},{user.getPsw()},{user.getBorrowedBooksQuantity()},{user.getLimitBooks()},""\n"
                f.write(userData)
        except Exception as e:
            print("ERROR: "  + str(e))

    def updateUser(self, user: User):
        for i, existing_user in enumerate(self.__users):
            if existing_user.getId() == user.getId():
                self.__users[i] = user
                return
        raise NotFoundError(f"Usuario con ID {user.getId()} no encontrado")