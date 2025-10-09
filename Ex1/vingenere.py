def vigenere_encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = key.upper()
    result = []
    for i, ch in enumerate(text):
        shift = ord(key[i % len(key)]) - ord('A')
        result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
    return ''.join(result)

def vigenere_decrypt(text, key):
    key = key.upper()
    result = []
    for i, ch in enumerate(text):
        shift = ord(key[i % len(key)]) - ord('A')
        result.append(chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A')))
    return ''.join(result)

# Main
plain = input("Enter the plaintext: ")
key = input("Enter the key: ")
cipher = vigenere_encrypt(plain, key)
print("Ciphertext:", cipher)
print("Decrypted Text:", vigenere_decrypt(cipher, key))
###############################
#Example Usage:
#Enter the plaintext: vigenere
#Enter the key: encrypt
#Ciphertext: ZVIVLTKI
#Decrypted Text: VIGENERE
#################################