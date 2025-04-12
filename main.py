from works1 import read_json, write_to_file
from caesar_cipher1 import caesar_cipher

def main() -> None:
    """Основная функция программы."""
    try:
        settings = read_json('settings1.json')
        shift = settings['shift']
        input_file = settings['input_file']
        output_file = settings['output_file']
        alphabet_file = settings['alphabet_file']

        alphabet_data = read_json(alphabet_file)
        alphabet = alphabet_data['alphabet']

        with open(input_file, 'r', encoding='utf-8') as file:
            input_text = file.read()

        encrypted_text = caesar_cipher(input_text, shift, alphabet)
        write_to_file(output_file, encrypted_text)

        print(f"Текст успешно зашифрован и сохранен в {output_file}.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
