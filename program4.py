# Write a random number generator that generates random numbers between 1 and 6.

import random

def generator():
    return random.randint(1, 6)

random_n = generator()
print(random_n)
