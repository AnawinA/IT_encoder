from collections import deque

def mov199(text, n, reverse=False):
    """mov199"""
    e = deque(text)
    if reverse:
        n = -n
    e.rotate(n)
    return ''.join(e)

# print(mov199('My name is Anawin', 3, True))
