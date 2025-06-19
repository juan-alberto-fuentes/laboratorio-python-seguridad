nombre = input("¿Cuál es tu tu nombre? ")
edad = input("¿Cuántos años tienes? ")

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

edad = int(edad)
if edad >= 18:
    print("Acceso permitido")
else:
    print("Acceso denegado")