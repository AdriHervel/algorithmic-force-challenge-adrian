N_msj = 1123

def es_primo(N_msj):
    if N_msj <= 1:
        return False
    for i in range(2, int(N_msj ** 0.5) + 1):
        if N_msj % i == 0:
            return False
    return True
if es_primo(N_msj):
    print(f"El número {N_msj} es primo")
else:
    print(f"El número {N_msj} no es primo")
    '''
    for i in range(2, N_msj):
        if i % 1 == 0:
            N_msj = False
        elif N_msj % i == 0:
            N_msj = False
    return True
if descifrar_mensaje(N_msj):

    print(f"El número número {N_msj} no es primo")
else:
    print(f"El número número {N_msj} es primo")
    '''