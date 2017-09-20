# with open("eits.csv",'r') as f:
#   for line in f.readlines():
#     print (line)

class School():
  def __init__(self, eits=[],fellows=[]):
    self.eits = eits
    self.fellows = fellows

  def register(self,eit):
    self.eits.append(eit)
    return print ("eit {} saved successfully".format(eit.name))

  def hire(self,fellow):
    self.fellows.append(fellow)
    return print ("fellow {} saved successfully".format(fellow.name))

  def fire(self,fellow):
    self.fellows.remove(fellow)
    return print ("Prez Trump says 'you're FIRED {}".format(fellow.name))


class Person():
  def __init__(self,name,nationality="Earthling"):
    self.name = name
    self.nationality = nationality


class EIT(Person):
  def __init__(self, name, nationality):
    super().__init__(name,nationality)




  # def drop_knowledge(self, facts=[]):
  #   self.facts = facts





class Fellow(Person):
  
  __instances = []

  def __init__(self,name, nationality,happiness_level=5):
    super().__init__(name,nationality)
    self.happiness_level = happiness_level
    self.__instances.append(self)

    if len(self.__instances) > 5:
      self.__instances.pop(0)
      raise "Andrew's weave drained MEST's account"
    

  def eat(self):
    self.happiness_level += 10
    print("Yummy, I love banku. happiness level now {}".format(self.happiness_level))

  def teach(self):
    self.happiness_level -= 7
    print ("I hate teaching. Happiness level now {}".format(self.happiness_level))

  def fellow_count(self):
    print(len(self.__instances))





mest = School()
# sadiq = EIT("sadiq")

miishe = Fellow("Miishe","ghanarican")
francis = Fellow("Francis","ghanaian")
andrew = Fellow("drew","amurricuh")
kerry = Fellow("drew","usa")
pascal = Fellow("drew","Congo")
simpiwe = Fellow("Sim","south african")
# edem = Fellow("Edem","ghanaian")

# print(sadiq.name,sadiq.nationality)
print ("hi i'm {}, my nationality is {} and my current happiness is {}".format(miishe.name, miishe.nationality, miishe.happiness_level))

miishe.eat()
miishe.teach()
# edem.fellow_count()
# miishe.teach()

# mest.hire(miishe)
# mest.hire(francis)
# mest.hire(andrew)
# mest.register(sadiq)
# mest.fire(andrew)



