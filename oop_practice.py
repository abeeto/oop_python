### My Answers:
# 
# what is a class?
    # a class is a type of 'object' that we can define. The class can contain specific attributes and methods specific to that class.
#what is an instance?
    # an instance is an individual object of a class
#what is encapsulation?
    # encapsulation is the idea of ensuring that the methods of a class is only able to be accessed by instances of that class. Setting and getting values may also be done anly via getter and setter methods.
#what is an abstraction?
    # abstraction is the ability for complex functions and objects be broken down into smaller classes and consequently, smaller objects
#what is inheritance?
    # inheritance allows classes to possess the same traits and methods of another class depending on their relationship. If a class extends another class, that class receives the traits of that class in addition to its existing attributes and methods.
#what is multiple inheritance?
    # multiple inheritance is when a class can inherit attributes from multipel classes.
#what is polymorphism?
    # polymorphism is the idea that classes can change dynamically 
#what is multiple resolution order or MRO?
    # MRO is the measure of how much inheritance a specific class takes and uses from other classes.



#create a deck of cards:
import math
import random as rnd

class Card:
    def __init__(self):
        self._suit = "nothing"
        self._value = 0
    @property
    def value(self):
        print("Card's Value: " + str(self._value))
        return self._value
    @property
    def suit(self):
        print("Card's Suit: " + str(self._suit))
        return self._suit
    @suit.setter
    def suit(self, s):
        if s.lower() in "hearts clubs diamonds spades":
            self._suit = s
        else:
            print("Not a possible suit")
    @value.setter
    def value(self, x):
        if x in list(range(2,11)):
            self._value = x
        elif x in [1, 11, 12, 13]:
            valueRole = {1: "A", 11: "J", 12: "Q", 13: "K"}
            self._value = valueRole[x]
        elif type(x) == str and x.upper() in ["A", "J", "Q", "K", "ACE", "JOKER", "QUEEN", "KING"]:
            self._value = x.upper()[0]
        else: 
            print( "Not a possible value")

class Deck:
    def __init__(self):
        self.all = []
        suitsToAssign = ["hearts", "clubs", "diamonds", "spades"]
        for i in range(4):
            for x in range(13):
                self.all.append(Card())
                self.all[i*13+x].value = x+1
                self.all[i*13+x].suit = suitsToAssign[i]
                self.all[i*13+x].value
                self.all[i*13+x].suit

    def deal(self):
        randCard = rnd.randint(0, 51)
        return self.all[randCard]
    def shuffle(self):
        rnd.shuffle(self.all)
        [x.value for x in self.all]
        [x.suit for x in self.all]


    

newDeck = Deck()
print("New Deck Shuffled")
print("*****************")
newDeck.shuffle()
