# Write a Python program to demonstrate the concept of variable length argument
# to calculate the product and power of the first 10 numbers.

def cproduct(*args):
	product = 1
	for n in args:
		product *= n
		
	return product

def cpower(power=1, *args):
	return [str(n ** power) for n in args]


numbers = list(range(1, 11))

rproduct = cproduct(*numbers)
rpower = cpower(2, *numbers)

print("Product of the first 10 numbers:", rproduct)
print("Power of the first 10 numbers(squared):", ", ".join(rpower))
