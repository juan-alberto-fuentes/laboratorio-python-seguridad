import subprocess

with open("resultado_scan.txt", "w") as archivo:
    for i in range(1, 6):
        ip = f"192.168.1.{i}"
        resultado = subprocess.run(["ping", "-c", "1", "-w", "1", ip], stdout=subprocess.DEVNULL)

        if resultado.returncode == 0:
            linea = f"[+] {ip} está ACTIVA\n"
        else:
            linea = f"[-] {ip} no responde\n"
        
        print(linea.strip())          #Mostrar por pantalla
        archivo.write(linea)            #Guardar en archivo