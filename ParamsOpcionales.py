# Ejemplo 4
""" 
    Parámetros opcioanales
Para convertir un parametro normal a opciona le vamos a poner un = 
y le damos un valor por defecto.
Entonces a la hora de pasar el parámetro o no, no va a marcar error porque 
le estamos ya dando un valor por defecto de que no es necesario.

"""
def getEmpleado(nombre, dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if(dni != None):
        print(f"DNI: {dni}")
    else:
        print(f"No hay un DNI")

getEmpleado("Diego Lopez", "12312312")

# Ejemplo 5
""" 
    Return
"""
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo
saludame("Diego Lopez")

# Ejemplo Calculadora 
def calculadora(numero1, numero2, basicos = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena  = ""

    if(basicos != False):
        cadena += "Suma: " + str(suma)
        cadena += "\rResta: " + str(resta)
    else:
        cadena += "\nMultiplicacion: " + str(multiplicacion)
        cadena += "\nDivision: " + str(division)

    return cadena

print(calculadora(5,2))

# Funciones dentro de otras
def getNombre(nombre):
    texto = f"El Nombre es {nombre}\n"
    return texto

def getApellido(apellido):
    texto = f"El Apellido es {apellido}"
    return texto

# Esta funcion cuenta con ambas dentro de ella en la variable Texto
def returnAll(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(returnAll("Diego", "Lopez"))

# Funciones Lambda
tell_me_year = lambda year: f"The year is {year * 50}"
print(tell_me_year(2024))