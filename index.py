"""index.py"""
from browser import document, alert, html
import bundle
import details
# note from ... import *  // "*" is not good practice
# can import only non-import files


ph_prev = "Hello IT!"
ph_prev_num = "67070197"
ph_prev_list = "1, 3, 4, 5, 7, 8, 10"

it_encode = {
    "binary": {
        "base64": (bundle.base64_encoder, bundle.base64_decoder, {'desc': details.base64, 'in': ph_prev, 'out': bundle.base64_encoder(ph_prev)}),
        "base32": (bundle.base32_encoder, bundle.base32_decoder, {'desc': details.base32, 'in': ph_prev, 'out': bundle.base32_encoder(ph_prev)}),
    },
    "iJudge": {
        "mealEncoding": (bundle.meal_encode, bundle.meal_decode, {'in': ph_prev, 'out': bundle.meal_encode(ph_prev)}),
        "numberFactory": (bundle.number_cut_encode, bundle.number_cut_decode, {'in': ph_prev_num, 'out': bundle.number_cut_encode(ph_prev_num)}),
        "runLength": (bundle.run_length_encode, bundle.run_length_decode, {'in': ph_prev, 'out': bundle.run_length_encode(ph_prev)}),
        "shorten": (bundle.shorten_num_encode, bundle.shorten_num_decode, {'in': ph_prev_list, 'out': bundle.shorten_num_encode(ph_prev_list)}),
        "test2": (bundle.shorten_num_encode, bundle.shorten_num_decode, {}),
        "test3": (bundle.shorten_num_encode, bundle.shorten_num_decode, {}),
        "test4": (bundle.shorten_num_encode, bundle.shorten_num_decode, {}),
    },
    "other test": {
        "test5": (bundle.shorten_num_encode, bundle.shorten_num_decode),
    }
}





def getName(e):
    mytopic, mytool = str(e.target.title).split(" ")
    document['topic-using'].textContent = mytopic
    document['tool-using'].textContent = mytool
    tool_details = it_encode[mytopic][mytool][2]
    if 'desc' in tool_details:
        document['details-desc'].textContent = 'description ' + mytool 
        document['details-content'].textContent = tool_details.get('desc')
        document['details-desc'].style.display = 'block'
    else:
        document['details-desc'].style.display = 'none'
    document['sidebar'].classList.remove('open')
    on_in, on_out = (tool_details['in'], tool_details['out']) if not input_text.classList.contains('swap-placeholder') else (tool_details['out'], tool_details['in'])
    input_text.attrs['placeholder'], output_text.attrs['placeholder'] = on_in, on_out


for i_topic in it_encode:
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
