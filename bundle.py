#!/usr/bin/env python

# a = []
# while b != 0:
#     b = float(input())
#     a.append(b)
# b.sort()
# for i in range(len(b),0,-1):
#     # print(i)

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

def encode_to_binary(text):
    """Encodes text into binary format."""
    binary_code = ""
    for char in text:
        binary_val = bin(ord(char))[2:]
        binary_val = binary_val.zfill(8)
        binary_code += binary_val + " " 
    return binary_code.strip()


def decode_from_binary(binary_code):
    """Decodes binary code back to text."""
    decoded_text = ""
    binary_values = binary_code.split()
    
    for binary_val in binary_values:
        decoded_text += chr(int(binary_val, 2))
    
    return decoded_text




"""Sha-1 and Sha-224 Hashing Algorithms"""

class SHA1:
    """SHA-1 hashing algorithm implementation"""
    def __init__(self):
        self.h0 = 0x67452301
        self.h1 = 0xEFCDAB89
        self.h2 = 0x98BADCFE
        self.h3 = 0x10325476
        self.h4 = 0xC3D2E1F0

    def update(self, message):
        """Update the hash object with the bytes-like object"""
        message = bytearray(message)
        orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
        message.append(0x80)
        while len(message) % 64 != 56:
            message.append(0)
        message += orig_len_in_bits.to_bytes(8, byteorder='big')
        for chunk in range(0, len(message), 64):
            w = [0] * 80
            for i in range(16):
                w[i] = int.from_bytes(message[chunk + i * 4:chunk + i * 4 + 4], byteorder='big')
            for i in range(16, 80):
                w[i] = self._left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1)
            a, b, c, d, e = self.h0, self.h1, self.h2, self.h3, self.h4
            for i in range(80):
                if 0 <= i <= 19:
                    f = (b & c) | (~b & d)
                    k = 0x5A827999
                elif 20 <= i <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i <= 79:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                temp = self._left_rotate(a, 5) + f + e + k + w[i] & 0xffffffff
                e = d
                d = c
                c = self._left_rotate(b, 30)
                b = a
                a = temp
            self.h0 = (self.h0 + a) & 0xffffffff
            self.h1 = (self.h1 + b) & 0xffffffff
            self.h2 = (self.h2 + c) & 0xffffffff
            self.h3 = (self.h3 + d) & 0xffffffff
            self.h4 = (self.h4 + e) & 0xffffffff

    def hexdigest(self):
        """Return the digest of the data passed to the update() method so far"""
        return ''.join(f'{value:08x}' for value in (self.h0, self.h1, self.h2, self.h3, self.h4))

    @staticmethod
    def _left_rotate(value, shift):
        """Left rotate a 32-bit integer value by shift bits"""
        return ((value << shift) & 0xffffffff) | (value >> (32 - shift))


class SHA224:
    """SHA-224 hashing algorithm implementation"""
    def __init__(self):
        self.h = [
            0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939,
            0xffc00b31, 0x68581511, 0x64f98fa7, 0xbefa4fa4
        ]

    def update(self, message):
        """Update the hash object with the bytes-like object"""
        message = bytearray(message)
        orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
        message.append(0x80)
        while len(message) % 64 != 56:
            message.append(0)
        message += orig_len_in_bits.to_bytes(8, byteorder='big')
        for chunk in range(0, len(message), 64):
            w = [0] * 64
            for i in range(16):
                w[i] = int.from_bytes(message[chunk + i * 4:chunk + i * 4 + 4], byteorder='big')
            for i in range(16, 64):
                s0 = self._right_rotate(w[i - 15], 7) ^ self._right_rotate(w[i - 15], 18) ^ (w[i - 15] >> 3)
                s1 = self._right_rotate(w[i - 2], 17) ^ self._right_rotate(w[i - 2], 19) ^ (w[i - 2] >> 10)
                w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xffffffff
            a, b, c, d, e, f, g, h = self.h
            for i in range(64):
                s1 = self._right_rotate(e, 6) ^ self._right_rotate(e, 11) ^ self._right_rotate(e, 25)
                ch = (e & f) ^ (~e & g)
                temp1 = h + s1 + ch + self._k[i] + w[i]
                s0 = self._right_rotate(a, 2) ^ self._right_rotate(a, 13) ^ self._right_rotate(a, 22)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = s0 + maj
                h = g
                g = f
                f = e
                e = (d + temp1) & 0xffffffff
                d = c
                c = b
                b = a
                a = (temp1 + temp2) & 0xffffffff
            self.h = [(x + y) & 0xffffffff for x, y in zip(self.h, [a, b, c, d, e, f, g, h])]

    def hexdigest(self):
        """Return the digest of the data passed to the update() method so far"""
        return ''.join(f'{value:08x}' for value in self.h[:7])

    @staticmethod
    def _right_rotate(value, shift):
        """Right rotate a 32-bit integer value by shift bits"""
        return (value >> shift) | ((value << (32 - shift)) & 0xffffffff)

    _k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

