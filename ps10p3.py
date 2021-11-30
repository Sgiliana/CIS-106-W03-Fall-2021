def displaynames(lastn,score):
  for i in lastn:
    print(i) 
  for y in score:
    print(y)

def hilow(lastn,score):
  l = len(lastn)
  hiscore = -1.0
  lowscore = 99999999.99
  for y in range (0,l,1):
    if float(score[y]) > float(hiscore):
      hiindex = y
      hiscore = score[y]

    if float(score[y]) < float(lowscore):
      loindex = y
      lowscore = score[y]
    
  print("The highest score is", lastn[hiindex], score[hiindex])
  print("The lowest score is", lastn[loindex], score[loindex])

f = open("lnames.txt", "r")

lastn = []
score = []

lastname = f.readline()

while lastname != "":
  lastn.append(str(lastname).rstrip("/n"))
  s = float(f.readline())
  score.append(s)
  lastname = f.readline()

f.close()

displaynames(lastn,score)
hilow(lastn,score)