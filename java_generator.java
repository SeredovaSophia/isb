import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class java_generator {
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
