import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Connect to MySQL server and create the database 'alxbookstore' if it doesn't exist.
    """
    connection = None
    cursor = None
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Antaidada@2"
        )

        if connection.is_connected():
            print("Connected to MySQL server successfully.")

        # Create a cursor to execute SQL statements
        cursor = connection.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        print("Database 'alxbookstore' created successfully!")

    except Error as e:
        # Handle any errors that occur during connection or execution
        print(f"Error: {e}")

    finally:
        # Close cursor and connection safely
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()


