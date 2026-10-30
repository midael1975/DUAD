import psycopg2
import csv
import os
from datetime import datetime

DB_CONFIG = {
    "dbname": "lyfter_rental_cars",
    "user": "postgres",
    "password": "midael#1975",
    "host": "localhost",
    "port": 5432
}

def create_backup():
    # Create a backup of the database tables and save it as a CSV file
    backup_folder = "db_backups"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        print(f"Backup folder '{backup_folder}' created.")

    # Get the current date for the backup file name
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Define the tables to back up
    tables_to_export = ["users", "cars", "rentals"]

    connection = None
    try:
        # Connect to the PostgreSQL database
        print("Connecting to the PostgreSQL database...")
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Create a backup for each table
        for table in tables_to_export:
            file_path = os.path.join(backup_folder, f"{table}_backup_{current_date}.csv")

        # Query to select all data from the users table
        query = (f"SELECT * FROM lyfter_car_rental.{table}")
        cursor.execute(query)

        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        # Write the data to a CSV file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header
            writer.writerow(column_names)
            # Write the data rows
            writer.writerows(rows)

        print(f"Backup created successfully: {file_path}")
        cursor.close()

    except Exception as e:
        print(f"Error creating backup: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    create_backup()