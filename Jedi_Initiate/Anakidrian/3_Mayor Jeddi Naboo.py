vel_Obi = 490
vel_Qui = 1123
vel_Anakin = 490

if vel_Obi > vel_Qui and vel_Anakin:
    mas_veloz = "Obi Wan Kenobi"
elif vel_Qui > vel_Anakin and vel_Obi:
    mas_veloz = "Qui-Gon Jinn"
elif vel_Anakin > vel_Obi and vel_Qui:
    mas_veloz = "El jovén Anakin Skywalker"
elif vel_Anakin == vel_Obi or vel_Anakin == vel_Qui:
    mas_veloz = "¡Empate!""
    
else:
    mas_veloz = "¡Hay un EMPATE!"
            
print("El mayor Jedi de Naboo es: ", mas_veloz)
