class Student:

  def __init__(self, first, last, code, credits):
    self.first = first
    self.last = last 
    self.code = code
    self.credits = credits

  
  def tuition(self,code,credits):
    if code == "I":
      tuition = 250 * credits
    else: 
      tuition = 500 * credits

    return tuition

st1 = Student("Test", "User", "I", 40)
print(st1.first)
print(st1.last) 
print(st1.code) 
print(st1.credits) 
print(st1.tuition("I",40))
print(st1.tuition("O",30))