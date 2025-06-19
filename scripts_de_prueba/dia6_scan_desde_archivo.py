import subprocess

with open("lista_ips.txt", "r") as lista:
    ips = lista.readlines()   # Crea una lista de líneas

activas = 0

with open("resultado_scan_ips.txt", "w") as resultado:
    for ip in ips:
        ip = ip.strip()   # Quita saltos de línea

        respuesta = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL)

        if respuesta.returncode == 0:
            linea = f"[+] {ip} está ACTIVA\n"
            activas += 1
        else:
            linea = f"[-] {ip} no responde\n"

        print(linea.strip())
        resultado.write(linea)

    resultado.write(f"\nTotal activas: {activas}\n")

print(f"\nTotal activas: {activas}")