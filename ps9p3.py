def sale(sales):
  if sales > 100000:
    rate = 0.10
  else: 
    rate = 0.05

  com = sales * rate
  target = sales + (sales * 0.05)

  return com,target

name = input("Enter last name ")
sales = float(input("Enter sales "))

com,target = sale(sales)

print("For ", name , " the commission is $",com, "and next years target sales is $", target)