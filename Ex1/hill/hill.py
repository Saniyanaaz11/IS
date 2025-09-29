def mod_inverse(a, m):
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def get_cofactor(matrix, p, q):
    size = len(matrix)
    return [
        [matrix[i][j] for j in range(size) if j != q]
        for i in range(size) if i != p
    ]

def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for c in range(size):
        cofactor = get_cofactor(matrix, 0, c)
        det += ((-1) ** c) * matrix[0][c] * determinant(cofactor)
    return det

def adjoint(matrix):
    size = len(matrix)
    adj = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            cofactor = get_cofactor(matrix, i, j)
            sign = (-1) ** (i + j)
            adj[j][i] = sign * determinant(cofactor)
    return adj

def inverse_matrix(matrix, mod):
    det = determinant(matrix)
    det %= mod
    inv_det = mod_inverse(det, mod)
    if inv_det is None:
        raise ValueError("Matrix is not invertible under mod {}".format(mod))
    adj = adjoint(matrix)
    size = len(matrix)
    inv = [[(adj[i][j] * inv_det) % mod for j in range(size)] for i in range(size)]
    return inv

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join(chr(n + ord('A')) for n in numbers)

def pad_text(text, block_size):
    text = ''.join(c for c in text.upper() if c.isalpha())
    while len(text) % block_size != 0:
        text += 'X'
    return text

def multiply_matrix_vector(matrix, vector, mod):
    size = len(matrix)
    result = []
    for row in matrix:
        val = sum(row[i] * vector[i] for i in range(size)) % mod
        result.append(val)
    return result

def encrypt(text, key_matrix):
    block_size = len(key_matrix)
    text = pad_text(text, block_size)
    numbers = text_to_numbers(text)
    ciphertext = []
    for i in range(0, len(numbers), block_size):
        block = numbers[i:i+block_size]
        encrypted_block = multiply_matrix_vector(key_matrix, block, 26)
        ciphertext.extend(encrypted_block)
    return numbers_to_text(ciphertext)

def decrypt(ciphertext, key_matrix):
    inverse_key = inverse_matrix(key_matrix, 26)
    return encrypt(ciphertext, inverse_key)

# main
n = int(input("Enter size of key matrix (n): "))
print("Enter the key matrix (row by row):")
key_matrix = [[int(input()) for _ in range(n)] for _ in range(n)]

try:
    plaintext = input("Enter plaintext: ")
    ciphertext = encrypt(plaintext, key_matrix)
    decrypted = decrypt(ciphertext, key_matrix)

    print("Encrypted Text:", ciphertext)
    print("Decrypted Text:", decrypted.rstrip('X'))
except ValueError as e:
    print("Error:", e)
