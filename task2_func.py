def char_counts(text: str) -> dict:
    """Подсчитывает частоту символов в тексте.

    :param text: Текст для анализа
    :return: Словарь с частотами символов
    """
    text = text.replace("\n", "")
    total = len(text)
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    for char in counts:
        counts[char] /= total
    return dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))


def make_key(freq_a: dict, freq_b: dict) -> dict:
    """ Создает словарь соответствий между двумя распределениями частот.

    :param freq_a: Первое распределение частот
    :param freq_b: Второе распределение частот
    :return: Словарь с соответствиями символов
    """
    key = {}
    chars_a = list(freq_a.keys())
    chars_b = list(freq_b.keys())
    for i in range(min(len(chars_a), len(chars_b))):
        key[chars_b[i]] = chars_a[i]
    return key


def decrypt_text(encrypted_text: str, key: dict) -> str:
    """Дешифрует текст с использованием словаря соответствий.

    :param encrypted_text: Зашифрованный текст
    :param key: Словарь соответствий символов
    :return: Расшифрованный текст
    """
    decrypted_text = ""

    for char in encrypted_text:
        if char in key:
            decrypted_text += key[char]
        else:
            decrypted_text += char

    return decrypted_text
