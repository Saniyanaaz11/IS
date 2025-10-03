print("Diffie-Hellman Key Exchange Setup")

p = int(input("Enter a prime number (p): "))
g = int(input(f"Enter a primitive root of {p} (g): "))

a = int(input("Enter private key for Alice (a): "))
b = int(input("Enter private key for Bob (b): "))

print("\nKey Exchange Process")

A = pow(g, a, p) 
B = pow(g, b, p)

print(f"Alice's Public Key (A): {A}")
print(f"Bob's Public Key (B): {B}")

print("\nShared Secret Computation")

K_alice = pow(B, a, p)

K_bob = pow(A, b, p)

print(f"Shared secret key (computed by Alice): {K_alice}")
print(f"Shared secret key (computed by Bob): {K_bob}")

if K_alice == K_bob:
    print("\nVerification: The shared secret keys match!")
else:
    print("\nVerification: ERROR! The shared secret keys DO NOT match.")
