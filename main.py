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
        Purchases.insert_database()

    if(menu == 2):
        Purchases.update_database()

    if(menu == 3):
        Purchases.delete_database()

    if(menu == 4):
        Extract.update_money()
        
    if(menu == 5):
        Extract.cashout()


    if(menu == 6):
        Extract_Scheduled.insert_database()


    if(menu == 7):
        Buy_parceled.insert_buy_parceled()



