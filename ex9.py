import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

try:
    n = int(input("Enter a number: "))
    if n < 2:
        print("Not prime")
        exit()
except ValueError:
    print("Invalid input! Please enter an integer.")
    exit()

print('Prime' if is_prime(n) else 'Not prime')
