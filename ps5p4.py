tgross = 0
c = 0
response = input("Do you want to continue (Yes or No) ")

while (response == "Yes"):
  name = input("Enter employee last name ")
  hours = float(input("Enter hours worked "))
  rate = float(input("Enter rate of pay "))
  
  if hours > 40:
    gross = (hours - 40) * (rate * 1.5) + (40 * rate)
  else: 
    gross = hours * rate
  
  c = c + 1
  tgross = tgross + gross
  
  print("For employee ", name)
  print("The gross pay is ", gross)

  response = input("Do you want to continue (Yes or No) ")
avg = tgross / c
print("The number of employees who entered data is ", c)
print("The sum of all gross pay is ", tgross)
print("The average gross pay is ", avg)