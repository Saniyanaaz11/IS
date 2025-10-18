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
##################################################
# Example Output:
#ECC Key Pair Generated (secp256k1)
#Public Key (hex): 030ac1de3a90225837b140ee8c992e479b59cdd8cf4af8ad5106408a1335668d3b
#Private Key (hex): 48eb02d2fc82b6c4e47d623634511fb081d916236dd9014766057e2f5ec5035c
#
#Enter plaintext to encrypt: ECC
#
#Encrypted Ciphertext (hex): 0456e4e4a91e43dfc760d2c9d284f7e03a2f110b27d3419f2b7e7c28e3bca6878f953d2e8c2e6959cc5545c91573f3e9a3456825e3b8ebbc4fb7ceba30450ccc18b8011f8f39a7d90576a2990cbe6883027ad6dd8e35030874b13bb210021e28554599fa
#
#Decrypted Text: ECC
##################################################