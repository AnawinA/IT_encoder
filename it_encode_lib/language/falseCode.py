def encode_false_ascii(text):
    """Encodes text into FALSE ASCII code."""
    false_code = ""
    for char in text:
        ascii_val = ord(char)
        false_code += f"{ascii_val}a"  # 'a' for output in FALSE
    return false_code


def decode_false_ascii(false_code):
    """Decodes FALSE ASCII code back to text."""
    decoded_text = ""
    index = 0

    while index < len(false_code):
        # Extract the ASCII value
        ascii_val_str = ""
        while index < len(false_code) and false_code[index].isdigit():
            ascii_val_str += false_code[index]
            index += 1
        
        # Convert ASCII value string to a character and add to result
        if ascii_val_str:
            decoded_text += chr(int(ascii_val_str))
        
        # Move to the next command (skip the 'a' command)
        if index < len(false_code) and false_code[index] == 'a':
            index += 1
    
    return decoded_text


def encode_false_binary(text):
    """Encodes text into FALSE Binary code."""
    false_binary_code = ""
    for char in text:
        binary_val = bin(ord(char))[2:]
        binary_val = binary_val.zfill(8)
        false_binary_code += binary_val
    return false_binary_code


def decode_false_binary(false_binary_code):
    """Decodes FALSE Binary code back to text."""
    decoded_text = ""
    for i in range(0, len(false_binary_code), 8):
        byte = false_binary_code[i:i+8]
        decoded_text += chr(int(byte, 2))
    return decoded_text


# Example usage
text = "I want to test it!"
encoded_false_ascii = encode_false_ascii(text)
print("Encoded FALSE ASCII code:", encoded_false_ascii)

decoded_text_ascii = decode_false_ascii(encoded_false_ascii)
print("Decoded text from ASCII:", decoded_text_ascii)  # Should match the original text

encoded_false_binary = encode_false_binary(text)
print("Encoded FALSE Binary code:", encoded_false_binary)

decoded_text_binary = decode_false_binary(encoded_false_binary)
print("Decoded text from Binary:", decoded_text_binary)  # Should match the original text