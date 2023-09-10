import pg8000
from models.config import DB_CONFIG

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



  
    def insert_database(product, message, price , store , category , duration , date, quantity):
      connection = pg8000.connect(**DB_CONFIG)
      cursor = connection.cursor()
      sql = "INSERT INTO purchases (product, message, price , store , category , duration, date , quantity) VALUES (%s, %s, %s , %s, %s, %s , %s, %s )"
      data = (product, message, price , store , category , duration, date, quantity)

      cursor.execute(sql, data)
      connection.commit()

      cursor.close()
      connection.close()

      return("Foi cadastrado o novo produto de ID:")

    def read_database():

      connection = connection = pg8000.connect(**DB_CONFIG)


      cursor = connection.cursor()

      sql = "SELECT * FROM purchases"

      cursor.execute(sql)
      results = cursor.fetchall()

      cursor.close()
      connection.close()

      for result in results:
        print("id: {0} | produto: {1}  | descrição: {2} | preço: {3} | loja: {4} | categoria: {5} |  Duração: {6} | quantidade: {7} |  data: {8}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))

    def update_database(id , product , quantity , message , price , store , category , duration ,date):
      connection = pg8000.connect(**DB_CONFIG)

      cursor = connection.cursor()

      sql = "UPDATE purchases SET product = %s , message = %s , price= %s , store= %s, category = %s , duration = %s  , date= %s , quantity = %s WHERE id = %s"
      data = (product, message, price , store , category , duration, date, quantity, id)

      cursor.execute(sql, data)
      connection.commit()

      recordsaffected = cursor.rowcount

      cursor.close()
      connection.close()

      print(recordsaffected, " registros alterados")


    def delete_database(id):
        connection = pg8000.connect(**DB_CONFIG)

        cursor = connection.cursor()

        sql = "DELETE FROM purchases WHERE id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()

        recordsaffected = cursor.rowcount

        cursor.close()
        connection.close()

        print(recordsaffected, " registros excluídos")

    def sum_price():
      #SELECT SUM(Quantity) AS TotalItemsOrdered FROM OrderDetails;
      connection = pg8000.connect(**DB_CONFIG)

      cursor = connection.cursor()

      sql = "SELECT SUM(price) AS TotalItemsOrdered FROM purchases"
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
