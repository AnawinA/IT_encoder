
def caesar_cipher(text, shift):
    if shift == '':
        shift = int(5)
    else:
        shift = int(shift)
    encoded = []
    for char in text:
        if char.isalpha():
            # Shift within alphabet bounds
            offset = 65 if char.isupper() else 97
            encoded.append(chr((ord(char) + shift - offset) % 26 + offset))
        else:
            encoded.append(char)
    return ''.join(encoded)

def caesar_decipher(encoded_text, shift):
    return caesar_cipher(encoded_text, "-" + shift)
