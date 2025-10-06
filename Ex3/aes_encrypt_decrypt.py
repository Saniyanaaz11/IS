from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

# Function to pad plaintext to be multiple of 16 bytes (AES block size)
def pad(text):
    padding_len = 16 - (len(text) % 16)
    return text + chr(padding_len) * padding_len

# Function to remove padding
def unpad(text):
    padding_len = ord(text[-1])
    return text[:-padding_len]

# Generate random 256-bit AES key
key = os.urandom(32)

# Generate random 128-bit IV for CBC mode
iv = os.urandom(16)

print("AES Key Generated")

# Prompt user for plaintext
plaintext = input("Enter plaintext: ")

# Pad plaintext
padded_text = pad(plaintext)

# Create AES cipher in CBC mode
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_text.encode()) + encryptor.finalize()

# Encode ciphertext as Base64
ciphertext_b64 = base64.b64encode(ciphertext).decode()

# Decrypt the ciphertext
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(base64.b64decode(ciphertext_b64)) + decryptor.finalize()
decrypted_text = unpad(decrypted_padded.decode())

# Final Output (matching your example)
print(f"Ciphertext: {ciphertext_b64}")
print(f"Decrypted Text: {decrypted_text}")
