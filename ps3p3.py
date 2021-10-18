nob = float(input("Enter number of books to order "))
cpb = float(input("Enter cost per book "))

total = nob * cpb 

if total > 50:
  shipcost = 0
else: 
  shipcost = 25

print("The order total is", total , "and the shipping charge is", shipcost)