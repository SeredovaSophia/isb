import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

/**
 * Class for generating a pseudo-random 128-bit binary sequence
 * and outputting it to a file.
 */
public class java_generator {

    /**
     * Main method that generates and prints a 128-bit binary sequence.
     *
     * @param args Command-line arguments (not used in this implementation)
     *
     * @implSpec
     * Uses the Random class to generate pseudo-random bits.
     * Generates 128 bits represented as '0'/'1' characters in a StringBuilder.
     * Outputs the resulting binary string to standard output and saves it to a file.
     */
    public static void main(String[] args) {
        Random random = new Random();
        int length = 128;
        StringBuilder binarySequence = new StringBuilder(length);

        for (int i = 0; i < length; i++) {
            binarySequence.append(random.nextInt(2));
        }

        System.out.println("Псевдослучайная бинарная последовательность (128 бит): " + binarySequence);

        try (FileWriter fileWriter = new FileWriter("java_bin_seq.txt")) {
            fileWriter.write(binarySequence.toString());
            System.out.println("Последовательность сохранена в java_bin_seq.txt.");
        } catch (IOException e) {
            System.out.println("Ошибка: Не удалось открыть файл для записи.");
            e.printStackTrace();
        }
    }
}
