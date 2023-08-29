#!/usr/bin/env python3

class CashRegister:
    item =[]
    def __init__(self,discount):
        self.discount = discount
        self.item.append(self) 
        

    def discount (self):
        return self.discount
    
    def add_item (item,price):
        print(f"ITEM ADDED:{item}   PRICE:{price}")

    def add_item_quantity (item,price,quantity):
        total= price*quantity
        discounted= total* (cash_register.discount/100)
        final_price = total-discounted
        print(f"ITEM ADDED:{item}   PRICE:{price}  Quantity:ksh{quantity}  Total price:ksh{total}  Discount:ksh{discounted}  Discounted price:ksh{final_price}")    

    def no_discount (item) :
        if cash_register.discount == 0 :
            print("There is no discount to apply.") 
            



        
        
        

cash_register = CashRegister(0)    
print(cash_register.discount)
CashRegister.add_item ("eggs", 98)     
CashRegister.add_item_quantity("eggs", 10, 5)  
print(CashRegister.no_discount())