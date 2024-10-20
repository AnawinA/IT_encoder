#!/usr/bin/env python

# from collections import deque

# def mov199(text, n, reverse=False):
#     """mov199"""
#     e = deque(text)
#     if reverse:
#         n = -n
#     e.rotate(n)
#     return ''.join(e)

# for i in range(100):
#     print(mov199('My name is Anawin', i, False))


# a = []
# while b != 0:
#     b = float(input())
#     a.append(b)
# b.sort()
# for i in range(len(b),0,-1):
#     print(i)

'''base32 encoder and decoder basic code no bugs'''
def base32_encoder(plain_txt):
    '''input text output base32'''
    enc_txt = ""
    base32_char = {
      '00000': 'A', '00001': 'B', '00010': 'C', '00011': 'D',
      '00100': 'E', '00101': 'F', '00110': 'G', '00111': 'H',
      '01000': 'I', '01001': 'J', '01010': 'K', '01011': 'L',
      '01100': 'M', '01101': 'N', '01110': 'O', '01111': 'P',
      '10000': 'Q', '10001': 'R', '10010': 'S', '10011': 'T',
      '10100': 'U', '10101': 'V', '10110': 'W', '10111': 'X',
      '11000': 'Y', '11001': 'Z', '11010': '2', '11011': '3',
      '11100': '4', '11101': '5', '11110': '6', '11111': '7'
    }
    bin_txt = ''.join(format(ord(i), '08b') for i in plain_txt)
    if (len(bin_txt))%5:
        bin_txt += "0"*(5-(len(bin_txt) % 5)) 
    for i in range(0,len(bin_txt),5):
        enc_txt += (base32_char[bin_txt[i:i+5]])
    if len(enc_txt) %8:
        enc_txt += "="*(8-(len(enc_txt)%8))
    return enc_txt

def base32_decoder(plain_txt):
    '''input base32 output text'''
    plain_txt = plain_txt.strip('=')
    dec_txt = ""
    dec_bin = ""
    base32_char = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011',
    'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111',
    'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011',
    'M': '01100', 'N': '01101', 'O': '01110', 'P': '01111',
    'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011',
    'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111',
    'Y': '11000', 'Z': '11001', '2': '11010', '3': '11011',
    '4': '11100', '5': '11101', '6': '11110', '7': '11111'
    }
    for i in plain_txt:
        dec_bin += base32_char[i]
    dec_len = len(dec_bin)
    for i in range(int(dec_len/8)):
        dec_txt += (chr(int(dec_bin[i*8:((i+1)*8)], 2)))
    return dec_txt

'''base64 encoder and decoder basic code no bugs'''
def base64_encoder(plain_txt):
    '''input text output base64'''
    enc_txt = ""
    base64_char = {
      '000000': 'A', '000001': 'B', '000010': 'C', '000011': 'D',
      '000100': 'E', '000101': 'F', '000110': 'G', '000111': 'H',
      '001000': 'I', '001001': 'J', '001010': 'K', '001011': 'L',
      '001100': 'M', '001101': 'N', '001110': 'O', '001111': 'P',
      '010000': 'Q', '010001': 'R', '010010': 'S', '010011': 'T',
      '010100': 'U', '010101': 'V', '010110': 'W', '010111': 'X',
      '011000': 'Y', '011001': 'Z', '011010': 'a', '011011': 'b',
      '011100': 'c', '011101': 'd', '011110': 'e', '011111': 'f',
      '100000': 'g', '100001': 'h', '100010': 'i', '100011': 'j',
      '100100': 'k', '100101': 'l', '100110': 'm', '100111': 'n',
      '101000': 'o', '101001': 'p', '101010': 'q', '101011': 'r',
      '101100': 's', '101101': 't', '101110': 'u', '101111': 'v',
      '110000': 'w', '110001': 'x', '110010': 'y', '110011': 'z',
      '110100': '0', '110101': '1', '110110': '2', '110111': '3',
      '111000': '4', '111001': '5', '111010': '6', '111011': '7',
      '111100': '8', '111101': '9', '111110': '+', '111111': '/'
    }
    bin_txt = ''.join(format(ord(i), '08b') for i in plain_txt)
    if (len(bin_txt))%6:
        bin_txt += "0"*(6-(len(bin_txt) % 6)) 
    for i in range(0,len(bin_txt),6):
        enc_txt += (base64_char[bin_txt[i:i+6]])
    if len(enc_txt) %4:
        enc_txt += "="*(4-(len(enc_txt)%4))
    return enc_txt

def base64_decoder(plain_txt):
    '''input base64 output text'''
    plain_txt = plain_txt.strip('=')
    dec_txt = ""
    dec_bin = ""
    base64_char = {
      'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011',
      'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111',
      'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011',
      'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111',
      'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011',
      'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111',
      'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011',
      'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111',
      'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011',
      'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111',
      'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011',
      's': '101100', 't': '101101', 'u': '101110', 'v': '101111',
      'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011',
      '0': '110100', '1': '110101', '2': '110110', '3': '110111',
      '4': '111000', '5': '111001', '6': '111010', '7': '111011',
      '8': '111100', '9': '111101', '+': '111110', '/': '111111'
    }
    for i in plain_txt:
        dec_bin += base64_char[i]
    dec_len = len(dec_bin)
    for i in range(int(dec_len/8)):
        dec_txt += (chr(int(dec_bin[i*8:((i+1)*8)], 2)))
    return dec_txt



