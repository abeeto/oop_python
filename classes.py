class person:
    def __init__(self, name, age, weight, height, type = "base"):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.type = type
        
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
    def __init__(self, name, pickable = False, type = "Base"):
        self.name = name
        self.pickable = pickable
        self.type = type
    def giveName(self):
        return self.name


# class armor(items):
# class potion(items):

class weapons(items):
    def __init__(self, damage, speed,cooldown, freq, equiped = False):
        self.damage = damage
        self.speed = speed
        self.cooldown = cooldown
        self.freq = freq
        self.equiped = equiped
    def equip(self):
        if(self.equiped == False):
            self.equiped = True
            print(f"""Ëquiped {super().giveName}""")
        else:
            self.equiped = False
            print(f"""Removed {super().giveName()}""")

    


myMain = fighter("Hiro", "18", "74", "182")
longsword = weapons("longsword", 24,13,10,0.8) 
print(myMain.health)
myMain.takeDamage(myMain.dealDamage())
print(myMain.health)
