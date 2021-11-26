def price(miles):
  if miles >= 30: 
    price = 12
  elif 20 <= miles <= 29:
    price = 10
  elif 10 <= miles <=19:
    price = 8
  else:
    price = 5

  return price 

sumprice = 0 
response = input("Would you like to run this program (Yes or No): ")
while (response == "Yes"):
  name = input("Enter last name ")
  miles = float(input("Enter miles from downtown Chicago "))
 
  tprice = price(miles)
  sumprice = sumprice + tprice  
  print("The ticket price is $",tprice)
  print("The sum of all ticket prices is $",sumprice)
  
  response = input("Would you like to run this program (Yes or No): ")
