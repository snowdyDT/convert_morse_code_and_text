def text_to_morse(text, morse_code_dict):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += ' '
    return morse_code


def morse_to_text(morse_code, morse_code_dict):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        if code in morse_code_dict.values():
            text += [k for k, v in morse_code_dict.items() if v == code][0]
        else:
            text += ' '
    return text
