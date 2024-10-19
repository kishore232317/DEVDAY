# Function to check if a number is prime
def is_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return False

    # Check for factors from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is prime and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
