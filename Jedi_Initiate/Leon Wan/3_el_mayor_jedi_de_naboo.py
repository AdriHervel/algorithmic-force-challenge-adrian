
"""
3. El mayor Jedi de Naboo (Máximo de tres números)
Contexto temático: 
Obi-Wan Kenobi, Qui-Gon Jinn y el joven Anakin Skywalker están compitiendo en una carrera en Naboo. Solo uno de ellos alcanzará la mayor velocidad en sus naves. Encuentra al más rápido.

Objetivo:
Dado tres números, encuentra el mayor de ellos.

Instrucciones:
- La función debe recibir tres números y devolver el mayor de los tres.
- No utilices funciones incorporadas como `max()`.

Pista: 
Compara los números dos a dos para encontrar el mayor.
"""

nums = [15, 20, 25]
"""


if nums[0] >= nums[1] and nums[0] >= nums[2]: 
    print(nums[0])
elif nums[1] >= nums[2]:
        print(nums[1])
else:
        print(nums[2])    

        """


for num in nums: 
    # print("num", num)
    for i in nums: 
        if num < i:
            break
        else: 
            print(num)
            
            
            



