## 🧩 Lab Exercises - Ex1: Classical Ciphers

### Caesar Cipher

The Caesar cipher is a classical encryption technique where each letter in the plaintext is shifted by a fixed number of positions down the alphabet.

**Features:**
- Encrypts and decrypts text using a shift key.
- Handles uppercase, lowercase, and non-alphabetic characters (punctuation, numbers, spaces remain unchanged).
- Command-line interface for easy testing.

Examples :

python ./caesar/Caesar_Improved.py encrypt "HELLO WORLD" 3
# Output: KHOOR ZRUOG

python ./caesar/Caesar_Improved.py decrypt "KHOOR ZRUOG" 3
# Output: HELLO WORLD

The shift key can be any integer (key > 26 wraps around).

Non-alphabetic characters are not modified.
