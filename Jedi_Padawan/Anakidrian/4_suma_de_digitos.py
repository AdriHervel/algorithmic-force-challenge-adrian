old_number = 5
def decoder_number(old_number):
    decoded = 0
    for i in range(1, old_number + 1):
        decoded += i
    return decoded
print(decoder_number(old_number))