from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

# Step 1: Key Generation
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Step 2: Signing the Message
def sign_message(private_key, message):
    message_bytes = message.encode('utf-8')
    signature = private_key.sign(
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Step 3: Verifying the Signature
def verify_signature(public_key, message, signature):
    message_bytes = message.encode('utf-8')
    try:
        public_key.verify(
            signature,
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

# Main Program
if __name__ == "__main__":
    print("Digital Signature Verification Demo")
    
    # User inputs the message
    user_message = input("Enter the message to sign: ")

    # Generate keys
    private_key, public_key = generate_keys()

    # Sign the message
    signature = sign_message(private_key, user_message)
    print("\nMessage signed successfully.")

    # Verify the signature
    is_valid = verify_signature(public_key, user_message, signature)
    print("Verifying signature...")
    print("Signature valid:", is_valid)
###############################################
# Example Output:
#Digital Signature Verification Demo
#Enter the message to sign: Hello, this is a test message.
#Message signed successfully.
#Verifying signature...
#Signature valid: True
###############################################