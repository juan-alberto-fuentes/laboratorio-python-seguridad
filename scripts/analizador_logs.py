ruta = input("Ruta del archivo log: ")
clave = input("Palabra a buscar (ej: failed, ssh, error): ")
try:
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            if clave.lower() in linea.lower():
                print(linea.strip())
except FileNotFoundError:
    print("Archivo no encontrado.")
except PermissionError:
    print("No tienes permisos para leer ese archivo.")