rol = input("Introduce tu rol (admin, usuario, invitado): ")
if rol == "admin":
    print("Acceso total al sistema")
elif rol == "usuario":
    print("Acceso limitado a herramientas")
elif rol == "invitado":
    print("Solo acceso de lectura")
else:
    print("Rol no reconocido. Acceso denegado")