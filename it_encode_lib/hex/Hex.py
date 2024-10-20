"""HexEncoder/decoder"""
def hex_encode(text):
    """encoderHex"""
    encode_text = text.encode("utf-8").hex()
    return encode_text

def hex_decode(text_encoded):
    """decodeHex"""
    decode_text = bytes.fromhex(text_encoded).decode('utf-8')
    return decode_text

