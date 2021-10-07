#input
p1 = float(input("Enter price of item $"))
d1 = float(input("Enter discount amount in decimal form "))

#process
p2 = p1 - p1 * d1
d2 = p1 * d1 

#output
print("The discounted amount was $", d2, "and the discounted price of the item is $", p2)