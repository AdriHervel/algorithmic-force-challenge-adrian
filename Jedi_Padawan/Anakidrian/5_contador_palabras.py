text = input("Escribe el mensaje del texto del maesro Yoda: ").split(" ")
def count_words(text):
    len_words = 0
    for word in text:
        word = 1
        len_words += word
    return len_words
print(count_words(text))