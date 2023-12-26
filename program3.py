# Write a program to calculate the nth term of Fibonacci series.

nth = int(input("Enter no. of terms to display: "))

n1, n2 = 0, 1
count = 0

if nth <= 0:
   print("Please enter a positive integer.")

else:
   print("Fibonacci sequence:")
   while count < nth:
       print(n1, end=" ")
       n = n1 + n2
       n1 = n2
       n2 = n
       count += 1
