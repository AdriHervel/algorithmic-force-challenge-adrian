fuerza_1 = int(input("Escribe tu nivel de fuerza inicial: "))
fuerza_2 = int(input("Escribe el incremento de tu fuerza en este entrenamiento: "))

def tu_fuerza_actual(fuerza_1, fuerza_2):
    total_de_fuerza = fuerza_1 + fuerza_2
    return total_de_fuerza
print(f"¡Felicidades! tu fuerza actual es de:", tu_fuerza_actual(fuerza_1, fuerza_2))
