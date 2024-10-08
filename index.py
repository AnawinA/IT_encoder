'''index.py'''
from it_encode_lib.base64.base64 import base64_encoder
x = str(input())
t = base64_encoder(x)
print(t)