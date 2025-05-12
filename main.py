import argparse
import nist
import os

def parse_arguments():
    """
    Парсинг аргументов командной строки.
    :return: Объект argparse с аргументами
    """
    parser = argparse.ArgumentParser(description="Сравнение последовательностей C++ и Java кода")
    parser.add_argument("cpp_file", help="Путь к файлу C++ с сгенерированной последовательностью")
    parser.add_argument("java_file", help="Путь к файлу Java с сгенерированной последовательностью")
    parser.add_argument("results", help="Файл для сохранения результатов тестов")
    return parser.parse_args()


def read_file(filename: str):
    """
    Чтение файла
    :param filename: Путь к файлу
    :return: Последовательность в виде строки
    """
    try:
        with open(filename, "r", encoding='utf-8') as file:
            sequence = file.read()
        return sequence
    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Файл не найден")
    except IOError:
        raise IOError(f"Ошибка: Не удалось прочитать файл ")
    except Exception as e:
        raise Exception("Произошла ошибка: {e}")

def write_res(freq_cpp, freq_java, consecutive_cpp, consecutive_java, long_cpp, long_java, results: str):
    """
    Сохранение результатов тестов в файл.
    :param freq_cpp: P-значение частотного теста для C++
    :param freq_java: P-значение частотного теста для Java
    :param consecutive_cpp: P-значение теста на одинаковые биты для C++
    :param consecutive_java: P-значение теста на одинаковые биты для Java
    :param long_cpp: P-значение теста на длинную последовательность единиц для C++
    :param long_java: P-значение теста на длинную последовательность единиц для Java
    :param results: Путь к файлу для записи результатов
    """
    with open(results, 'w', encoding='utf-8') as file:
        file.write("Частотный побитовый тест:\n")
        file.write(f"C++: {freq_cpp}\n")
        file.write(f"Java: {freq_java}\n\n")

        file.write("Тест на одинаковые подряд идущие биты:\n")
        file.write(f"C++: {consecutive_cpp}\n")
        file.write(f"Java: {consecutive_java}\n\n")

        file.write("Тест на самую длинную последовательность единиц:\n")
        file.write(f"C++: {long_cpp}\n")
        file.write(f"Java: {long_java}\n")


def main():
    args = parse_arguments()

    if not os.path.exists(args.cpp_file):
        raise FileNotFoundError(f"Файл {args.cpp_file} не найден")
    if not os.path.exists(args.java_file):
        raise FileNotFoundError(f"Файл {args.java_file} не найден")

    try:
        seq_cpp = read_file(args.cpp_file)
        seq_java = read_file(args.java_file)

        freq_cpp = nist.bit_frequency_test(seq_cpp)
        freq_java = nist.bit_frequency_test(seq_java)

        consecutive_cpp = nist.consecutive_bits_test(seq_cpp)
        consecutive_java = nist.consecutive_bits_test(seq_java)

        long_cpp = nist.longest_run_in_block_test(seq_cpp)
        long_java = nist.longest_run_in_block_test(seq_java)

        write_res(freq_cpp, freq_java, consecutive_cpp, consecutive_java, long_cpp, long_java, args.results)

        print(f"Результаты тестов успешно сохранены в {args.results}")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
