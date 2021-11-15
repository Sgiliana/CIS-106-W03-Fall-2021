def batavg(hits, bats):
  avg = float(hits) / float(bats)

  return avg

name = input("Enter player's last name ")
hits = float(input("Enter number of hits "))
bats = float(input("Enter number of at bats "))

avg = batavg(hits,bats)

print("The batting average for ", name, "is ", avg)