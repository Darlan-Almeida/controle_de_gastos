from models.config import DB_CONFIG
import pg8000

class DatabaseManager:
    def __init__(self):
        self.connection = pg8000.connect(**DB_CONFIG)

    def execute_query_with_data(self, query, data=None):
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        self.connection.commit()
        cursor.close()
    
    def execute_query_without_data(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def return_results(self , query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        results = cursor.fetchall()
        cursor.close()
        return(results)