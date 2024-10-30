competition = list(map(int,input("¿Cuáles son los numeros de los mejores jedis? ").split(',')))

def element_max(competition):
    Stronger = 0
    for i in competition:
        if i > Stronger:
            Stronger = i
    return Stronger
print(element_max(competition))
            