def caesar_cipher(text: str, shift: int, alphabet: str) -> str:
    """Шифрует текст с использованием шифра Цезаря.

    :param text: Исходный текст для шифрования.
    :param shift: Количество позиций для сдвига.
    :param alphabet: Алфавит для шифрования.
    :return: Зашифрованный текст.
    """
    encrypted_text = ""
    alphabet_length = len(alphabet)

    for char in text:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index + shift) % alphabet_length
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char

    return encrypted_text

def caesar_decipher(text: str, shift: int, alphabet: str) -> str:
    """Дешифрует текст с использованием шифра Цезаря.

    :param text: Исходный зашифрованный текст для дешифрования.
    :param shift: Количество позиций для сдвига.
    :param alphabet: Алфавит для дешифрования.
    :return: Дешифрованный текст.
    """
    decrypted_text = ""
    alphabet_length = len(alphabet)

    for char in text:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index - shift) % alphabet_length
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char

    return decrypted_text
