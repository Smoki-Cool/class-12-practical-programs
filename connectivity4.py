# Write a Python program to increase the price of product whose name contains
# alphabet ‘a’ in it. Also display a message how many records are updated.


import mysql.connector as connector

def increase_price(percent):
    try:
        conn = connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='Store'
        )

        cur = conn.cursor()

        query = '''
            UPDATE Products
            SET Price = Price * {0}
            WHERE Product_Name LIKE '%a%'
        '''.format(1 + percent/100)

        cur.execute(query)
        conn.commit()
      
        updated_count = cur.rowcount

        print(updated_count, "records updated successfully.")

        cur.execute("SELECT * FROM Products")
        records = cur.fetchall()

        print("\nAll Records in 'Products' table:")
        for record in records:
            print(record)

    except connector.Error as err:
        print("Error:", err)

    finally:
        if conn.is_connected():
            cur.close()
            conn.close()
          
percent = float(input("Enter the percentage by which you want to change the price: ))
increase_price(percent)
