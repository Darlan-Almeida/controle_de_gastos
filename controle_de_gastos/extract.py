import mysql.connector


class Extract():

    def read_database():

      connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="12345",
      database="spendingcontrol"
    )

      cursor = connection.cursor()

      sql = "SELECT bankroll FROM extract2 LIMIT 1"

      cursor.execute(sql)
      results = cursor.fetchall()

      cursor.close()
      connection.close()

      for result in results:
        return result[0]



    def update_money():
        money = float(input("digite o valor que você deseja adicionar na carteira: "))
        update_bankroll = money + Extract.read_database()
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="spendingcontrol"
        )

        cursor = connection.cursor()

        sql = "UPDATE extract2 SET bankroll = %s  WHERE id = %s"
        data = (update_bankroll , 0)

        cursor.execute(sql, data)
        connection.commit()


        cursor.close()
        connection.close()

        print("dinheiro adicionado")
        
    def cashout():
        money = float(input("digite o valor que você deseja sacar da carteira: "))
        cashout_bankroll =  Extract.read_database() - money


        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="spendingcontrol"
        )

        cursor = connection.cursor()

        sql = "UPDATE extract2 SET bankroll = %s  WHERE id = %s"
        data = (cashout_bankroll , 0)

        cursor.execute(sql, data)
        connection.commit()


        cursor.close()
        connection.close()

        print("dinheiro saquado")

    def add_money_scheduled(money):
      
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="spendingcontrol"
        )

        cursor = connection.cursor()

        sql = "UPDATE extract2 SET bankroll = %s  WHERE id = %s"
        data = (money , 0)

        cursor.execute(sql, data)
        connection.commit()


        cursor.close()
        connection.close()

        print("dinheiro adicionado")
