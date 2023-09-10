from models.databasemanager import DatabaseManager


class Purchases:
    def __init__(self, product, message, price, store, category, duration, date, quantity):
        self.__product = product
        self.__message = message
        self.__price = price
        self.__store = store
        self.__category = category
        self.__duration = duration
        self.__date = date
        self.__quantity = quantity

    # Adicione getters e setters conforme necessário

    def insert_database(self):
        query = "INSERT INTO purchases (product, message, price, store, category, duration, date, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (self.__product, self.__message, self.__price, self.__store, self.__category, self.__duration, self.__date, self.__quantity)
        db_manager = DatabaseManager()
        db_manager.execute_query(query, data)
        db_manager.close_connection()

    @staticmethod
    def read_database():
        query = "SELECT * FROM purchases"
        db_manager = DatabaseManager()
        cursor = db_manager.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db_manager.close_connection()

        for result in results:
            print("id: {0} | produto: {1}  | descrição: {2} | preço: {3} | loja: {4} | categoria: {5} |  Duração: {6} | quantidade: {7} |  data: {8}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))

    @staticmethod
    def update_database(id, product, quantity, message, price, store, category, duration, date):
        query = "UPDATE purchases SET product = %s , message = %s , price= %s , store= %s, category = %s , duration = %s  , date= %s , quantity = %s WHERE id = %s"
        data = (product, message, price, store, category, duration, date, quantity, id)
        db_manager = DatabaseManager()
        db_manager.execute_query(query, data)
        db_manager.close_connection()

    @staticmethod
    def delete_database(id):
        query = "DELETE FROM purchases WHERE id = %s"
        data = (id,)
        db_manager = DatabaseManager()
        db_manager.execute_query(query, data)
        db_manager.close_connection()

    @staticmethod
    def sum_price():
        query = "SELECT SUM(price) AS TotalItemsOrdered FROM purchases"
        db_manager = DatabaseManager()
        cursor = db_manager.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db_manager.close_connection()

        for result in results:
            sum_prices = result[0]
            if sum_prices is not None:
                return sum_prices
            else:
                print("Adicione compras")
                return
