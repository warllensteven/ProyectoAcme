import hashlib
import json

archivo = "usuarios.json"

def encriptacion(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def cargarUsuarios(archivo):
    usuarios = {}
    try:
        with open(archivo, 'r') as fd:
            return json.load(fd)
    except Exception:
        print(f"Inicio de sistema")
    return usuarios

def guardarUsuarios(usuarios, archivo):
    with open(archivo, 'w') as fd:
        json.dump(usuarios, fd)

def inicio(archivo):
    usuarios = cargarUsuarios(archivo)
    print("Bienvenido a ACME")
    
    while True:
        usuario = input("Ingrese su usuario: ")
        if len(usuario.strip()) <= 0:
            print(">>> Error. Usuario no valido, intenta otra vez")
            continue
        
        if usuario in usuarios:
            contrasena = input("Ingrese su contraseña: ")
            if usuarios[usuario] == encriptacion(contrasena):
                print("Inicio de sesion exitoso")
                return usuario
            else:
                print(">>> Error. Contraseña incorrecta, intenta de nuevo")
        else:
            print("Usuario no encontrado")
            print("Desea crear usuario? (s/n)")
            if input().lower() == 's':
                contrasena = "SISGESA"
                usuarios[usuario] = encriptacion(contrasena)
                guardarUsuarios(usuarios, archivo)
                print("Usuario creado. Su contraseña por defecto es: SISGESA")
                return usuario

def cambiarContrasena(usuarios, arch):
    print("--- h. Cambio de contraseña ---")
    with open(arch, "r") as fd:
        json.load(fd)
    while True:
        usuario = input("Ingrese su usuario: ")
        if usuario in usuarios:
            contrasena = input("Ingrese su contrasena: ")
            if usuarios[usuario] == encriptacion(contrasena):
                contrasenaNueva = input("Ingrese su nueva contrasena: ")
                contrasenaCompr = input("Confirme su nueva contraseña: ")
                if contrasenaNueva == contrasenaCompr:
                    usuarios[usuario] = encriptacion(contrasenaNueva)
                    guardarUsuarios(usuarios, arch)
                    break
                else:
                    print("La contraseña no coincide,intenta nuevamente")
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario invalido")



