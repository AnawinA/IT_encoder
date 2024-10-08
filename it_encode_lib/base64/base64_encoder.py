def decode_base64(ct):

  #remove = if there is one
  ct = ct.replace('=', '')

  #from the base64 table, convert it to binary
  base64_dict = {"110000": "w", "110001": "x", "110101": "1", "110100": "0", "010100": "U", "010101": "V", "001100": "M", "001101": "N", "011110": "e", "011111": "f", "001001": "J", "001000": "I", "011011": "b", "011010": "a", "000110": "G", "000111": "H", "000011": "D", "000010": "C", "100100": "k", "100101": "l", "111100": "8", "111101": "9", "100010": "i", "100011": "j", "101110": "u", "101111": "v", "111001": "5", "111000": "4", "101011": "r", "101010": "q", "110011": "z", "110010": "y", "010010": "S", "010011": "T", "010111": "X", "010110": "W", "110110": "2", "110111": "3", "011000": "Y", "011001": "Z", "001111": "P", "001110": "O", "011101": "d", "011100": "c", "001010": "K", "001011": "L", "101101": "t", "000000": "A", "000001": "B", "100111": "n", "100110": "m", "000101": "F", "000100": "E", "111111": "/", "111110": "+", "100001": "h", "100000": "g", "010001": "R", "010000": "Q", "101100": "s", "111010": "6", "111011": "7", "101000": "o", "101001": "p"}
  
  ct_bi = ""
  for i in ct:
    keys = [k for k, v in base64_dict.items() if v == i] 
    keys_str = "".join(keys)
    ct_bi += keys_str 
  
  #brake it into 8 bits, remove the 0 left
  ct_bi = [ct_bi[i:i+8] for i in range(0, len(ct_bi), 8)]
  if len(ct_bi[-1]) != 8:
    ct_bi.pop()
 
  #convert to binary
  ct_binary = []
  for i in ct_bi:
    ct_binary.append(i.encode())

  #convert to hex
  ct_hex = []
  for i in ct_binary:
    ct_hex.append(hex(int(i, 2)))

  #convert to char
  ct_decode = ""
  for i in ct_hex:
    ct_decode += chr(int(i, 16))

  return ct_decode