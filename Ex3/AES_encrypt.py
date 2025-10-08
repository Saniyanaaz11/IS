from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import os

# Generate AES key and IV
key = os.urandom(16)  # 128-bit key
iv = os.urandom(16)   # Initialization vector

def encrypt(plaintext):
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded) + encryptor.finalize()

    return b64encode(iv + encrypted).decode()

def decrypt(ciphertext):
    raw = b64decode(ciphertext)
    iv, encrypted = raw[:16], raw[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

    return decrypted.decode()

# Main
text = input("Enter plaintext: ")
ciphertext = encrypt(text)
print("Ciphertext:", ciphertext)

decrypted = decrypt(ciphertext)
print("Decrypted Text:", decrypted)
