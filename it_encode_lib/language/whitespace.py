
def whitespace_encode(text):
    """Encodes a given text into whitespace characters."""
    encoded_text = ""
    for char in text:
        binary_representation = f"{ord(char):08b}"
        whitespace_representation = binary_representation.replace("0", " ").replace("1", "\t")
        encoded_text += whitespace_representation + "\n"
    return encoded_text


def whitespace_decode(encoded_text):
    """Decodes whitespace characters back into the original text."""
    decoded_text = ""
    for line in encoded_text.splitlines():
        binary_representation = line.replace(" ", "0").replace("\t", "1")
        decoded_text += chr(int(binary_representation, 2))
    return decoded_text
