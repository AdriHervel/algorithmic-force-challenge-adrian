num =int(input("Elige un número para aprenderte su tabla de multiplicar: "))

def tabla_de_multiplicar(num):
    tabla = []
    for i in range(1, 11):
        resultado = num * i
        tabla.append(f" {num} * {i} = {resultado}")
    return tabla
tabla = tabla_de_multiplicar(num)
print(f"Tabala de multiplicar del número {num}: ")
for linea in tabla:
    print(linea)