"""Caesar shift"""

def shift(char, n):
    """shift"""
    if not char.isalpha():
        return char
    cp = chr((ord(char) - 97 + n) % 26 + 97)
    return cp

def caesar_cipher(text: str, n: int) -> tuple[str, str]:
    """Caesar shift"""
    return ("".join(shift(char, n) for char in text),
"".join(shift(char, -n) for char in text))
