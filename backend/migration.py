import mysql.connector
import os

# MySQL connection configuration
db_config = {
    "host": "db",
    "user": "root",
    "password": "rootpassword",
    "database": "testdb",
}

# SQL for creating the table
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
"""

def run_migration():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE_QUERY)
        conn.commit()
        print("Migration completed: Table 'items' created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    run_migration()
