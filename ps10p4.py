f = open("lnames.txt", "r")

lastn = []
score = []

lastname = f.readline()

while lastname != "":
  lastn.append(str(lastname).rstrip("\n"))
  s = float(f.readline())
  score.append(s) 
  lastname = f.readline()

f.close

namescores = zip(lastn,score)
clist = list(namescores)
print(clist)

def search(lastn, pname):
  l = len(lastn)
  sindex = -1
  for y in range (0,l,1):
    if lastn[y] == pname:
      sindex = y
  
  return sindex

response = input("Would you like to run this program (Yes or No): ")
while response == "Yes":
  pname = input("Enter last name: ")
  i = search(lastn,score)
  print("The score is ", score[i]) 
  
  response = input("Would you like to run this program (Yes or No): ")