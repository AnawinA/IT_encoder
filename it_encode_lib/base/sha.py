"""Sha-1"""
import hashlib
def generate_sha1(input_string):
    """Sha-1 hashing algorithm"""
    encoded_string = input_string.encode('utf-8')
    
    sha1_hash = hashlib.sha1()
    
    sha1_hash.update(encoded_string)
    
    return sha1_hash.hexdigest()

input_string = "Hello, World!"
hash_result = generate_sha1(input_string)
print(f"SHA-1 hash of '{input_string}': {hash_result}")

"""Sha-2 Family"""
import hashlib
def generate_sha256(input_string):
    """Sha-256 hashing algorithm"""
    encoded_string = input_string.encode('utf-8')

    sha256_hash = hashlib.sha256()

    sha256_hash.update(encoded_string)
    
    return sha256_hash.hexdigest()

input_string = "Hello, World!"
hash_result = generate_sha256(input_string)
print(f"SHA-256 hash of '{input_string}': {hash_result}")

import hashlib
def generate_sha384(input_string):
    """Sha-384 hashing algorithm"""
    encoded_string = input_string.encode('utf-8')

    sha384_hash = hashlib.sha384()
    
    sha384_hash.update(encoded_string)
    
    return sha384_hash.hexdigest()

input_string = "Hello, World!"
hash_result = generate_sha384(input_string)
print(f"SHA-384 hash of '{input_string}': {hash_result}")

import hashlib
def generate_sha512(input_string):
    """Sha-512 hashing algorithm"""
    encoded_string = input_string.encode('utf-8')

    sha512_hash = hashlib.sha512()

    sha512_hash.update(encoded_string)
    
    return sha512_hash.hexdigest()

input_string = "Hello, World!"
hash_result = generate_sha512(input_string)
print(f"SHA-512 hash of '{input_string}': {hash_result}")
