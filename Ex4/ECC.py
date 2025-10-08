from ecies.utils import generate_key
from ecies import encrypt, decrypt
import binascii

# Step 1: Generate ECC key pair using secp256k1
key = generate_key()
private_key_hex = key.to_hex()
public_key_hex = key.public_key.format(True).hex()

print("\nECC Key Pair Generated (secp256k1)")
print("Public Key (hex):", public_key_hex)
print("Private Key (hex):", private_key_hex)

# Step 2: Get plaintext input from user
plaintext = input("\nEnter plaintext to encrypt: ").encode()

# Step 3: Encrypt using public key
ciphertext = encrypt(public_key_hex, plaintext)
ciphertext_hex = binascii.hexlify(ciphertext).decode()
print("\nEncrypted Ciphertext (hex):", ciphertext_hex)

# Step 4: Decrypt using private key
decrypted = decrypt(private_key_hex, ciphertext)
print("\nDecrypted Text:", decrypted.decode())
