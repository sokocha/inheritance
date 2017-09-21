import time
import csv
import random




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

  def drop_knowledge(self, facts=[]):
    self.facts = facts


class FactManager():
  def __init__(self,facts=[]):
    self.facts = facts

  def add_fact(self,fact):
    self.facts.append(fact)
    print("Fact saved successfully to Fact Manager")

  def loop(self):
    while True:
      new_factbook = FactManager()
      choice = input("Would you like to 'add' a fact or 'hear' a fact?  ").lower()

      if choice == 'add':
        new_fact = input("What's your new fact?  ")
        new_factbook.add_fact(new_fact)
        print ("there are {} fact(s)".format(len(self.facts)))
      elif choice == "hear":
        fact_quantity = len(self.facts)
        fact_index = random.randint(1,fact_quantity)
        print (self.facts[fact_index - 1])
      elif choice == "quit" or choice == "exit":
        return







class Fellow(Person):
  
  __instances = []

  def __init__(self,name, nationality,happiness_level=5):
    super().__init__(name,nationality)
    self.happiness_level = happiness_level
    self.__instances.append(self)

    if len(self.__instances) > 5:
      removed_instance = self.__instances.pop(-1)
      raise ValueError ("{} could not be hired. blame Andrew's weave".format(self.name))
    

  def eat(self):
    self.happiness_level += 10
    print("preparing to eat..")
    time.sleep(2)
    print("All done. Happiness level now {}".format(self.happiness_level))

  def teach(self):
    self.happiness_level -= 7
    print("preparing for class..")
    time.sleep(2)
    print ("Teaching sucks, happiness level now {}".format(self.happiness_level))

  def fellow_count(self):
    print(len(self.__instances))


def nationality_checker():
  with open('eits.csv','r') as my_file:
    for line in my_file.readlines():
      # print(line)
 
      name = line.split(',')[0].strip()
      nationality = line.split(',')[1].strip()
      

      if nationality == "Nigerian" or nationality == "Kenyan" or nationality == "Ivorian" or nationality == "Ghanaian" or nationality == "South African":
        print ("{} is a MESTER".format(name))
      else:
        print("Sorry {}, {} is NOT a MEST nationality".format(name,nationality))



nationality_checker()


# guiness_book = FactManager()
# guiness_book.loop()





mest = School()
sadiq = EIT("Sadiq","nigerian")




miishe = Fellow("Miishe","ghanarican")
francis = Fellow("Francis","ghanaian")
andrew = Fellow("drew","amurricuh")
kerry = Fellow("drew","usa")
pascal = Fellow("drew","Congo")
simpiwe = Fellow("Sim","south african")
# edem = Fellow("Edem","ghanaian")

# print(sadiq.name,sadiq.nationality)
# print ("{} is {} & current happiness is {}".format(miishe.name, miishe.nationality, miishe.happiness_level))

miishe.eat()
miishe.teach()

# edem.fellow_count()
# miishe.teach()

# mest.hire(miishe)
# mest.hire(francis)
# mest.hire(andrew)
# mest.register(sadiq)
# mest.fire(andrew)



