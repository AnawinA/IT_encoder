"""is prime"""

def is_prime(n):
    """is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if not n % 2:
        return False
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if not n % i:
            return False
    return True
