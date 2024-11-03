
numbers = [12,1, 23, 4, 35, 2, 21, 24, 45, 35, 56, 32, 56, 11]
def suma_num_pars(numbers):
    sum_pars = sum(number for number in numbers if number%2==0)
    return sum_pars
print(f"La suma de los números pares es: ", suma_num_pars(numbers))
