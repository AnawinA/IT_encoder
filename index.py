"""index.py"""
from browser import document, alert, html
import bundle
import details
# note from ... import *  // "*" is not good practice
# can import only non-import files


ph_prev = "Hello IT!"
ph_prev_num = "67070197"
ph_prev_small_num = "196"
ph_prev_list = "1, 3, 4, 5, 7, 8, 10"
ph_prev_ip = ("161,246,38,35", "255,255,0,128")

bundle.generate_sha1("hi")

it_encode = {
    "binary": {
        "base64": (bundle.base64_encoder, bundle.base64_decoder, {'src': 'images/b64 icon.png', 'desc': details.base64, 'in': ph_prev, 'out': bundle.base64_encoder(ph_prev)}),
        "base32": (bundle.base32_encoder, bundle.base32_decoder, {'src': 'images/b32 icon.png', 'desc': details.base32, 'in': ph_prev, 'out': bundle.base32_encoder(ph_prev)}),
        "hex/base16": (bundle.hex_encode, bundle.hex_decode,{'src': 'images/H.png', 'desc': details.hex_base16, 'in': ph_prev, 'out': bundle.hex_encode(ph_prev)}),
        "sha1": (bundle.generate_sha1, None, {'desc': details.sha1, 'in': ph_prev, 'out': bundle.generate_sha1(ph_prev), 'no_decode': True}),
        "sha224": (bundle.generate_sha224, None, {'desc': details.sha122, 'in': ph_prev, 'out': bundle.generate_sha224(ph_prev), 'no_decode': True}),
    },
    "iJudge": {
        "mealEncoding": (bundle.meal_encode, bundle.meal_decode, {'in': ph_prev, 'out': bundle.meal_encode(ph_prev)}),
        "numberFactory": (bundle.number_cut_encode, bundle.number_cut_decode, {'in': ph_prev_num, 'out': bundle.number_cut_encode(ph_prev_num)}),
        "runLength": (bundle.run_length_encode, bundle.run_length_decode, {'in': ph_prev, 'out': bundle.run_length_encode(ph_prev)}),
        "shorten": (bundle.shorten_num_encode, bundle.shorten_num_decode, {'in': ph_prev_list, 'out': bundle.shorten_num_encode(ph_prev_list)}),
        "roman": (bundle.en_roman, bundle.de_roman, {'in': ph_prev_small_num, 'out': bundle.en_roman(ph_prev_small_num)}),
    },
    "ICS": {
        "networkID": (bundle.networkid, bundle.networkid, {'in': ph_prev_ip[0], 'out': bundle.networkid(*ph_prev_ip), 'input2': '252,127,63,6', 'no_decode': True}),
    },
    "Text": {
        "upper/lowercase": (str.upper, str.lower, {'in': str.lower(ph_prev), 'out': str.upper(ph_prev)}),
        "swapcase": (str.swapcase, str.swapcase, {'in': ph_prev, 'out': str.swapcase(ph_prev)}),
        "capitalize": (str.capitalize, str.capitalize, {'in': str.lower(ph_prev), 'out': str.capitalize(ph_prev), 'no_decode': True}),
        "title": (str.title, str.title, {'in': str.lower(ph_prev), 'out': str.capitalize(ph_prev), 'no_decode': True}),
        "join/split-text": (lambda x: ''.join(x), str.split, {'in': ph_prev, 'out': str.split(ph_prev)}),
        "snake->camel": (bundle.toCamelCase, bundle.to_snakecase, {'in': 'hello_it!', 'out': bundle.toCamelCase('hello_it!'), 'input2': 'delimiter: _'}),
    },
}


def getName(e):
    """getName for execute from 'it_encode' dict"""
    mytopic, mytool = str(e.target.title).split(" ")
    document['topic-using'].textContent = mytopic
    document['tool-using'].textContent = mytool

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
        html.BUTTON(html.IMG(src=it_encode[i_topic][i_tool][2].get("src", "images/default.png"), alt=i_tool, title=i_topic+" "+i_tool) + html.SPAN(i_tool)).bind('click', getName)
        ) for i_tool in it_encode[i_topic]), Class="nav-grid")


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

def translate(e):
    """encode"""
    try:
        text_input = input_text.value
        if text_input != "":
            is_decode = 1 if document["isDecode"].checked else 0
            output_result = execute(is_decode, text_input)
            output_text.value = output_result
        else:
            alert("Error: Nothing to translate")
    except ValueError as err:
        alert("Error: Something went wrong " + str(err))

document["translateBtn"].bind("click", translate)

# from it_encode_lib.base64.base64 import *
# a = str(input())
# b = base64_decoder(base64_encoder(a))
# print(b)

def clear(_):
    input_text.value = ""
    output_text.value = ""

document["clearBtn"].bind("click", clear)


def swap(_):
    input_text.value, output_text.value = output_text.value, input_text.value
    input_text.classList.toggle("swap-placeholder")
    input_text.attrs['placeholder'], output_text.attrs['placeholder'] = output_text.attrs['placeholder'], input_text.attrs['placeholder']


document["isDecode"].bind("click", swap)
