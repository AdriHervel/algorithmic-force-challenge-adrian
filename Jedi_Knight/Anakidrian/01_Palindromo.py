frase = "Anita lava la tina"
def verify_palindroma(frase):
    format_frase = ''.join(frase.split()).lower()
    return format_frase==format_frase[::-1]
print(f"La {frase} Palindróma a verificar es: {verify_palindroma(frase)}")