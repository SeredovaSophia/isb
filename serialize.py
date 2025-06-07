from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import (
    load_pem_public_key,
    load_pem_private_key,
)


def serialize_public_key(path: str, public_key: rsa.RSAPublicKey) -> None:
    """
    Сериализует открытый RSA-ключ в файл.
    :param path: Путь к файлу для сохранения
    :param public_key: Открытый RSA-ключ
    :raises ValueError: Если ключ недействителен
    :raises IOError: Если произошла ошибка записи
    """
    if not isinstance(public_key, rsa.RSAPublicKey):
        raise ValueError("Неверный тип открытого ключа")

    try:
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(path, 'wb') as f:
            f.write(pem)
    except IOError as e:
        raise IOError(f"Ошибка записи открытого ключа: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка сериализации открытого ключа: {e}")


def serialize_private_key(path: str, private_key: rsa.RSAPrivateKey) -> None:
    """
    Сериализует закрытый RSA-ключ в файл.
    :param path: Путь к файлу для сохранения
    :param private_key: Закрытый RSA-ключ
    :raises ValueError: Если ключ недействителен
    :raises IOError: Если произошла ошибка записи
    """
    if not isinstance(private_key, rsa.RSAPrivateKey):
        raise ValueError("Неверный тип закрытого ключа")

    try:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(path, 'wb') as f:
            f.write(pem)
    except IOError as e:
        raise IOError(f"Ошибка записи закрытого ключа: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка сериализации закрытого ключа: {e}")


def serialize_sym_key(path: str, sym_key: bytes) -> None:
    """
    Сериализует симметричный ключ в файл.
    :param path: Путь к файлу для сохранения
    :param sym_key: Симметричный ключ
    :raises ValueError: Если ключ пустой
    :raises IOError: Если произошла ошибка записи
    """
    if not sym_key:
        raise ValueError("Симметричный ключ не может быть пустым")

    try:
        with open(path, 'wb') as f:
            f.write(sym_key)
    except IOError as e:
        raise IOError(f"Ошибка записи симметричного ключа: {e}")


def deserialize_public_key(path: str) -> rsa.RSAPublicKey:
    """
    Десериализует открытый RSA-ключ из файла.
    :param path: Путь к файлу с ключом
    :return: Открытый RSA-ключ
    :raises IOError: Если произошла ошибка чтения
    :raises ValueError: Если файл поврежден
    """
    try:
        with open(path, 'rb') as f:
            pem = f.read()
            return load_pem_public_key(pem, backend=default_backend())
    except IOError as e:
        raise IOError(f"Ошибка чтения открытого ключа: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка десериализации открытого ключа: {e}")


def deserialize_private_key(path: str) -> rsa.RSAPrivateKey:
    """
    Десериализует закрытый RSA-ключ из файла.
    :param path: Путь к файлу с ключом
    :return: Закрытый RSA-ключ
    :raises IOError: Если произошла ошибка чтения
    :raises ValueError: Если файл поврежден
    """
    try:
        with open(path, 'rb') as f:
            pem = f.read()
            return load_pem_private_key(pem, password=None, backend=default_backend())
    except IOError as e:
        raise IOError(f"Ошибка чтения закрытого ключа: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка десериализации закрытого ключа: {e}")


def deserialize_sym_key(path: str) -> bytes:
    """
    Десериализует симметричный ключ из файла.
    :param path: Путь к файлу с ключом
    :return: Симметричный ключ
    :raises IOError: Если произошла ошибка чтения
    :raises ValueError: Если файл пустой
    """
    try:
        with open(path, 'rb') as f:
            key = f.read()
            if not key:
                raise ValueError("Файл с симметричным ключом пуст")
            return key
    except IOError as e:
        raise IOError(f"Ошибка чтения симметричного ключа: {e}")