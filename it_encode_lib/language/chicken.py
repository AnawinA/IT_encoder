def encode_chicken(text):
    """Encodes text into Chicken code."""
    chicken_code = ""
    for char in text:
        ascii_val = ord(char)
        chicken_code += " ".join(["chicken"] * ascii_val) + "\n"
    return chicken_code


def decode_chicken(chicken_code):
    """Decodes Chicken code back to text."""
    decoded_text = ""
    for line in chicken_code.splitlines():
        chicken_count = line.split().count("chicken")
        decoded_text += chr(chicken_count)
    return decoded_text

