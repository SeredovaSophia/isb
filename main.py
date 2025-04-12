import json
from works1 import read_json, write_to_file
from caesar_cipher1 import caesar_cipher
from task2_func import char_counts, make_key, decrypt_text

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

        settings2 = read_json('settings2.json')
        input_file2 = settings2['input_file2']
        output_file2 = settings2['output_file2']
        freq_output_file = settings2['freq']
        keys_output_file = settings2['keys']
        rus_freq_file = settings2['rus_freq']

        with open(input_file2, 'r', encoding='utf-8') as file:
            encrypted_text2 = file.read()
        new_freq = char_counts(encrypted_text2)
        write_to_file(freq_output_file, json.dumps(new_freq, ensure_ascii=False, indent=4))
        freq1 = read_json(rus_freq_file)
        freq2 = new_freq
        keys = make_key(freq1, freq2)
        write_to_file(keys_output_file, json.dumps(keys, ensure_ascii=False))
        decrypted_text = decrypt_text(encrypted_text2, keys)
        write_to_file(output_file2, decrypted_text)
        print(f"Текст успешно расшифрован и сохранен в {output_file2}.")


    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
