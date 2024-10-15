"""index.py"""
from browser import document, alert, html
import bundle
# note from ... import *  // "*" is not good practice
# can import only non-import files


it_encode = {
    "binary": {
        "base64": (bundle.base64_encoder, bundle.base64_decoder),
        # "base32": (bundle.base32_encoder, bundle.base32_decoder),
    },
    "iJudge": {
        "mealEncoding": (bundle.meal_encode, bundle.meal_decode),
        "numberFactory": (bundle.number_cut_encode, bundle.number_cut_decode),
        "runLength": (bundle.run_length_encode, bundle.run_length_decode),
        "test": (bundle.shorten_num_encode, bundle.shorten_num_decode),
        "test2": (bundle.shorten_num_encode, bundle.shorten_num_decode),
        "test3": (bundle.shorten_num_encode, bundle.shorten_num_decode),
        "test4": (bundle.shorten_num_encode, bundle.shorten_num_decode),
    },
    "other test": {
        "test5": (bundle.shorten_num_encode, bundle.shorten_num_decode),
    }
}



def getName(e):
    mytopic, mytool = str(e.target.title).split(" ")
    document['topic-using'].textContent = mytopic
    document['tool-using'].textContent = mytool

for i_topic in it_encode:
    print(i_topic)
    document['search-box'] <= html.H2(i_topic, Class="category-divider")
    document['search-box'] <= html.UL((html.LI(
        html.BUTTON(html.IMG(src="images/default.png", alt=i_tool, title=i_topic+" "+i_tool) + html.SPAN(i_tool)).bind('click', getName)
        ) for i_tool in it_encode[i_topic]), Class="nav-grid")



input_text = document["inputText"]
output_text = document["outputText"]

topic = document["topic-using"]
tool = document["tool-using"]

def execute(is_decode, text_input):
    """execute"""
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
