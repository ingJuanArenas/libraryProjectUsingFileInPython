from Model.User import User
from utils.Exceptions import NotFoundError
from Service.BookService import BookService
from Service.UserService import UserService


class LibraryService: 
    def __init__(self) -> None:
        self.__userService = UserService()
        self.__bookService= BookService()

    def getUserService(self):
        return self.__userService
    def getBookService(self):
        return self.__bookService
    

    def login(self, userdId, userPsw):
        try:
            userToLogin= self.__userService.getUserById(userdId)
            if userToLogin.getPsw() == userPsw:
                print("Login exitoso ....... ")
                if userToLogin.getRole() == "Admin":
                    from Service.AdminMenuService import AdminMenuService
                    AdminMenuService().executeAdminOption(userToLogin)
                else:
                    from Service.UserMenuService import UserMenuService
                    UserMenuService().executeUserOption(userToLogin)
            else:
                print("Contraseña incorrecta")
        except NotFoundError:
            print("Usuario no encontrado")
    
    def lendBook(self, bookTitle, user:User):
        try:
            book = self.__bookService.getBookByTitle(bookTitle)
            if book.getStatus() == "Disponible":
                if user.getBorrowedBooksQuantity() < user.getLimitBooks():
                    print("PROCESANDO PRESTAMO .......")
                # libro prestado
                    book.setStatus("Prestado")
                # lo agrego al historial
                    user.borrowedBooks.append(bookTitle)
                #aumento la cuenta de libros prestados
                    user.setBorrowedBooksQuantity(user.getBorrowedBooksQuantity() + 1)
                # Guardar cambios
                    self.__bookService.saveBooks()
                    self.__userService.updateUser(user) # Asegurarse de actualizar el usuario
                    self.__userService.saveUsersToFile()
                    print("Prestamo exitoso")
                else:
                    print("Limite de libros alcanzados")
            else:
                print("El libro no esta disponible")
        except NotFoundError as e:
            print("ERROR: " + str(e))
        except Exception as e:
            print(e)

    def returnBook(self, user:User, bookTitle):
        try:
            book = self.__bookService.getBookByTitle(bookTitle)
            if bookTitle in user.getBorrowedBooks():
                print("PROCESANDO DEVOLUCION....")
                book.setStatus("Disponible")
                # Remover el libro de la lista de prestados del usuario
                user.borrowedBooks.remove(bookTitle)
                user.setBorrowedBooksQuantity(user.getBorrowedBooksQuantity() - 1)
                # Guardar cambios
                self.__bookService.saveBooks()
                self.__userService.updateUser(user)  # Asegurarse de actualizar el usuario
                self.__userService.saveUsersToFile()
                print("Devolucion exitosa")
            else:
                print("El usuario no tiene prestado ese libro")
        except NotFoundError as e:
            print("Error: " + str(e))
        except Exception as e:
            print(e)
