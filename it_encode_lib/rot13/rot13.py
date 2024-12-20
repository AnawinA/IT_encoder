"""rot13Encode"""
def rot13_encode(text):
    """text to rot13"""
    rot13 = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    )
    return text.translate(rot13)
"""rot13Decode"""
def rot13_decode(text):
    """rot13 to text"""
    textrot = str.maketrans(
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    )
    return text.translate(textrot)

print(rot13_encode("hello"))