# Write a python program to create a binary file to store RollNo, Name and marks of the 
# student. Take input from the user to update the marks of the entered Rollno.

import pickle

def create():
    data = {
        101: {"Name": "Thor", "Marks": 99},
        102: {"Name": "Spiderman", "Marks": 93},
        103: {"Name": "Ironman", "Marks": 95},
        104: {"Name": "Hulk", "Marks": 80},
        105: {"Name": "Capt America", "Marks": 85}
    }

    with open('student_data.bin', 'wb') as file:
        pickle.dump(data, file)

def update_marks(roll, new_marks):
    try:
        with open('student_data.bin', 'rb') as file:
            data = pickle.load(file)
            if roll in data:
                data[roll]['Marks'] = new_marks
                with open('student_data.bin', 'wb') as file:
                    pickle.dump(data, file)
                print("Marks updated for Roll Number", roll)
            else:
                print("Roll Number not found.")
    except FileNotFoundError:
        print("Student data file not found.")

create()

roll = int(input("Enter Roll Number: "))
new_marks = int(input("Enter new Marks: "))

update_marks(roll, new_marks)
