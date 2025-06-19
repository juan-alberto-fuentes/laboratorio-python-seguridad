# Script: scanner_usuarios.py
# Descripción: Genera una lista de nombres de usuario a partir de un nombre base
# Resultado: Guarda los usuarios en logs/usuarios_generados.txt

try:
    base = input("🔤 Escribe el nombre base (ej: admin): ")
    cantidad = int(input("🔢 ¿Cuántos usuarios quieres generar?: "))

    if cantidad <= 0:
        print("⚠️ Por favor, introduce un número positivo mayor que cero.")
    else:
        ruta_salida = "../logs/usuarios_generados.txt"
        with open(ruta_salida, "w") as archivo:
            for i in range(1, cantidad + 1):
                usuario = f"{base}{i}"
                archivo.write(usuario + "\n")

        print(f"\n✅ {cantidad} usuarios generados y guardados en {ruta_salida}")

except ValueError:
    print("❌ Error: Debes introducir un número entero válido para la cantidad.")
