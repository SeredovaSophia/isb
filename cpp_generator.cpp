#include <iostream>
#include <fstream>
#include <random>
#include <bitset>

int main() {
    std::random_device rd;
    std::mt19937 gen(rd());  // Стандартный генератор Mersenne Twister
    std::uniform_int_distribution<> dis(0, 1);

    const int length = 128;
    std::bitset<length> randomBits;

    for (int i = 0; i < length; ++i) {
        randomBits[i] = dis(gen);
    }

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
