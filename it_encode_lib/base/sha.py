"""Sha-1"""
import hashlib
def generate_sha1(input_string):
    """Sha-1 hashing algorithm"""
    encoded_string = input_string.encode('utf-8')
    
    sha1_hash = hashlib.sha1()
    
    sha1_hash.update(encoded_string)
    
    return sha1_hash.hexdigest()

