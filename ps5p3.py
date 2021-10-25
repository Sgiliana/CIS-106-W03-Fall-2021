c = 0
response = input("Do you want to run this program (Yes or No ")

while (response == "Yes"):
  name = input("Please enter last name ")
  score1 = float(input("Enter first exam score "))
  score2 = float(input("Enter second exam score "))
  avg = (score1 + score2) / 2
  c = c + 1
  print("The average for", name , "is ", avg)
  response = input("Do you want to run this program again (Yes or No)")

else:
  print("The number of students who have entered data is ", c)