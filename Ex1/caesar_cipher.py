def encrypt(text, shift):
    return ''.join(
        chr((ord(c) - base + shift) % 26 + base) if c.isalpha() else c
        for c in text
        for base in [ord('A') if c.isupper() else ord('a')] if c.isalpha() or True
    )

decrypt = lambda text, shift: encrypt(text, 26 - shift)

if __name__ == "__main__":
    text = input("Enter the plaintext: ")
    shift = int(input("Enter the key value: "))
    print("Encrypted Text is ", cipher := encrypt(text, shift))
    print("Decrypted Text is ", decrypt(cipher, shift))
####################################
# Example usage:
# Input: "Hello", Key: 1
# Output: "Ifmmp" (Encrypted), "Hello" (Decrypted)
####################################
#  Sample Input/Output:
####################################
#Enter the plaintext: Hello
#Enter the key value: 1
#Encrypted Text is Ifmmp
#Decrypted Text is Hello
####################################