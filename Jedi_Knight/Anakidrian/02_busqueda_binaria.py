lista = list(range(0, 21, 3))
objetivo = 7
def num_binary(lista, objetivo):
    izquierda = 0
    derecha = len(lista)-1
    while izquierda <= derecha:
        medio = (izquierda + derecha // 2)
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return "¡Encontramos al Objetivo!"
        elif valor_medio < objetivo:
            valor_medio = medio + 1
        else:
            valor_medio = medio - 1
        
    return -1
resultado = num_binary(lista, objetivo)
print(f"El código {objetivo} {'se encuentra en la posición' if resultado != -1 else 'no se encuentra en la lista'} {resultado if resultado != -1 else ''}.")