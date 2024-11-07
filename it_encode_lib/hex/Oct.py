def encode_to_base8(text):
    encoded_text = ' '.join(format(ord(char), 'o') for char in text)
    return encoded_text

def decode_from_base8(encoded_text):
    decoded_text = ''.join(chr(int(octal, 8)) for octal in encoded_text.split())
    return decoded_text

input_text = "Hello, World!"
encoded = encode_to_base8(input_text)
decoded = decode_from_base8(encoded)

print("Original Text:", input_text)
print("Encoded in Base-8:", encoded)
print("Decoded from Base-8:", decoded)
