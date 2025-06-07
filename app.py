from serialize import *
from asymmetric_alg import AsymCipherManager
from symmetric_alg import SymCipherManager
from file_work import *


class HybridCryptosystem:
    def __init__(self):
        self._initialize_settings()

    def _initialize_settings(self) -> None:
        """Инициализация настроек приложения"""
        try:
            self._settings = read_json_file("settings.json")
            self._is_running = True
        except Exception as e:
            print("Ошибка: Не удалось загрузить файл настроек (settings.json)")
            self._is_running = False

    def _display_menu(self) -> None:
        """Отображение меню приложения"""
        menu_items = [
            "\nВыберите действие:",
            "1 - Сгенерировать ключи",
            "2 - Зашифровать текст симметричным ключом",
            "3 - Расшифровать текст",
            "4 - Выход\n"
        ]
        print("\n".join(menu_items))

    def _handle_key_generation(self) -> None:
        """Обработка генерации ключей"""
        try:
            # Генерация ключей
            private_key, public_key = AsymCipherManager.generate_rsa_keys()
            symmetric_key = SymCipherManager.generate_sm4_key()

            # Сохранение ключей
            serialize_public_key(self._settings["public_key"], public_key)
            serialize_private_key(self._settings["private_key"], private_key)

            # Шифрование и сохранение симметричного ключа
            encrypted_key = AsymCipherManager.encrypt_key(symmetric_key, public_key)
            serialize_sym_key(self._settings["encrypt_sym_key"], encrypted_key)

            print("\n[Успех] Ключи сгенерированы и сохранены")
        except Exception as e:
            print(f"\n[Ошибка] Генерация ключей: {e}")

    def _handle_encryption(self) -> None:
        """Обработка шифрования текста"""
        try:
            # Получение ключей
            encrypted_key = deserialize_sym_key(self._settings["encrypt_sym_key"])
            private_key = deserialize_private_key(self._settings["private_key"])
            symmetric_key = AsymCipherManager.decrypt_key(encrypted_key, private_key)

            # Шифрование текста
            text = read_bin_file(self._settings["text"])
            encrypted_text = SymCipherManager.encrypt_sm4(text, symmetric_key)
            write_bytes_file(self._settings["encrypt_text"], encrypted_text)

            print("\n[Успех] Текст зашифрован")
        except Exception as e:
            print(f"\n[Ошибка] Шифрование текста: {e}")

    def _handle_decryption(self) -> None:
        """Обработка дешифрования текста"""
        try:
            # Получение ключей
            encrypted_key = deserialize_sym_key(self._settings["encrypt_sym_key"])
            private_key = deserialize_private_key(self._settings["private_key"])
            symmetric_key = AsymCipherManager.decrypt_key(encrypted_key, private_key)

            # Дешифрование текста
            encrypted_text = read_bin_file(self._settings["encrypt_text"])
            decrypted_text = SymCipherManager.decrypt_sm4(encrypted_text, symmetric_key)
            write_txt_file(decrypted_text.decode("UTF-8"), self._settings["decrypt_text"])

            print("\n[Успех] Текст расшифрован")
        except Exception as e:
            print(f"\n[Ошибка] Дешифрование текста: {e}")

    def console_app(self) -> None:
        """Основной цикл работы приложения"""
        if not self._is_running:
            return

        while self._is_running:
            self._display_menu()
            user_choice = input("Ваш выбор: ").strip()

            match user_choice:
                case "1":
                    self._handle_key_generation()
                case "2":
                    self._handle_encryption()
                case "3":
                    self._handle_decryption()
                case "4":
                    self._is_running = False
                    print("\nЗавершение работы программы...")
                case _:
                    print("\n[Ошибка] Неверный ввод. Выберите пункт 1-4")


if __name__ == "__main__":
    app = HybridCryptosystem()
    app.console_app()