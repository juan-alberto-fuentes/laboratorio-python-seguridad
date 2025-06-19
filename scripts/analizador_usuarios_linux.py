# Script: analizador_usuarios_linux.py
# Descripción: Analiza /etc/passwd y extrae usuarios reales del sistema

try:
    ruta_salida = "../logs/usuarios_sistema.txt"
    usuarios_reales = []

    with open("/etc/passwd", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(":")

            if len(partes) >= 7:
                usuario = partes[0]
                uid = int(partes[2])
                home = partes[5]
                shell = partes[6]

                if uid >= 1000 and shell not in ["/usr/sbin/nologin", "/bin/false"]:
                    usuarios_reales.append((usuario, uid, home, shell))

    if usuarios_reales:
        with open(ruta_salida, "w") as salida:
            for u in usuarios_reales:
                salida.write(f"Usuario: {u[0]} | UID: {u[1]} | Home: {u[2]} | Shell: {u[3]}\n")

        print(f"\n✅ {len(usuarios_reales)} usuarios reales encontrados.")
        print(f"📁 Resultado guardado en {ruta_salida}")
    else:
        print("⚠️ No se encontraron usuarios reales con UID >= 1000.")

except Exception as e:
    print(f"❌ Error inesperado: {e}")
