from purchases import  Purchases
from extract import Extract
from datetime import datetime , date
from extract_scheduled import Extract_Scheduled
from purchases_parceled import Purchases_parceled

import os


while True:
    os.system("cls")
    #apagas as compras parceladas que tiveram o ultimo pagamento agora
    Purchases_parceled.delete_purchases_parceled()

    #Exibe as compras parceladas
    print(Purchases_parceled.money_parceled(Purchases_parceled.read_purchases_parceled() , Purchases_parceled.count_register_parceled()))

    # adiciona o dinheiro caso o dia cadastrado, que são passados nos parametros, seja hoje
    Extract_Scheduled.add_money_moneyscheduled (Extract.read_database() , Extract_Scheduled.view_date_moneyscheduled() , Extract_Scheduled.count_register_moneyscheduled())


    #conjuntos de condicionais que fazem operações matemáticas, conforme os dados preenchidos nas tabelas do banco de dados, a fim de exibir o saldo
    
    if(type( Purchases_parceled.sum_money_parceled()) != float and type(Purchases.sum_price()) == float):
        print("SALDO:", Extract.read_database() - Purchases.sum_price())

    if(type( Purchases_parceled.sum_money_parceled()) == float and type(Purchases.sum_price()) != float):
        print("SALDO:", Extract.read_database() - Purchases_parceled.sum_money_parceled())

    if(type( Purchases_parceled.sum_money_parceled()) == float and type(Purchases.sum_price()) == float):
        print("SALDO:", Extract.read_database() - Purchases_parceled.sum_money_parceled() - Purchases.sum_price())

    if(type( Purchases_parceled.sum_money_parceled()) != float and type(Purchases.sum_price()) != float):
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
        money = float(input("digite o valor que você deseja adicionar na carteira: "))
        extract = Extract(money)
        extract.update_money()
        
    if(menu == 5):
        money = float(input("digite o valor qufe você deseja sacar da carteira: "))
        extract = Extract(money)
        extract.cashout()


    if(menu == 6):
        day = int(input("Diigite o dia do mês que você deseja adicionar: "))
        money = int(input("Diigite o valor que você deseja adicionar: "))
        extract_scheduled = Extract_Scheduled(money , day)
        extract_scheduled.insert_database()


    if(menu == 7):
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
            purchase_parceled = Purchases_parceled(product, message, price , store , category , duration , date , quantity, payment , paidinstallment, moneypaid)
            purchase_parceled.insert_purchases_parceled()
        else:
            print("Essa compra não tem parcela")



