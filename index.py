"""index.py"""
from browser import document, alert, html
import bundle
import details
# note from ... import *  // "*" is not good practice
# can import only non-import files


ph_prev = "Hello IT!"
ph_prev_num = "67070197"
ph_prev_small = "IT!"
ph_prev_small_num = "196"
ph_prev_list = "1, 3, 4, 5, 7, 8, 10"
ph_prev_ip = ("161,246,38,35", "255,255,0,128")
ph_prev_zero = "0"
ph_prev_emoji = "Hello 💻"

it_encode = {
    "binary": {
        "base64": (bundle.base64_encoder, bundle.base64_decoder, {'c': 'T', 'src': 'images/b64 icon.png', 'desc': details.base64, 'in': ph_prev, 'out': bundle.base64_encoder(ph_prev)}),
        "base32": (bundle.base32_encoder, bundle.base32_decoder, {'c': 'T', 'src': 'images/b32 icon.png', 'desc': details.base32, 'in': ph_prev, 'out': bundle.base32_encoder(ph_prev)}),
        "hex/base16": (bundle.hex_encode, bundle.hex_decode,{'c': 'P', 'src': 'images/H.png', 'desc': details.hex_base16, 'in': ph_prev, 'out': bundle.hex_encode(ph_prev)}),
        "binary/base2": (bundle.encode_to_binary, bundle.decode_from_binary, {'c': 'W', 'src': 'images/binary.png', 'desc': details.binary, 'in': ph_prev, 'out': bundle.encode_to_binary(ph_prev)}),
        "sha1": (bundle.generate_sha1, None, {'c': 'K', 'desc': details.sha1, 'in': ph_prev, 'out': bundle.generate_sha1(ph_prev), 'no_decode': True}),
        "sha224": (bundle.generate_sha224, None, {'c': 'K', 'desc': details.sha224, 'in': ph_prev, 'out': bundle.generate_sha224(ph_prev), 'no_decode': True}),
        "ROT13": (bundle.rot13_encode, bundle.rot13_decode, {'c': 'P', 'desc': details.rot13, 'in': ph_prev, 'out': bundle.rot13_encode(ph_prev)}),
        "Morse": (bundle.morse_encode, bundle.morse_decode, {'c': 'P', 'desc': details.Morse, 'in': ph_prev, 'out': bundle.morse_encode(ph_prev)}),
    },
    "iJudge": {
        "mealEncoding": (bundle.meal_encode, bundle.meal_decode, {'c': 'W', 'src': 'images/ijudge/ij meanEn.png', 'in': ph_prev, 'out': bundle.meal_encode(ph_prev)}),
        "numberFactory": (bundle.number_cut_encode, bundle.number_cut_decode, {'c': 'W', 'src': 'images/ijudge/ij numberFac.png', 'in': ph_prev_num, 'out': bundle.number_cut_encode(ph_prev_num)}),
        "runLength": (bundle.run_length_encode, bundle.run_length_decode, {'c': 'W', 'src': 'images/ijudge/ij runLength.png', 'in': ph_prev, 'out': bundle.run_length_encode(ph_prev)}),
        "shorten": (bundle.shorten_num_encode, bundle.shorten_num_decode, {'c': 'W', 'src': 'images/ijudge/ij shorten.png', 'in': ph_prev_list, 'out': bundle.shorten_num_encode(ph_prev_list)}),
        "roman": (bundle.en_roman, bundle.de_roman, {'c': 'W', 'src': 'images/ijudge/ij roman.png', 'in': ph_prev_small_num, 'out': bundle.en_roman(ph_prev_small_num)}),
        "temperature": (bundle.temperature, lambda x, y: bundle.temperature(float(x, (y[::-1] if y != '' else 'FC'))), {'c': 'T', 'in': ph_prev_zero, 'out': bundle.temperature("0", 'CF'), 'input2': 'CF (Celsius to Fahrenheit)'}),
    },
    "ICS": {
        "networkID": (bundle.networkid, bundle.networkid, {'c': 'T', 'in': ph_prev_ip[0], 'out': bundle.networkid(*ph_prev_ip), 'input2': '252,127,63,6', 'no_decode': True}),
        "URL": (bundle.url_encode, bundle.url_decode, {'c': 'W', 'src': 'images/url.png', 'in': ph_prev, 'out': bundle.url_encode(ph_prev), 'desc': details.url}),
    },
    "Text": {
        "upper/lowercase": (str.upper, str.lower, {'c': 'W', 'src': 'images/text_images/upperlowercase.png', 'in': str.lower(ph_prev), 'out': str.upper(ph_prev)}),
        "swapcase": (str.swapcase, str.swapcase, {'c': 'W', 'src': 'images/text_images/swapcase.png', 'in': ph_prev, 'out': str.swapcase(ph_prev)}),
        "capitalize": (str.capitalize, str.capitalize, {'c': 'W', 'src': 'images/text_images/capitalize.png', 'in': str.lower(ph_prev), 'out': str.capitalize(ph_prev), 'no_decode': True}),
        "title": (str.title, str.title, {'c': 'W', 'src': 'images/text_images/title.png', 'in': str.lower(ph_prev), 'out': str.capitalize(ph_prev), 'no_decode': True}),
        "join/split-text": (lambda x: list(x), lambda x: ''.join(x), {'c': 'W', 'src': 'images/text_images/join-split.png', 'in': ph_prev, 'out': str.split(ph_prev)}),
        "snake->camel": (bundle.toCamelCase, bundle.to_snakecase, {'c': 'W', 'src': 'images/text_images/snake-camel.png', 'in': 'hello_it!', 'out': bundle.toCamelCase('hello_it!'), 'input2': 'delimiter: _'}),
        "reverse": (lambda x: x[::-1], lambda x: x[::-1], {'c': 'W', 'src': 'images/text_images/reverse.png', 'in': ph_prev, 'out': ph_prev[::-1]}),
    },
    "Language": {
        "Whitespace": (bundle.whitespace_encode, bundle.whitespace_decode, {'c': 'W', 'src': 'images/language/white-space.png', 'desc': details.whitespace, 'in': ph_prev, 'out': bundle.whitespace_encode(ph_prev)}), 
        "Brainfk": (bundle.encode_brainfk, bundle.decode_brainfk, {'c': 'W', 'src': 'images/language/Brainf.png', 'desc': details.brainfk, 'in': ph_prev_small, 'out': bundle.encode_brainfk(ph_prev_small)}),
        "Chicken": (bundle.encode_chicken, bundle.decode_chicken, {'c': 'W', 'src': 'images/language/chicken.png', 'desc': details.chicken, 'in': ph_prev_small, 'out': bundle.encode_chicken(ph_prev_small)}),
        "FalseASCII": (bundle.encode_false_ascii, bundle.decode_false_ascii, {'c': 'W', 'src': 'images/language/false ASCII.png', 'desc': details.false_ascii, 'in': ph_prev, 'out': bundle.encode_false_ascii(ph_prev)}),
        "FalseBinary": (bundle.encode_false_binary, bundle.decode_false_binary, {'c': 'W', 'src': 'images/language/false binary.png', 'desc': details.false_binary, 'in': ph_prev, 'out': bundle.encode_false_binary(ph_prev)}),
    },
    "BuiltIn": {
        "UTF-8": (bundle.encode_utf8, bundle.decode_utf8, {'c': 'W', 'in': ph_prev_emoji, 'out': bundle.encode_utf8(ph_prev_emoji), 'no_decode': True}),
        "ISO-8859-1": (bundle.encode_iso_8859_1, bundle.encode_iso_8859_1, {'c': 'W', 'in': ph_prev_emoji, 'out': bundle.encode_iso_8859_1(ph_prev_emoji)}),
        "ASCII": (bundle.encode_ascii, bundle.decode_ascii, {'c': 'W', 'in': ph_prev, 'out': bundle.encode_ascii(ph_prev)}),
    },
    "External": {
        "UTF-16": (None, None, {'c': 'W'}),
        "MD-5": (None, None, {'c': 'W'}),
        "SHA-1": (None, None, {'c': 'K'}),
        "SHA-256": (None, None, {'c': 'K'}),
        "SHA-512": (None, None, {'c': 'K'}),
        "quopri": (None, None, {'c': 'W'}),
    }
}

