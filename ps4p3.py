principle = float(input("Enter principle amount of a CD $"))
years = float(input("Enter year to maturity of CD "))

if principle > 100000 and years == 5:
  intrate = 0.06
elif principle >= 50000 and principle <= 100000 and years == 10: 
  intrate = 0.05
elif principle >= 50000 and principle <= 100000 and years == 5:
  intrate = 0.04
else: 
  intrate = 0.02
  


intramt = principle * intrate

print("The principle amount was $", principle)
print("The interest rate is", intrate)
print("The interest amount for the first year is $", intramt)