"""index.py"""
from browser import document, alert
import bundle
# note from ... import *  // "*" is not good practice
# can import only non-import files


it_encode = {
    "Main": {
        "base64": (bundle.base64_encoder, bundle.base64_decoder),
    },
    "iJudge": {
        
    }
}


input_text = document["inputText"]
output_text = document["outputText"]

topic = "Main"
tool = "base64"

def execute(is_decode, text_input):
    """execute"""
    return it_encode[topic][tool][is_decode](text_input)

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
    except ValueError:
        alert("Error: Something went wrong")

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


document["isDecode"].bind("click", swap)
