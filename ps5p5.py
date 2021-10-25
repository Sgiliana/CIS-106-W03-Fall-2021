discsum = 0.0
response = input("Do you want to continue (Yes or No)")

while (response == "Yes"):
  qty = float(input("Enter quantity"))
  price = float(input("Enter price"))

  extprice = price * qty

  if extprice > 1000.00:
    discamt = extprice * 0.25
  else:
    discamt = extprice * 0.10
  
  total = extprice - discamt

  discsum = discsum + discamt

  print("Extended price ", extprice)
  print("Discount amount ", discamt)
  print("New total", total)

  response = input("Do you want to continue (Yes or No)")

print("Total discounts given ", discsum)