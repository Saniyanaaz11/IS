from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets
 
def ecc_point_to_256_bit_key(point):
    sha = hashlib.sha256(int(point.x).to_bytes(32, "big"))
    return sha.digest()

def encrypt_AES_GCM(msg, secretKey):
    cipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = cipher.encrypt_and_digest(msg)
    return (cipher.nonce, authTag, ciphertext)

def decrypt_AES_GCM(encryptedMsg, secretKey):
    (nonce, authTag, ciphertext) = encryptedMsg
    cipher = AES.new(secretKey, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

def encrypt_ECC(msg, pubKey, curve):
    # Generate ephemeral key pair
    privKey = secrets.randbelow(curve.field.n)
    sharedECCKey = privKey * pubKey
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)

    encryptedMsg = encrypt_AES_GCM(msg.encode("utf-8"), secretKey)
    pubKeyEph = privKey * curve.g
    return (encryptedMsg, pubKeyEph)

def decrypt_ECC(encryptedMsg, privKey, curve):
    (ciphertext, pubKeyEph) = encryptedMsg
    sharedECCKey = privKey * pubKeyEph
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)
    decryptedMsg = decrypt_AES_GCM(ciphertext, secretKey)
    return decryptedMsg.decode("utf-8")

if __name__ == "__main__":
    curve = registry.get_curve('secp256r1')

    # Generate key pair
    privKey = secrets.randbelow(curve.field.n)
    pubKey = privKey * curve.g

    print("ECC Key Pair Generated")
    print("Public Key (hex):", pubKey.x.to_bytes(32, "big").hex())
    print("Private Key (hex):", hex(privKey)[2:])

    plaintext = input("\nEnter plaintext to encrypt: ")

    encryptedMsg, pubKeyEph = encrypt_ECC(plaintext, pubKey, curve)
    (nonce, authTag, ciphertext) = encryptedMsg

    full_cipher_hex = (
        nonce.hex() + authTag.hex() + ciphertext.hex() + pubKeyEph.x.to_bytes(32, "big").hex()
    )
    print("\nEncrypted Ciphertext (hex):", full_cipher_hex)
#################################################
#Example Usage:
#ECC Key Pair Generated
#Public Key (hex): fdb6e0771b8dd8c6e737abed8495edca8386638de912b32394738305f1248bae
#Private Key (hex): 1d32a22fc41438119a8ade5a00e66c94d500ba886250179825860f24a863eaa1
#
#Enter plaintext to encrypt: ECC
#
#Encrypted Ciphertext (hex): c7e37b90033ee5fd68c173829b3a5a61c9e9704e64f45cd2d538385cd2f8d144e423c4855e1e515611870b0e145105341a1d9c2ac3c54bd247717b7410d74c82de9969
##################################################