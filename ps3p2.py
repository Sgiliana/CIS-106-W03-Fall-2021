item = input("Enter an item to order (A or B) ")
qty = float(input("Enter quantity to order "))

if item == "A": 
  up = 10.00
else:
  up = 20.00

extprice = up * qty

print("Item Ordered: ", item)
print("Quantity: ", qty)
print("Unit Price ", up)
print("Extprice: ", extprice)


