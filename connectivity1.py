import mysql.connector as connector

conn = connector.connect(
    host='localhost',
    user='root',
    password='root'
)

cur = conn.cursor()

try:
    cur.execute("CREATE DATABASE IF NOT EXISTS Store")

    cur.execute("SHOW DATABASES")
    databases = cur.fetchall()

    print("List of Databases:")
    for database in databases:
        print(database[0])

except connector.Error as err:
    print("Error:", err)

finally:
    cur.close()
    conn.close()
