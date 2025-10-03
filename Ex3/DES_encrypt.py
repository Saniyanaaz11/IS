from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    encrypted_bytes = cipher.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(base64.b64decode(ciphertext))
    return decrypted_bytes.decode('utf-8').rstrip()

def main():
    plaintext = input("Enter plaintext: ")
    key = get_random_bytes(8) 
    
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
    
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()