def generate_sha1(input_string):
    """Generate SHA-1 hash"""
    sha1 = SHA1()
    sha1.update(input_string.encode('utf-8'))
    return sha1.hexdigest()

def generate_sha224(input_string):
    """Generate SHA-224 hash"""
    sha224 = SHA224()
    sha224.update(input_string.encode('utf-8'))
    return sha224.hexdigest()

if __name__ == "__main__":
    input_string = "Hello, World!"
    sha1_result = generate_sha1(input_string)
    sha224_result = generate_sha224(input_string)
    # print(f"SHA-1 hash of '{input_string}': {sha1_result}")
    # print(f"SHA-224 hash of '{input_string}': {sha224_result}")



def encode_utf8(text):
    """Encodes a string into bytes using UTF-8 encoding."""
    try:
        return str(text.encode('utf-8')).replace('b', '').strip("'")
    except UnicodeEncodeError as e:
        return f"Error encoding string to UTF-8: {e}"

def decode_utf8(byte_data):
    """Decodes bytes back into a string using UTF-8 encoding."""
    try:
        return str.encode(byte_data).decode('utf-8')
    except UnicodeDecodeError as e:
        return f"Error decoding bytes from UTF-8: {e}"

def encode_ascii(text):
    """Encodes a string into bytes using ASCII encoding."""
    try:
        return text.encode('ascii')
    except UnicodeEncodeError as e:
        return f"Error encoding string to ASCII: {e}"

def decode_ascii(byte_data):
    """Decodes bytes back into a string using ASCII encoding."""
    try:
        return byte_data.decode('ascii')
    except UnicodeDecodeError as e:
        return f"Error decoding bytes from ASCII: {e}"

def encode_utf16(text):
    """Encodes a string into bytes using UTF-16 encoding."""
    try:
        return text.encode('utf-16')
    except UnicodeEncodeError as e:
        return f"Error encoding string to UTF-16: {e}"

def decode_utf16(byte_data):
    """Decodes bytes back into a string using UTF-16 encoding."""
    try:
        return byte_data.decode('utf-16')
    except UnicodeDecodeError as e:
        return f"Error decoding bytes from UTF-16: {e}"

def encode_iso_8859_1(text):
    """Encodes a string into bytes using ISO-8859-1 encoding."""
    try:
        return text.encode('iso-8859-1')
    except UnicodeEncodeError as e:
        return f"Error encoding string to ISO-8859-1: {e}"

def decode_iso_8859_1(byte_data):
    """Decodes bytes back into a string using ISO-8859-1 encoding."""
    try:
        return byte_data.decode('iso-8859-1')
    except UnicodeDecodeError as e:
        return f"Error decoding bytes from ISO-8859-1: {e}"



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
        # print(num.strip())
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

def temperature(temp: float, type_="CF"):
    """Temperature"""
    if type_ == "":
        type_ = "CF"
    type_ = type_.strip().upper()
    type_temp, to_type = type_[0], type_[1]
    c_temp = float(temp)
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





'''change nandgate to othergate'''
def main():
    '''nnn'''
    x = str(input())





