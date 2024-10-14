from  it_encode_lib.base64.base64 import base64_decoder, base64_encoder
def base64(text, is_decode):
    if is_decode:
        return base64_decoder(text)
    return base64_encoder(text)

from it_encode_lib.from_ijudge import caesar_cipher, meal_encoding, run_length_encoding
def caesar(text, is_decode):
    if is_decode:
        return caesar_cipher.caesar_cipher(text, -5)
    return caesar_cipher.caesar_cipher(text, 5)

def meal(text, is_decode):
    if is_decode:
        return meal_encoding.meal_decode(text)
    return meal_encoding.meal_encode(text)