credits = {}

def getName(e):
    """getName for execute from 'it_encode' dict"""
    mytopic, mytool = str(e.target.title).split(" ")
    document['topic-using'].textContent = mytopic
    document['tool-using'].textContent = mytool
    document['icon-prev'].attrs['src'] = e.target.attrs['src']
    document['icon-prev'].attrs['title'] = e.target.attrs['title']

    tool_details = it_encode[mytopic][mytool][2]
    config(tool_details, mytool)

    document['sidebar'].classList.remove('open')
    on_in, on_out = (tool_details['in'], tool_details['out']) if not input_text.classList.contains('swap-placeholder') else (tool_details['out'], tool_details['in'])
    input_text.attrs['placeholder'], output_text.attrs['placeholder'] = on_in, on_out


def config(td, mytool):
    """[-] Ignore"""
    if 'no_decode' in td:
        document['isDecode'].checked = False
        document['isDecode'].disabled = True
    else:
        document['isDecode'].parent.style.display = 'block'
        document['isDecode'].disabled = False
    if 'desc' in td:
        document['details-desc'].textContent = 'description ' + mytool 
        document['details-content'].textContent = td.get('desc')
        document['details-desc'].style.display = 'block'
    else:
        document['details-desc'].style.display = 'none'

    if 'input2' in td:
        document['input2-input'].attrs['placeholder'] = td.get('input2')
        document['input2-input'].disabled = False
        document['input2-input'].parent.style.display = 'block'
    else:
        document['input2-input'].disabled = True
        document['input2-input'].parent.style.display = 'none'

