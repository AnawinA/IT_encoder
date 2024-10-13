"""ArmStrong"""

def armstrong(num: int):
    """ArmStrong"""
    # is 153 3n = 1**3 + 5**3 + 3**3 = 153 
    sem = 0
    for digit in str(num):
        sem += int(digit) ** len(str(num))
    return num == sem

