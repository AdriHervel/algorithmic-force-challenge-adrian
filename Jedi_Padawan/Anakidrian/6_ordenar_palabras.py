name_Jedis = ["Obi-Wan", "Anakin", "Yoda", "Mace", "Luke"]

def ordenar_names(name_Jedis):
    name = len(name_Jedis)
    for i in range(name):
        for j in range(0, name-i-1):
            if name_Jedis[j] > name_Jedis[j+1]:
                name_Jedis[j], name_Jedis[j+1] = name_Jedis[j+1], name_Jedis[j]
    return name_Jedis
print(f"El orden de los nombres de los caballeros de la orden es el siguiente:", ordenar_names(name_Jedis))
