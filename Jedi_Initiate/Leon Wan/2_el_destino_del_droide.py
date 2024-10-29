# Version: 1.0
# Date: 2021-09-14
# Author: Leo Wan
# GitHub: @leolicona

def is_even_or_odd(n):
    if n % 2 == 0: 
        print(f"El numero {n} es par.")
    else:
        print(f"El numero {n} es impar.")

def main():
    print("R2-D2, necesitamos tu ayuda.")
    print("Este es el programa que determina si un numero es par o impar.")
    while True:
        try:
            print("1. Comprobar si un numero es par o impar.")
            print("2. Salir.")

            option = int(input("Elige una opción: "))

            if option == 1:
                numero = int(input("Ingresa un numero: "))
                is_even_or_odd(numero)
            if option == 2:
                print("Que la Fuerza te acompañe.")
                break

        except ValueError:
            print("Por favor, ingresa un número entero.")
            continue
main()

