
def menu():
    while True:
        print("*************ACME*************")
        print()
        print("-------------Menu-------------")
        print("|                            |")
        print("| a. Registro de grupos      |")
        print("| b. Registro de modulos     |")
        print("| c. Registro de estudiantes |")
        print("| d. Registro de docentes    |")
        print("| e. Registro asistencias    |")
        print("| f. Consultas informacion   |")
        print("| g. Generacion informes     |")
        print("| h. Cambio de contraseña    |")
        print("| i. Salida del sistema      |")
        print("|                            |")
        print("------------------------------")

        print(">>> Opcion? ", end="")
        try:
            opcion = str(input())
            if not opcion:
                print("Error. Opcion no valida...")
                input("Presione cualquier tecla  para volver al menu")
                continue
            return opcion.lower()
        except ValueError:
            print("Error. Opcion no valida...")
            input("Presione cualquier tecla para volver al menu") 

