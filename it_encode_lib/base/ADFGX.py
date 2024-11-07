def preprocess(text):
    return ''.join(filter(str.isalnum, text)).upper()

def columnar_transposition(text, keyword):
    n = len(keyword)
    sorted_key = sorted([(char, i) for i, char in enumerate(keyword)])
    columns = [''] * n
    for i, char in enumerate(text):
        columns[i % n] += char
    return ''.join(columns[i[1]] for i in sorted_key)

def columnar_transposition_decrypt(text, keyword):
    n = len(keyword)
    sorted_key = sorted([(char, i) for i, char in enumerate(keyword)])
    col_lengths = [len(text) // n + (1 if i < len(text) % n else 0) for i in range(n)]
    columns = [''] * n
    start = 0
    for i, (char, idx) in enumerate(sorted_key):
        columns[idx] = text[start:start + col_lengths[i]]
        start += col_lengths[i]
    return ''.join(''.join(row) for row in zip(*columns))

def encode(plaintext, key_square, keyword):
    adfgx = 'ADFGX'
    plaintext = preprocess(plaintext)
    pairs = [key_square[char] for char in plaintext]
    ciphertext = ''.join([adfgx[p[0]] + adfgx[p[1]] for p in pairs])
    return columnar_transposition(ciphertext, keyword)

def decode(ciphertext, key_square_inv, keyword):
    adfgx = 'ADFGX'
    ciphertext = preprocess(ciphertext)
    transposed = columnar_transposition_decrypt(ciphertext, keyword)
    pairs = [(adfgx.index(transposed[i]), adfgx.index(transposed[i+1])) for i in range(0, len(transposed), 2)]
    plaintext = ''.join([key_square_inv[p] for p in pairs])
    return plaintext

def encode_adfgx(text, key):
    if key == '':
        key = 'KEY'
    key_square = {
        'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4),
        'F': (1, 0), 'G': (1, 1), 'H': (1, 2), 'I': (1, 3), 'J': (1, 3), 'K': (1, 4),
        'L': (2, 0), 'M': (2, 1), 'N': (2, 2), 'O': (2, 3), 'P': (2, 4),
        'Q': (3, 0), 'R': (3, 1), 'S': (3, 2), 'T': (3, 3), 'U': (3, 4),
        'V': (4, 0), 'W': (4, 1), 'X': (4, 2), 'Y': (4, 3), 'Z': (4, 4)
    }
    return encode(text, key_square, key)

def decode_adfgx(text, key):
    if key == '':
        key = 'KEY'
    key_square = {
        'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4),
        'F': (1, 0), 'G': (1, 1), 'H': (1, 2), 'I': (1, 3), 'J': (1, 3), 'K': (1, 4),
        'L': (2, 0), 'M': (2, 1), 'N': (2, 2), 'O': (2, 3), 'P': (2, 4),
        'Q': (3, 0), 'R': (3, 1), 'S': (3, 2), 'T': (3, 3), 'U': (3, 4),
        'V': (4, 0), 'W': (4, 1), 'X': (4, 2), 'Y': (4, 3), 'Z': (4, 4)
    }
    key_square_inv = {v: k for k, v in key_square.items()}
    return decode(text, key_square_inv, key)

