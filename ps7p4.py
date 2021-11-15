def payrate(code):
  if code == "L":
    rate = 25
  elif code == "A":
    rate = 30
  else:
    rate = 50
  
  return rate

def grosspay(hours,rate):
  if hours > 40:
    pay = (hours - 40) * (rate * 0.5) + (hours * rate)
  else:
    pay = rate * hours

  return pay

name = input("Enter employee's last name ")
code = input("Enter job code (A, L, or J) ")
hours = float(input("Enter number of hours worked "))

rate = payrate(code)
pay = grosspay(hours,rate)

print("The gross pay for ", name , " is ", pay)