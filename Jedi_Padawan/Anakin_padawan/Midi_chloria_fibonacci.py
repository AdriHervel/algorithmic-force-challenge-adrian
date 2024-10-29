n = int(input("Escribe un número: "))

def midi_fibonacci(n):
    if n <= 0:
        return "El número debe ser mayor a 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return midi_fibonacci(n-1) + midi_fibonacci(n-2)
print(f"El {n}-ésimo número de Fibonacci es {midi_fibonacci(n-1)}")