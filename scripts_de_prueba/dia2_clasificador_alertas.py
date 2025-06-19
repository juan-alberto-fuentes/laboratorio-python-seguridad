alerta = input("Introduce nivel de alerta (bajo, medio, crítico): ")

if alerta == "bajo":
    print ("Monitorizar actividad")
elif alerta == "medio":
    print("Activar medidas de control")
elif alerta == "crítico":
    print("Ejecutar plan de respuesta inmediata")
else:
    print("Nivel no reconocido")