import mysql.connector 
from datetime import date , datetime

class Purchases():
    def __init__(self, product, message, price , store , category , duration , date, quantity):
        self.__product = product
        self.__message = message
        self.__price = price
        self.__store = store
        self.__category = category
        self.__duration = duration
        self.__date = date
        self.__quantity = quantity



  
    def insert_database():
      product = input("Produto: ")
      quantity = int(input("quantidade: "))
      message = input("descrição: ")
      price = (float(input("preço unitário: ")) * quantity)
      store = input("loja: ")
      category = input("categoria: ")
      duration = input("duração do produto: ")
      date = datetime.now()

      connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="12345",
      database="spendingcontrol"
    )
      cursor = connection.cursor()
      sql = "INSERT INTO purchases2 (product, message, price , store , category , duration, date , quantity) VALUES (%s, %s, %s , %s, %s, %s , %s, %s )"
      data = (product, message, price , store , category , duration, date, quantity)

      cursor.execute(sql, data)
      connection.commit()

      userid = cursor.lastrowid

      cursor.close()
      connection.close()

      print("Foi cadastrado o novo produto de ID:", userid)

    def read_database():

      connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="12345",
      database="spendingcontrol"
    )

      cursor = connection.cursor()

      sql = "SELECT * FROM purchases2"

      cursor.execute(sql)
      results = cursor.fetchall()

      cursor.close()
      connection.close()

      for result in results:
        print("produto: {0} | descrição: {1}  | preço: {2} | loja: {3} | categoria: {4} | duração: {5} |  data: {6} | quantidade: {7} | id: {8}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))

    def update_database():
      id = int(input("digite o ID do produto quue deseja atualizar: "))
      product = input("Produto: ")
      quantity = int(input("quantidade: "))
      message = input("descrição: ")
      price = float(input("preço: ")) * quantity
      store = input("loja: ")
      category = input("categoria: ")
      duration = input("duração do produto: ")
      date = datetime.now()

      connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="12345",
      database="spendingcontrol"
    )

      cursor = connection.cursor()

      sql = "UPDATE purchases2 SET product = %s , message = %s , price= %s , store= %s, category = %s , duration = %s  , date= %s , quantity = %s WHERE id = %s"
      data = (product, message, price , store , category , duration, date, quantity, id)

      cursor.execute(sql, data)
      connection.commit()

      recordsaffected = cursor.rowcount

      cursor.close()
      connection.close()

      print(recordsaffected, " registros alterados")


    def delete_database():
        id = int(input("digite o ID do produto que deseja excluir: "))

        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="spendingcontrol"
      )

        cursor = connection.cursor()

        sql = "DELETE FROM purchases2 WHERE id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()

        recordsaffected = cursor.rowcount

        cursor.close()
        connection.close()

        print(recordsaffected, " registros excluídos")

    def sum_price():
      #SELECT SUM(Quantity) AS TotalItemsOrdered FROM OrderDetails;
      connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="spendingcontrol"
      )

      cursor = connection.cursor()

      sql = "SELECT SUM(price) AS TotalItemsOrdered FROM purchases2"
      cursor.execute(sql)

      results = cursor.fetchall()

      cursor.close()
      connection.close()

      for result in results:
        sum_prices = result[0]
        try:
          sum_prices + 0
          return sum_prices
        except:
          print("adicione compras")
          return
