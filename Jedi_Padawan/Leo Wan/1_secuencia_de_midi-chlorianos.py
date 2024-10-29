# Version: 1.0
# Date: 2021-09-14
# Author: Leo Wan
# GitHub: @leolicona

while True:
    print("********************************")
    print("Secuencia de Midi-chlorianos (Fibonacci)")
    print("Elige una opción:")
    print("1. Calcular el n-ésimo número en la secuencia de Fibonacci")
    print("2. Salir")
    option = int(input("Opción: "))
    if option == 2:
        break
    def midi_chlorians(n):
        fi = [0, 1] 
        for i in range(n):
            f =  fi[i] + fi[i+1]
            fi.append(f)
        return fi[n]

    number = int(input("Ingresa un numnero para calcular la secuencia de Fibonacci: "))
    print("Calculando...")
    print(f"El número en la posición {number} de la secuencia de Fibonacci es: {midi_chlorians(number)}")