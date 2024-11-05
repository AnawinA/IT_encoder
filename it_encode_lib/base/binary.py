def encode_to_binary(text):
    """Encodes text into binary format."""
    binary_code = ""
    for char in text:
        binary_val = bin(ord(char))[2:]
        binary_val = binary_val.zfill(8)
        binary_code += binary_val + " " 
    return binary_code.strip()


def decode_from_binary(binary_code):
    """Decodes binary code back to text."""
    decoded_text = ""
    binary_values = binary_code.split()
    
    for binary_val in binary_values:
        decoded_text += chr(int(binary_val, 2))
    
    return decoded_text
