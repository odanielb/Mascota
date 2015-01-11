#-------------------------------------------------------------------------------
# Name:        Pet
# Purpose: Defines a class called Pet which may interact with Item objects in order
# to boost its stats and help it live as a virtual pet.
#
# Author:      odanielb (Bridget O'Daniel)
#
# Acknowledgements:
#-------------------------------------------------------------------------------

import time

class Pet(object):
    """This class defines a Pet that has needs such as hunger, health and
    happiness that need to be satisfied with Item objects."""

    MAX_FULLNESS = 100
    MIN_FULLNESS = 0
    MAX_HEALTH = 100
    MIN_HEALTH = 0
    MAX_HAPPINESS = 100
    MIN_HAPPINESS = 0
    MAX_FRIENDSHIP = 5
    SICK_DECREASE = 20
    HUNGER_RATE = 5
    SAD_RATE = 5
    CHANGE_STATE_TIME = 10 #Things will change every 10 seconds (yes, it is a high maintainence pet)

    def __init__(self, name = "Pet"):
        """Creates a Pet object that has needs such as fullness, happiness,
        health and friendship that keep it alive. Interacts with Item objects
        to help keep these needs met!
        NOTE: A Pet without an Owner will soon die!"""
        self.name = name
        self.fullness = self.MAX_FULLNESS
        self.happiness = self.MAX_HAPPINESS
        self.health = self.MAX_HEALTH
        self.friendship = 0
        self.alive = True

        self.__time_fullness_last_decreased = time.time()
        self.__time_happiness_last_decreased = time.time()
        self.__time_health_last_decreased = 0                                   #Health should not start decreasing until fullness or happiness is at 0

#------------ Returning Pet Attributes ----------------------------------------#

    def get_fullness(self):
        """Gets Pet's current fullness level and returns it."""
        return self.fullness


    def get_happiness(self):
        """Gets Pet's current happiness level and returns it."""
        return self.happiness


    def get_health(self):
        """Gets Pet's current health level and returns it."""
        return self.health


    def get_friendship(self):
        """Gets Pet's current friendship level and returns it."""
        return self.friendship


    def is_alive(self):
        """Checks if Pet is alive or dead.
        post: returns True or False."""
        if self.alive == True:
            return True
        else:
            return False


    def check_states(self):
        """Checks if fullness, happiness, and health need to be changed
        due to the time that has elapsed. Checks if health is at 0 (ie, dead pet).
        post: If so, makes those changes."""
        if self.alive == True:                                                  #If pet is alive,
            self.check_fullness_need_decrease()                                     #Check to see if fullness needs decreasing (and do it, if so)
            self.check_happiness_need_decrease()                                    #Same but happiness
            self.check_health_need_decrease()                                       #Same but health
            if self.health <= 0:                                                    #If health is all gone,
                self.kill_pet()                                                         #Pet is dead.
        else:                                                                   #If pet is dead, do nothing
            pass

#------------ Time Based State Changes ----------------------------------------#

    def decrease_fullness(self):
        """Makes Pet hungrier by a constant amount.
        post: Decreases Pet's fullness level."""
        if self.fullness >= self.HUNGER_RATE:                                   #If fullness will not be lowered past zero,
            self.fullness -= self.HUNGER_RATE                                       #Decrease by HUNGER_RATE
        else:                                                                   #Otherwise,
            self.fullness = 0                                                       #Make it zero

        self.__time_fullness_last_decreased = time.time()                       #Changes the time since fullness was decreased to NOW


    def decrease_happiness(self):
        """Makes Pet less happy by a predetermined amount.
        post: Decreases happiness and is affected by friendship levels.
        (the greater the friendship, the less happiness is decreased)"""
        if (self.friendship >= 1) and (self.happiness >= (self.SAD_RATE-(self.friendship-1))):   #If the friendship level is 1+ AND its happiness will not be lowered past zero,
            self.happiness -= self.SAD_RATE-(self.friendship-1)                                      #Happiness is lessened according to friendship level
        elif (self.friendship >= 1):                                                        #Else if the friendship level is 1+ (but it would be lowered past zero),
            self.happiness = 0                                                                  #Make happiness zero
        elif (self.friendship < 1) and (self.happiness >= self.SAD_RATE):                        #If the friendship level is 0 AND its happiness will not be lowered past zero,
                self.happiness -= self.SAD_RATE                                                      #Happiness is lessened according to the worst case SAD_RATE
        else:                                                                               #Otherwise (if friendship level is 0 and would be past zero),
            self.happiness = 0                                                                  #Make happiness zero

        self.__time_happiness_last_decreased = time.time()                                  #Update time since happiness was decreased.


    def make_sick(self):
        """Makes Pet sicker by a constant amount.
        post: Decreases Pet's health by a significant amount."""
        if self.health >= self.SICK_DECREASE:                                        #If health will not decrease below zero,
            self.health -= self.SICK_DECREASE                                            #Decrease it by SICK_DECREASE
        else:                                                                   #Otherwise,
            self.health = 0                                                         #Make it zero

        self.__time_health_last_decreased= time.time()                          #Update time since health was decreased.

