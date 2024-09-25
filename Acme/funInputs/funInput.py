def leerCod():
    while True:
        try:
            cod = (input("Codigo? "))
            if len(cod.strip()) <= 0:
                print(">>> Error. codigo invalido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el codigo\n" + e)

def leerEdad():
    while True:
        try:
            edad = int(input("Edad? "))
            if edad <= 10 or edad >= 65:
                print(">>> Error. edad invalida")
                continue
            return edad
        except Exception as e:
            print("Error al ingresar el edad\n" + e)

def leerCed():
    while True:
        try:
            edad = str(input("Cedula? "))
            if len(edad.strip()) <= 8 and len(edad.strip()) >= 12:
                print(">>> Error. cedula invalida")
                continue
            return edad
        except Exception as e:
            print("Error al ingresar la cedula\n" + e)

def leerNombre():
    while True:
        try:
            name = input("Nombre? ")
            if len(name.strip()) == 0:
                print(">>> Error. Nombre invalido")
                continue
            return name
        except ValueError:
            print("Error al ingresar el nombre\n")

def leerSexo():
    while True:
        try:
            sexo = input("Sexo? ")
            if sexo.lower() == "m" or sexo.lower() == "f":
                return sexo
            else:
                print(">>> Error. sexo invalido")
                continue
        except ValueError:
            print("Error al ingresar el sexo\n")

def leerSigla():
    while True:
        try:
            sigla = input("Sigla del grupo? ")
            if len(sigla.strip()) == 0:
                print("Sigla incorrecta,por favor ingresar una sigla valido")
                continue
            return sigla
        except Exception as e:
            print(f">>> Error al ingresar la sigla {e}")

def leerSemanas():
    while True:
        try:
            semanas = int(input("Ingresar las semanas de duracion del modulo: "))
            if semanas <= 0:
                print("Duracion incorrecta,por favor ingresar una duracion valida")
                continue
            return semanas
        except ValueError:
            print(f">>> Error al ingresar la duracion, ingrese el numero de semanas")


