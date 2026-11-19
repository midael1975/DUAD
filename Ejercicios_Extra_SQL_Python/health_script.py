import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "lyfter_car_rental",
    "user": "postgres",
    "password": "midael#1975",
    "port": 5432
}


def check_system_health():

    conn = None
    cursor = None

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        required_tables = [
            "users",
            "cars",
            "rentals"
        ]

        for table in required_tables:

            cursor.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM pg_tables
                    WHERE schemaname = 'public'
                    AND tablename = %s
                )
            """, (table,))

            exists = cursor.fetchone()[0]

            if not exists:
                print(f"DB ERROR. Table '{table}' does not exist.")
                return

        cursor.execute("""
            SELECT COUNT(*)
            FROM cars
            WHERE car_status = 'AVAILABLE'
        """)

        available_cars = cursor.fetchone()[0]

        if available_cars >= 1:
            print("DB OK. System operating normally")
        else:
            print("DB ERROR. No cars available")

    except Exception as e:
        print(f"DB ERROR. {e}")

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


if __name__ == "__main__":
    check_system_health()