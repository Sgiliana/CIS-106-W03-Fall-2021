def amnt(qty,price):
  global total
  global tax 
  total = qty * price
  tax = total * 0.07

  return total,tax


qty = float(input("Enter quantity "))
price = float(input("Enter price of item "))

total,tax = amnt(qty,price)

print("The total amount is $", total)
print("The  tax amount is $", tax)