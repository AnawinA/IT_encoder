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

