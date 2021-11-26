def disc(qty,price,rate):
  discamt = (price * qty) * rate
  discprice = (price * qty) - discamt 

  return discamt,discprice

qty = float(input("Enter quantity "))
price = float(input("Enter price "))
rate = float(input("Enter rate "))

discamt,discprice = disc(qty,price,rate)
print("The discounted amount is $", discamt)
print("The discounted price is ", discprice)
print("The original price was ", price)
print("The quantity was ", qty)