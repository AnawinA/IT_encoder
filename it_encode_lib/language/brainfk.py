
def encode_brainfk(text):
    """Encodes text into more optimized Brainfuck code using loops."""
    brainfuck_code = ""

    for char in text:
        ascii_val = ord(char)
        multiplier = ascii_val // 10
        remainder = ascii_val % 10
        if multiplier > 0:
            brainfuck_code += "+" * multiplier + "[>++++++++++<-]>"
        brainfuck_code += "+" * remainder + "."
        brainfuck_code += "[-]\n"
    return brainfuck_code


def decode_brainfk(brainfuck_code):
    """Decodes Brainfuck code back to text by interpreting it."""
    cells = [0] * 30
    pointer = 0
    output = ""
    code_ptr = 0

    while code_ptr < len(brainfuck_code):
        command = brainfuck_code[code_ptr]
        if command == "+":
            cells[pointer] = (cells[pointer] + 1) % 256
        elif command == "-":
            cells[pointer] = (cells[pointer] - 1) % 256
        elif command == ">":
            pointer += 1
        elif command == "<":
            pointer -= 1
        elif command == ".":
            output += chr(cells[pointer])
        elif command == "[":
            if cells[pointer] == 0:
                open_loops = 1
                while open_loops != 0:
                    code_ptr += 1
                    if brainfuck_code[code_ptr] == "[":
                        open_loops += 1
                    elif brainfuck_code[code_ptr] == "]":
                        open_loops -= 1
        elif command == "]":
            if cells[pointer] != 0:
                close_loops = 1
                while close_loops != 0:
                    code_ptr -= 1
                    if brainfuck_code[code_ptr] == "[":
                        close_loops -= 1
                    elif brainfuck_code[code_ptr] == "]":
                        close_loops += 1
        code_ptr += 1
    return output

