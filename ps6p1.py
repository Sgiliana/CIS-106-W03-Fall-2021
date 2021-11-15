# count from 1 to 10 by 1's
# start value
# stop value
# increment value 

for count in range (1,11, 2):
  print(count)

for number in range(11):
  print(number)
response = (input("Would you like to start this program (Yes or No) "))
while (response == "Yes"):
  p = float(input("Enter Principle "))
  r = float(input("Enter interest rate "))
  # header
  for count in range (1, 6, ):
    i = p * r
    eb = p + i
    print (count, "  ", p, "   ", eb)
    p = eb
  response = (input("Would you like to start this program (Yes or No) "))