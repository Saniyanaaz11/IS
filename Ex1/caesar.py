letters = 'abcdefghijklmnopqrstuvwxyz'

print("Enter the plaintext:")
plainText = input().lower()

print("Enter the key value:")
try:
    key = int(input())
except ValueError:
    print("Invalid key. Please enter a number.")
    exit()

# Encryption Logic
cipherText = ''
for char in plainText:
    if char in letters:
        index = letters.index(char)
        shiftedIndex = (index + key) % 26
        cipherText += letters[shiftedIndex]
    else:
        cipherText += char

print("\nEncrypted Text:")
print(cipherText)

# Decryption Logic
decryptedText = ''
for char in cipherText:
    if char in letters:
        index = letters.index(char)
        shiftedIndex = (index - key) % 26
        decryptedText += letters[shiftedIndex]
    else:
        decryptedText += char

print("\nDecrypted Text:")
print(decryptedText)
   
# Example usage:
# Input: "Hello", Key: 1
# Output: "ifmmp" (Encrypted), "hello" (Decrypted)
####################################
#  Sample Input/Output:
####################################
# Enter the plaintext:
#Hello
#Enter the key value:
#1

#Encrypted Text:
#ifmmp

#Decrypted Text:
#hello
####################################