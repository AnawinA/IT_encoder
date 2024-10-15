"""Shorten"""

def shorten_num_encode(str_arr: str) -> str:
    """Shorten"""
    arr = map(int, str_arr.replace("[", '').replace("]", '').split(","))
    is_wait = False
    prev = None
    encoded = ""
    for num in arr:
        if not is_wait:
            if prev is None:
                encoded += str(num)
            elif num - prev == 1:
                is_wait = True
            elif num - prev != -1:
                encoded += f', {num}'
        else:
            if num - prev != 1:
                encoded += f'-{prev}, {num}'
                is_wait = False
        prev = num
    if is_wait:
        encoded += f'-{prev}'
    return encoded

def shorten_num_decode(text: str) -> list[int]:
    """Shorten"""
    arr = []
    for num in text.split(','):
        print(num.strip())
        if '-' in num.strip():
            start, end = num.strip().split('-')
            arr.extend(range(int(start), int(end) + 1))
        else:
            arr.append(int(num.strip()))
    return arr
