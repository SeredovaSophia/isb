from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend


class AsymCipherManager:
    """Класс для асимметричного шифрования с использованием RSA"""

    @staticmethod
    def generate_rsa_keys() -> tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        """
        Генерирует пару закрытый RSA ключ и открытый RSA ключ
        :return: Кортеж (закрытый ключ, открытый ключ)
        :raises RuntimeError: Если не удалось сгенерировать ключи
        """
        try:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            public_key = private_key.public_key()
            return private_key, public_key
        except Exception as e:
            raise RuntimeError("Ошибка генерации RSA ключей") from e

    @staticmethod
    def encrypt_key(sym_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        """
        Шифрует симметричный ключ с помощью открытого
        :param sym_key: Симметричный ключ для шифрования
        :param public_key: Открытый RSA ключ
        :return: Зашифрованный симметричный ключ
        :raises TypeError: Если неверный тип аргументов
        :raises ValueError: Если ключ пустой или слишком большой
        :raises RuntimeError: Если ошибка шифрования
        """
        if not isinstance(sym_key, bytes):
            raise TypeError("Симметричный ключ должен быть в формате bytes")
        if not isinstance(public_key, rsa.RSAPublicKey):
            raise TypeError("Открытый ключ должен быть типа RSAPublicKey")
        if not sym_key:
            raise ValueError("Симметричный ключ не может быть пустым")

        try:
            return public_key.encrypt(
                sym_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except Exception as e:
            raise RuntimeError("Ошибка шифрования ключа") from e

    @staticmethod
    def decrypt_key(encr_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:

        if not isinstance(encr_key, bytes):
            raise TypeError("Зашифрованный ключ должен быть в формате bytes")
        if not isinstance(private_key, rsa.RSAPrivateKey):
            raise TypeError("Закрытый ключ должен быть типа RSAPrivateKey")
        if not encr_key:
            raise ValueError("Зашифрованный ключ не может быть пустым")

        try:
            return private_key.decrypt(
                encr_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except Exception as e:
            raise RuntimeError("Ошибка дешифрования ключа") from e