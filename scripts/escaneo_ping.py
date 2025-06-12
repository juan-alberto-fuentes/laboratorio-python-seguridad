import os
import subprocess
base_ip = "192.168.1."

print("Escaneando la red...\n")

for i in range(1, 21):
    ip = base_ip + str(i)
    resultado = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL)
    if resultado.returncode == 0:
        print(f"[+] {ip} está ACTIVA")
    else:
        print(f"[-] {ip} no responde")