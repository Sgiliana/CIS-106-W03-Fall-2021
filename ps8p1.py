def next(month,sales):
  if month == "Jan" or "Feb" or "Mar":
    percent = 0.10
  elif month == "Apr" or "May" or "Jun":
    percent = 0.15
  elif month == "Jul" or "Aug" or "Sep":
    percent = 0.20
  else:
    percent = 0.25
  
  return percent

response = input("Would you like to run this program (Yes or No): ")
while (response == "Yes"):  
  name = input("Enter last name ")
  month = input("Enter month ")
  sales = float(input("Enter sales "))

  percent = next(month,sales)
  nextsales = sales * (1+percent)

  print("Next months sales is ", nextsales)
  
  response = input("Would you like to run this program (Yes or No): ")