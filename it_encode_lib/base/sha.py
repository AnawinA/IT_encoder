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
    print(f"SHA-1 hash of '{input_string}': {sha1_result}")
    print(f"SHA-224 hash of '{input_string}': {sha224_result}")
