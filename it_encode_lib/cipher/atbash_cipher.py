def atbash_cipher(text):
    encoded = []
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            # Map letter to its reverse
            encoded.append(chr(offset + (25 - (ord(char) - offset))))
        else:
            encoded.append(char)
    return ''.join(encoded)
