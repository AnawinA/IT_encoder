"""index.py"""
from browser import document, alert
import packages
# note from ... import *  // "*" is not good practice
# can import only non-import files

it_encode = {
    "Main": {
        "base64": packages.base64,
    },
    "iJudge": {
        
    }
}


input_text = document["inputText"]
output_text = document["outputText"]

def test(e):
    """what"""
    try:
        text_input = input_text.value
        if text_input != "":
            is_decode = document["isDecode"].checked
            output_result = packages.base64(text_input, True if is_decode else False)
            output_text.value = output_result
        else:
            alert("Error: Nothing to translate")
    except ValueError:
        alert("Error: Something went wrong")

document["translateBtn"].bind("click", test)

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
