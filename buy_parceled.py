import pg8000
from config.configBD import DB_CONFIG
from datetime import date , datetime
from purchases import Purchases

class Buy_parceled(Purchases):


    def insert_buy_parceled():
      product = input("Produto: ")
      quantity = int(input("quantidade: "))
      message = input("descrição: ")
      payment = int(input("total de parcelas: "))
      price = (float(input("preço unitário: ")) * quantity)
      store = input("loja: ")
      category = input("categoria: ")
      duration = input("duração do produto: ")
      date = datetime.now()
      paidinstallment = 0 
      moneypaid = 0
      if(payment > 0):
        connection = pg8000.connect(**DB_CONFIG)
        cursor = connection.cursor()
        sql = "INSERT INTO buyparceled (product, message, price , store , category , duration , date , quantity, payment , paidinstallment, moneypaid) VALUES (%s, %s, %s , %s, %s, %s , %s, %s, %s, %s, %s )"
        data = (product, message, price , store , category , duration , date , quantity, payment , paidinstallment, moneypaid)

        cursor.execute(sql, data)
        connection.commit()

        userid = cursor.lastrowid

        cursor.close()
        connection.close()

        print("Foi cadastrado o novo produto de ID:", userid)

      else:
        print("Essa compra não tem parcela")

    def read_buy_parceled():
      connection = pg8000.connect(**DB_CONFIG)

      cursor = connection.cursor()

      sql = "SELECT * FROM buyparceled WHERE payment > 0;"

      cursor.execute(sql)
      results = cursor.fetchall()

      cursor.close()
      connection.close()

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


    def money_parceled(buy_parceled , count_register):
       count_register_loop = count_register

       # Toda vez que o dia da compra parcelada for igual ao dia de hoje, pagará a parcela, registrando o total de parcelas pagas. defini-se um horário único, a fim de que a ação só aconteça uma vez
       for i in range(0, count_register_loop , 1):
        if( buy_parceled[i][8].day == date.today().day and buy_parceled[i][8].month != date.today().month and buy_parceled[i][8].year == date.today().year and datetime.now().hour == 0 and datetime.now().minute == 10 and datetime.now().second == 0 or  buy_parceled[i][8].day == date.today().day and buy_parceled[i][8].month == date.today().month and buy_parceled[i][8].year != date.today().year and datetime.now().hour == 0 and datetime.now().minute == 10 and datetime.now().second == 0):
          moneypaid = buy_parceled[i][11] + (buy_parceled[i][3] / buy_parceled[i][7])
          paidinstallment = (buy_parceled[i][10] + 1)
          id = buy_parceled[i][0]
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


    def delete_buy_parceled():
      connection = pg8000.connect(**DB_CONFIG)

      cursor = connection.cursor()


      # Onde as parcelas pagas for igual ao total, exclua esse registro, pois todas as parcelas foram pagas

      sql = "DELETE FROM buyparceled WHERE paidinstallment = payment"

      cursor.execute(sql)
      connection.commit()

      cursor.close()
      connection.close()
