# Manual DES (Data Encryption Standard) Implementation
# This is a from-scratch implementation of DES encryption and decryption,
# following the repo's style of manual algorithms (like RSA). No external crypto libraries are used.
# DES is a symmetric block cipher: 64-bit blocks, 56-bit effective key, 16 Feistel rounds.
# Input: Plaintext string
# Output: Base64-encoded ciphertext, then decrypted plaintext for verification
# Key: Randomly generated 8-byte (64-bit) key
# Padding: PKCS7 for variable-length input
# Mode: ECB (Electronic Codebook) for simplicity

import base64
import os

# DES Permutation and Substitution Tables
# These are standard DES tables for initial/final permutations, expansion, S-boxes, etc.
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]  # Initial Permutation
FP = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]  # Final Permutation
E = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]  # Expansion Permutation (32-bit to 48-bit)
P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]  # Permutation after S-boxes
PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]  # Permuted Choice 1 (64-bit key to 56-bit)
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]  # Permuted Choice 2 (56-bit to 48-bit subkeys)
SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]  # Left shifts for each round in key scheduling

# S-boxes: 8 substitution boxes, each 4x16 (row x column)
S_BOXES = [
    # S1
    [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
    # S2
    [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
    # S3
    [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
    # S4
    [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
    # S5
    [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
    # S6
    [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
    # S7
    [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
    # S8
    [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]

def bytes_to_bits(data):
    # Convert bytes to a list of bits (MSB first)
    bits = []
    for byte in data:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    return bits

def bits_to_bytes(bits):
    # Convert list of bits back to bytes
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte |= bits[i + j] << (7 - j)
        bytes_list.append(byte)
    return bytes(bytes_list)

def permute(bits, table):
    # Apply a permutation table to the bits
    return [bits[i - 1] for i in table]

def left_shift(bits, n):
    # Circular left shift
    return bits[n:] + bits[:n]

def generate_subkeys(key_bits):
    # Generate 16 48-bit subkeys from the 64-bit key
    key56 = permute(key_bits, PC1)
    C, D = key56[:28], key56[28:]
    subkeys = []
    for shift in SHIFTS:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        subkey = permute(C + D, PC2)
        subkeys.append(subkey)
    return subkeys

def s_box_substitute(expanded):
    # Substitute using S-boxes: 48-bit input to 32-bit output
    output = []
    for i in range(8):
        block = expanded[i * 6:(i + 1) * 6]
        row = (block[0] << 1) | block[5]
        col = (block[1] << 3) | (block[2] << 2) | (block[3] << 1) | block[4]
        val = S_BOXES[i][row][col]
        bin_val = [(val >> j) & 1 for j in range(3, -1, -1)]
        output.extend(bin_val)
    return output

def feistel(right, subkey):
    # Feistel function: expansion, XOR with subkey, S-boxes, permutation
    expanded = permute(right, E)
    xored = [a ^ b for a, b in zip(expanded, subkey)]
    substituted = s_box_substitute(xored)
    permuted = permute(substituted, P)
    return permuted

def des_encrypt_block(block_bits, subkeys):
    # Encrypt a single 64-bit block
    permuted = permute(block_bits, IP)
    L, R = permuted[:32], permuted[32:]
    for subkey in subkeys:
        new_R = [a ^ b for a, b in zip(L, feistel(R, subkey))]
        L, R = R, new_R
    combined = R + L
    ciphertext_bits = permute(combined, FP)
    return ciphertext_bits

def des_decrypt_block(block_bits, subkeys):
    # Decrypt by using subkeys in reverse order
    rev_subkeys = subkeys[::-1]
    return des_encrypt_block(block_bits, rev_subkeys)

def pad(data):
    # PKCS7 padding to make length multiple of 8 bytes
    block_size = 8
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    pad_byte = pad_len
    return data + bytes([pad_byte] * pad_len)

def unpad(data):
    # Remove PKCS7 padding
    pad_len = data[-1]
    return data[:-pad_len]

def main():
    # Main function: input plaintext, encrypt with random key, output ciphertext and decrypted text
    plaintext = input("Enter plaintext: ")
    key = os.urandom(8)  # Random 8-byte key
    key_bits = bytes_to_bits(key)
    subkeys = generate_subkeys(key_bits)
    data = plaintext.encode()
    padded = pad(data)
    ciphertext_bytes = b''
    for i in range(0, len(padded), 8):
        block = padded[i:i + 8]
        block_bits = bytes_to_bits(block)
        encrypted_bits = des_encrypt_block(block_bits, subkeys)
        encrypted_bytes = bits_to_bytes(encrypted_bits)
        ciphertext_bytes += encrypted_bytes
    ciphertext_b64 = base64.b64encode(ciphertext_bytes).decode()
    print("Ciphertext:", ciphertext_b64)
    # Decrypt
    ciphertext_bytes = base64.b64decode(ciphertext_b64)
    decrypted_bytes = b''
    for i in range(0, len(ciphertext_bytes), 8):
        block = ciphertext_bytes[i:i + 8]
        block_bits = bytes_to_bits(block)
        decrypted_bits = des_decrypt_block(block_bits, subkeys)
        decrypted_block = bits_to_bytes(decrypted_bits)
        decrypted_bytes += decrypted_block
    unpadded = unpad(decrypted_bytes)
    decrypted_text = unpadded.decode()
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()

####################################
# Example Usage:
# Input: "Information"
# Output: Ciphertext: <base64 string>, Decrypted Text: Information
####################################
