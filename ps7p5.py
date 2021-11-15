def to(hours,code):
  if code == "I":
    tuition = hours * 250
  else: 
    tuition = hours * 550
  
  return tuition

name = input("Enter student's last name ")
hours = float(input("Enter number of credit hours "))
code = input("Enter district code (I or O)")

tuition = to(hours,code) 

print("The tuition for ", name , " is ",tuition)