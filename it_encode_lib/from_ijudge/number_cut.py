"""Number Factory"""

def number_cut_encode(num: str) -> list[int]:
    """Number Factory"""
    i_number = int(num)
    cut = 10
    l = []
    while i_number > 0:
        cut_number = i_number % cut
        if cut_number:
            l.append(cut_number)
        i_number -= cut_number
        cut *= 10
    return l

def number_cut_decode(str_arr: str) -> int:
    """Number Factory"""
    arr = map(int, str_arr.replace("[", '').replace("]", '').split(","))
    return sum(arr)
