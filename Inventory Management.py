import json

records = { 11202101: {"Name": "Ferrero Rocher", "Price": 849.00, "Quantity": 50, "Weight": "300", "Status": "In Stock", "Category": "Veg"},
            11202102: {"Name": "Patchi", "Price": 5599.00, "Quantity": 10, "Weight": "350", "Status": "In Stock", "Category": "Veg"},
            11202103: {"Name": "Cadbury Bournville", "Price": 405.00, "Quantity": 80, "Weight": "100", "Status": "In Stock", "Category": "Veg"},
            11202104: {"Name": "Mars Bars", "Price": 79.25, "Quantity": 100, "Weight": "100", "Status": "In Stock", "Category": "Non-Veg"},
            11202105: {"Name": "Snickers", "Price": 40.00, "Quantity": 100, "Weight": "100", "Status": "In Stock", "Category": "Veg"},
            11202106: {"Name": "KitKat", "Price": 24.00, "Quantity": 80, "Weight": "37.3", "Status": "In Stock", "Category": "Veg"},
            11202107: {"Name": "Galaxy", "Price": 70.00, "Quantity": 50, "Weight": "56", "Status": "In Stock", "Category": "Veg"},
            11202108: {"Name": "Amul Dark Chocolate", "Price": 119.20, "Quantity": 50, "Weight": "100", "Status": "In Stock", "Category": "Veg"},
            11202109: {"Name": "BarOne", "Price": 50.00, "Quantity": 100, "Weight": "12", "Status": "In Stock", "Category": "Veg"},
            11202110: {"Name": "Crunchie", "Price": 75.00, "Quantity": 50, "Weight": "26", "Status": "In Stock", "Category": "Veg"},
            11202111: {"Name": "5 Star", "Price": 20.00, "Quantity": 80, "Weight": "40", "Status": "In Stock", "Category": "Veg"},
            11202112: {"Name": "Hershey Bar", "Price": 138.00, "Quantity": 50, "Weight": "100", "Status": "In Stock", "Category": "Veg"},
            11202113: {"Name": "Milky Way", "Price": 89.90, "Quantity": 60, "Weight": "100", "Status": "In Stock", "Category": "Veg"},
            11202114: {"Name": "Reese's Sticks", "Price": 101.68, "Quantity": 40, "Weight": "200", "Status": "In Stock", "Category": "Veg"},
            11202115: {"Name": "Crispello", "Price": 10.00, "Quantity": 100, "Weight": "35", "Status": "In Stock", "Category": "Veg"},
            11202116: {"Name": "Toblerone", "Price": 121.67, "Quantity": 20, "Weight": "100", "Status": "In Stock", "Category": "Non-Veg"},
            11202117: {"Name": "Fabelle", "Price": 495.00, "Quantity": 20, "Weight": "121", "Status": "In Stock", "Category": "Veg"},
            11202118: {"Name": "Dukes Waffy Rolls", "Price": 112.00, "Quantity": 20, "Weight": "250", "Status": "In Stock", "Category": "Veg"},
            11202119: {"Name": "Gourmet Popcorn", "Price": 184.00, "Quantity": 10, "Weight": "150", "Status": "In Stock", "Category": "Veg"},
            11202120: {"Name": "Tosca Muso Gold Chocolate", "Price": 209.00, "Quantity": 20, "Weight": "420", "Status": "In Stock", "Category": "Veg"},
            }

js = json.dumps(records)
fd = open("records.json",'w')
fd.write(js)
fd.close()

# Adding new data

ans = True

while ans:
    productId = input("Enter Product ID: ")
    Name = input("Enter Product name: ")
    Price = input("Enter Price of Product: ")
    Quantity = input("Enter the Quantity of Product: ")
    Weight = input("Enter the Weight of Product(in grams): ")
    Status = input("Enter the Status of Product(in stock or not): ")
    Category = input("Enter the Category of Product(Veg or Non-Veg): ")

    records[productId] = {'Name': Name, 'Price': Price, 'Quantity': Quantity, 'Weight': Weight, 'Status': Status, 'Category': Category}

    ask = input("Do you want to add more items (Y/N): ")
    if ask == 'N':
        ans = False

js = json.dumps(records)

fd = open("records.json",'w')
fd.write(js)
fd.close() 