'''parity bits'''
def parity_even_bit(data):
    '''evenbit'''
    dat = str(data)
    sum_dat = 0
    for i in dat:
        sum_dat += int(i)
    if not sum_dat %2:
        dat += "0"
    else:
        dat += "1"
    return dat

def parity_dff_bit(data):
    '''odd bit'''
    dat = str(data)
    sum_dat = 0
    for i in dat:
        sum_dat += int(i)
    if not sum_dat %2:
        dat += "1"
    else:
        dat += "0"
    return dat


def url_encode(url):
    encoded_url = ""
    for char in url:
        if char.isalnum() or char in ('-', '_', '.', '~'):
            encoded_url += char
        else:
            encoded_url += '%' + format(ord(char), '02X')
    return encoded_url

def url_decode(encoded_url):
    decoded_url = ""
    i = 0
    while i < len(encoded_url):
        if encoded_url[i] == '%' and i + 2 < len(encoded_url):
            hex_value = encoded_url[i + 1:i + 3]
            decoded_url += chr(int(hex_value, 16))
            i += 3
        else:
            decoded_url += encoded_url[i]
            i += 1
    return decoded_url



'''input ip address and subnet mask output network id'''
def networkid(address, subnet):
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
# # print(networkid([161,246,38,35],[255,255,0,128]))



def encode_brainfk(text):
    """Encodes text into more optimized Brainfuck code using loops."""
    brainfuck_code = ""

    for char in text:
        ascii_val = ord(char)
        multiplier = ascii_val // 10
        remainder = ascii_val % 10
        if multiplier > 0:
            brainfuck_code += "+" * multiplier + "[>++++++++++<-]>"
        brainfuck_code += "+" * remainder + "."
        brainfuck_code += "[-]\n"
    return brainfuck_code


def decode_brainfk(brainfuck_code):
    """Decodes Brainfuck code back to text by interpreting it."""
    cells = [0] * 30
    pointer = 0
    output = ""
    code_ptr = 0

    while code_ptr < len(brainfuck_code):
        command = brainfuck_code[code_ptr]
        if command == "+":
            cells[pointer] = (cells[pointer] + 1) % 256
        elif command == "-":
            cells[pointer] = (cells[pointer] - 1) % 256
        elif command == ">":
            pointer += 1
        elif command == "<":
            pointer -= 1
        elif command == ".":
            output += chr(cells[pointer])
        elif command == "[":
            if cells[pointer] == 0:
                open_loops = 1
                while open_loops != 0:
                    code_ptr += 1
                    if brainfuck_code[code_ptr] == "[":
                        open_loops += 1
                    elif brainfuck_code[code_ptr] == "]":
                        open_loops -= 1
        elif command == "]":
            if cells[pointer] != 0:
                close_loops = 1
                while close_loops != 0:
                    code_ptr -= 1
                    if brainfuck_code[code_ptr] == "[":
                        close_loops -= 1
                    elif brainfuck_code[code_ptr] == "]":
                        close_loops += 1
        code_ptr += 1
    return output



def encode_chicken(text):
    """Encodes text into Chicken code."""
    chicken_code = ""
    for char in text:
        ascii_val = ord(char)
        chicken_code += " ".join(["chicken"] * ascii_val) + "\n"
    return chicken_code


def decode_chicken(chicken_code):
    """Decodes Chicken code back to text."""
    decoded_text = ""
    for line in chicken_code.splitlines():
        chicken_count = line.split().count("chicken")
        decoded_text += chr(chicken_count)
    return decoded_text



def encode_false_ascii(text):
    """Encodes text into FALSE ASCII code."""
    false_code = ""
    for char in text:
        ascii_val = ord(char)
        false_code += f"{ascii_val}a"  # 'a' for output in FALSE
    return false_code


def decode_false_ascii(false_code):
    """Decodes FALSE ASCII code back to text."""
    decoded_text = ""
    index = 0

    while index < len(false_code):
        # Extract the ASCII value
        ascii_val_str = ""
        while index < len(false_code) and false_code[index].isdigit():
            ascii_val_str += false_code[index]
            index += 1
        
        # Convert ASCII value string to a character and add to result
        if ascii_val_str:
            decoded_text += chr(int(ascii_val_str))
        
        # Move to the next command (skip the 'a' command)
        if index < len(false_code) and false_code[index] == 'a':
            index += 1
    
    return decoded_text


