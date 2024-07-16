from inventory import Grocery, Beer_and_Wine, Tobacco
import time
import pandas as pd
import os
from dotenv import load_dotenv
Grocery1 = Grocery(1,'Pepsi',str(time.time()),'Cashier_1',True,'Cash','Grocery_NonTax','Aquafina 24 pk')
Grocery1.write_to_csv()
Grocery2 =  Grocery(2,'Little Debbies',str(time.time()),'Cashier_1',True,'Net_Banking','Grocery_NonTax','Zebra Cake 2 pk')
Grocery2.write_to_csv()
Tobacco1 = Tobacco(2,'Hackney',str(time.time()),'Manager',True,'Net_Banking','Cigarettes','Marloboro')
Tobacco1.write_to_csv()
Beer_and_Wine1 = Beer_and_Wine(4,'Heidelberg',str(time.time()),'cashier_2',True,'Cheque','Beer','Modelo Especial 12 pk')
Beer_and_Wine1.write_to_csv()
order_name = 'null'
def time_of_arrival():
    return str(time.time())
def main():
    print("Welcome to the Inventory Management System.")
    while True:
        print('Type of Inventory: \n a: Grocery \n s: Tobacco \n d: Beer and Wine')
        inv = input('Type a,b or c')
        if inv is 'a' or 's' or 'd':
            if inv is 'a':
                order_name = input("Name of the order: \n")
                supplier = input("Name of the Supplier: \n")
                count = int(input("Count of cases from the supplier \n"))
                time = time_of_arrival()
                print("Person that monitored the stock exchange:\n 1. Owner \n 2. Manager \n 3. Cashier_1 \n 4. Cashier_2 \n 5. Cashier_3")
                recieved_by = input("Provide the input associated with the person: (Type 1,2,3,4 or 5) ")
                if recieved_by is '1' or '2' or '3' or '4' or '5':
                    pass
                else:
                    main()
        else:
            print("Please provide valid input...")