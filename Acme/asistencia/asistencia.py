from funInputs.funInput import *
from persistencia.persistencia import *
from datetime import datetime

acme = {}
archivo = "dicAcme.json"
acme = cargar(archivo)

def leerLlegadaFecha(msg):
    fecha = datetime.now()
    ano, mes, dia = str(fecha).split()[0].split("-")
    return f"{dia}/{mes}/{ano}"

def leerLlegadaHora(msg):
    hora = datetime.now()
    hor, min = str(hora).split()[1].split(":")[:2]
    return f"{hor}:{min}"

def registrarAsistencia(acme):
    modulos = acme["modulos"]
    estudiantes = acme["estudiantes"]
    try:
        codEst = str(input("Ingresar código de estudiante: "))     

        if codEst in estudiantes:
            codMod = str(input("Ingresar código de módulo: "))
            if codMod in modulos:
                llegadaFecha = leerLlegadaFecha("Oprima cualquier tecla para marcar asistencia")
                llegadaHora = leerLlegadaHora("Oprima cualquier tecla para confirmar asistencia")

                asistencia = {
                    "estudiante": codEst,
                    "modulo": codMod,
                    "fecha": llegadaFecha,
                    "hora": llegadaHora
                }


                if "asistencias" not in modulos[codMod]:
                    modulos[codMod]["asistencias"] = []

                modulos[codMod]["asistencias"].append(asistencia)

                acme = dict(sorted(acme.items()))
                guardar(acme, archivo)

                print(f"Asistencia registrada correctamente para el estudiante {codEst} en el modulo {codMod}.")
                return acme
            else:
                print(f"Codigo de modulo invalido")
                input("Presione cualquier tecla para intentar nuevamente o volver al menu")
        else:
            print(f"Codigo de estudiante invalido")
            input("Presione cualquier tecla para intentar nuevamente o volver al menu")
    except Exception as e:
        print(f"Error: {e}")
        input("Presione cualquier tecla para volver al menu")


def registrarSalida(acme):
    modulos = acme["modulos"]
    estudiantes = acme["estudiantes"]
    
    try:
        codEst = str(input("Ingresar codigo de estudiante: "))

        if codEst in estudiantes:
            codMod = str(input("Ingresar codigo de modulo: "))
            if codMod in modulos:
                salidaFecha = leerLlegadaFecha("Oprima cualquier tecla para marcar salida")
                salidaHora = leerLlegadaHora("Oprima cualquier tecla para confirmar salida")

                if "asistencias" in modulos[codMod]:
                    asistencias = modulos[codMod]["asistencias"]

                    for asistencia in asistencias:
                        if asistencia["estudiante"] == codEst and asistencia["fecha"] == salidaFecha:
                            asistencia["salida"] = salidaHora
                            print(f"Salida registrada para el estudiante {codEst} en el modulo {codMod} a las {salidaHora}.")
                            break
                    else:
                        print("No se encontro asistencia registrada en la fecha indicada")
                else:
                    print("No hay asistencias registradas para este modulo")

                acme = dict(sorted(acme.items()))
                guardar(acme, archivo)

                return acme
            else:
                print(f"Codigo de modulo invalido")
                input("Presione cualquier tecla para intentar nuevamente o volver al menu")
        else:
            print(f"Codigo de estudiante invalido")
            input("Presione cualquier tecla para intentar nuevamente o volver al menu")
    except Exception as e:
        print(f">>>Error. {e}")
        input("Presione cualquier tecla para volver al menu")

    

def menuE():
    while True:
        print("*************ACME*************")
        print()
        print("----Registro de asistencia----")
        print("| 1. Registrar llegada       |")
        print("| 2. Registrar salida        |")
        print("| 3. Salir                   |")
        print("\n------------------------------\n")

        print(">>> Opcion? ", end="")
        try:
            opcion = int(input())
            if not opcion:
                print("Error. Opcion no valida...")
                input("Presione cualquier tecla  para volver al menu")
                continue
            return opcion
        except Exception:
            print("Error. Opcion no valida...")
            input("Presione cualquier tecla para volver al menu") 

def menuOpcE(acme):
    while True:
        op = menuE()
        match op:
            case 1:
                registrarAsistencia(acme)
            case 2:
                registrarSalida(acme)
            case 3:
                print("\nDe vuelta al menu principal\n")
                break