word1 = "amor"
word2= "roma"

def anagrama(word1, word2):
    if word1.lower() == word2.lower():
        return False
    return sorted(word1.lower()) == sorted(word2.lower())

print(anagrama(word1, word2))
