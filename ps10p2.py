lastn = ["Smith", "Brown", "Williams", "White", "Watson", "Daniels", "Thompson", "Davis", "Garcia", "Jones"]
scores = [76, 90, 74, 82, 93, 89, 65, 90, 99, 88]

def printArrays(lastn, scores):
  l = len(lastn)
  for x in range(0, l, 1):
    print(x, " ", lastn[x], " ", scores[x])
  
printArrays(lastn,scores)