import mysql.connector
from mysql.connector import Error

try:
    # Try connecting to MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Antaidada@2"
    )
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
else:
    # Only execute if connection succeeded
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    cursor.close()
    connection.close()
