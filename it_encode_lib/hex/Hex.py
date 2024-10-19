"""HexEncoder"""
def encode():
    """encoderHex"""
    text = str(input("encode: "))
    encode_text = text.encode("utf-8").hex()
    print(encode_text)
encode()
def decode():
    """decodeHex"""
    text = str(input("decode: "))
    decode_text = bytes.fromhex(text).decode('utf-8')
    print(decode_text)
decode()
