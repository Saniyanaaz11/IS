def primality_test(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

def main():
    number = int(input("Enter number to test primality: "))
    result = primality_test(number)
    print("Primality Test Result:", result)

if __name__ == "__main__":
    main()
#################################################
# Example Output:
#Enter number to test primality: 29
#Primality Test Result: Prime
###################################################