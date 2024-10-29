# Version: 1.0
# Date: 2021-09-14
# Author: Leo Wan
# GitHub: @leolicona

def sort_pilots_times(times):
    print("Processing...")
    print(type(times))
    times_list = times.split()

    for i in times_list:
       print(i)
        

def main():
    print("Bienvenido a la carrera de vainas de Boonta Eve.")
    print("Este es el programa que organiza los tiempos de los pilotos.")
    while True:
        try:
            print("1. Organizar tiempos.")
            print("2. Salir.")

            option = int(input("Elige una opción: "))

            if option == 1:
                pilot_times = input("Ingresa los tiempos de los pilotos separados por espacios: ")
                sort_pilots_times(pilot_times)
            if option == 2:
                print("Que la Fuerza te acompañe.")
                break

        except ValueError:
            print("Por favor, ingresa un número entero.")
            continue

main()

