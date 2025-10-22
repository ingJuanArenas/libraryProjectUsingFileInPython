from Model.User import User
from Service.LibraryService import LibraryService
from utils.Exceptions import NotFoundError
from utils.Inputs import Inputs


class UserMenuService:
    def showUserMenu(self):
        print(""" 
        ------- Menu usuario ------
        1. Mostrar Biblioteca
        2. Consultar libro
        3. Prestar libro
        4. Devolver libro
        0. salir
""")
        
    def executeUserOption(self, userLogged:User):
        while True:
           try:
                self.showUserMenu()
                option = int(input("Selecciona una opcion: "))
                match option:
                    case 1:
                        LibraryService().getBookService().getAllBooksAvaliable()
                    case 2:
                        titleToSearch = Inputs().getTitleInput()
                        bookFound= LibraryService().getBookService().getBookByTitle(titleToSearch)
                        print(bookFound)
                    case 3:
                        titleToLend = Inputs().getTitleInput()
                        LibraryService().lendBook( titleToLend, userLogged)
                    case 4:
                        titleToReturn = Inputs().getTitleInput()
                        LibraryService().returnBook(userLogged, titleToReturn)
                    case 5:
                        print(userLogged)
                    case 0:
                        LibraryService().getUserService().saveUsersToFile()
                        LibraryService().getBookService().saveBooks()
                        print("Saliendo ....")
                        break
                    case _:
                        print("Opcion invalida")   
           except ValueError:
                print("Ingrese un dato valido")
           except NotFoundError:
                print("Elemento no encontrado")
           except Exception as e:
                print("Error: "+ str(e))  