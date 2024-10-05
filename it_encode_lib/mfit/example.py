"""de code"""
from mfit_ende_matrix import decode_matrix, encode_matrix
import numpy as np

ENCODE_MATRIX = np.array([
    [1, -2, 2],
    [-1, 1, 3],
    [1, -1, -4]
])
def main() -> None:
    """uncode"""
    text = "MEET ME MONDAY"
    encode_text = encode_matrix(text, ENCODE_MATRIX)
    print(text)
    print(encode_text)
    text_d = decode_matrix(encode_text, ENCODE_MATRIX)
    print(text_d)

if __name__ == '__main__':
    main()
