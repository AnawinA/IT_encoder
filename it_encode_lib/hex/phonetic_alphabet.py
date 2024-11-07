def encode_to_phonetic(text):
    phonetic_alphabet = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
        'Z': 'Zulu'
    }

    text = text.upper()  # Convert text to uppercase
    encoded_text = []

    for char in text:
        if char.isalpha():  # Only encode alphabetic characters
            encoded_text.append(phonetic_alphabet.get(char, char))
        else:
            encoded_text.append(char)  # Non-alphabetic characters are added as is

    return ' '.join(encoded_text)

def decode_from_phonetic(encoded_text):
    phonetic_to_letter = {
        'Alpha': 'A', 'Bravo': 'B', 'Charlie': 'C', 'Delta': 'D', 'Echo': 'E',
        'Foxtrot': 'F', 'Golf': 'G', 'Hotel': 'H', 'India': 'I', 'Juliett': 'J',
        'Kilo': 'K', 'Lima': 'L', 'Mike': 'M', 'November': 'N', 'Oscar': 'O',
        'Papa': 'P', 'Quebec': 'Q', 'Romeo': 'R', 'Sierra': 'S', 'Tango': 'T',
        'Uniform': 'U', 'Victor': 'V', 'Whiskey': 'W', 'X-ray': 'X', 'Yankee': 'Y',
        'Zulu': 'Z'
    }

    words = encoded_text.split()
    decoded_text = []

    for word in words:
        if word in phonetic_to_letter:
            decoded_text.append(phonetic_to_letter[word])  # Replace phonetic word with the letter
        else:
            decoded_text.append(word)  # Non-phonetic words (like punctuation) are added as is

    return ''.join(decoded_text)
