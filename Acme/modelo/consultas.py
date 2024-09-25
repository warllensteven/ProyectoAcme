import json
from persistencia.persistencia import *

acme = {}
archivo = "dicAcme.json"
acme = cargar(archivo)

def consultarEstudiantesPorGrupo(acme):
    codigoGrupo = input("Inserte el codigo del grupo: ")
    if "grupos" in acme and codigoGrupo in acme["grupos"]:
        if "estudiantes" in acme:
            estudiantes = acme["estudiantes"]
        else:
            estudiantes = {}

        estudiantesEnGrupo = []

        for est in estudiantes.values():
            try:
                if est["grupo"] == codigoGrupo:
                    estudiantesEnGrupo.append(est)
            except Exception:
                continue

        if estudiantesEnGrupo:
            print(f"Estudiantes matriculados en el grupo {codigoGrupo}:")
            for estudiante in estudiantesEnGrupo:
                print(f"- {estudiante['nombre']}, codigo: {estudiante['codigo']}")
            input("Presiona cualquier tecla para volver")
        else:
            print(f"No hay estudiantes matriculados en el grupo {codigoGrupo}.")
    else:
        print(f"El grupo con codigo {codigoGrupo} no existe")



def consultarEstudiantesPorModulo(acme):
    codigoModulo = input("Inserte el codigo del modulo: ")
    modulos = acme["modulos"]
    if "modulos" in acme and codigoModulo in acme["modulos"]:
        if "estudiantes" in acme:
            estudiantes = acme["estudiantes"]
        else:
            estudiantes = {}

        estudiantesModulo = []

        for est in estudiantes.values():
            try:
                if est["modulos"]:
                    for i in est["modulos"]:
                        if i == codigoModulo:
                            estudiantesModulo.append(est)
            except Exception:
                    continue

        if estudiantesModulo:
            print(f"Estudiantes matriculados en el modulo {modulos[codigoModulo]['nombre']}:")
            for estudiante in estudiantesModulo:
                print(f"- {estudiante['nombre']} codigo: {estudiante['codigo']}")
        else:
            print(f"No hay estudiantes matriculados en el modulo {modulos[codigoModulo]['nombre']}")
    else:
        print(f"El modulo con codigo {codigoModulo} no existe")
    input("Presione cualquier tecla para volver al menú")


def consultarDocentesPorModulo(acme):
    codigoModulo = input("Inserte el código del modulo: ")

    if "modulos" in acme and codigoModulo in acme["modulos"]:
        modulo = acme["modulos"][codigoModulo]
        
        if "docentes" in modulo and modulo["docentes"]:
            print(f"Los docentes del modulo {modulo['nombre']} son:")
            for docente in modulo["docentes"]:
                print(f"{docente['nombre']}, cedula: {docente['cedula']}")
        else:
            print(f"No hay docentes asignados al modulo {modulo['nombre']}")
    else:
        print(f"El modulo con código {codigoModulo} no existe")
    input("Presione cualquier tecla para volver al menú")

def consultarEstudiantesPorDocente(acme):
    codigoModulo = input("Inserte el codigo del modulo: ")

    if "modulos" in acme and codigoModulo in acme["modulos"]:
        modulo = acme["modulos"][codigoModulo]
        
        if "docentes" in modulo and modulo["docentes"]:
            print(f"Los docentes del modulo {modulo['nombre']} son:")
            for docente in modulo["docentes"]:
                print(f"{docente['nombre']}, cedula: {docente['cedula']}")
        else:
            print(f"No hay docentes asignados al modulo {modulo['nombre']}")
    else:
        print(f"El modulo con codigo {codigoModulo} no existe")
    input("Presione cualquier tecla para volver al menú")

def consultarEstudiantesPorDocenteModulo(acme):
    codigoModulo = input("Inserte el codigo del modulo: ")
    
    if codigoModulo in acme["modulos"]:
        modulo = acme["modulos"][codigoModulo]

        if "docentes" in modulo:
            cedDocente = input("Inserte el codigo del docente: ")
            for doc in modulo["docentes"]:
                if doc["cedula"] == cedDocente:
                    estudiantesEnModulo = []

                    for dicEStudiante in acme["estudiantes"]:
                        estudiante = acme["estudiantes"][dicEStudiante]
                        if codigoModulo in estudiante["modulos"]:
                            estudiantesEnModulo.append(estudiante)

                    if estudiantesEnModulo:
                        print(f"Estudiantes a cargo del docente {doc['nombre']} con cedula {cedDocente} en el modulo {modulo['nombre']}:")
                        for estudiante in estudiantesEnModulo:
                            print(f"{estudiante['nombre']}, codigo: {estudiante['codigo']}")
                    else:
                        print(f"No hay estudiantes a cargo del docente {doc['nombre']} con cedula {cedDocente} en el modulo {modulo['nombre']}")
        else:
            print(f"El docente {doc['nombre']} con cedula {cedDocente} no se encuentra en el modulo {modulo['nombre']}.")
    else:
        print("El modulo con el codigo ingresado no existe")
    input("Presione cualquier tecla para volver al menú")





def menuConsultas():
    print("******************************ACME********************************")
    print()
    print("--------------------- Consultar informacion ----------------------")
    print("|                                                                |")
    print("| 1. Consultar los estudiantes matriculados en un grupo          |")
    print("| 2. Consultar los estudiantes inscritos en un módulo            |")
    print("| 3. Consultar los docentes que imparten un módulo               |")
    print("| 4. Consultar los estudiantes a cargo de un docente en un módulo|")
    print("| 5. Salir                                                       |")
    print("|                                                                |")
    print("------------------------------------------------------------------")

    print(">>> Opcion? ", end="")
    while True:
        try:
            opcion = int(input())
            if not opcion:
                print("Error. Opcion no valida...")
                input("Presione cualquier tecla para volver al menu")
                continue
            return opcion
        except Exception:
            print("Error. Opcion no valida...")
            break
        
def menuOpc(acme):
    while True:
        op = menuConsultas()
        match op:
            case 1:
                consultarEstudiantesPorGrupo(acme)
            case 2:
                consultarEstudiantesPorModulo(acme)
            case 3:
                consultarDocentesPorModulo(acme)
            case 4:
                consultarEstudiantesPorDocenteModulo(acme)
                break
            case 5:
                print("\nDe vuelta al menu principal\n")
                break









