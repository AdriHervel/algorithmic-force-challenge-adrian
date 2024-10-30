grados_C = int(input("Ingresa la temperatura en grados Celcius: "))

def conversor_temp(grados_C):
    grados_f = ((grados_C * (9/5)) + 32)
    return grados_f
print(conversor_temp(grados_C))