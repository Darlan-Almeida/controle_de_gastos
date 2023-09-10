from purchases import  Purchases
from extract import Extract
from datetime import datetime , date
from extract_scheduled import Extract_Scheduled
from buy_parceled import Buy_parceled

import os


while True:
    os.system("cls")

    #apagas as compras parceladas que tiveram o ultimo pagamento agora
    Buy_parceled.delete_buy_parceled()

    #Exibe as compras parceladas
    print(Buy_parceled.money_parceled(Buy_parceled.read_buy_parceled() , Buy_parceled.count_register_parceled()))

    # adiciona o dinheiro caso o dia cadastrado, que são passados nos parametros, seja hoje
    Extract_Scheduled.add_money_moneyscheduled (Extract.read_database() , Extract_Scheduled.view_date_moneyscheduled() , Extract_Scheduled.count_register_moneyscheduled())


    #conjuntos de condicionais que fazem operações matemáticas, conforme os dados preenchidos nas tabelas do banco de dados, a fim de exibir o saldo

    if(type( Buy_parceled.sum_money_parceled()) != float and type(Purchases.sum_price()) == float):
        print("SALDO:", Extract.read_database() - Purchases.sum_price())

    if(type( Buy_parceled.sum_money_parceled()) == float and type(Purchases.sum_price()) != float):
        print("SALDO:", Extract.read_database() - Buy_parceled.sum_money_parceled())

    if(type( Buy_parceled.sum_money_parceled()) == float and type(Purchases.sum_price()) == float):
        print("SALDO:", Extract.read_database() - Buy_parceled.sum_money_parceled() - Purchases.sum_price())

    if(type( Buy_parceled.sum_money_parceled()) != float and type(Purchases.sum_price()) != float):
        print("SALDO:", Extract.read_database())
        

    Purchases.read_database()


    menu =  int(input((" 1- Registrar compra à vista \n 2- atualizar dados da compra \n 3- deletar compras \n 4- adicionar dinheiro na carteira \n 5- sacar dinheiro \n 6- adicionar dinheiro na carteira automáticamente \n 7- registrar uma compra parcelada \n Escolha uma opção: ")))


    if(menu == 1):
        product = input("Produto: ")
        quantity = int(input("quantidade: "))
        message = input("descrição: ")
        price = (float(input("preço unitário: ")) * quantity)
        store = input("loja: ")
        category = input("categoria: ")
        duration = input("duração do produto: ")
        date = datetime.now()
        purchase = Purchases(product, message, price, store, category, duration, date, quantity)
        print(purchase.insert_database())

    if(menu == 2):
      id = int(input("digite o ID do produto quue deseja atualizar: "))
      product = input("Produto: ")
      quantity = int(input("quantidade: "))
      message = input("descrição: ")
      price = float(input("preço: ")) * quantity
      store = input("loja: ")
      category = input("categoria: ")
      duration = input("duração do produto: ")
      date = datetime.now()
      Purchases.update_database(id , product , quantity , message , price , store , category , duration ,date)

    if(menu == 3):
        id = int(input("digite o ID do produto que deseja excluir: "))
        Purchases.delete_database(id)

    if(menu == 4):
        Extract.update_money()
        
    if(menu == 5):
        Extract.cashout()


    if(menu == 6):
        Extract_Scheduled.insert_database()


    if(menu == 7):
        Buy_parceled.insert_buy_parceled()



