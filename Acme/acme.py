from inicio.inicio import *
from interfaz.menu import menu
from modelo.insertaciones import *
from modelo.consultas import *
from informes.informes import *
from persistencia.persistencia import cargar
from asistencia.asistencia import *

#Programa
usuarios = {}
archivoUs = "usuarios.json"
usuarios = cargar(archivoUs)
acme = {}
archivo = "dicAcme.json"
acme = cargar(archivo)
usuario = inicio(archivoUs)

while True:
    op = menu()
    match op:
        case "a":
            acme = insertarGrupo(acme, archivo)
        case "b":
            acme = insertarModulos(acme, archivo)
        case "c":
            acme = insertarEstudiantes(acme, archivo)
        case "d":
            acme = insertarDocentes(acme, archivo)
        case "e":
            menuOpcE(acme)
        case "f":
            menuOpc(acme)
        case "g":
            menuOpcI(acme)
        case "h":
            acme = cambiarContrasena(usuarios, archivoUs)
        case "i":
            print("\Gracias por usar el software\n")
            break