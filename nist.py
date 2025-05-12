import math
from scipy.special import gammaincc

def bit_frequency_test(seq):
    """
    Частотный побитовый тест.
    :param seq: Последовательность, состоящая из "0" и "1"
    :return: P-значение для последовательности
    """
    n = len(seq)
    if n == 0:
        return 1.0
    sums = (seq.count("1") - seq.count("0")) / math.sqrt(n)
    p = math.erfc(abs(sums) / math.sqrt(2)) # Вычисление p с помощью дополнительной функции ошибок
    return p


def consecutive_bits_test(seq):
    """
    Тест на одинаковые подряд идущие биты.
    :param seq: Последовательность, состоящая из "0" и "1"
    :return: P-значение для последовательности
    """
    n = len(seq)
    if n == 0:
        return 1.0
    ones_count = seq.count('1')
    z = ones_count / n

    if abs(z - 0.5) >= (2 / math.sqrt(n)):
        return 0.0

    series = sum(1 for i in range(n - 1) if seq[i] != seq[i + 1])

    numerator = abs(series - 2 * n * z * (1 - z))
    denominator = 2 * math.sqrt(2 * n) * z * (1 - z)
    if denominator == 0:
        return 0.0
    p = math.erfc(numerator / denominator)

    return p


def longest_run_in_block_test(seq, m=8):
    """
    Тест на самую длинную последовательность единиц в блоке
    :param seq: Последовательность, состоящая из "0" и "1"
    :param m: Размер блока
    :return: P-значение для последовательности
    """

    n = len(seq)
    if n % m != 0:
        raise ValueError(f"Длина последовательности ({n}) должна быть кратна размеру блока ({m})")

    num_blocks = n // m
    if num_blocks == 0:
        return 1.0

    pi = [0.2148, 0.3672, 0.2305, 0.1875] # Теоретические вероятности
    v = [0, 0, 0, 0]

    for i in range(num_blocks):
        block = seq[i * m: (i + 1) * m]
        max_run_length = 0
        current_run_length = 0

        for bit in block:
            if bit == '1':
                current_run_length += 1
                max_run_length = max(max_run_length, current_run_length)
            else:
                current_run_length = 0

        if max_run_length <= 1:
            v[0] += 1
        elif max_run_length == 2:
            v[1] += 1
        elif max_run_length == 3:
            v[2] += 1
        elif max_run_length >= 4:
            v[3] += 1

    hi_square = sum((v[i] - num_blocks * pi[i]) ** 2 / (num_blocks * pi[i]) for i in range(4))

    p = gammaincc(1.5, hi_square / 2) # Вычисление p c помощью неполной гамма-функции

    return p
