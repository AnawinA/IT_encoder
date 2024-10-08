"""Number Factory"""

def number_cut_encode(num: int) -> list[int]:
    """Number Factory"""
    i_number = num
    cut = 10
    l = []
    while i_number > 0:
        cut_number = i_number % cut
        if cut_number:
            l.append(cut_number)
        i_number -= cut_number
        cut *= 10
    return l

def number_cut_decode(arr: list[int]) -> int:
    """Number Factory"""
    return sum(arr)
