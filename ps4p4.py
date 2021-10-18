numb = float(input("Enter number of tickets: "))

if numb >= 25:
  price = 50
elif numb >= 10 and numb <= 24:
  price = 60
elif numb >= 5 and numb <= 9:
  price = 70
else: 
  price = 75

total = numb * price

print("The number of tickets is: ", numb)
print("The price per ticket is: ", price)
print("The total cost is: ", total)