# """Sha-1"""
# import hashlib
# def generate_sha1(input_string):
#     """Sha-1 hashing algorithm"""
#     encoded_string = input_string.encode('utf-8')
    
#     sha1_hash = hashlib.sha1()
    
#     sha1_hash.update(encoded_string)
    
#     return sha1_hash.hexdigest()

# input_string = "Hello, World!"
# hash_result = generate_sha1(input_string)
# print(f"SHA-1 hash of '{input_string}': {hash_result}")

# """Sha-2 Family"""
# import hashlib
# def generate_sha224(input_string):
#     """Sha-224 hashing algorithm"""
#     encoded_string = input_string.encode('utf-8')
    
#     sha224_hash = hashlib.sha224()
    
#     sha224_hash.update(encoded_string)

#     return sha224_hash.hexdigest()

# input_string = "Hello, World!"
# hash_result = generate_sha224(input_string)
# print(f"SHA-224 hash of '{input_string}': {hash_result}")

# import hashlib
# def generate_sha256(input_string):
#     """Sha-256 hashing algorithm"""
#     encoded_string = input_string.encode('utf-8')

#     sha256_hash = hashlib.sha256()

#     sha256_hash.update(encoded_string)
    
#     return sha256_hash.hexdigest()

# input_string = "Hello, World!"
# hash_result = generate_sha256(input_string)
# print(f"SHA-256 hash of '{input_string}': {hash_result}")

# import hashlib
# def generate_sha384(input_string):
#     """Sha-384 hashing algorithm"""
#     encoded_string = input_string.encode('utf-8')

#     sha384_hash = hashlib.sha384()
    
#     sha384_hash.update(encoded_string)
    
#     return sha384_hash.hexdigest()

# input_string = "Hello, World!"
# hash_result = generate_sha384(input_string)
# print(f"SHA-384 hash of '{input_string}': {hash_result}")

# import hashlib
# def generate_sha512(input_string):
#     """Sha-512 hashing algorithm"""
#     encoded_string = input_string.encode('utf-8')

#     sha512_hash = hashlib.sha512()

#     sha512_hash.update(encoded_string)
    
#     return sha512_hash.hexdigest()

# input_string = "Hello, World!"
# hash_result = generate_sha512(input_string)
# print(f"SHA-512 hash of '{input_string}': {hash_result}")


"""Caesar shift"""

def shift(char, n):
    """shift"""
    if not char.isalpha():
        return char
    cp = chr((ord(char) - 97 + n) % 26 + 97)
    return cp

def caesar_cipher(text: str, n: int) -> tuple[str, str]:
    """Caesar shift"""
    return ("".join(shift(char, n) for char in text),
"".join(shift(char, -n) for char in text))


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


"""Meal encoding"""

def meal_encode(text: str) -> str:
    """Meal encoding"""
    first = text[1::2]
    last = text[::2]
    return first + last

def meal_decode(text: str) -> str:
    """Meal decoding"""
    middle_str = len(text) // 2
    t1, t2 = text[:middle_str], text[middle_str:]
    clean_text = ""
    for i, v in enumerate(t1):
        clean_text += t2[i] + v
    if len(t2) > len(t1):
        clean_text += t2[-1]
    return clean_text


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


"""password"""
# import hashlib
# def password(text: str):
#     """password"""
#     word = hashlib.sha512(text.encode('utf-8'))
#     print(word.hexdigest().upper())

# def break_password(word: str):
#     """BreakPassword"""
#     for i in range(0, 100000):
#         tmp = hashlib.sha512(str(i).zfill(5).encode('utf-8')).hexdigest().upper()
#         if tmp == word:
#             print(str(i).zfill(5))
#             break


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
        if i.isdigit():
            current_count += i
        else:
            text += i * int(current_count)
            current_count = ""
    return text


"""Shorten"""

def shorten_num_encode(str_arr: str) -> str:
    """Shorten"""
    arr = map(int, str_arr.replace("[", '').replace("]", '').split(","))
    is_wait = False
    prev = None
    encoded = ""
    for num in arr:
        if not is_wait:
            if prev is None:
                encoded += str(num)
            elif num - prev == 1:
                is_wait = True
            elif num - prev != -1:
                encoded += f', {num}'
        else:
            if num - prev != 1:
                encoded += f'-{prev}, {num}'
                is_wait = False
        prev = num
    if is_wait:
        encoded += f'-{prev}'
    return encoded

def shorten_num_decode(text: str) -> list[int]:
    """Shorten"""
    arr = []
    for num in text.split(','):
        print(num.strip())
        if '-' in num.strip():
            start, end = num.strip().split('-')
            arr.extend(range(int(start), int(end) + 1))
        else:
            arr.append(int(num.strip()))
    return arr


"""Temperature"""

