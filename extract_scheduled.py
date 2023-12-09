import pg8000
from config.configBD import DB_CONFIG
from datetime import date , datetime

class Extract_Scheduled():

    def insert_database():
        day = int(input("Diigite o dia do mês que você deseja adicionar: "))
        money = int(input("Diigite o valor que você deseja adicionar: "))
        connection = pg8000.connect(**DB_CONFIG)

        cursor = connection.cursor()

        sql = "INSERT INTO moneyscheduled (money, day) VALUES (%s, %s)"
        data = (money , day)

        cursor.execute(sql, data)
        connection.commit()


        cursor.close()
        connection.close()

        print("dinheiro programado adicionado")

    def view_date_moneyscheduled():
      connection = pg8000.connect(**DB_CONFIG)

      cursor = connection.cursor()

      sql = "SELECT * FROM moneyscheduled"

      cursor.execute(sql)
      results = cursor.fetchall()

      return results

    def count_register_moneyscheduled():
      connection = pg8000.connect(**DB_CONFIG)

      cursor = connection.cursor()

      sql = "SELECT COUNT(money) FROM moneyscheduled"

      cursor.execute(sql)
      results = cursor.fetchall()

      return results[0][0]

   
    def add_money_moneyscheduled (money, scheduling, count_register):
       count_register_loop = count_register - 1

         # Toda vez que o dia da adição de dinheiro progrmada pelo usuário for hoje, adicione as 00:10 do dia
       for i in range(0 , count_register_loop , 1):
        if(scheduling[i][1] == date.today().day and datetime.now().hour == 0 and datetime.now().minute == 10 and datetime.now().second == 0):
          new_extract = scheduling[i][0]
          add_new_extract = new_extract + money
          connection = pg8000.connect(**DB_CONFIG)

          cursor = connection.cursor()
                
          sql = "UPDATE extract SET bankroll = %s  WHERE id = %s"
          data = ( add_new_extract , 0)

          cursor.execute(sql , data)
          connection.commit()

          cursor.close()
          connection.close()

          return "Dinheiro programado adicionado!"

      

                