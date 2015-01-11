#-------------------------------------------------------------------------------
# Name:        Item
# Purpose: Defines a class called Item that creates an object that interacts
# with a Pet object in order to help the Pet stay alive.
#
# Author:      odanielb (Bridget O'Daniel)
#
# Acknowledgements: Help with string formatting for __str__ from: http://stackoverflow.com/questions/2763432/how-to-print-the-sign-of-a-digit-for-positive-numbers-in-python
#
#-------------------------------------------------------------------------------

class Item(object):
    """This class defines an Item with certain qualities that represent a
    potential to fill needs such as hunger, health and happiness that need to be
    satisfied in a given Pet object."""

    MAX_HUNGER_POINTS = 100
    MIN_HUNGER_POINTS = -100
    MAX_HAPPY_POINTS = 100
    MIN_HAPPY_POINTS = -100
    MAX_FRIEND_POINTS = 1
    MIN_FRIEND_POINTS = 0
    MAX_HEAL_POINTS = 100
    MIN_HEAL_POINTS = -100
    MAX_COST = 100000
    MIN_COST = 1

    def __init__(self, name = "Item", cost = 1, hunger_points = 0, happy_points = 0, heal_points = 0, friend_points = 0):
        """Creates an item that could interact with a Pet object.
        pre: name - a string containing the name of the item (eg, Apple, Toy, etc). Named "Item" by default (no name provided).
             cost - an int between 1 and 100,000. Defaults to 1.
             hunger_points - an int between -100 and 100. Defaults to 0.
             happy_points - an int between -100 and 100. Defaults to 0.
             heal_points - an int between -100 and 100. Defaults to 0.
             friend_points - an int, either 0 or 1. Defaults to 0."""
        self.name = name        #name of item
        self.hunger_points = 0  #how much fullness item could restore/deplete
        self.happy_points = 0   #how much happiness item could restore/deplete
        self.friend_points = 0  #how much friendship item could give
        self.heal_points = 0    #how much health item could restore/deplete
        self.cost = 1           #how much item costs

        self.set_cost(cost)                     #Will only use provided values if they are valid
        self.set_hunger_points(hunger_points)
        self.set_happy_points(happy_points)
        self.set_heal_points(heal_points)
        self.set_friend_points(friend_points)

#------------ Returning Item Attributes ---------------------------------------#

    ##Added the following get functions, to match proper class style (ie, not directly accessing instance variables)
    def get_name(self):
        """Returns the name of the item (as a string)."""
        return self.name


    def get_hunger_points(self):
        """Returns the hunger point value of the item (as an int)."""
        return self.hunger_points


    def get_happy_points(self):
        """Returns the happy point value of the item (as an int)."""
        return self.happy_points


    def get_friend_points(self):
        """Returns the friend point value of the item (as an int)."""
        return self.friend_points


    def get_heal_points(self):
        """Returns the healing point value of the item (as an int)."""
        return self.heal_points


    def get_cost(self):
        """Returns the cost of the item (as an int)."""
        return self.cost

#------------ Setting Item Attributes -----------------------------------------#

    def set_hunger_points(self, hunger_points = -200):
        """Sets the fullness points this Item would give to a Pet object.
        pre: hunger_points is an int between -100 and 100.
        post: The item is set to give the provided number of fullness points. If
        no number (or an invalid number) is provided, defaults to 0"""
        if (hunger_points >= self.MIN_HUNGER_POINTS) and (hunger_points <= self.MAX_HUNGER_POINTS): #If the provided value is within the acceptable range
            self.hunger_points = hunger_points                                                          #Make the change
        else:
            self.hunger_points = 0                                                                  #Otherwise default it to 0


    def set_happy_points(self, happy_points = -200):
        """Sets the happiness points this Item would give to a Pet object.
        pre: happy_points is an int between -100 and 100.
        post: The item is set to give the provided number of happiness points.
        If no number (or an invalid number) is provided, defaults to 0"""
        if (happy_points >= self.MIN_HAPPY_POINTS) and (happy_points <= self.MAX_HAPPY_POINTS): #If the provided value is within the acceptable range
            self.happy_points = happy_points                                                        #Make the change
        else:
            self.happy_points = 0                                                               #Otherwise default to 0


    def set_heal_points(self, heal_points = -200):
        """Sets the health points this Item would give to a Pet object.
        pre: heal_points is an int between -100 and 100.
        post: The item is set to give the provided number of health points. If
        no number (or an invalid number) is provided, defaults to 0."""
        if (heal_points >= self.MIN_HEAL_POINTS) and (heal_points <= self.MAX_HEAL_POINTS): #If the provided value is within the acceptable range
            self.heal_points = heal_points
        else:
            self.heal_points = 0


    def set_friend_points(self, friend_points = -1):
        """Sets the friend points this Item would give to a Pet object.
        pre: friend_points is an int, either 0 or 1.
        post: The item is set to give the provided number of friend points. If
        no number (or an invalid number) is provided, defaults to 0"""
        if (friend_points >= self.MIN_FRIEND_POINTS) and (friend_points <= self.MAX_FRIEND_POINTS): #If the provided value is within the acceptable range
            self.friend_points = friend_points
        else:
            self.friend_points = self.MIN_FRIEND_POINTS


    def set_cost(self, cost = 0):
        """Sets cost of the Item.
        pre: cost is a positive int between 1 and 100,000. If not provided or an
        invalid number is provided, cost is set to 1.
        post: Cost of item is changed to provided amount."""
        if (cost >= self.MIN_COST) and (cost <= self.MAX_COST): #If the provided value is within the acceptable range
            self.cost = cost
        else:
            self.cost = self.MIN_COST

#------------ Output ----------------------------------------------------------#

    def __str__(self):
        """Prints the benefits/traits of the Item, such as cost and how much it
        would boost a pet's fullness, happiness, etc if bought."""
        return """{name}'s properties:
            Fullness:   {0:+}
            Happiness:  {1:+}
            Health:     {2:+}
            Friendship: {3:+}
            COST:       {cost}\n""".format(self.hunger_points, self.happy_points, self.heal_points, self.friend_points, name=self.name, cost=self.cost)

