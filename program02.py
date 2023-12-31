# Write a python program to take numbers from the user and check if it is prime or not.

import math

def isprime(n: int):
    if n == 1:
        print(n, "is not a prime number")
    elif n > 1:
        for i in range(2, math.floor(math.sqrt(n)+1)):
            if (n % i) == 0:
                 return False
        return True

try:
    n = int(input("Enter a number: "))
    if isprime(n):
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

except ValueError:
    print("Number must be an integer.")
