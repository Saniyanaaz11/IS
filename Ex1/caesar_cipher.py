def encrypt(text, shift):
    return ''.join(
        chr((ord(c) - base + shift) % 26 + base) if c.isalpha() else c
        for c in text
        for base in [ord('A') if c.isupper() else ord('a')] if c.isalpha() or True
    )

decrypt = lambda text, shift: encrypt(text, 26 - shift)

if __name__ == "__main__":
    shift = int(input("Enter shift key (1-25): "))
    text = input("Enter plaintext: ")
    print("Ciphertext:", cipher := encrypt(text, shift))
    print("Decrypted Text:", decrypt(cipher, shift))
####################################
# Example usage:
# Input: "Hello", Key: 1
# Output: "Ifmmp" (Encrypted), "Hello" (Decrypted)
####################################
#  Sample Input/Output:
####################################
#Enter plaintext: Hello
#Enter shift key (1-25): 1
#Ciphertext: Ifmmp
#Decrypted Text: Hello
####################################