#DL1
def dl1(mylist):
  n = int(input("Enter number of items for your list)"))
  for n in range(0,n,1):
    s = int(input("Enter an integer "))
    mylist.append(s) 
  return mylist
def displaylist(mylist):
  for item in mylist:
    print(item)


mylist = []
mylist = dl1(mylist)
displaylist(mylist)

#DL2
mylist.insert(0,99)
print(mylist)

#DL3
mylist[0] = 100
print(mylist)

#DL4
mylist2 = [500, 600, 700, 800, 900]
print(mylist2)
mylist.extend(mylist2)
print(mylist)

#DL5
mylist.remove(800)
print(mylist)

#DL6
mylist.pop(2)
print(mylist)

#DL7
grades = ["A", "B", "C", "A", "A", "C"]

#DL8
agrade = grades.count("A")
print("The number of A grades is", agrade)

#DL9
bindex = grades.index("B")
print("The index of the first B grade is", bindex)

#DL10
look_for = "F"
if look_for in grades:
  print(str(look_for) + "is at index " + str(grades.index(look_for)))
else:
  print(str(look_for) + " is not in the list")

#DL11
mylist2.clear()
print(mylist2)

#DL12
del mylist2
# print(mylist2) causes error

#DL13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

#DL14
players.sort()
print(players)

#DL15
players2 = players.copy()
print(players2)

#DL16
players2.sort(reverse=True)
print(players)
print(players2)