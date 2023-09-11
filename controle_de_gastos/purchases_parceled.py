from models.databasemanager import DatabaseManager
from purchases import Purchases


class Purchases_parceled(Purchases):
    def __init__(self , product, message, price , store , category , duration , date , quantity, payment , paidinstallment, moneypaid):
      super().__init__(product, message, price , store , category , duration , date , quantity,)
      self.__payment = payment
      self.__paidinstallment = paidinstallment
      self.__moneypaid = moneypaid



    def insert_purchases_parceled(self):
        
        query = "INSERT INTO buyparceled (product, message, price , store , category , duration , date , quantity, payment , paidinstallment, moneypaid) VALUES (%s, %s, %s , %s, %s, %s , %s, %s, %s, %s, %s )"
        data = (self)
        db_manager = DatabaseManager()
        db_manager.execute_query(query, data)
        db_manager.close_connection()

        return ("Foi cadastrado o novo produto ")

    def read_purchases_parceled():
  
      query = "SELECT * FROM buyparceled WHERE payment > 0;"
      
      db_manager = DatabaseManager()
      db_manager.execute_query(query)
      db_manager.close_connection()


      for result in results:
        print("id: {0}  |  produto: {1} | descrição: {2}  | preço: {3} | loja: {4} | categoria: {5} | duração: {6} | tipo de pagamento {7} data: {8} | quantidade: {9} | Total de parcelas: {10}  | valor pago: {11}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11] ))
    
      return results
  
    def count_register_parceled():
      connection = pg8000.connect(**DB_CONFIG)

      cursor = connection.cursor()

      sql = "SELECT COUNT(id) FROM buyparceled"

      cursor.execute(sql)
      results = cursor.fetchall()

      return results[0][0]


    def money_parceled(purchases_parceled , count_register):
       count_register_loop = count_register

       # Toda vez que o dia da compra parcelada for igual ao dia de hoje, pagará a parcela, registrando o total de parcelas pagas. defini-se um horário único, a fim de que a ação só aconteça uma vez
       for i in range(0, count_register_loop , 1):
        if( purchases_parceled[i][8].day == date.today().day and purchases_parceled[i][8].month != date.today().month and purchases_parceled[i][8].year == date.today().year and datetime.now().hour == 0 and datetime.now().minute == 10 and datetime.now().second == 0 or  purchases_parceled[i][8].day == date.today().day and purchases_parceled[i][8].month == date.today().month and purchases_parceled[i][8].year != date.today().year and datetime.now().hour == 0 and datetime.now().minute == 10 and datetime.now().second == 0):
          moneypaid = purchases_parceled[i][11] + (purchases_parceled[i][3] / purchases_parceled[i][7])
          paidinstallment = (purchases_parceled[i][10] + 1)
          id = purchases_parceled[i][0]
          connection = pg8000.connect(**DB_CONFIG)
    
          cursor = connection.cursor()
                
          sql = "UPDATE buyparceled SET moneypaid = %s , paidinstallment  = %s WHERE id = %s"
          data = (  moneypaid, paidinstallment ,  id)

          cursor.execute(sql , data)
          connection.commit()

          cursor.close()
          connection.close()

  

    def sum_money_parceled():
      connection = pg8000.connect(**DB_CONFIG)

      cursor = connection.cursor()

      sql = "SELECT SUM(moneypaid) AS TotalItemsOrdered FROM buyparceled"
      cursor.execute(sql)

      results = cursor.fetchall()

      cursor.close()
      connection.close() 

      for result in results:
        return result[0]     


    def delete_purchases_parceled():
      connection = pg8000.connect(**DB_CONFIG)

      cursor = connection.cursor()


      # Onde as parcelas pagas for igual ao total, exclua esse registro, pois todas as parcelas foram pagas

      sql = "DELETE FROM buyparceled WHERE paidinstallment = payment"

      cursor.execute(sql)
      connection.commit()

      cursor.close()
      connection.close()
