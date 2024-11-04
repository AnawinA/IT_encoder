"""Ejudge"""

def de_roman(roman):
    """Roman"""
    romanvalue = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    for i, j in enumerate(roman):
        if i == len(roman)-1:
            ans += romanvalue[j]
        elif romanvalue[j] >= romanvalue[roman[i+1]]:
            ans += romanvalue[j]
        else:
            ans -= romanvalue[j]
    return ans

def en_roman(num):
    """Convert an integer to a Roman numeral."""
    num = int(num)
    roman_numerals = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV",
        1: "I"
    }
    result = ""
    for value in sorted(roman_numerals.keys(), reverse=True):
        while num >= value:
            result += roman_numerals[value]
            num -= value
    return result
