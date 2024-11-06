import crypto
import pyodide

it_encode = {
    "UTF-16": (crypto.encode_utf16, None),
    "MD-5": (crypto.md5_encode, None),
    "SHA-1": (crypto.sha1_encode, None),
    "SHA-256": (crypto.sha256_encode, None),
    "SHA-512": (crypto.sha512_encode, None),
    "quopri": (crypto.encode_quopri, crypto.decode_quopri),
}

def get_tool():
    return Element("tool-using").element.innerText


def translate(e):
    # Element("decoded_output").write(decoded)
    # print(get_tool())
    is_decode = int(Element("isDecode").element.checked)
    input_text = Element("inputText").element.value
    get_encode = it_encode[get_tool()][is_decode]
    print(get_encode)
    if get_encode is None:
        Element("outputText").element.value = "Not supported"
    else:
        Element("outputText").element.value = get_encode(input_text)

Element('translateBtn').element.addEventListener('click', pyodide.create_proxy(translate))
Element('inputText').element.addEventListener('input', pyodide.create_proxy(translate))


def clear(e):
    Element("inputText").element.value = ""
    Element("inputText").element.innerText = ""
    Element("outputText").element.value = ""
    Element("outputText").element.innerText = ""

Element('clearBtn').element.addEventListener('click', pyodide.create_proxy(clear))

