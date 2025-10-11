def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# main
num = int(input("Enter the Number (message): "))
p = int(input("Enter 1st prime number: "))
q = int(input("Enter 2nd prime number: "))

n = p * q
phi = (p - 1) * (q - 1)
print("Value of z =", phi)

# Choose e such that 1 < e < phi and gcd(e, phi) == 1
for e in range(2, phi):
    if gcd(e, phi) == 1:
        break
print("Value of e =", e)

d = mod_inverse(e, phi)
if d is None:
    raise ValueError("No modular inverse found for e.")
print("Value of d =", d)

# encryption
cipher = mod_exp(num, e, n)
print("Encrypted message is:", float(cipher))

# decryption
decrypted = mod_exp(cipher, d, n)
print("Decrypted message is", decrypted)
##################################
# Example Input/Output:
# Enter the Number (message): 12    
# Enter 1st prime number: 5
# Enter 2nd prime number: 11
# Value of z = 40
# Value of e = 3
# Value of d = 27
# Encrypted message is: 23.0
# Decrypted message is 12
##################################    