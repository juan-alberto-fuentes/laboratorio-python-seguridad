intentos = 0

while intentos < 3:
    clave = input("Introduce la clave de acceso: ")
    if clave == "juan":
        print("Acceso concedido")
        break
    else:
        print("Clave incorrecta")
        intentos +=1

if intentos == 3:
    print("Demasiados intentos. Bloqueado.")