def c_to_f(c):
    """Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def c_to_k(c):
    """Celsius to Kelvin"""
    return c + 273.15

def c_to_r(c):
    """Celsius to Rankine"""
    return (c * 9/5) + 491.67

def all_to_c(x, type_in):
    """All to Celsius"""
    expression = 0
    if type_in == "F":
        expression = (x - 32) * 5/9
    elif type_in == "K":
        expression = x - 273.15
    elif type_in == "R":
        expression = (x - 491.67) * 5/9
    return expression

def temperature(temp: float, type_temp="C", to_type="F"):
    """Temperature"""
    type_temp = type_temp.strip().upper()
    to_type = to_type.strip().upper()
    c_temp = temp
    if type_temp != "C":
        c_temp = all_to_c(temp, type_temp)
    new_temp = c_temp
    if to_type == "F":
        new_temp = c_to_f(c_temp)
    elif to_type == "K":
        new_temp = c_to_k(c_temp)
    elif to_type == "R":
        new_temp = c_to_r(c_temp)
    return new_temp


"""HexEncoder/decoder"""
def hex_encode(text):
    """encoderHex"""
    encode_text = text.encode("utf-8").hex()
    return encode_text

def hex_decode(text_encoded):
    """decodeHex"""
    decode_text = bytes.fromhex(text_encoded).decode('utf-8')
    return decode_text











'''input ip address and subnet mask output network id'''
def networkid(address,subnet):
    '''input address [255, 082, 255, 000] subnet [252, 127, 063, 006] list[4][3] '''
    address = address.replace("[", '').replace("]", '').split(",")
    subnet = subnet.replace("[", '').replace("]", '').split(",")
    netid = []
    for i in range(4):
        atemp = ""
        stemp = ""
        kaddress = int(address[i])
        ksubnet = int(subnet[i])
        atmp = bin(kaddress).replace("0b","")
        stmp = bin(ksubnet).replace("0b","")
        atemp = "0"*(8-len(atmp))+atmp
        stemp = "0"*(8-len(stmp))+stmp
        addsub = [int(i) and int(j) for (i, j) in zip(atemp, stemp)]
        astemp = ""
        for i in addsub:
            astemp += str(i)
        netid.append(int(astemp,2))
    return netid

# '''pep8borntojudge'''
# import random
# def main():
#     '''pep9'''
#     error=24
#     score=41
#     while score <=72 :
#         proba=random.randint(100,999)
#         print(f"{score}.) {proba} * 999 = ")
        
#         answer_user=int(input("your answer : "))
#         if answer_user != proba * 999 :
#             error-=1
#             print("wrong answer, heart = ",error,", score = ", score)
#         else:
#             score+=1
#             print("correct answer, heart = ",error, ", score = ", score)
#         print("game over")
    
#         score += 1
# main()


# '''pep8borntojudge'''
# import random
# def main():
#     '''pep9'''
#     print("Welcome \n1. +\n2. -\n3. *\n4. /")
#     var=""
#     error="0"
#     while error=="0":
#         mode_program=str(input("Please Select : "))
#         if mode_program=="1":
#             var ="+"
#             error="1"
#         elif mode_program=="2":
#             var ="-"
#             error="1"
#         elif mode_program=="3":
#             var ="x"
#             error="1"
#         elif mode_program=="4":
#             var ="/"
#             error="1"
#         else:
#             error="0"
#             print("invalid key Try again . . .")
#     minimum_number=int(input("minimum : "))
#     maximum_number=int(input("maximum : "))
#     prob_length=int(input("number ex.0-100 : "))
#     for i in range(1,prob_length+1):
#         proba=random.randint(minimum_number,maximum_number)
#         probb=random.randint(minimum_number,maximum_number)
#         print(f"{i}.) {proba} {var} {probb} = ")
# main()


# '''pep8'''
# import random
# def main():
#     '''fwedscx'''
#     a = random.randint(0,19)
#     b = random.randint(0,29)
#     c = random.randint(10,29)
#     d = random.randint(10,19)
#     num = 1
#     heart = 5
#     score = 0
#     while heart>0:
#         a = random.randint(0,9)
#         b = random.randint(0,9)
#         c = random.randint(0,9)
#         d = random.randint(0,9)
#         print("\n\n-------------score =",score,"-------- heart =",heart,"-----------------")
#         print(f"{num}.) {a} + {b} + {c} + {d} = ")
#         x = int(input())
#         if x != a+b+c+d:
#             heart -= 1
#             if score >= 0.25:
#                 score -= 0.25
#             print("incorrect")
#         else:
#             score += 1
#             print("correct")
#         num += 1
#     print("Game Over your score is",score)
# main()


'''all text to uppercase'''
def lowercase(plaintext):
    return plaintext.lower()

'''all text to uppercase'''
def uppercase(plaintext):
    return plaintext.upper()

"""ArmStrong"""

def armstrong(num: int):
    """ArmStrong"""
    # is 153 3n = 1**3 + 5**3 + 3**3 = 153 
    sem = 0
    for digit in str(num):
        sem += int(digit) ** len(str(num))
    return num == sem



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


"""is sorted"""

def is_sorted(x):
    """is sorted"""
    return x == sorted(x)


