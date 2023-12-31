# Write a python program to create binary file to store Employee Name, Employee code 
# and take input from user to display name of the employee if employee code is found in 
# the file otherwise display “Employee not found”

import pickle

def create():
    empdata = {
        101: "Thor",
        102: "Spiderman",
        103: "Ironman",
        104: "Hulk",
        105: "Capt America"
    }

    with open('empdata.bin', 'wb') as file:
        pickle.dump(empdata, file)

def search(empcode):
    try:
        with open('empdata.bin', 'rb') as file:
            data = pickle.load(file)
            if empcode in data:
                print("Employee Name:", data[empcode])
            else:
                print("Employee not found.")
    except FileNotFoundError:
        print("Employee data file not found.")
        
create()

empcode = int(input("Enter Employee Code: "))
search(empcode)
