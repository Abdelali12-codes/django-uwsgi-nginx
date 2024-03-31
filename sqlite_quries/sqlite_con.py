import sqlite3
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def list_tables():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(os.path.join(BASE_DIR,'django-uwsgi-nginx/db.sqlite3'))
        cursor = conn.cursor()

        # Execute a query to fetch table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Print the list of tables
        print("List of Tables:")
        for table in tables:
            print(table[0])

        # Close the cursor and connection
        cursor.close()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)


def fetch_session():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(os.path.join(BASE_DIR,'django-uwsgi-nginx/db.sqlite3'))
        cursor = conn.cursor()

        # Execute a query to fetch table names
        cursor.execute("SELECT * FROM django_session;")
        sessions = cursor.fetchall()
        for session in sessions:
            print(session)
            print("\n")
        cursor.close()
        conn.close()

    except sqlite3.Error as e:
        print("Error", e)

def columns_names_of_table():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(os.path.join(BASE_DIR,'django-uwsgi-nginx/db.sqlite3'))
        cursor = conn.cursor()

        # Execute a query to fetch table names
        cursor.execute("PRAGMA table_info(django_session);")
        columns_info = cursor.fetchall()

        # Print column names
        print("Column Names:")
        for column_info in columns_info:
            print(column_info[1])  # Column name is in the second position


        cursor.close()
        conn.close()

    except sqlite3.Error as e:
        print("Error", e)
