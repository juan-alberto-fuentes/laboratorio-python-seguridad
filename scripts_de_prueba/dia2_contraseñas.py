print ("Bienvenido al gestor de contraseñas")
contraseña = input("Escribe una contraseña: ")

len_contraseña = len(contraseña)

if len_contraseña < 6:
    print("Debil")
elif len_contraseña >= 6 and len_contraseña <= 10:
    print("Aceptable")
else:
    print("Fuerte")