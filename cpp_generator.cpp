#include <iostream>
#include <fstream>
#include <random>
#include <bitset>

/**
 * @brief Generates a random 128-bit sequence represented as a binary string.
 *
 * The function uses a Mersenne Twister pseudo-random number generator (std::mt19937)
 * with a hardware-based seed from std::random_device. Produces a bitset of 128 bits,
 * where each bit is randomly set to '0' or '1'.
 *
 * @return std::bitset<128> - A bitset representing the generated 128-bit binary sequence.
 */
std::bitset<128> generate_128_bit_sequence() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 1);

    std::bitset<128> randomBits;

    for (int i = 0; i < 128; ++i) {
        randomBits[i] = dis(gen);
    }

    return randomBits;
}

int main() {
    std::bitset<128> randomBits = generate_128_bit_sequence();
    std::cout << "Псевдослучайная бинарная последовательность (128 бит) на С++: "
              << randomBits << std::endl;
    std::ofstream outfile("cpp_bin_seq.txt");
    if (outfile.is_open()) {
        outfile << randomBits;
        outfile.close();
        std::cout << "Последовательность сохранена в cpp_bin_seq.txt." << std::endl;
    } else {
        std::cout << "Ошибка: Не удалось открыть файл для записи." << std::endl;
        return 1;
    }

    return 0;
}
