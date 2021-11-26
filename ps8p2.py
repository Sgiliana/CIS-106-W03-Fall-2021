def sqfoot(length,width,height):
  sqft = (2 * width * length) + (2 * length * height) +(2 * width * height)

  return sqft

response = input("Would you like to run this program (Yes or No): ")
while (response == "Yes"):  
  length = float(input("Enter length "))
  width = float(input("Enter width "))
  height = float(input("Enter height "))

  sqft = sqfoot(length,width,height)
  gallons = sqft / 50 

  print("The number of gallons needed is", gallons)
  
  response = input("Would you like to run this program (Yes or No): ")