n = 5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(f"El factorial del {n} es: {factorial(n)}")