
def vigenere(text, key, encode=True):
    if key == '':
        key = 'KEY'
    encoded = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shift = ord(key[i % key_length].upper()) - 65
            shift = shift if encode else -shift
            encoded.append(chr((ord(char) + shift - offset) % 26 + offset))
        else:
            encoded.append(char)
    return ''.join(encoded)

def vigenere_cipher(text, key):
    return vigenere(text, key, encode=True)

def vigenere_decipher(text, key):
    return vigenere(text, key, encode=False)

