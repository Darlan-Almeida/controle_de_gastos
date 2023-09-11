from models.databasemanager import DatabaseManager
from models.config import DB_CONFIG
from datetime import date , datetime
from extract import Extract

class Extract_Scheduled(Extract):
    def __init__(self, money , day):
       super().__init__(money)
       self.day = day

    def insert_database(self):

        query = "INSERT INTO moneyscheduled (money, day) VALUES (%s, %s)"
        data = (self.money , self.day)

        db_manager = DatabaseManager()
        db_manager.execute_query_with_data(query , data)

        print("dinheiro programado adicionado")

    def view_date_moneyscheduled():


      query = "SELECT * FROM moneyscheduled"

      db_manager = DatabaseManager()
      results = db_manager.return_results(query)

      return results

    def count_register_moneyscheduled():
      query = "SELECT COUNT(money) FROM moneyscheduled"

      db_manager = DatabaseManager()
      results = db_manager.return_results(query)

      return results[0][0]

   
    def add_money_moneyscheduled (money, scheduling, count_register):
       count_register_loop = count_register - 1

         # Toda vez que o dia da adição de dinheiro progrmada pelo usuário for hoje, adicione as 00:10 do dia
       for i in range(0 , count_register_loop , 1):
        if(scheduling[i][1] == date.today().day and datetime.now().hour == 0 and datetime.now().minute == 10 and datetime.now().second == 0):
          new_extract = scheduling[i][0]
          add_new_extract = new_extract + money
        
                
          query = "UPDATE extract SET bankroll = %s  WHERE id = %s"
          data = ( add_new_extract , 0)

          db_manager = DatabaseManager()
          db_manager.execute_query_with_data(query , data)
          
          return "Dinheiro programado adicionado!"

      

                
            

