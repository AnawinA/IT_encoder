def _encode_builtins(text: str, type_encode: str):
    try:
        return str(text.encode(type_encode)).replace('b', '').strip("'")
    except Exception as e:
        return f"Error encoding string to {text}: {e}"

def _decode_builtins(byte_data: str, type_encode: str):
    try:
        return byte_data.encode(type_encode).decode('utf-8')
    except Exception as e:
        return f"Error decoding bytes from {byte_data}: {e}"


def encode_utf16(text):
    """Encodes a string into bytes using UTF-16 encoding."""
    return _encode_builtins(text, 'UTF-16')

def decode_utf16(byte_data):
    """Decodes bytes back into a string using UTF-16 encoding."""
    return _decode_builtins(byte_data, 'UTF-16')

def encode_utf32(text):
    """Encodes a string into bytes using UTF-32 encoding."""
    _encode_builtins(text, 'UTF-32')

def decode_utf32(byte_data):
    """Decodes bytes back into a string using UTF-32 encoding."""
    _decode_builtins(byte_data, 'UTF-32')

def encode_windows_1252(text):
    """Encodes a string into bytes using Windows-1252 encoding."""
    _encode_builtins(text, 'Windows-1252')

def decode_windows_1252(byte_data):
    """Decodes bytes back into a string using Windows-1252 encoding."""
    _decode_builtins(byte_data, 'Windows-1252')

def encode_shift_jis(text):
    """Encodes a string into bytes using Shift JIS encoding."""
    try:
        return text.encode('shift_jis')
    except UnicodeEncodeError as e:
        return f"Error encoding string to Shift JIS: {e}"

def decode_shift_jis(byte_data):
    """Decodes bytes back into a string using Shift JIS encoding."""
    try:
        return byte_data.decode('shift_jis')
    except UnicodeDecodeError as e:
        return f"Error decoding bytes from Shift JIS: {e}"

def encode_big5(text):
    """Encodes a string into bytes using Big5 encoding."""
    try:
        return text.encode('big5')
    except UnicodeEncodeError as e:
        return f"Error encoding string to Big5: {e}"

def decode_big5(byte_data):
    """Decodes bytes back into a string using Big5 encoding."""
    try:
        return byte_data.decode('big5')
    except UnicodeDecodeError as e:
        return f"Error decoding bytes from Big5: {e}"
