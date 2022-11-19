from datetime import *
import random
  

l="""
*****PRICE LIST*****
Rice- ₹50/kg
Sugar- ₹30/kg
Salt- ₹20/kg
Maggie- ₹10 each
Milk - ₹25/Lt
Biscuits- ₹10 each
Oil- ₹150/Lt
"""
print(l)
items={"Rice":50,"Sugar":30,"Salt":20,
"Biscuits":10,"Oil":150,"Milk":25,"Maggie":10}
#print(items)
price=0;total_price=0
pricelist,chosenlist,quantlist,plist=[],[],[],[]


name=input("Enter your name")
for i in range(len(items)):
  inp=input("enter 1 to continue or 2 to exit")
  if inp=="2":
    break
  elif inp=="1":
    
    chosen=input("enter what you want to buy")
    if chosen in items.keys():
      item_quant=int(input("enter quantity"))
      price=item_quant*items[chosen]
      pricelist.append((chosen,item_quant,items,price))
     #  print(pricelist)
      total_price+=price
      chosenlist.append(chosen)
      quantlist.append(item_quant)
      plist.append(price)
       #print("price:",price)
     #  print("total:",total_price)
      print("-"*60)
    elif chosen not in items.keys():
      print("Item requested is not available right now\nPlease try after some time")
      print("-"*60)
  elif inp!="1" or inp!="2":
    print("Please enter valid response")
    print("-"*60)
if total_price!=0:
  print("="*10,"Bright Kirana and Wholesale,Patancheru","="*10)
  print("-"*60)
  print(" "*35,"Bill No:",random.randint(1,10000))
  print("-"*60)
  print("Customer Name:",name,11*" ",datetime.now()) 
  print("-"*60)
  print("S.No"," "*8,'Items Purchased'," "*7,'Quantity'," "*5,"Price")
  for i in range(len(pricelist)):
    print(i," "*12,chosenlist[i]," "*16,quantlist[i]," "*14,plist[i])
  print("-"*60)
  print(" "*45,"Total:",total_price)
  print("-"*60)
  print(" "*20,"Thanks for Visiting")







