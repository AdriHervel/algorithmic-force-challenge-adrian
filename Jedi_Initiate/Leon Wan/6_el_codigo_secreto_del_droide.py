# Version: 1.0
# Date: 2021-09-14
# Author: Leo Wan
# GitHub: @leolicona



def is_prime(n):
    if n == 2 or n % 2 != 0:
        print(f"El numero {n} es primo.")
    else: 
        print(f"El numero {n} no es primo.")
    
 
def main(): 
    while True:
        try: 
            print("Bienvenido a la Orden Jedi.")
            print("Este es el programa que verifica si un numero es primo.")
            print("1. Comprobar si un numero es primo.")
            print("2. Salir.")

            option = int(input("Elige una opcion: "))

            if option == 1:
            
                numero = int(input("Caballero Jedi, ingresa un numero: "))
                print("Processing...")
                is_prime(numero)
            if option == 2:
                print("Que la Fuerza te acompañe.")
                break
        except ValueError:
            print("Por favor, ingresa un numero entero.")
            continue
      
main()
    