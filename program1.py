# Write a python program using functions to take input from the user and calculate the factorial of the number.

def factorial(n: int):
    if n == 1:
        return 1
    
    else:
        return n*factorial(n-1)

try:
    n = int(input("Enter your number: "))
    print(f"{n}! = {factorial(n)}")
    
except ValueError:
    print("Number must be an integer.")
