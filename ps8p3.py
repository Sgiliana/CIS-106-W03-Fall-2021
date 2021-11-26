def otdprice(msrp, make, model, code):
  if make == "Honda" and model == "Accord":
    pomsrp = 0.10
  elif make == "Toyota" and model == "Rav4":
    pomsrp = 0.30
  elif code == "Y":
    pomsrp = 0.30
  else: 
    pomsrp = 0.05
  
  total = msrp - pomsrp + 0.07

  return total

totalmsrp = 0
totalprice = 0 
response = input("Would you like to run this program (Yes or No): ")
while (response == "Yes"):  
  make = (input("Enter make "))
  model = (input("Enter model "))
  code = input("Enter electric code (Y or N) ")
  msrp = float(input("Enter MSRP "))

  total = otdprice(msrp, make, model, code)
  
  print("The total is ", total)

  totalmsrp = totalmsrp + msrp
  totalprice = totalprice + total

  print("The sum of all MSRP is", totalmsrp)
  print("The sum of all out the door prices is ", totalprice)
  
  response = input("Would you like to run this program (Yes or No): ")