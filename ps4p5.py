name = str(input("Enter employee's last name: "))
salary = float(input("Enter salary: "))
jl = float(input("Enter job level: "))

if jl >= 10:
  br = 0.25
elif jl >= 5 and jl <= 9:
  br = 0.20
else: 
  br = 0.10

bonus = salary * br

print("For employee: ", name)
print("The bonus is: $",bonus)