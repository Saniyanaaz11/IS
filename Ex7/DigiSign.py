from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

# Generate RSA key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Get message from user
message = input("Enter your message: ").encode()

# Sign the message
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# Verify the signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Signature is valid. Message is authentic and unchanged.")
except:
    print("Signature is invalid. Message may have been tampered with.")
###############################################
# Example Output:
#Enter your message: Hello, this is a test message.
#Signature is valid. Message is authentic and unchanged.
###############################################