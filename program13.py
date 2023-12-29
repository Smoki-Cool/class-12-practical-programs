# Create a binary file “Employee.dat” with emp id, name and salary. Write a function 
# Update_Sal(empid), receive an employee id and update the salary.


import pickle


def create():
    empdata = {
        101: {"Name": "Thor", "Salary": 99000},
        102: {"Name": "Spiderman", "Salary": 60000},
        103: {"Name": "Ironman", "Salary": 999999},
        104: {"Name": "Hulk", "Salary": 60000},
        105: {"Name": "Capt America", "Salary": 80000}
        }

    with open('Employee.dat', 'wb') as file:
        pickle.dump(empdata, file)


def update_salary(empid, new_salary):
    try:
        with open('Employee.dat', 'rb') as file:
            data = pickle.load(file)
            if empid in data:
                data[empid]['Salary'] = new_salary
                with open('Employee.dat', 'wb') as file:
                    pickle.dump(data, file)
                	print(f"Salary updated for Employee ID {empid}")
            else:
                print("Employee ID not found.")
    except FileNotFoundError:
        print("Employee data file not found.")


create()

empid = int(input("Enter Employee ID: "))
new_salary = int(input("Enter new salary: "))

update_salary(empid, new_salary)
