from Model.User import User
from Service.LibraryService import LibraryService
from utils.Exceptions import NotFoundError
from utils.Inputs import Inputs


class AdminMenuService:
    def showAdminMenu(self):
        print(""" 
        ------ Menú administrador ------
        1. Guardar informacion Usuario
        2. Guardar informacion libro
        3. Consultar Usuario
        4. Agregar libro
        5. Consultar libro
        6. Mostrar Biblioteca
        7. Prestar libro
        8. Devolver libro
        9. Eliminar libro
        0. salir
""")
        
    def executeAdminOption(self, adminLogged: User):
        while True:
            try:
                self.showAdminMenu()
                option= int(input("Seleccione una opcion: "))
                match option:
                    case 1:
                        LibraryService().getUserService().saveUsersToFile()
                    case 2:
                        LibraryService().getBookService().saveBooks()
                    case 3:
                        idToSearch = Inputs().getUserIdInput()
                        userFound= LibraryService().getUserService().getUserById(idToSearch)
                        print(userFound)
                    case 4:
                        bookToAdd = Inputs().getBookToAddInfoInput()
                        LibraryService().getBookService().addBook(bookToAdd)
                    case 5:
                        titleToSearch= Inputs().getTitleInput()
                        bookFound =LibraryService().getBookService().getBookByTitle(titleToSearch)
                        print( bookFound)
                    case 6:
                        LibraryService().getBookService().getAllBooks()
                    case 7:
                        titleToLend= Inputs().getTitleInput()
                        LibraryService().lendBook( titleToLend, adminLogged)
                    case 8: 
                        titleToReturn= Inputs().getTitleInput()
                        LibraryService().returnBook(adminLogged, titleToReturn)
                    case 9:
                        titleToDelete = Inputs().getTitleInput()
                        LibraryService().getBookService().deleteBookByTitle(titleToDelete)
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
                
