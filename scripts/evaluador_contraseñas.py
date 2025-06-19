# Script: evaluador_contraseñas.py
# Descripción: Evalúa la fortaleza de una contraseña

import string

contraseña = input("🔑 Escribe una contraseña para evaluar: ")

if contraseña.strip() == "":
    print("❌ Error: No se puede evaluar una contraseña vacía.")
else:
    longitud = len(contraseña)
    tiene_mayus = any(c.isupper() for c in contraseña)
    tiene_minus = any(c.islower() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    tiene_simbolo = any(c in string.punctuation for c in contraseña)

    # Evaluar
    if longitud > 10 and tiene_mayus and tiene_minus and tiene_numero and tiene_simbolo:
        evaluacion = "Fuerte"
    elif longitud >= 6:
        evaluacion = "Aceptable"
    else:
        evaluacion = "Débil"

    print(f"🔐 Contraseña evaluada como: {evaluacion}")

    # Guardar en archivo
    with open("../logs/evaluacion_contraseña.txt", "w") as archivo:
        archivo.write(f"Contraseña: {contraseña}\n")
        archivo.write(f"Evaluación: {evaluacion}\n")

    print("✅ Resultado guardado en logs/evaluacion_contraseña.txt")
