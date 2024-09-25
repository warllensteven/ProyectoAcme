import json
from pathlib import Path


def guardar(acme, arch):
    with open(arch, "w") as fd:
        json.dump(acme, fd, indent=4)

    if not fd.closed:
        fd.close()

def cargar(arch):
    archivo = Path(arch)
    acme = {}
    if archivo.is_file(): #True  si existe y es un archivo
        try:
            with open(arch, "r") as fd:
                acme = json.load(fd)

            if not fd.closed:
                fd.close()
        except Exception as e:
            print()
    
    else:
        print(">>> Error. El archivo no existe.")
        input(">>> Presione cualquier tecla para continuar...")

    return acme






