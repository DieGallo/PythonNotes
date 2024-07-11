"""
    Variables LOCALES
Son aquellas que se definen dentro de la función y no puede ser usada
fuera de la funcion solamente se puede utilizar en la funcion donde se
inicializa

    Variables GLOBALES
Son aquellas que tu las declaras fuera de todas las funciones y estan
disponibles para utilizarlas en donde sean ya que no pertenecen a ninguna
funcion
"""

# Variable Global
frase = "Hola como estas"
print(frase)

# Variable Local
def holaMundo():
    frase =  "Hola mundo"
    print("Dentro de la funcion")
    print(frase)

    # Para convertir una variable local a Global utilizar el prefijo "global"
    global website
    website = "diegolopez.com"

holaMundo()