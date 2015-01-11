#-------------------------------------------------------------------------------
# Name:        Owner
# Purpose: To create class objects that represent the Owner of a Pet object, who
#    will take care of it by spending time with it, performing actions, and
#    buying it Items from a Shop.
#
# Author:      odanielb, Bridget O'Daniel
#
# Acknowledgements:
#-------------------------------------------------------------------------------

from Pet import Pet
import time

class Owner(object):
    """Creates Owner class objects that represent the Owner of a Pet object, who
    will take care of it by spending time with it, performing actions, and
    buying it Items from a Shop."""

    MIN_MONEY = 0
    MIN_SALARY = 100
    MAX_SALARY = 600
    PAY_DAY = 10        #Pay Day every 10 seconds
    MAX_ITEMS = 5

    def __init__( self, pet=Pet("Pet") ):
        """Creates an Owner object who owns a provided pet. THe Owner takes care
        of the pet, earns money, and buys items for the pet.
        pre: pet is a Pet object. If nothing is provided, a new Pet object named
        'Pet' is created."""
        self.pet = pet
        self.money = 0
        self.salary = 100
        self.items = []

        self.__time_money_last_increased = time.time()

#------------ Returning Owner Attributes --------------------------------------#

    def money_balance(self):
        """Returns the amount of money Owner has."""
        return self.money


    def get_pet(self):
        """Returns the Pet that Owner has.
        post: Returns a Pet object."""
        return self.pet


    def get_salary(self):
        """Returns the current amount of money Owner regularly earns."""
        return self.salary

#------------ Money Management ------------------------------------------------#

    def receive_paycheck(self):
        """Owner receives their regular paycheck and it is added to their money.
        Note: The amount of money received is based on the Owner's salary.
        post: Owner's money is increased according to salary."""
        self.money += self.salary                                               #Adds paycheck to money available
        self.__time_money_last_increased = time.time()                          #Resets the time salary was last given


    def is_affordable(self, cost):
        """Checks if Owner has enough money to afford the provided cost.
        pre: cost is a positive int (1 <= cost <= 100,000)
        post: Returns True or False."""
        if cost > self.money:                                                   #If the cost is greater than what money Owner has,
            return False                                                            #Return False
        else:                                                                   #Otherwise,
            return True                                                             #Return True


    def pay(self, cost):
        """The Owner pays the cost. Owner does not
        pay if the cost is more money than they have.
        pre: cost is a positive int (1 <= cost <= 100,000)
        post: The Owner's money is reduced by the cost."""
        if self.is_affordable(cost):
            self.money -= cost


    def update_salary(self):
        """Increases or decreases the amount of money Owner receives based on
        friendship levels with their Pet. (More friendship = more money!)
        post: Increases or decreases Owner's salary."""
        friendship = self.pet.get_friendship()
        if friendship >= 1:                                                     #If friendship is greater than 1,
            self.salary = (friendship + 1)*self.MIN_SALARY                          #The salary is made according to this
        else:                                                                   #If friendship is less than 1 (ie 0),
            self.salary = self.MIN_SALARY                                           #The money rate is the minimum


    def check_if_pay_day(self):
        """Checks to see if enough time has elapsed to give more money. If so,
        increases money.
        post: Adds money if applicable, otherwise does nothing."""
        secs_passed = time.time() - self.__time_money_last_increased            #Seconds that have passed since last paycheck
        times_to_decrease = secs_passed//self.PAY_DAY                           #Figure out how many times to decrease based on the seconds
        for d in range(int(times_to_decrease)):                                 #For each calculated time,
            self.receive_paycheck()                                                 #Increase money


    def got_a_raise(self):
        """The Owner has gotten a raise, so it is changed.
        Note: The raises are based on Owner's friendship with their Pet."""
        self.update_salary()

#------------ Item Handling ---------------------------------------------------#

    def add_item(self, item):
        """Adds the provided item to the Owner's inventory of items for later use.
        pre: item is an Item object
        post: The item is added to the Owner's items, as long as there's room.
        (Owner objects can only own 5 items at a time!)."""
        if len(self.items) < 5:
            self.items.append(item)


    def get_num_items(self):
        """Returns the number of items the Owner has (as an int)."""
        return len(self.items)


    def get_items(self):
        """Returns the items currently in the Owner's possession as a list."""
        return self.items


    def toss_item(self, item):
        """Owner gets rid of the provided item.
        pre: item is an Item object currently in the Owner's items.
        post: item is removed from Owner's possessions."""
        if item in self.items:
            self.items.remove(item)


    def is_item_owned(self, item):
        """Checks if the Owner owns the provided item. Returns True or False.
        pre: item is an Item object.
        post: Returns True or False"""
        if item in self.items:
            return True
        return False


    def use_item(self, item):
        """Owner uses the item on their Pet.
        pre: item is an Item object currently in the Owner's items
        post: The Pet is affected by the item and it is removed from the Owner's
        items."""
        if self.is_item_owned(item):
            self.items.remove(item)
            self.pet.apply_item_effects(item)
            if item.get_friend_points() > 0:
                self.got_a_raise()

    def is_items_full(self):
        """Returns True if Owner has 5 objects, False if less."""
        return 5 == self.get_num_items()


#------------ Buying ----------------------------------------------------------#

    def buy(self, item):
        """Owner buys the provided Item for its cost and adds it to their
        inventory.
        pre: item is an Item object.
        post: Money is reduced by Item price and Item is in Owner's items."""
        self.pay( item.get_cost() )
        self.add_item(item)

