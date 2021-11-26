def pts(exam1,exam2,exam3):
  total = exam1 +exam2 + exam3
  avg = (exam1 +exam2 + exam3) / 3
  
  return total,avg

name = input("Enter last name ")
exam1 = float(input("Enter first exam score "))
exam2 = float(input("Enter second exam score "))
exam3 = float(input("Enter third exam score "))

total,avg = pts(exam1,exam2,exam3)

print("For student :", name)
print("The total points is ", total)
print("The average score is ", avg)