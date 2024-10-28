CheckUp = int(input("Cuál es la medición? "))

def nivel_midiclonarios(CheckUp):
    midiclonarios = 1
    for i in range(1, CheckUp + 1):
        midiclonarios += i
        if midiclonarios <= 100:
            calificacion = "Por lo cual: --> Lo sentimos Anakin, aún no eres Elegido, estás a poco de lograrlo"
        else:
            calificacion = "Por lo cual: --> ¡Felicidades! Anakin, has sido Elegido"
    return midiclonarios, calificacion


print(f"El nivel de midiclonarios de Anakin es de:", nivel_midiclonarios(CheckUp))