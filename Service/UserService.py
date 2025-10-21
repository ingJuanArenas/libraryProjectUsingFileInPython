
from GestorTareas.excepciones import NotFoundError
from libraryUsingFiles.Model.User import User


USERS_FILE = "users.txt"
ENCONDING= "utf-8"

class UserService:
    def __init__(self) -> None:
        self.users:list[User]= []

        try:
            with open(USERS_FILE,"r", encoding= ENCONDING) as f:
                for line in f:
                    userToAdd= User.fromString(line)
                    self.users.append(userToAdd)
        except FileNotFoundError:
            print("No se ha encontrado el archivo, se creará uno vacio")
            with open(USERS_FILE, "x", encoding= ENCONDING) as f:
                pass
    
    def getAllUsers(self):
        for user in self.users:
            print(user)

    def getUserById(self, id):
        for user in self.users:
            if user.getId()== id:
                return user
        raise NotFoundError("Usuario no encontrado")
    
    def addUser(self, user:User):
        try:
            self.getUserById(user.getId())
            print("El id ya se encuentra registrado")
        except NotFoundError:
            self.users.append(user)
            print("Operacion exitosa")

    def deleteUserById(self, id):
        try:
            userToDelete= self.getUserById(id)
            self.users.remove(userToDelete)
            print("Usuario eliminado exitosamente")
        except NotFoundError:
            print("Usuario no encontrado")

    def saveUsersToFile(self):
        try:
            with open(USERS_FILE,"w", encoding=ENCONDING) as f:
                 for user in self.users:
                    userData= f"{user.getName()},{user.getRole()},{user.getId()},{user.getPsw()},{user.getBorrowedBooks()},{user.getLimitBooks()},{user.getBorrowedBooksQuantity()}\n"
                    f.write(userData)
            print("Usuarios guardados exitosamente")
        except Exception as e:
            print("Error al guardar: " + str(e))
