import subprocess

def escanear_ip(ip):
    """Escanea ina IP con ping y devuelve True si responde, False si no"""
    resultado = subprocess.run(["ping", "1", "-W", "1", ip], stdout=subprocess.DEVNULL)
    return resultado.returncode == 0

#lista de IPs para probar
ips = ["192.168.1.1", "8.8.8.8", "10.0.0.1"]

for ip in ips:
    if escanear_ip(ip):
        print(f"[+] {ip} está ACTIVA")
    else:
        print(f"[-] {ip} no responde")