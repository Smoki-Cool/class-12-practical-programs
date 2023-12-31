# Write a Python program to Create a Table name “Products” under database “Store”
# containing Product name, category, price, and discount.


import mysql.connector as connector

def create_products_table():
    try:
        conn = connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='Store'
        )

        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                Product_Name VARCHAR(20) NOT NULL,
                Category VARCHAR(20),
                Price DECIMAL(10, 2),
                Discount DECIMAL(3, 2)
            )
        ''')

        print("Table 'Products' created successfully.")

    except connector.Error as err:
        print("Error:", err)

    finally:
        if conn.is_connected():
            cur.close()
            conn.close()

create_products_table()
