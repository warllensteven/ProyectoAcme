from persistencia.persistencia import *

acme = {}
archivo = "dicAcme.json"
acme = cargar(archivo)

def informeLlegadaTarde(acme):
    estudiantesTarde = []
    mes = int(input("Ingrese el mes (numero): "))
    for modulo in acme["modulos"]:
        if "asistencias" in acme["modulos"][modulo]:
            asistencias = acme["modulos"][modulo]["asistencias"]
            horaInicio = acme["modulos"][modulo]["horaInicio"]

            for asistencia in asistencias:
                dia, mesAsistencia, ano = asistencia["fecha"].split("/")
                horaEntrada = asistencia["hora"]

                if int(mesAsistencia) == mes and horaEntrada > horaInicio:
                    estudiantesTarde.append(asistencia)
        
    if estudiantesTarde:
        print("Estudiantes que llegaron tarde:")
        for estudiante in estudiantesTarde:
            print(f"Estudiante: {estudiante['estudiante']} en modulo {estudiante['modulo']} a las {estudiante['hora']}.")
    else:
        print("No hay estudiantes que llegaron tarde.")

def betaVers():
    print("Funcion no disponible en la version beta, seguimos trabajando en una actualizacion")
    input("Presione cualquier tecla para regresar")




def informe():
    while True:
        print("******************************************ACME************************************************")
        print()
        print("--------------------------------- Generacion de informes -------------------------------------")
        ("|                                                                                                 |")
        print("| 1. Estudiantes que han llegado tarde a un módulo en un mes específico                      |")
        print("| 2. Estudiantes que se retirarán antes de la finalización de una sesión en un mes específico|")
        print("| 3. Estudiantes que no han faltado a ningún módulo durante un mes                           |")
        print("| 4. Porcentaje de asistencia por módulo, calculado como la proporción de estudiantes que    |")
        print("|    asistieron al inicio de clase respecto al total de estudiantes matriculado              |")
        print("| 5. Salir                                                                                   |")
        print("|                                                                                            |")
        print("---------------------------------------------------------------------------------------------")

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

def menuOpcI(acme):
    while True:
        op = informe()
        match op:
            case 1:
                
                informeLlegadaTarde(acme)
                
            case 2:
                betaVers()
            case 3:
                betaVers()
            case 4:
                betaVers()
            case 5:
                print("\nDe vuelta al menu principal\n")
                break
