from funInputs.funInput import *
from persistencia.persistencia import *

def insertarGrupo(acme, archivo):
    print("\n|      a. Agregar Grupos       |\n")

    if "grupos" not in acme:
        acme["grupos"] = {}

    grupos = acme["grupos"] 

    codigoGrupo = leerCod()
    
    if codigoGrupo not in grupos:
        codigo = codigoGrupo
        nombre = leerNombre()
        sigla = leerSigla()

        grupo = {
            "codigo": codigo,
            "nombre": nombre,
            "sigla": sigla
        }

        grupos[codigoGrupo] = grupo

        print("Grupo registrado exitosamente")

        acme = dict(sorted(acme.items()))

        guardar(acme, archivo)
    else:
        print("El grupo ya existe")
    input("Presione cualquier tecla para volver al menu")
    print("")
    
    return acme



def insertarModulos(acme, archivo):
    print("\n\n|      b. Agregar Modulos      |")

    if "modulos" not in acme:

        acme["modulos"] = {}

    modulos = acme["modulos"] 

    codModulo = leerCod()
    if codModulo not in modulos:
        codigo = codModulo
        nombre = leerNombre()
        sem = leerSemanas()
        horaInicio = input("Ingresa el horario de inicio de clase (formato HH:MM), ejemplo(07:05): ")
        horaSalida = input("Ingresa el horario de salida de clase (formato HH:MM), ejemplo(20:05): ")

        modulo = {
            "codigo": codigo,
            "nombre": nombre,
            "semanas": sem,
            "horaInicio": horaInicio,
            "horaSalida": horaSalida,
            "docentes": [],
            "asistencias": []
        }

        modulos[codModulo] = modulo

        print("Modulo registrado exitosamente")

        acme = dict(sorted(acme.items()))

        guardar(acme, archivo)
        
    else:
        input("El modulo ya existe")
    input("Presione cualquier tecla para volver al menu")
    print("")

    return acme   

def insertarEstudiantes(acme, archivo):
    print("\n|    c. Agregar estudiantes     |")
    
    if "estudiantes" not in acme:
        acme["estudiantes"] = {}

    estudiantes = acme["estudiantes"]

    while True:
        estCod = leerCod()
        
        if estCod not in estudiantes:
            nombre = leerNombre()
            sexo = leerSexo()
            edad = leerEdad()

            lstmod = []

            while True:
                grupo = input("Ingrese el grupo en el que se ingresara el estudiante: ")
                if grupo in acme["grupos"]:
                    break
                else:
                    print("Grupo invalido, ingrese uno valido.")
            while True:
                modulo = input("Ingrese el modulo que cursara el estudiante (-1 para terminar): ")
                if modulo == "-1" or len(lstmod) == 3:
                    print("El limite de modulos por estudiante es 3, cupo lleno")
                    break
                elif modulo in acme["modulos"]:
                    if modulo not in lstmod:
                        lstmod.append(modulo)
                    else:
                        print(">>>Error, el estudiante ya esta registrado en este modulo")
                else:
                    print("Modulo invalido, ingrese un modulo valido.")

            estudiante = {
                "codigo": estCod,
                "nombre": nombre,
                "sexo": sexo,
                "edad": edad,
                "grupo": grupo,
                "modulos": lstmod
            }
                

            estudiantes[estCod] = estudiante

            print("Estudiante registrado exitosamente")

            acme = dict(sorted(acme.items()))
            guardar(acme, archivo)

            break
        else:
            print("Codigo invalido, el estudiante ya existe, presione cualquier tecla para volver al menu")
    input("Presione cualquier tecla para volver al menu")
    print("")

    return acme



def insertarDocentes(acme, archivo):
    print("\n|    d. Agregar docentes     |")
    modulos = acme["modulos"]
    
    cedula = leerCed()
    nombre = leerNombre()
    
    codModulo = input("Ingresa el codigo del modulo que dictara el docente: ")
    
    if codModulo in modulos:
        modulosDocente = 0
        
        for modulo in modulos.values():
            if "docentes" in modulo:
                for docente in modulo["docentes"]:
                    if docente["cedula"] == cedula:
                        modulosDocente += 1
        
        if modulosDocente >= 3:
            print("El docente solo puede dictar 3 modulos")
        else:
            docente = {
                "cedula": cedula,
                "nombre": nombre
            }

            if "docentes" in modulos[codModulo]:
                modulos[codModulo]["docentes"].append(docente)
            else:
                modulos[codModulo]["docentes"] = [docente]

            acme = dict(sorted(acme.items()))
            guardar(acme, archivo)

    
    else:
        print("El módulo no existe, intenta con uno existente.")

    input("Presione cualquier tecla para volver al menu")
    print("")

    return acme




