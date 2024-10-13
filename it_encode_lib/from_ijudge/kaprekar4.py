"""kaprekar"""

def k_find(num_str):
    """kaprekar"""
    num_l = list(num_str)
    asc = "".join(sorted(num_l))
    desc = "".join(reversed(asc))
    num_calc = int(desc) - int(asc)
    return f"{num_calc:04d}"

def kaprekar(num_str: str):
    """Kaprekar mystery number"""
    num_str = str(num_str)
    count = 0
    inum = num_str
    l = [inum]
    while inum != "6174":
        inum = k_find(inum)
        l.append(inum)
        assert int(inum) % 1111, "impossible"
        count += 1
    return l, count

def kaprekar_n(num_str: str) -> int:
    """Kaprekar mystery number"""
    return kaprekar(num_str)[1]

def kaprekar_list(num_str: str) -> int:
    """Kaprekar mystery number"""
    return kaprekar(num_str)[0]
