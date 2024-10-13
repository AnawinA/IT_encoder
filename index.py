'''index.py'''
from it_encode_lib.base64.base64 import *
a = str(input())
b = base64_decoder(base64_encoder(a))
print(b)