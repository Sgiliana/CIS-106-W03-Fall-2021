name = input("Enter name of appliance ")
cost = float(input("Enter cost of appliance "))

if cost > 1000:
  warrantee = cost * 0.10
else: 
  warrantee = cost * 0.05

total = cost + warrantee

print("The appliance being purchased is", name)
print("The cost of the item is", cost)
print("The cost of the warrantee is", warrantee)
print("The total cost of the item plus its warrantee is", total)