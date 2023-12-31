# Write a Python Program to create a Database named “Store”.
# Display the List of Databases available in MySQL.


import mysql.connector as connector

try:
    conn = connector.connect(
        host='localhost',
        user='root',
        password='root'
    )
    
    cur = conn.cursor()

    cur.execute("CREATE DATABASE IF NOT EXISTS Store")

    cur.execute("SHOW DATABASES")
    databases = cur.fetchall()

    print("List of Databases:")
    for database in databases:
        print(database[0])

except connector.Error as err:
    print("Error:", err)

finally:
    if conn.is_connected():
        cur.close()
        conn.close()
