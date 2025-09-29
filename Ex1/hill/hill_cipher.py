import numpy as np

def mod_inverse(a, m):
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inv(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det % modulus, modulus)
    if det_inv is None:
        raise ValueError("Matrix determinant has no modular inverse under mod {}".format(modulus))

    matrix_mod = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * matrix_mod) % modulus

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join(chr(n + ord('A')) for n in numbers)

def pad_text(text, block_size):
    text = ''.join(c for c in text.upper() if c.isalpha())
    while len(text) % block_size != 0:
        text += 'X'
    return text

def encrypt(text, key_matrix):
    n = key_matrix.shape[0]
    text = pad_text(text, n)
    numbers = text_to_numbers(text)
    ciphertext = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext.extend(encrypted_block)
    return numbers_to_text(ciphertext)

def decrypt(ciphertext, key_matrix):
    inverse_matrix = matrix_mod_inv(key_matrix, 26)
    return encrypt(ciphertext, inverse_matrix)

# main
n = int(input("Enter size of key matrix (n): "))
print("Enter the key matrix (row by row):")
key_matrix = np.array([[int(input()) for _ in range(n)] for _ in range(n)])

try:
    plaintext = input("Enter plaintext: ")
    ciphertext = encrypt(plaintext, key_matrix)
    decrypted = decrypt(ciphertext, key_matrix)

    print("Encrypted Text:", ciphertext)
    print("Decrypted Text:", decrypted.rstrip('X'))
except ValueError as e:
    print("Error:", e)