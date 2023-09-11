from models.databasemanager import DatabaseManager


class Purchases:
    def __init__(self, product, message, price, store, category, duration, date, quantity):
        self.product = product
        self.message = message
        self.price = price
        self.store = store
        self.category = category
        self.duration = duration
        self.date = date
        self.quantity = quantity

    # Adicione getters e setters conforme necessário

    def insert_database(self):
        query = "INSERT INTO purchases (product, message, price, store, category, duration, date, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (self.product, self.message, self.price, self.store, self.category, self.duration, self.date, self.quantity)
        db_manager = DatabaseManager()
        db_manager.execute_query_with_data(query, data)

    @staticmethod
    def read_database():
        query = "SELECT * FROM purchases"
        db_manager = DatabaseManager()
        results = db_manager.return_results(query)
        for result in results:
            print("id: {0} | produto: {1}  | descrição: {2} | preço: {3} | loja: {4} | categoria: {5} |  Duração: {6} | quantidade: {7} |  data: {8}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))

    @staticmethod
    def update_database(id, product, quantity, message, price, store, category, duration, date):
        query = "UPDATE purchases SET product = %s , message = %s , price= %s , store= %s, category = %s , duration = %s  , date= %s , quantity = %s WHERE id = %s"
        data = (product, message, price, store, category, duration, date, quantity, id)
        db_manager = DatabaseManager()
        db_manager.execute_query_with_data(query, data)
       

    @staticmethod
    def delete_database(id):
        query = "DELETE FROM purchases WHERE id = %s"
        data = (id,)
        db_manager = DatabaseManager()
        db_manager.execute_query_with_data(query, data)
       

    @staticmethod
    def sum_price():
        query = "SELECT SUM(price) AS TotalItemsOrdered FROM purchases"
        db_manager = DatabaseManager()
        results = db_manager.return_results(query)
        for result in results:
            sum_prices = result[0]
            if sum_prices is not None:
                return sum_prices
            else:
                print("Adicione compras")
                return
