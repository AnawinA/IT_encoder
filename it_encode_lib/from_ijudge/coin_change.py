"""coin change"""

def baht_change(baht: int, values=None) -> int:
    """coin change"""
    if values is None:
        values = [1, 2, 5, 10, 20]
    ibaht = int(baht)
    coin = 0
    for value in sorted(values, reverse=True):
        coin += ibaht // value
        ibaht %= value
    return coin
