from importlib import import_module
import csv

class person:
    all = []
    def __init__(self, name, age, weight, height, type = "base"):
        self.__name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.type = type
        if self.type == None:
            self.type = "base"
        person.all.append(self)
    @property
    def name(self):
        print("you are trying to receive the name")
        return self.__name

    @name.setter
    def name(self, value):
        print("you are trying to change the name")
        self.__name = value

    def __repr__(self):
        return(f"{self.__class__.__name__}[{self.name},{self.age},{self.weight},{self.height},{self.type}]")
    def display_stats(self):
        print(f"""Name: {self.name} \nAge: {self.age} \nName: {self.weight} kg \nHeight: {self.height} cm \nType:{self.type}""")
    
    
    #we use @ as a decorator to declare a class method
    @classmethod
    def importFromCSV(cls):
        with open('persons.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter = ",")
            items = list(reader)
        for item in items:
            person(
                name = item.get('name'),
                age = float(item.get('age')),
                weight = float(item.get('weight')),
                height = float(item.get('height')),
                type = item.get('type'),
            )
    #staticMethod - does not pass class method as an argument
    #treat static method like a normal, isolated function

    @staticmethod
    def is_integer(num):
        if(isinstance(num, float)):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
#inheritence
class fighter(person):
    all = []
    def __init__(self, name, age, weight, height, type = "fighter"):
        super().__init__(name, age, weight, height,type)
        self.health = 100
        self.speed = 15
        self.attackSpeed = 35
        self.base_att = 15
        self.base_def = 35
        fighter.all.append(self)
    def takeDamage(self, damageGiven):
        damageGiven *= (1 - self.base_def/1000)
        self.health -= damageGiven
    def dealDamage(self):
        return self.base_att
    def displayStats(self):
        return super().display_stats()
        # return super().display_stats()  + f"Health: {self.health} \nSpeed: {self.speed} \nAttack speed: {self.attackSpeed} \nAttack: {self.base_att} \nDefence: {self.base_def} "
    
person.importFromCSV()
# fighterHiro = fighter("Alex", 19, 190, 176)
# print(fighterHiro.health)
# fighterHiro.takeDamage(fighterHiro.dealDamage())
# print(fighterHiro.displayStats())
