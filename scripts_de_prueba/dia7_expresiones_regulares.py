import re

ruta = input("Ruta del archivo log: ")

try:
    with open(ruta, "r") as archivo:
              contenido = archivo.read()

    # Buscar todas las direcciones IP con este patrón
    ips = re.findall("r\b\d{1,3}(?:\.\d{1,3}){3}\b", contenido)

    print("Direcciones IP encontradas:")
    for ip in ips:
           print(ip)

    print(f"\nTotal: {len(ips)} IPs encontradas.")
    
except FileNotFoundError:
       print("❌ Archivo no encontrado.")
except Exception as e:
       print(f"❌ Error: {e}")