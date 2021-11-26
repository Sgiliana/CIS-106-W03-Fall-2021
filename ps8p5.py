def avalue(county,mvalue):
  if county == "Cook":
    avalue = mvalue * 0.90
  elif county == "DuPage":
    avalue = mvalue * 0.80
  elif county == "McHenry":
    avalue = mvalue * 0.75
  elif county == "Kane":
    avalue = mvalue * 0.60
  else:
    avalue = mvalue * 0.70
  
  return avalue

totalmv = 0
totalav = 0
response = input("Would you like to run this program (Yes or No) ")
while (response == "Yes"):
  county = input("Enter county ")
  mvalue = float(input("Enter market value of home "))

  asvalue = avalue(county,mvalue)
  totalmv = totalmv + mvalue
  totalav = totalav + asvalue
  print("The assessed value of the home is $",asvalue)
  print("The total of all market values is $",totalmv)
  print("The total of all assessed values is $",totalav)

  response = input("Would you like to run this program (Yes or No) ")
