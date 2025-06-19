# Script: analizador_logs.py
# Descripción: Analiza un archivo de logs buscando una palabra clave
# Resultado: Guarda líneas coincidentes en logs/logs_filtrados.txt

try:
    archivo_entrada = input("📂 Nombre del archivo a analizar (ej: resultado_scan.txt): ").strip()
    palabra_clave = input("🔍 Palabra clave a buscar (ej: error): ").strip().lower()

    ruta_entrada = f"../logs/{archivo_entrada}"
    ruta_salida = "../logs/logs_filtrados.txt"

    coincidencias = []

    with open(ruta_entrada, "r") as archivo:
        for linea in archivo:
            if palabra_clave in linea.lower():
                coincidencias.append(linea)

    if coincidencias:
        with open(ruta_salida, "w") as salida:
            for linea in coincidencias:
                salida.write(linea)
        print(f"\n✅ {len(coincidencias)} coincidencias encontradas.")
        print(f"📁 Resultado guardado en {ruta_salida}")
    else:
        print("\n⚠️ No se encontraron coincidencias.")

except FileNotFoundError:
    print("❌ Error: El archivo indicado no existe en la carpeta logs/")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