def encode_false_binary(text):
    """Encodes text into FALSE Binary code."""
    false_binary_code = ""
    for char in text:
        binary_val = bin(ord(char))[2:]
        binary_val = binary_val.zfill(8)
        false_binary_code += binary_val
    return false_binary_code


def decode_false_binary(false_binary_code):
    """Decodes FALSE Binary code back to text."""
    decoded_text = ""
    for i in range(0, len(false_binary_code), 8):
        byte = false_binary_code[i:i+8]
        decoded_text += chr(int(byte, 2))
    return decoded_text


# Example usage
text = "I want to test it!"
encoded_false_ascii = encode_false_ascii(text)
# print("Encoded FALSE ASCII code:", encoded_false_ascii)

decoded_text_ascii = decode_false_ascii(encoded_false_ascii)
# print("Decoded text from ASCII:", decoded_text_ascii)  # Should match the original text

encoded_false_binary = encode_false_binary(text)
# print("Encoded FALSE Binary code:", encoded_false_binary)

decoded_text_binary = decode_false_binary(encoded_false_binary)
# print("Decoded text from Binary:", decoded_text_binary)  # Should match the original text


def whitespace_encode(text):
    """Encodes a given text into whitespace characters."""
    encoded_text = ""
    for char in text:
        binary_representation = f"{ord(char):08b}"
        whitespace_representation = binary_representation.replace("0", " ").replace("1", "\t")
        encoded_text += whitespace_representation + "\n"
    return encoded_text


def whitespace_decode(encoded_text):
    """Decodes whitespace characters back into the original text."""
    decoded_text = ""
    for line in encoded_text.splitlines():
        binary_representation = line.replace(" ", "0").replace("\t", "1")
        decoded_text += chr(int(binary_representation, 2))
    return decoded_text


"""morseEncode"""
def morse_encode(text):
    """text to morse"""
    text_tomorse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '/', '.': '.--.--.--', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
        '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
        '@': '.--.-.'
    }
    return ' '.join(text_tomorse.get(char.upper(), '') for char in text)



#text = "HELLO WORLD"
## print(morse_encode(text))

"""morseDecode"""
def morse_decode(text):
    """morse to text"""
    morse_totext = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
        '/': ' ', '.--.--.--': '.', '--..--': ',', '..--..': '?', ".----.": "'", '-.-.--': '!',
        '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';',
        '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$',
        '.--.-.': '@'
    }
    return ''.join(morse_totext.get(symbol, '') for symbol in text.split())
text = ".... .."
# print(morse_decode(text))



"""rot13Encode"""
def rot13_encode(text):
    """text to rot13"""
    rot13 = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    )
    return text.translate(rot13)
"""rot13Decode"""
def rot13_decode(text):
    """rot13 to text"""
    textrot = str.maketrans(
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    )
    return text.translate(textrot)

# print(rot13_encode("hello"))

# '''change unit of temp'''
# def c_to_f(temp):
#     '''cel to fah'''
#     return (temp*(9/5))+32
# def f_to_c(temp):
#     '''fah to cel'''
#     return (temp-32*(5/9))
# def c_to_k(temp):
#     '''cel to kavin'''
#     return (temp+273.15)
# def f_to_k(temp):
#     '''cel to kavin'''
#     return (temp*(9/5))+32+237.15

"""to camel case and snake case"""

def toCamelCase(str_snake, delimiter='_'):
    """camel"""
    if delimiter == '':
        delimiter = '_'
    init, *temp = str_snake.split(delimiter)
    res = ''.join([init.lower(), *map(str.title, temp)])
    return res

def to_snakecase(strCamel, delimiter='_'):
    """snake"""
    if delimiter == '':
        delimiter = '_'
    return ''.join([delimiter+i.lower() if i.isupper() 
        else i for i in strCamel]).lstrip(delimiter)


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


