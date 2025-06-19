# Script: generador_roles.py
# Descripción: Genera una lista de roles personalizados y los guarda en logs/roles_generados.txt

try:
    base = input("🔤 Escribe el nombre base para los roles (ej: admin, auditor): ").strip()
    cantidad = int(input("🔢 ¿Cuántos roles quieres generar?: "))

    if base == "":
        print("❌ Error: El nombre base no puede estar vacío.")
    elif cantidad <= 0:
        print("❌ Error: Debes introducir un número positivo mayor que cero.")
    else:
        ruta_salida = "../logs/roles_generados.txt"
        with open(ruta_salida, "w") as archivo:
            for i in range(1, cantidad + 1):
                rol = f"{base}{i}"
                archivo.write(rol + "\n")

        print(f"\n✅ {cantidad} roles generados y guardados en {ruta_salida}")

except ValueError:
    print("❌ Error: Debes introducir un número entero válido para la cantidad.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
