import subprocess

def escanear_ip(ip):
    """Devuelve True si la IP responde al ping, False si no"""
    resultado = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL)
    return resultado.returncode == 0

# Leer IPs desde archivo
with open("lista_ips.txt", "r") as lista:
    ips = lista.readlines()

activas = 0

# Guardar resultados en archivo
with open("lista_ips.txt", "w") as resultado:
    for ip in ips:
        ip = ip.strip()

        if escanear_ip(ip):
            linea = f"[+] {ip} está ACTIVA\n"
            activas +=1
        else:
            linea =f"[-] {ip} no responde\n"

        print(linea.strip())
        resultado.write(linea)

    resultado.write(f"\nTotal activas: {activas}\n")

print(f"\Total activas: {activas}")