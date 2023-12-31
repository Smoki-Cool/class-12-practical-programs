# Write a Python Program to Insert Records in “Product” table. Display all records.


import mysql.connector as connector

def insert_product_records():
    num_products = int(input("Enter no. of products you want to insert: "))

    for n in range(num_products):
        print("\nEnter details for Product", n + 1 + ": ")
        product_name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        discount = float(input("Enter Discount: "))

        query = '''INSERT INTO Products VALUES 
                ({0}, {1}, {2}, {3})'''.format(product_name, category, price, discount)

        cur.execute(query)
        conn.commit()

        print("Record inserted successfully.")

def display_all_records():
    cur.execute("SELECT * FROM Products")
    records = cur.fetchall()
    
    print("\nAll Records in 'Products' table:")
    for record in records:
        print(record)

try:
    conn = connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='Store'
    )

    cur = conn.cursor()
    
    insert_product_records()
    display_all_records()

except connector.Error as err:
    print("Error:", err)

finally:
    if conn.is_connected():
        cur.close()
        conn.close()
