import json

def read_json(file_path: str) -> dict:
    """Читает JSON файл и возвращает его содержимое.

    :param file_path: Путь к файлу.
    :return: Содержимое файла в формате словаря.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    except json.JSONDecodeError:
        raise ValueError(f"Ошибка декодирования JSON в файле {file_path}.")
    except IOError:
        raise IOError(f"Ошибка чтения файла {file_path}.")
    except Exception as e:
        raise Exception(f"Ошибка: {e}")

def write_to_file(file_path: str, content: str) -> None:
    """Записывает содержимое в файл.

    :param file_path: Путь к файлу.
    :param content: Содержимое для записи.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except IOError:
        raise IOError(f"Не удалось записать в файл {file_path}.")
    except Exception as e:
        raise Exception(f"Ошибка: {e}")