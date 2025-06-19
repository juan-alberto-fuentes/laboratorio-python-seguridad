# Script: verificador_ips.py
# Descripción: Extrae todas las IPs de un archivo y las guarda en logs/ips_detectadas.txt

import re

try:
    nombre_archivo = input("📂 Nombre del archivo en logs/ a analizar (ej: resultado_scan.txt): ").strip()
    ruta_entrada = f"../logs/{nombre_archivo}"
    ruta_salida = "../logs/ips_detectadas.txt"

    # Expresión regular para buscar IPs
    patron_ip = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ips_encontradas = set()

    with open(ruta_entrada, "r") as archivo:
        for linea in archivo:
            coincidencias = re.findall(patron_ip, linea)
            for ip in coincidencias:
                ips_encontradas.add(ip)

    if ips_encontradas:
        with open(ruta_salida, "w") as salida:
            for ip in sorted(ips_encontradas):
                salida.write(ip + "\n")
        print(f"\n✅ {len(ips_encontradas)} IPs encontradas y guardadas en {ruta_salida}")
    else:
        print("\n⚠️ No se encontraron IPs en el archivo.")

except FileNotFoundError:
    print("❌ Error: El archivo indicado no existe en la carpeta logs/")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
