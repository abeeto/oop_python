class person:
    all = []
    def __init__(self, name, age, weight, height, type = "base"):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.type = type
        person.all.append(self)
    # def __repr__(self):
    #     return(f"{self.name},{self.age},{self.weight},{self.height},{self.type}")
    def display_stats(self):
        print(f"""Name: {self.name} \nAge: {self.age} \nName: {self.weight} kg \nHeight: {self.height} cm \nType:{self.type}""")


#inheritence
class fighter(person):
    health = 100
    speed = 30
    attackSpeed = 35
    base_att = 15
    base_defence = 35
    def takeDamage(self, damageGiven):
         damageGiven *= (1 - self.base_defence/1000)
         self.health -= damageGiven
    def dealDamage(self):
        return self.base_att
    

class items:
    def __init__(self,name, type = "Base"):
        self.name = name
        self.type = type
    def giveName(self):
        return self.name


# class armor(items):
# class potion(items):

class weapons(items):
    def __init__(self, name,damage, speed,cooldown, freq, equiped = False):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.cooldown = cooldown
        self.freq = freq
        self.equiped = equiped
    def equip(self):
        if(self.equiped == False):
            self.equiped = True
            print(f"""Equiped {self.name}""")
        else:
            self.equiped = False
            print(f"""Removed {self.name}""")

    



#testing
myMain = person("Hiro", "18", "74", "182")
ogre = person("Shrek", "43", "300", "220")

for instance in person.all:
    print(instance.age)

longsword = weapons("rusty longsword", 24,13,10, 5, 0.8)
longsword.equip()
longsword.equip()