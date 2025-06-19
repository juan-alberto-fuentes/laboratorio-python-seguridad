import re

ruta = input("Ruta del archivo log: ")

try:
    with open(ruta, "r") as archivo:
              contenido = archivo.read()

    # Buscar todas las direcciones IP en el texto
    ips = re.findall("r\b\d{1,3}(?:\.\d{1,3}){3}\b", contenido)

    if ips:
       print("Direcciones IP encontradas:")
       for ip in ips:
             print(f"✅ {ip}")

       # Guardar las IPs encontradas en un archivo
       with open("ips_detectadas.txt", "w") as salida:
             for ip in ips:
                   salida.write(i + "\n")

       
    print(f"\nTotal: {len(ips)} IPs encontradas.")
    
except FileNotFoundError:
       print("❌ Archivo no encontrado.")
except Exception as e:
       print(f"❌ Error: {e}")