from cryptography.hazmat.primitives import padding as symmetric_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os


class SymCipherManager:
    """Класс для симметричного шифрования с использованием алгоритма SM4"""

    @staticmethod
    def generate_sm4_key() -> bytes:
        """
        Генерирует ключ алгоритма шифрования SM4
        :return: 16-байтный ключ
        :raises RuntimeError: Если не удалось сгенерировать ключ
        """
        try:
            return os.urandom(16)
        except Exception as e:
            raise RuntimeError("Ошибка генерации ключа") from e

    @staticmethod
    def apply_padding(data: bytes) -> bytes:
        """
        Добавляет PKCS7 паддинг к данным
        :param data: Данные для паддинга
        :return: Данные с паддингом
        :raises TypeError: Если данные не в формате bytes
        """
        if not isinstance(data, bytes):
            raise TypeError("Данные должны быть в формате bytes")

        padder = symmetric_padding.PKCS7(128).padder()
        return padder.update(data) + padder.finalize()

    @staticmethod
    def remove_padding(data: bytes) -> bytes:
        """
        Удаляет PKCS7 паддинг из данных
        :param data: данные с паддингом
        :return: данные без паддинга
        :raises TypeError: Если данные не в формате bytes
        """
        if not isinstance(data, bytes):
            raise TypeError("Данные должны быть в формате bytes")

        unpadder = symmetric_padding.PKCS7(128).unpadder()
        try:
            return unpadder.update(data) + unpadder.finalize()
        except Exception as e:
            raise RuntimeError("Ошибка удаления паддинга") from e

    @staticmethod
    def encrypt_sm4(text: bytes, key: bytes) -> bytes:
        """
        Шифрует текст с помощью алгоритма SM4
        :param text: Текст для шифрования
        :param key: Ключ шифрования (16 байт)
        :return: iv + зашифрованный текст
        :raises TypeError: Если неверный тип данных
        :raises ValueError: Если неверная длина ключа или данных
        :raises RuntimeError: Если ошибка шифрования
        """
        if not isinstance(text, bytes) or not isinstance(key, bytes):
            raise TypeError("Данные и ключ должны быть в формате bytes")
        if len(key) != 16:
            raise ValueError("Ключ должен быть длиной 16 байт")
        if not text:
            raise ValueError("Текст для шифрования не может быть пустым")

        try:
            iv = os.urandom(16)
            padded_data = SymCipherManager.apply_padding(text)
            cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()

            return iv + ciphertext
        except Exception as e:
            raise RuntimeError("Ошибка шифрования") from e

    @staticmethod
    def decrypt_sm4(ciphertext: bytes, key: bytes) -> bytes:
        """
        Расшифровывает текст с помощью алгоритма SM4
        :param ciphertext: iv + зашифрованный текст
        :param key: Ключ расшифровки
        :return: Расшифрованный текст
        :raises TypeError: Если неверный тип данных
        :raises ValueError: Если неверная длина ключа или данных
        :raises RuntimeError: Если ошибка дешифрования
        """
        if not isinstance(ciphertext, bytes) or not isinstance(key, bytes):
            raise TypeError("Данные и ключ должны быть в формате bytes")
        if len(key) != 16:
            raise ValueError("Ключ должен быть 16 байт")
        if len(ciphertext) < 16:
            raise ValueError("Шифротекст короткий")

        try:
            iv = ciphertext[:16]
            encrypted_data = ciphertext[16:]
            cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            padded_text = decryptor.update(encrypted_data) + decryptor.finalize()

            return SymCipherManager.remove_padding(padded_text)
        except Exception as e:
            raise RuntimeError("Ошибка дешифрования") from e