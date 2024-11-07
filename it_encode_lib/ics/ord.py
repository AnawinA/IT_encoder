
def ord_encode(char):
    """Ordinary"""
    # return ' '.join(map(str, map(ord, char))) # Slower than *memoryview*
    return ' '.join(map(str, memoryview(bytearray(char, 'utf-8'))))

def ord_decode(str_arr: str) -> str:
    """Ordinary"""
    return ''.join(map(chr, map(int, str_arr.split())))