#------------ General Changes in State ----------------------------------------#

    def change_fullness(self, change_amount):
        """Makes Pet hungrier or less hungry.
        pre: change_amount is a positive or negative int
        post: Changes fullness level based on change_amount, unless at max/min
        fullness, where it will cap off."""
        if ((self.fullness + change_amount) < self.MIN_FULLNESS):                    #If the change would make it less than 0,
            self.fullness = 0                                                       #Just bring it down to 0
        elif ((self.fullness + change_amount) > self.MAX_FULLNESS):                  #If the change would make it over 100,
            self.fullness = 100                                                     #Just bring it up to 100
        else:                                                                   #Otherwise,
            self.fullness += change_amount                                          #Add the change.


    def change_happiness(self, change_amount):
        """Makes pet happier or unhappier.
        pre: change_amount is a positive or negative int
        post: Changes happiness levels based on change_amount, unless at max/min
        happiness, where it will cap off."""
        if ((self.happiness + change_amount) < self.MIN_HAPPINESS):                  #If the change would make it less than 0,
            self.happiness = 0                                                      #Just bring it down to 0
        elif ((self.happiness + change_amount) > self.MAX_HAPPINESS):                #If the change would make it over 100,
            self.happiness = 100                                                    #Just bring it up to 100
        else:                                                                   #Otherwise,
            self.happiness += change_amount                                         #Add the change.


    def change_health(self, change_amount):
        """Makes pet healthier or unhealthier.
        pre: change_amount is a positive or negative int
        post: Changes health level base on change_amount, unless at max/min
        health, where it will cap off."""
        if ((self.health + change_amount) < self.MIN_HEALTH):                        #If the change would make it less than 0,
            self.health = 0                                                         #Just bring it down to 0
        elif ((self.health + change_amount) > self.MAX_HEALTH):                      #If the change would make it over 100,
            self.health = 100                                                       #Just bring it up to 100
        else:                                                                   #Otherwise,
            self.health += change_amount                                            #Add the change.


    def increase_friendship(self,increase_amount):
        """Increases friendship level with Pet. Cannot be decreased.
        pre: increase_amount is a positive int
        post: Increases friendship level, unless at max friendship, where it
        will cap off."""
        if ((self.friendship + increase_amount) > self.MAX_FRIENDSHIP):              #If the change would make it over 5,
            self.friendship = 5                                                      #Just bring it up to 5
        else:                                                                   #Otherwise,
            self.fullness += increase_amount                                         #Add the change.


##Money management processes are now handled by the Owner class -- (is_affordable, charge_money)

#------------ Item Interaction ------------------------------------------------#

    def apply_item_effects(self, item):
        """Applies the effects of a bought Item object on self.
        pre: item is an Item object
        post: if item indicates a change in fullness, happiness, health or
        friendship, it shall be changed for Pet."""
        if self.alive == True:
            self.change_fullness(item.get_hunger_points())                          #Add the matching attributes of the Item to Pet
            self.change_happiness(item.get_happy_points())
            self.change_health(item.get_heal_points())
            self.increase_friendship(item.get_friend_points())
        else:
            pass

#------------ Time Based Checking Methods -------------------------------------#

    def check_fullness_need_decrease(self):
        """Checks to see if enough time has elapsed to decrease fullness. If so,
        decreases fullness according to how much time has elapsed.
        post: Decreases fullness if applicable, otherwise does nothing."""
        secs_passed = time.time() - self.__time_fullness_last_decreased         #Seconds that have passed since last change
        times_to_decrease = secs_passed//self.CHANGE_STATE_TIME                 #Figure out how many times to decrease based on the seconds
        for d in range(int(times_to_decrease)):                                 #For each calculated time,
            self.decrease_fullness()                                                #Decrease fullness


    def check_happiness_need_decrease(self):
        """Checks to see if enough time has elapsed to decrease happiness. If so,
        decreases happiness according to how much time has elapsed.
        post: Decreases happiness if applicable, otherwise does nothing."""
        secs_passed = time.time() - self.__time_happiness_last_decreased
        times_to_decrease = secs_passed//self.CHANGE_STATE_TIME
        for d in range(int(times_to_decrease)):
            self.decrease_happiness()                                                        #Decrease happiness


    def check_health_need_decrease(self):
        """Checks to see if health needs to be decreased (if fullness or happiness
        are at zero and enough time has elapsed). If so, makes Pet sicker.
        post: Decreases health if applicable, otherwise does nothing."""    #If happiness/fullness are low enough and enough time has passed,
        if (self.fullness == 0 or self.happiness == 0) and ((time.time() - self.__time_health_last_decreased) >= self.CHANGE_STATE_TIME):
            self.make_sick()


#------------ Output ----------------------------------------------------------#

    def __str__(self):
        """Convert the information of this Pet into a string and returns it."""
        return """{name}'s current status:
            Alive:      {alive}
            Fullness:   {fullness}
            Happiness:  {happiness}
            Health:     {health}
            Friendship: {friendship}
            """.format(name = self.name, alive=self.alive, fullness=self.fullness, happiness=self.happiness, health=self.health, friendship=self.friendship)

#------------ Death -----------------------------------------------------------#

    def kill_pet(self):
        """Checks if conditions for death are true (ie, health is zero) and pet
        dies if so. Otherwise, nothing changes."""
        if self.health == 0:    #If health is 0,
            self.die()              #Pet is dead


    def die(self):
        """Pet dies. :(
        post: Pet is dead, meaning it cannot be played with anymore."""
        self.alive = False  #Pet dead now ;;


