"""password"""
# import hashlib
# def password(text: str):
#     """password"""
#     word = hashlib.sha512(text.encode('utf-8'))
#     print(word.hexdigest().upper())

# def break_password(word: str):
#     """BreakPassword"""
#     for i in range(0, 100000):
#         tmp = hashlib.sha512(str(i).zfill(5).encode('utf-8')).hexdigest().upper()
#         if tmp == word:
#             print(str(i).zfill(5))
#             break
