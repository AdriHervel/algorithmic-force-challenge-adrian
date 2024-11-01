matriz1 = [[1, 2], [2, 4]]
matriz2 = [[2, 1], [3, 2]]
def multi_matrices(matriz1, matriz2):
    # Obtener el número de filas y columnas de las matrices 
    filas_matriz1 = len(matriz1) 
    columnas_matriz1 = len(matriz1[0]) 
    columnas_matriz2 = len(matriz2[0]) 
    # Crear la matriz resultado con ceros 
    matriz_resultado = [[0 for _ in range(columnas_matriz2)] for _ in range(filas_matriz1)]
    # Realizar la multiplicación de matrices 
    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(columnas_matriz1):
                matriz_resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return matriz_resultado

resultado = multi_matrices(matriz1, matriz2)
print(resultado)