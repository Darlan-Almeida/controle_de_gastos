from models.databasemanager import DatabaseManager
from models.config import DB_CONFIG


class Extract():
    def __init__(self , money):
       self.money = money


    def read_database():
      query = "SELECT bankroll FROM extract LIMIT 1"
      db_manager = DatabaseManager()

      results = db_manager.return_results(query)
    
      for result in results:
        return result[0]



    def update_money(self):
        update_bankroll = self.money + Extract.read_database()
    

        query = "UPDATE extract SET bankroll = %s  WHERE id = %s"
        data = (update_bankroll , 1)

        db_manager = DatabaseManager()
        db_manager.execute_query_with_data(query, data)

        print("dinheiro adicionado")
        
    def cashout(self):
        
        cashout_bankroll =  float(Extract.read_database()) - self.money

        query = "UPDATE extract SET bankroll = %s  WHERE id = %s"
        data = (cashout_bankroll , 1)
        
        db_manager = DatabaseManager()
        db_manager.execute_query_with_data(query, data)


        print("dinheiro saquado")