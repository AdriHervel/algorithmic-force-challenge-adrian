oracion = input("Escribe una oración: ")

def contador_vocales(oracion):
    vocales = ["a", "e", "i", "o", "u"]
    num_vocales = 0
    for vocal in oracion.lower():
        if vocal in vocales:
            num_vocales += 1
    return num_vocales
print(f"El número de vocales en la oración es: {contador_vocales(oracion)}")
