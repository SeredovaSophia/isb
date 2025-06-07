import json

def read_json_file(file_path: str) -> dict:
    """
    Читает данные из JSON файла
    :param file_path: Путь к JSON файлу
    :return: Словарь с данными из файла
    :raises FileNotFoundError: Если файл не существует
    :raises PermissionError: Если нет прав на чтение файла
    :raises Exception: При других ошибках чтения
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не найден: {file_path}") from e
    except PermissionError as e:
        raise PermissionError(f"Нет прав на чтение файла: {file_path}") from e
    except Exception as e:
        raise Exception(f"Ошибка при чтении JSON файла: {file_path}") from e

def write_json_file(file_path: str, data: dict) -> None:
    """
    Записывает данные в JSON файл
    :param file_path: Путь к файлу для записи
    :param data: Данные для записи (словарь)
    :raises TypeError: Если данные не сериализуемы в JSON
    :raises PermissionError: Если нет прав на запись
    :raises Exception: При других ошибках записи
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except TypeError as e:
        raise TypeError(f"Ошибка сериализации данных в JSON: {e}") from e
    except PermissionError as e:
        raise PermissionError(f"Нет прав на запись в файл: {file_path}") from e
    except Exception as e:
        raise Exception(f"Ошибка при записи JSON файла: {file_path}") from e

def read_bin_file(file_path: str) -> bytes:
    """
    Читает содержимое бинарного файла
    :param file_path: Путь к бинарному файлу
    :return: Байтовая строка с содержимым файла
    :raises FileNotFoundError: Если файл не существует
    :raises PermissionError: Если нет прав на чтение
    :raises Exception: При других ошибках чтения
    """
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не найден: {file_path}") from e
    except PermissionError as e:
        raise PermissionError(f"Нет прав на чтение файла: {file_path}") from e
    except Exception as e:
        raise Exception(f"Ошибка при чтении бинарного файла: {file_path}") from e

def write_txt_file(data: str, file_path: str) -> None:
    """
    Сохраняет текстовые данные в файл
    :param data: Текст который нужно записать в файл
    :param file_path: Путь к файлу
    :return: None
    :raises FileNotFoundError: Если не удалось найти или создать файл по указанному пути
    :raises PermissionError: Если нет прав на запись в файл
    :raises Exception: При других ошибках записи
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не найден: {file_path}") from e
    except PermissionError as e:
        raise PermissionError(f"Нет прав на запись в файл: {file_path}") from e
    except Exception as e:
        raise Exception(f"Ошибка при записи файла ммм: {file_path}") from e
