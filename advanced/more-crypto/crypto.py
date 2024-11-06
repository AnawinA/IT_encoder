def _encode_builtins(text: str, type_encode: str):
    try:
        return str(text.encode(type_encode)).replace('b', '').strip("'")
    except Exception as e:
        return f"Error encoding string to {text}: {e}"

def _decode_builtins(byte_data: str, type_encode: str):
    try:
        return bytes(byte_data, "latin1").decode(type_encode)
    except Exception as e:
        return f"Error decoding bytes from {byte_data}: {e}"

def encode_utf16(text):
    """Encodes a string into bytes using UTF-16 encoding."""
    return _encode_builtins(text, 'UTF-16')

def decode_utf16(byte_data):
    """Decodes bytes back into a string using UTF-16 encoding."""
    return _decode_builtins(byte_data, 'UTF-16')


# Sha group
import hashlib

def sha(message, fn):
    message_bytes = message.encode('utf-8')
    sha_hash = fn(message_bytes)
    return sha_hash.hexdigest()

def sha1_encode(message):
    return sha(message, hashlib.sha1)

def md5_encode(message):
    return sha(message, hashlib.md5)

def sha256_encode(message):
    return sha(message, hashlib.sha256)

def sha512_encode(message):
    return sha(message, hashlib.sha512)

import quopri
def encode_quopri(text):
    return quopri.encodestring(text.encode('utf-8')).decode('utf-8')

def decode_quopri(text):
    return quopri.decodestring(text.encode('utf-8')).decode('utf-8')
