import pandas as pd
import warnings
import time
from dotenv import load_dotenv
import os
warnings.filterwarnings(action='ignore',category=DeprecationWarning)

class Inventory:
    """
    count: Count of the order recieved from the supplier.(Integer)
    supplier: Name of the supplier.(String)
    time: Time of order recieved.(String) [Converted to stromg from time]
    recieved_by: Name of the person who recieved the order(string)
    is_paid: Payment Status (Boolean) [True or False]
    payment: Mode of Payment (String) [Cash, Cheque, Net_Banking]

    """
    def __init__(self,count:int,supplier:str,time:str,recieved_by:str,is_paid:bool,payment:str) -> None:
        load_dotenv()
        self.count = count
        self.supplier = supplier
        self.time = time
        self.recieved_by = recieved_by
        self.is_paid = is_paid,
        self.payment = payment

class Grocery(Inventory):
    """
    type: Type of Beverage (String) [Nontaxable, Taxable] 
    brand: Manufacturer of the Beverage(String)

    """
    def __init__(self, count: int, supplier: str, time: str, recieved_by: str, is_paid: bool, payment: str,type:str,brand:str) -> None:
        super().__init__(count, supplier, time, recieved_by, is_paid, payment)
        self.type = type
        self.brand = brand
        self.loc = os.getenv('GROCERY_INVENTORY')
        
    def write_to_csv(self):
        data =pd.DataFrame({
            'Order_Name': self.brand,
            'count':self.count,
            'supplier': self.supplier,
            'time': self.time,
            'recieved_by': self.recieved_by,
            'Payment_Status': self.is_paid,
            'Mode_of_Payment': self.payment,
            'Type_of_Grocery': self.type,
             })
        #checks if the file exists or not. Else makes a new filw and writes into it
        if os.path.exists(self.loc):
            """
            If a certain stock is already present. we will just increase the count of the cases of product
            instead of inserting rows of same order. If it is a new item which is not in the inventory a new 
            row will be inserted.

            """
            df1 = pd.read_csv(self.loc)
            if self.brand in df1["Order_Name"].values:
                print(f'The stock for {self.brand} already exist. So, current stock will be added to the existing ones.')
                pos = df1[df1['Order_Name'] == self.brand].index[0]
                updated_count = df1["count"][pos] + self.count
                df1.loc[pos,'count'] = updated_count
                df1.to_csv(self.loc,index = False)
                print('The order has been entered into the inventory. Check GROCERY_INVENTORY.csv')
            else :
                data.to_csv(self.loc,mode='a',header= False,index=False)
                print('The order has been entered into the inventory. Check GROCERY_INVENTORY.csv')
        else:
            data.to_csv(self.loc,mode='a',index=False)
            print('The order has been entered into the inventory. Check GROCERY_INVENTORY.csv')


class Tobacco(Inventory):
    """
    type: Type of Tobacco (String) [Cigarette, Cigar,Cigarillo,Vape,Nicotine Pouches,CBD] 
    brand: Manufacturer of the Tobacco item (String)

    """
    def __init__(self, count: int, supplier: str, time: str, recieved_by: str, is_paid: bool, payment: str,type:str,brand:str) -> None:
        super().__init__(count, supplier, time, recieved_by, is_paid, payment)
        self.type = type
        self.brand = brand
        self.loc = os.getenv('TOBACCO_INVENTORY')
    
    def write_to_csv(self):
        data =pd.DataFrame({
            'Order_Name': self.brand,
            'count':self.count,
            'supplier': self.supplier,
            'time': self.time,
            'recieved_by': self.recieved_by,
            'Payment_Status': self.is_paid,
            'Mode_of_Payment': self.payment,
            'Type_of_Tobacco': self.type,
             })
        if os.path.exists(self.loc):
            """
            If a certain stock is already present. we will just increase the count of the cases of product
            instead of inserting rows of same order. If it is a new item which is not in the inventory a new 
            row will be inserted.

            """
            df1 = pd.read_csv(self.loc)
            if self.brand in df1["Order_Name"].values:
                print(f'The stock for {self.brand} already exist. So, current stock will be added to the existing ones.')
                pos = df1[df1['Order_Name'] == self.brand].index[0]
                updated_count = df1["count"][pos] + self.count
                df1.loc[pos,'count'] = updated_count
                df1.to_csv(self.loc,index = False)
                print('The order has been entered into the inventory. Check TOBACCO_INVENTORY.csv')
            else :
                data.to_csv(self.loc,mode='a',header= False,index=False)
                print('The order has been entered into the inventory. Check TOBACCO_INVENTORY.csv')
        else:
            data.to_csv(self.loc,mode='a',index=False)
            print('The order has been entered into the inventory. Check TOBACCO_INVENTORY.csv')

class Beer_and_Wine(Inventory):
    """
    type: Type of Beer (String) [Beer, Wine,Alcohol(<16% conc.)] 
    brand: Manufacturer of the Tobacco item (String)

    """
    def __init__(self, count: int, supplier: str, time: str, recieved_by: str, is_paid: bool, payment: str,type:str,brand:str) -> None:
        super().__init__(count, supplier, time, recieved_by, is_paid, payment)
        self.type = type
        self.brand = brand
        self.loc = os.getenv('BEER_AND_WINE_INVENTORY')
    def write_to_csv(self):
        data =pd.DataFrame({
            'Order_Name': self.brand,
            'count':self.count,
            'supplier': self.supplier,
            'time': self.time,
            'recieved_by': self.recieved_by,
            'Payment_Status': self.is_paid,
            'Mode_of_Payment': self.payment,
            'Type_of_Alcohol': self.type,
             })
        if os.path.exists(self.loc):
            """
            If a certain stock is already present. we will just increase the count of the cases of product
            instead of inserting rows of same order. If it is a new item which is not in the inventory a new 
            row will be inserted.

            """
            df1 = pd.read_csv(self.loc)
            if self.brand in df1["Order_Name"].values:
                print(f'The stock for {self.brand} already exist. So, current stock will be added to the existing ones.')
                pos = df1[df1['Order_Name'] == self.brand].index[0]
                updated_count = df1["count"][pos] + self.count
                df1.loc[pos,'count'] = updated_count
                df1.to_csv(self.loc,index = False)
                print('The order has been entered into the inventory. Check BEER_AND_WINE_INVENTORY.csv')
            else :
                data.to_csv(self.loc,mode='a',header= False,index=False)
                print('The order has been entered into the inventory. Check BEER_AND_WINE_INVENTORY.csv')
        else:
            data.to_csv(self.loc,mode='a',index=False)
            print('The order has been entered into the inventory. Check BEER_AND_WINE_INVENTORY.csv')


