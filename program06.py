# Write a program to accept the number of days and display appropriate weeks in an 
# integer. Display an appropriate error message if input is not an integer. Handle the 
# errors including the finally clause.

try:
	days = int(input("Enter no. of days: "))
	weeks = days//7
	d = "day" if days == 1 else "days"
	w = "week" if weeks == 1 else "weeks"
	print("There are {0} {1} in {2} {3}.".format(weeks, w, days, d))
	
except ValueError:
    print("Please input a valid integer for no. of days")
		
finally:
	print("Execution completed.")
