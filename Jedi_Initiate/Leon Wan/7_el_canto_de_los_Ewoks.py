# Version: 1.0 
# Date: 2021-09-14
# Author: Leo Wan
# GitHub: @leolicona

def count_vowels(song):
    count_vowels = 0
    vowels = "aeiouAEIOU"
    for letter in song: 
        for vowel in vowels: 
            if letter == vowel: 
                count_vowels += 1

    return count_vowels

def main(): 
    print("Bienvenido a la celebración en Endor.")
    print("Durante la celebración, los Ewoks cantan una canción de victoria.")
    print("Este es el programa que cuenta cuántas vocales tiene la canción.")
    while True:
        try:
            print("1. Contar vocales.")
            print("2. Salir.")

            option = int(input("Elige una opción: "))

            if option == 1: 
                song = input("Ingresa la canción de los Ewoks: ")
                result = count_vowels(song)
                print(f"La canción de los Ewoks tiene {result} vocales.")
            if option == 2:
                print("Que la Fuerza te acompañe.")
                break

        except ValueError:
            print("Por favor, ingresa un número entero.")
            continue
main()
