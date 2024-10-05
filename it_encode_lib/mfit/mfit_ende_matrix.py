"""Uncode Message"""
import numpy as np

def to_ord_list(text: str) -> list:
    nu, de = divmod(len(text), 3)
    if len(text) % 3:
        text += " " * (3 - de)
        nu += 1
    text_w = text.replace(" ", "_")
    """uncode"""
    encode_l = []
    for i in text_w.upper():
        if i == "_":
            encode_l.append(0)
        else:
            encode_l.append(ord(i) - 64)
            if not i.isalpha():
                encode_l.append(-1)
    return encode_l

def reshape_3cols(encode_l: list) -> np.ndarray:
    """reshape to 3 columns"""
    return np.array(encode_l).reshape(len(encode_l) // 3 , 3)

def encode_by(encode_l: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """encode by matrix"""
    return np.dot(encode_l, matrix)

def to_chr_text(encode_l: np.ndarray) -> np.ndarray:
    """to character text encode/decode"""
    plane_l = encode_l.flatten()
    return plane_l

def decode_by(encode_l: list, matrix: np.ndarray) -> np.ndarray:
    """decode by"""
    encode_np = np.array(encode_l).reshape(len(encode_l) // 3, 3)
    inverse = np.linalg.inv(matrix)
    return np.array(np.dot(encode_np, inverse), dtype=int)

def ord_to_chr(encode_l: np.ndarray[int]) -> np.ndarray:
    """ord to chr"""
    string_decode = ""
    for i in encode_l.flatten():
        if not 26 > i > 0:
            string_decode += " "
        else:
            string_decode += chr(i + 64)
    return string_decode.strip()

def encode_matrix(text: str, matrix: np.ndarray) -> list:
    """encode matrix"""
    encode_l = to_ord_list(text)
    text_np = reshape_3cols(encode_l)
    text_encode = encode_by(text_np, matrix)
    text_encode_plan = to_chr_text(text_encode)
    return list(text_encode_plan)

def decode_matrix(encode_l: list, matrix: np.ndarray) -> np.ndarray:
    """decode matrix"""
    decode_text = decode_by(encode_l, matrix)
    finish_text = ord_to_chr(decode_text)
    return finish_text



