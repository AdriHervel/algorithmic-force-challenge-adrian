tu_fuerza =  int(input("Escribe aquí cuál es tu fuerza: "))

def poder_dela_fuerza(tu_fuerza):
    factorial = 1
    for i in range(1, tu_fuerza + 1):
        factorial *= i
    return factorial

print(f"El poder de tu fuerza","(-->", tu_fuerza, "<--), es: ", poder_dela_fuerza(tu_fuerza))


            

