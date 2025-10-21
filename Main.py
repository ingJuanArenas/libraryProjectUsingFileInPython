import traceback
from Service.LibraryService import LibraryService
from utils.Inputs import Inputs


while True:
    try:
        print(""" 
        ------- Bienvenido a la biblioteca -------
        1. Ingresar 
        2. Crear cuenta
        0. Salir
        """)
        
        op= int(input("Seleccione una opcion: "))
        match op:
            case 1:
                userId= Inputs().getUserIdInput()
                psw = Inputs().getPassWordInput()
                LibraryService().login(userId,psw)
            case 2:
                userToAdd= Inputs().getUserToAddInput()
                LibraryService().getUserService().addUser(userToAdd)
                LibraryService().login(userToAdd.getId(), userToAdd.getPsw())
            case 0:
                print("Gracias por usar la biblioteca")
                break
            case _: 
                print("Opcion no valida")   
    except ValueError:
        print("Ingrese un dato valido")
        traceback.print_exc() 