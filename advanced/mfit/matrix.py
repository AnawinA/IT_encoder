from mfit_ende_matrix import encode_matrix, decode_matrix
import pyodide
import json

MATRIX = Element("matrix_str")

def encoding(e):
    encoded = encode_matrix(Element("encode_string").element.value
                            , json.loads(MATRIX.element.innerText))
    Element("encoded_output").write(encoded)
Element('encode_button').element.addEventListener('click', pyodide.create_proxy(encoding))

def decoding(e):
    decoded = decode_matrix(json.loads(Element("decode_list").element.value)
                            , json.loads(MATRIX.element.innerText))
    Element("decoded_output").write(decoded)
Element('decode_button').element.addEventListener('click', pyodide.create_proxy(decoding))