import config
import util

if __name__ == '__main__':
    input_language = input("Выберите язык (EN - английский, RU - русский): ").upper()

    if input_language == 'EN':
        morse_code_dict = config.ENGLISH_MORSE_CODE_DICT
    elif input_language == 'RU':
        morse_code_dict = config.RUSSIAN_MORSE_CODE_DICT
    else:
        print("Неверный выбор языка.")
        exit()

    input_text = input(f"Введите текст для преобразования в азбуку Морзе ({input_language}): ")
    morse_result = util.text_to_morse(input_text, morse_code_dict)
    print(f"Результат: {morse_result}")

    input_morse = input(f"Введите азбуку Морзе для преобразования в текст ({input_language}): ")
    text_result = util.morse_to_text(input_morse, morse_code_dict)
    print(f"Результат: {text_result}")
