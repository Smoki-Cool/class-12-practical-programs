# Final Practical Python Programs and SQL Queries

This repository contains Python programs developed for my final practical file in CBSE Class 12th. These programs showcase my understanding and application of various concepts covered during the course.

## Usage

No extra installations are needed to run the python programs. However, `mysql-connector-python` module is required to run the python-sql connectivity programs.

## Python Programs

### 1. [Factorial Calculator](/program01.py)
- This program calculates the factorial of a user-input number using functions.

### 2. [Prime Number Checker](/program02.py)
- This program checks if a user-input number is prime or not.

### 3. [Fibonacci Series](/program03.py)
- Calculates the nth term of the Fibonacci series.

### 4. [Random Number Generator](/program04.py)
- Generates random numbers between 1 and 6.

### 5. [Variable-Length Arguments](/program05.py)
- Demonstrates variable-length arguments to calculate the product and power of the first 10 numbers.

### 6. [Days to Weeks Converter](/program06.py)
- Accepts the number of days, converts it to weeks, and handles errors including the `finally` clause.

### 7. [Word Search in String](/program07.py)
- Searches for a user-provided word in a given string or sentence.

### 8. [File Content Display](/program08.py)
- Reads and displays file content line by line with words separated by '*'.

### 9. [Uppercase and Lowercase Counter](/program09.py)
- Reads file content and displays the total number of uppercase and lowercase characters.

### 10. [Employee Database](/program10.py)
- Creates a binary file to store Employee Name and Employee Code, allowing the user to display employee names based on the entered code.

### 11. [Student Database](/program11.py)
- Creates a binary file to store RollNo, Name, and marks of students, allowing the user to update marks based on the entered RollNo.

### 12. [File Content Filter](/program12.py)
- Reads file content line by line and writes it to another file, excluding lines containing the letter 'o'.

### 13. [Employee Salary Updater](/program13.py)
- Creates a binary file with emp id, name, and salary, provides a function to update the salary based on employee id.

### 14. [Cursor Position](/program14.py)
- Prints cursor position and text according to specific specifications.

### 15. [Stack Implementation](/program15.py)
- Implements a stack in Python using a list.

## [SQL Queries](/queries.sql)

### 1. Movie Database
- Creates a database MOVIE_DATABASE with a table MOVIE and performs various operations on it.

### 2. Movie Queries
- Performs queries on the MOVIE table to retrieve information about movies.

### 3. Movie Yearly Statistics
- Retrieves yearly statistics from the MOVIE table.

### 4. Movie Updates
- Updates records in the MOVIE table.

### 5. Review Queries
- Performs queries on the Review table based on movie ratings and collection.

## Python-SQL Connectivity Programs

### 1. [Database Creation and Listing](/connectivity1.py)
- Creates a database named "Store" and displays the list of databases available in MySQL.

### 2. [Products Table Creation](/connectivity2.py)
- Creates a table named "Products" under the "Store" database with columns for Product name, category, price, and discount.

### 3. [Product Records Insertion](/connectivity3.py)
- Description: Inserts records into the "Products" table and displays all records.

### 4. [Price Increase for 'a'-Containing Products](/connectivity4.py)
- Increases the price of products whose names contain the alphabet 'a' and displays the number of updated records.

## Running the Programs

To run a specific program, navigate to its directory and execute the following command:

```bash
python program_name.py
```

Replace `program_name.py` with the name of the Python file you want to run.

## Running the SQL Queries

1. **MySQL Command-Line:**
   - Open a terminal or command prompt.
   - Connect to your MySQL server using the following command, replacing `[username]` with your MySQL username and `[password]` with your password:

     ```bash
     mysql -u [username] -p
     ```

   - Enter your password when prompted.

3. **Execute SQL Script:**
   - Run the SQL script using the following command, replacing `[path/to/sql/script.sql]` with the path to your SQL script:

     ```bash
     source /path/to/sql/script.sql
     ```

> [!WARNING]
> The `Review` table creation queries needed to run the last sets of queries is not provided in the script.

## License

This repository is licensed under the [MIT License](/LICENSE).

## Author

Jairaj K. Bhuyan (GitHub: Smoki-Cool)
