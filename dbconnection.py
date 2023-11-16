import sqlite3

def drop_table(table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    try:
        # Drop the specified table
        cursor.execute(f"DROP TABLE {table_name}")
        print(f"Table {table_name} dropped successfully.")
    except sqlite3.Error as e:
        print(f"Error dropping table {table_name}: {e}")
    finally:
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

def list_tables():
    # Connect to the SQLite database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    try:
        # Retrieve the list of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Print the list of tables
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")
    except sqlite3.Error as e:
        print(f"Error listing tables: {e}")
    finally:
        # Close the connection
        conn.close()

import os
import django

# Set the environment variable to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DroneMotionPlannerApp.settings")
django.setup()

def delete_all_rows_from_table(db_file, table_name):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Execute a DELETE query to delete all rows from the specified table
        cursor.execute(f"DELETE FROM {table_name}")

        # Commit the changes to the database
        connection.commit()

        print(f"All rows deleted from {table_name}.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if connection:
            connection.close()

# Replace 'your_db_file.sqlite3' and 'your_table_name' with your actual database file and table name
# delete_all_rows_from_table('db.sqlite3', 'PathCalculator_hiddenobstacle')
# delete_all_rows_from_table('db.sqlite3', 'PathCalculator_obstacle')
delete_all_rows_from_table('db.sqlite3', 'PathCalculator_droneflightpath')
# Call the function to list tables
# list_tables()
# Replace 'your_table_name' with the actual name of the table you want to drop
# drop_table('PathCalculator_droneflightpath')
