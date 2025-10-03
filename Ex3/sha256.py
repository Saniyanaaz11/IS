import hashlib


def get_sha256_hash(input_string):
    """
    Calculates the SHA-256 hash of a given string.

    Args:
        input_string (str): The string to hash.

    Returns:
        str: The 256-bit hash as a hexadecimal string.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode("utf-8"))

    return sha256_hash.hexdigest()


if __name__ == "__main__":
    user_input = input("Enter string to hash (SHA-256): ")
    hashed_string = get_sha256_hash(user_input)

    print(f"SHA-256 Hash: {hashed_string}")
#####################################
# Example Usage:
# Enter string to hash (SHA-256): asd
# SHA-256 Hash: 688787d8ff144c502c7f5cffaafe2cc588d86079f9de88304c26b0cb99ce91c6
#####################################