# Script: scanner_ping.py (versión profesional)
# Descripción: Escanea un rango de IPs usando ping y guarda las IPs activas
# Resultado: logs/resultado_scan.txt

import subprocess

# Solicitar al usuario la IP base
base_ip = input("Introduce la IP base (ejemplo: 192.168.1.): ")

# Solicitar el rango de IPs a escanear
inicio = int(input("Primer número a escanear (por ejemplo 1): "))
fin = int(input("Último número a escanear (por ejemplo 20): "))

ips_activas = []

print(f"\n🔎 Escaneando desde {base_ip}{inicio} hasta {base_ip}{fin}...\n")

for i in range(inicio, fin + 1):
    ip = base_ip + str(i)
    resultado = subprocess.run(["ping", "-c", "1", "-W", "1", ip],
                               stdout=subprocess.DEVNULL)

    if resultado.returncode == 0:
        mensaje = f"[+] {ip} está ACTIVA"
        ips_activas.append(mensaje)
    else:
        mensaje = f"[-] {ip} no responde"

    print(mensaje)

# Guardar resultados en logs
with open("../logs/resultado_scan.txt", "w") as archivo:
    for linea in ips_activas:
        archivo.write(linea + "\n")

print("\n✅ Escaneo completado. Resultados guardados en logs/resultado_scan.txt")
