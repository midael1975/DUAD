import psycopg2
from psycopg2.extras import RealDictCursor


class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            print("Connection created succesfully")

    def create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port,
            )

            connection.autocommit = True  # Set autocommit mode
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None

    def close_connection(self):
        if self.connection:
            self.connection.close()
        print("Connection closed")

    def execute_query(self, query, params=None):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            # Revisamos si el query devolvió algo
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            return None