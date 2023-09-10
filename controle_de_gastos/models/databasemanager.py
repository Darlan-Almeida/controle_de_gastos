from models.config import DB_CONFIG
import pg8000

class DatabaseManager:
    def __init__(self):
        self.connection = pg8000.connect(**DB_CONFIG)

    def close_connection(self):
        self.connection.close()

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        self.connection.commit()
        cursor.close()