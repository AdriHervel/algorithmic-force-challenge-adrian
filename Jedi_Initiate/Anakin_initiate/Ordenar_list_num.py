# Solicitar la lista de tiempos separadas por comas y convertirla a una lista de enteros
tiempos = list(map(int, input("Dame la lista de tiempos separadas por comas: ").split(',')))
def tiempos_ordenados(tiempos):
    # Se guarda en la variable el numero de tiempos contados en la lista.
    n = int(len(tiempos))
    for i in range(n):
        for j in range(0, n-i-1):
            if tiempos[j] > tiempos[j+1]:
                tiempos[j], tiempos[j+1] = tiempos[j+1], tiempos[j]
    return tiempos
# Ordenar de menor a mayor y luego invertir para obtener de mayor a menor
tiempos_ordenados = tiempos_ordenados(tiempos)[::-1]
print("Los tiempos de los competidores son en orden de mayor a menor, los siguientes:", tiempos_ordenados)