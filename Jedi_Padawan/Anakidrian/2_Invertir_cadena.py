message_code = "Obi-Wan Kenobi, el plan esta en marcha. \n El pueblo esta enterado y mañana avanzamos. Count Dooku"

def decode_message(message_code):
  message = message_code.split()
  decoded_message = []
  for word in message:
    decoded_message.append(word[::-1])
  return ' '.join(decoded_message)

print(decode_message(message_code))