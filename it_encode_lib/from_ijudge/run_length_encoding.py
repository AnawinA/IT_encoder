"""Run Length Encoding"""

def run_length_encode(text: str) -> str:
    """Run Length Encoding"""
    current_text = text[0]
    current_text_count = 0
    text_encoded = ""

    for i in text:
        if i == current_text:
            current_text_count += 1
        else:
            text_encoded += f"{current_text_count}{current_text}"
            current_text = i
            current_text_count = 1
    text_encoded += f"{current_text_count}{current_text}"
    return text_encoded

def run_length_decode(text_encoded: str) -> str:
    """Run Length Decoding"""
    text = ""
    current_count = ""
    for i in text_encoded:
        if i.isnumeric():
            current_count += i
        else:
            text += i * int(current_count)
            current_count = ""
    return text
