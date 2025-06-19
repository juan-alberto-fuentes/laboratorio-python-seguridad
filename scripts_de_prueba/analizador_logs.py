# Script: analizador_logs.py
# Descripcion: Busca líneas que contengan una palabra clave en un archivo de log
# Resultado: Guarda las coincidencias en logs/log_resultado_<clave>.txt

ruta = input("Ruta del archivo log: ")
clave = input("Palabra a buscar (ej: failed, ssh, error): ").lower()

try:
    with open(ruta, 'r') as archivo:
        #Crear la lista donde guardaremos las líneas encontradas
        lineas_encontradas = []

        for linea in archivo:
            if clave in linea.lower():
                print(linea.strip())
                lineas_encontradas.append(linea.strip())
    # Guardar los resultados en logs/
    nombre_salida = f"../logs/log_resultado_{clave}.txt"
    with open(nombre_salida, "w") as salida:
        for l in lineas_encontradas:
            salida.write(l + "\n")

    print(f"\n Resultados guardados en {nombre_salida}")
    
except FileNotFoundError:
    print("Archivo no encontrado.")
except PermissionError:
    print("No tienes permisos para leer ese archivo.")