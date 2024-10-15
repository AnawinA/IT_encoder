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