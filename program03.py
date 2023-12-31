# Write a program to calculate the nth term of Fibonacci series.

try:
    n = int(input("Enter no. of terms to display: "))
    if n <= 0:
        print("Please enter a positive integer.")

    else:
        terms = ['0', '1']
        sum = 1 
  
        for i in range(1, n-1):
            a = int(terms[i-1]) 
            b = int(terms[i]) 
            next = a + b 
  
            terms.append(str(next)) 
            sum += next 
 
        print('Fabonacci series:', ", ".join(terms))

except ValueError: 
    print("Number must be an integer.")
