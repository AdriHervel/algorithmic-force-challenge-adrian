# Version: 1.0
# Date: 2021-09-14
# Author: Leo Wan
# GitHub: @leolicona

def sum_force(a, b):
    return a + b

def main():
    print("Bienvenido a la Orden Jedi.")
    print("Este es el programa que calcula la suma de la Fuerza.")

    while True:
        try:
            print("1. Calcular la suma de la Fuerza.")
            print("2. Salir.")

            option = int(input("Elige una opción: "))

            if option == 1:
                value_a = int(input("Ingresa el primer número: "))
                value_b = int(input("Ingresa el segundo número: "))
                result = sum_force(value_a, value_b)
                print(f"La suma de la Fuerza es: {result}")
            if option == 2:
                print("Que la Fuerza te acompañe.")
                break

        except ValueError:
            print("Por favor, ingresa un número entero.")
            continue

main()