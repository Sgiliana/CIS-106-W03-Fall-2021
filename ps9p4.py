def scores(score1,score2,score3,hc):
  avg = (score1 + score2 +score3) / 3
  avghc = (((score1 +hc) + (score2 + hc) + (score3+hc))) / 3

  return avg,avghc

name = input("Enter last name ")
score1 = float(input("Enter first game score "))
score2 = float(input("Enter second game score "))
score3 = float(input("Enter third game score "))
hc = float(input("Enter handicap "))

avg,avghc = scores(score1,score2,score3,hc)

print("For: ", name)
print("The average score is ", avg)
print("The average score with handicap is ", avghc)

