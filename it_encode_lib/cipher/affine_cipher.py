def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and 26 must be coprime.")
    return ''.join(chr(((a * (ord(char) - 65) + b) % 26) + 65) if char.isupper() else char for char in text)

def affine_decrypt(encoded_text, a, b):
    a_inv = mod_inverse(a, 26)
    return ''.join(chr((a_inv * ((ord(char) - 65) - b) % 26) + 65) if char.isupper() else char for char in encoded_text)

original_text = "HELLOAFFINE"
a, b = 5, 8  # Example keys
encoded = affine_encrypt(original_text, a, b)
decoded = affine_decrypt(encoded, a, b)

print("Original Text:", original_text)
print("Encoded Text (Affine Cipher):", encoded)
print("Decoded Text:", decoded)