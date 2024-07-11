# Ejemplo de funciones
def tabla(numero):
    print(f"Tabla de multiplciar del numero: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

tabla(3)

# Ejemplo 3.1
print("#############")
for numeroTabla in range(1,11):
    tabla(numeroTabla) 
    # Le pasamos la primer función para que su parámetro sea el for