def gascost(gallons):
  cost = gallons * 2.50
  
  return cost
def mpg(miles, gallons):
  mpg = miles / gallons
  
  return mpg

city = input("Enter destination city ")
miles = float(input("Enter miles travelled "))
gallons = float(input("Enter gallons used "))

mpg = mpg(miles, gallons)
cost = gascost(gallons) 

print("For destination city ", city, "the miles per gallon was ", mpg, "and the cost for gas was ", cost)