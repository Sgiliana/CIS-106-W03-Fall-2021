qty = float(input("Enter quantity of widgets: "))

if qty > 10000: 
  price = 10
elif qty < 5000:
  price = 30
else:
  price = 20 

extprice = qty * price 
tax = extprice * 0.07 
total = extprice + tax 

print("The extended price is: $", extprice)
print("The tax amount is: $", tax)
print("The total amount is: $", total)