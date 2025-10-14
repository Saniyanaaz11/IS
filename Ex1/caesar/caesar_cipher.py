def encrypt(text, shift):
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return ''.join(result)

def decrypt(text, shift):
    return encrypt(text, 26 - shift)

def main():
    plaintext = input("Enter plaintext: ")
    shift = int(input("Enter shift key (1-25): "))
    ciphertext = encrypt(plaintext, shift)
    print("Ciphertext:", ciphertext)
    decrypted_text = decrypt(ciphertext, shift)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
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
