# Diffie-Hellman Key Exchange Simulation

# Step 1: Get inputs
p = int(input("Enter a prime number (p): "))
g = int(input(f"Enter a primitive root of {p} (g): "))
a = int(input("Enter private key for Alice: "))
b = int(input("Enter private key for Bob: "))

# Step 2: Compute public keys
A = pow(g, a, p)  # Alice's public key
B = pow(g, b, p)  # Bob's public key

# Step 3: Compute shared secret keys
shared_secret_alice = pow(B, a, p)
shared_secret_bob = pow(A, b, p)

# Step 4: Display results
print(f"\nAlice's public key: {A}")
print(f"Bob's public key: {B}")
print(f"Shared secret key (computed by Alice): {shared_secret_alice}")
print(f"Shared secret key (computed by Bob): {shared_secret_bob}")
#####################################################
# Example Output:
#Enter a prime number (p): 7
#Enter a primitive root of 7 (g): 3
#Enter private key for Alice: 5
#Enter private key for Bob: 3
#
#Alice's public key: 5
#Bob's public key: 6
#Shared secret key (computed by Alice): 6
#Shared secret key (computed by Bob): 6
#####################################################