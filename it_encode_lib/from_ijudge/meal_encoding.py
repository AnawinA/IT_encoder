"""Meal encoding"""

def meal_encode(text: str) -> str:
    """Meal encoding"""
    first = text[1::2]
    last = text[::2]
    return first + last

def meal_decode(text: str) -> str:
    """Meal decoding"""
    middle_str = len(text) // 2
    t1, t2 = text[:middle_str], text[middle_str:]
    clean_text = ""
    for i, v in enumerate(t1):
        clean_text += t2[i] + v
    if len(t2) > len(t1):
        clean_text += t2[-1]
    return clean_text
