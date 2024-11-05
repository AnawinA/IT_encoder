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

