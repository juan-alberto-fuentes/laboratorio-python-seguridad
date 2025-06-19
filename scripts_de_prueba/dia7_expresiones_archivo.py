import re
ruta = input("Ruta del archivo log: ")

try:
    with open(ruta, "r") as archivo:
        contenido = archivo.read()

    # Buscar todas las direcciones IP en el texto
    ips = re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", contenido)

    if ips:
        print("Direcciones IP encontradas:")
        for ip in ips:
            print(f"✅ {ip}")

    # Guardar las IPs encontradas en un archivo
    with open("ips_detectadas.txt", "w") as salida:
        for ip in ips:
            salida.write(ip + "\n")
            print(f"\n IPs guardadas en 'ips_detectadas.txt'")
            print(f" Total: {len(ips)}IPs encontradas.")
        else:
            print("No de encontraron IPs en el archivo.")

except FileNotFoundError:
    print("Archivo no encontrado.")
except Exception as e:
    print(f"Error inesperado: {e}")