for i_topic in it_encode:
    document['search-box'] <= html.H2(i_topic, Class="category-divider")
    document['search-box'] <= html.UL((html.LI(
        (html.BUTTON(html.IMG(src=it_encode[i_topic][i_tool][2].get("src", "images/default.png"), alt=i_tool, title=i_topic+" "+i_tool) + html.SPAN(i_tool)).bind('click', getName) ) \
            if not it_encode[i_topic][i_tool][0] is None \
            else html.BUTTON(html.A(html.IMG(src=it_encode[i_topic][i_tool][2].get("src", "images/default.png"), alt=i_tool, title=i_topic+" "+i_tool) + html.SPAN(i_tool), href="./advanced/more-crypto/index.html?c=" + i_tool))
        ) for i_tool in it_encode[i_topic]), Class="nav-grid")
    
    for i_tool in it_encode[i_topic]:
        by = it_encode[i_topic][i_tool][2]['c']
        name_by = None
        match by:
            case 'W':
                name_by = 'อนาวิล'
            case 'P':
                name_by = 'วสวัตติ์'
            case 'T':
                name_by = 'อภิพล'
            case 'K':
                name_by = 'คทาฤทธี'
        if name_by not in credits:
            credits[name_by] = [i_tool]
        else:
            credits[name_by] += [i_tool]

print(credits)
for i in credits:
    document['credits-here'] <= html.LI(html.STRONG(i + f" [{len(credits[i])}]: " ) + ", ".join(credits[i]))


input_text = document["inputText"]
output_text = document["outputText"]

topic = document["topic-using"]
tool = document["tool-using"]

def execute(is_decode, text_input):
    """execute"""
    if False if document["input2-input"].disabled else True:
        my_value = document["input2-input"].value
        return it_encode[topic.textContent][tool.textContent][is_decode](text_input, my_value or "")
    return it_encode[topic.textContent][tool.textContent][is_decode](text_input)

def translate(_):
    """encode"""
    try:
        text_input = input_text.value
        if text_input != "":
            is_decode = 1 if document["isDecode"].checked else 0
            output_result = execute(is_decode, text_input)
            output_text.value = output_result
        else:
            output_text.value = ""
    except ValueError as err:
        output_text.value ="Error: Something went wrong " + str(err)

document["translateBtn"].bind("click", translate)
document["inputText"].bind("input", translate)


def clear(_):
    input_text.value = ""
    output_text.value = ""

document["clearBtn"].bind("click", clear)

def swap(_):
    input_text.value, output_text.value = output_text.value, input_text.value
    input_text.classList.toggle("swap-placeholder")
    input_text.attrs['placeholder'], output_text.attrs['placeholder'] = output_text.attrs['placeholder'], input_text.attrs['placeholder']

document["isDecode"].bind("click", swap)
