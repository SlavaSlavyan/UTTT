import os
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

class SLL:

    def derive_key(password: str, salt: bytes, iterations: int = 1_000_000) -> bytes:
        """Генерация ключа с использованием PBKDF2HMAC"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=64,
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )
        return kdf.derive(password.encode('utf-8'))

    def encrypt_data(data: list, password: str, output_file: str) -> None:
        # Генерация соли
        salt = os.urandom(32)
        
        # Генерация ключа
        key = SLL.derive_key(password, salt)
        encryption_key = key[:32]
        auth_key = key[32:]
        
        # Генерация IV
        iv = os.urandom(16)
        
        # Шифрование данных
        cipher = Cipher(
            algorithms.AES(encryption_key),
            modes.CBC(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        
        # Сериализация и дополнение данных
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(json.dumps(data).encode()) + padder.finalize()
        
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # Создание HMAC для аутентификации
        h = hashes.Hash(hashes.SHA512(), backend=default_backend())
        h.update(auth_key + iv + ciphertext)
        hmac = h.finalize()
        
        # Сохранение всех параметров в файл
        with open(output_file, 'wb') as f:
            f.write(salt)
            f.write(iv)
            f.write(hmac)
            f.write(ciphertext)

    def decrypt_data(input_file: str, password: str) -> list:
        with open(input_file, 'rb') as f:
            salt = f.read(32)
            iv = f.read(16)
            hmac = f.read(64)
            ciphertext = f.read()
        
        # Генерация ключа
        key = SLL.derive_key(password, salt)
        encryption_key = key[:32]
        auth_key = key[32:]
        
        # Проверка HMAC
        h = hashes.Hash(hashes.SHA512(), backend=default_backend())
        h.update(auth_key + iv + ciphertext)
        calculated_hmac = h.finalize()
        
        if calculated_hmac != hmac:
            raise ValueError("Invalid password or corrupted data")
        
        # Дешифровка
        cipher = Cipher(
            algorithms.AES(encryption_key),
            modes.CBC(iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Удаление дополнения
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        
        return json.loads(data.decode())