import json
import time
import random

'''fd = open("records.json",'r')
txt = json.load(fd)
fd.close()

#records = ("records.json", "w")

txt['11202130']['Price'] = 10

fd = open("records.json",'w')
js2 = json.dump(txt, fd)
fd.close()'''

print("Hello! Choose an item from the Menu to purchase.\n")

fd = open("records.json",'r')
txt = fd.read()
fd.close()

records = json.loads(txt)

left_alignment="Product ID"
center_alignment="Item"
right_alignment="Price"
print(f"{left_alignment:<30}{center_alignment:^25}{right_alignment:>30}")
print("-----------------------------------------------------------------------------------")
for i in records:
    left_alignment=i
    center_alignment=records[i]["Name"]
    right_alignment=records[i]["Price"]
    print(f"{left_alignment:<30}{center_alignment:^25}{right_alignment:>30}")

cart = {}
shop = "Y"
while(shop=="Y"):
    product = input("Enter Product ID: ")
    if product in records:
        print("Product Avaliable!")
        quantity = input("Enter Product Quantity: ")
        if (int(quantity) <= int(records[product]["Quantity"])):
            print("In Stock!")
            print("Item added to Cart!")
            new_quantity = int(records[product]["Quantity"]) - int(quantity)
            records[i]["Quantity"] = str(new_quantity)
            total_price = int(records[product]["Price"]) * int(quantity)
            val = str(random.randint(1000,9999))
            cart[val] = {}
            cart[val]["Product ID"] = product
            cart[val]["Item"] = records[product]["Name"]
            cart[val]["Price"] = records[product]["Price"]
            cart[val]["Quantity"] = quantity
            cart[val]["Total Price"] = str(total_price)
        else:
            print("Sorry only "+ records[product]["Quantity"] +" left in stock!")         
    else:
        print("Product not in stock!")
    shop = input("Do you want to continue shopping?(Y/N): ")

#print(cart)

total_price = 0
for i in cart:
    total_price = total_price + int(cart[i]["Total Price"])

name = input("Enter your Name: ")
time = time.ctime()
bill = {}

bill["Name"] = name
bill["Time"] = time
#bill["Product ID"] = product
#bill["Item"] = records[product]["Name"]
bill["Total Amount"] = str(total_price)

print("**************************")
print("Name of Customer: " + bill["Name"])
#print("Product ID: " + bill["Product ID"])
#print("Item: " + bill["Item"])
print("Time of Purchase: " + bill["Time"])
print("---------------------------")
print("Total Billing Amount: "+ bill["Total Amount"])
print("***************************")

sales={}
sales.update(bill)

#print(sales)
js2 = json.dumps(sales)
fd2 = open("sales.json",'w')
fd2.write(js2)
fd2.close()

fd2 = open("sales.json",'r')
txt2 = fd2.read()
fd2.close()

sales = json.loads(txt2)

