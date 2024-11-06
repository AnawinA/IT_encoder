
def xor_encrypt_decrypt(data, key):
    # XOR encryption/decryption
    if key == '':
        key = int(123)
    else:
        key = int(key)
    return ''.join(chr(ord(c) ^ key) for c in data)

