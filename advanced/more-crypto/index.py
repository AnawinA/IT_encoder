import crypto
import pyodide

it_encode = {
    "UTF-8": (crypto.encode_utf8, crypto.decode_utf8),
}

def get_tool():
    return Element("tool-using").element.innerText


def translate(e):
    # Element("decoded_output").write(decoded)
    # print(get_tool())
    is_decode = int(Element("isDecode").element.checked)
    input_text = Element("inputText").element.value
    Element("outputText").element.value = it_encode[get_tool()][is_decode](input_text)
Element('translateBtn').element.addEventListener('click', pyodide.create_proxy(translate))

def clear(e):
    Element("inputText").element.value = ""
    Element("inputText").element.innerText = ""
    Element("outputText").element.value = ""
    Element("outputText").element.innerText = ""

Element('clearBtn').element.addEventListener('click', pyodide.create_proxy(clear))

# def encoding(e):
#     encoded = encode_matrix(Element("encode_string").element.value
#                             , json.loads(MATRIX.element.innerText))
#     Element("encoded_output").write(encoded)
# Element('encode_button').element.addEventListener('click', pyodide.create_proxy(encoding))

# def decoding(e):
#     decoded = decode_matrix(json.loads(Element("decode_list").element.value)
#                             , json.loads(MATRIX.element.innerText))
#     Element("decoded_output").write(decoded)
# Element('decode_button').element.addEventListener('click', pyodide.create_proxy(decoding))
