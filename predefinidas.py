# Funciones Generales
nombre = "Diego Lopez"
print(nombre)

# Detectar el tipo de Dato con isinstance
comprobar = isinstance(nombre, int)
if comprobar:
    print("Esa variable es un String")
else:
    print("Print no es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# Limpiar espacios de un String
frase = "            Mi contenido            "
print(frase)
# .strip limpia los espacios en blanco
print(frase.strip())

# Eliminar las variables
year = 2024
print(year)
# Borramos la variable con del 
del year
#print(year)

# Comprobar variables vacias
texto = "  ff  "
# len() es lo que se conoce como .length en JS
if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido", len(texto))

# Encontrar caracteres
frase = "La vida es bella"
# .find buscamos coincidencia con la variable
print(frase.find("vida"))

# Reemplazar palabras en un String
nuevaFrase = frase.replace("vida", "mujer")
print(nuevaFrase)

# Mayusculas y minisculas
print(nombre)
print(nombre.lower())
print(nombre.upper())