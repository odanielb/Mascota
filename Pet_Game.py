#-------------------------------------------------------------------------------
# Name:        Pet_Game.py
# Purpose: To create a class to play with a virtual pet!
#
# Author:      odanielb, Bridget O'Daniel
#
# Acknowledgements:
# The following images were borrowed and then edited:
#    Shop: https://cdn2.iconfinder.com/data/icons/windows-8-metro-style/512/shop.png
#    Money: http://cdn.flaticon.com/png/256/16302.png
#    Backpack: https://cdn3.iconfinder.com/data/icons/outdoor-and-camping-icons/512/Backpack-512.png
#    Stethoscope: https://cdn3.iconfinder.com/data/icons/healthcare-and-medicine-icons-1/512/Stethoscope-512.png
#    Home: https://cdn2.iconfinder.com/data/icons/windows-8-metro-style/512/home.png
#-------------------------------------------------------------------------------

from turtle_user_input import input_string   #This is the string that the user inputs
from turtle_user_input import set_up_window  #This sets up the onkey functions for that input
from turtle_user_input import unbind_keys    #This unbinds the onkey functions as needed

from Owner import Owner
from Pet import Pet         #This class was utilized by my first version of this game!
from Shop import Shop       #The Shop contains instances of an Item class, which was used in my first version of this game!

import sys
import Tkinter
import turtle
import time


class Pet_Game(object):
    """To create a class to handle and play a game using the Pet, Owner, Shop,
    and Item classes. It is designed so that a program using this class only
    needs to create an instance of this class for the game to run correctly."""

    def __init__(self):
        """Creates an instance of the Pet_Game class, which includes one Pet,
        one Owner (that's you!), and it will end when quit or when the pet dies.
        Note: Only one instance of this class will work at a time."""

        turtle.setup(700,500)   #Set up screen
        self.wn = turtle.Screen()
        self.wn.colormode(255)
        self.wn.bgcolor(0,0,52)

        name = self.__ask_for_name()
        self.__add_shapes()

        self.owner = Owner( Pet(name) )
        self.shop = Shop()
        self.is_game_over = False
        self._home_cursor_positions = [(-300, 150), (270, 150), (290, -150), (-300, -150)] #Shop, Money, Status, Items

        self.messenger = self._initialize_turtle( turtle.Turtle() )                  #Turtle for the message box
        self.instructor = self._initialize_turtle( turtle.Turtle() )                 #Turtle for writing instructions
        self.inventory_clerk = self._initialize_turtle( turtle.Turtle() )            #Turtle for the Owner's item menu
        self.doctor = self._initialize_turtle( turtle.Turtle() )                     #Turtle for Pet status
        self.pet_turtle = self._initialize_turtle( turtle.Turtle() )                 #Turtle to BE the pet on screen
        self.shop_button = self. _initialize_turtle( turtle.Turtle() )               #Turtle to BE the shop button
        self.balance = self._initialize_turtle( turtle.Turtle() )                    #Turtle to BE the money symbol
        self.bag = self._initialize_turtle( turtle.Turtle() )                        #Turtle to BE the item bag

        self.wn.onkey(self.Quit, "q")
        self.wn.listen()

        self.setup_home_screen()

        #Instructions
        self.messenger.setpos(0,100)
        self.messenger.write("Welcome! Here is your new pet, please take care of it!",move=False,align='center',font=("Century Gothic",18,("bold","normal")))
        self.messenger.setpos(0,80)
        self.messenger.write("Its status will decrease over time, so you'll need to buy items from the Shop to help.",move=False,align='center',font=("Century Gothic",11,("bold","normal")))
        self.messenger.setpos(0,60)
        self.messenger.write("As you navigate, you'll earn money, and you might even earn more if you and your pet",move=False,align='center',font=("Century Gothic",11,("bold","normal")))
        self.messenger.setpos(0,40)
        self.messenger.write("become friends! Navigate using the arrow keys, Enter to select, and Backspace to go back.",move=False,align='center',font=("Century Gothic",11,("bold","normal")))
        self.messenger.setpos(0,20)
        self.messenger.write("Press 'q' to quit at any time!",move=False,align='center',font=("Century Gothic",11,("bold","normal")))
        self.messenger.setpos(0,70)

        self.play()



#------------ Initializing Game Methods ---------------------------------------#

    def play(self):
        """Begins the to play the game. Waits until the game is quit by the user."""
        Tkinter.mainloop()


    def update_time_events(self):
        """Updates all of the time based events for the Shop, Pet and Owner.
        post: Stock in the Shop, states of the Pet, the Owner's money may be changed."""
        self.owner.check_if_pay_day()
        self.owner.pet.check_states()
        self.shop.check_if_restock()


    def __add_shapes(self):
        """Adds the shapes for the turtles that are necessary for the game."""
        self.wn.addshape("pack.gif")
        self.wn.addshape("thePet1.gif")
        self.wn.addshape("shop.gif")
        self.wn.addshape("money2.gif")
        self.wn.addshape("doctor.gif")
        self.wn.addshape("arrow_right.gif")
        self.wn.addshape("arrow_up.gif")
        self.wn.addshape("arrow_down.gif")
        self.wn.addshape("home.gif")
        self.wn.addshape("thePet_dead.gif")


    def __ask_for_name(self):
        """Asks user what to name their pet.
        post: returns the name as a string."""
        question_writer = self._initialize_turtle( turtle.Turtle() )
        question_writer.setpos(0, 90)
        question_writer.color(71, 230, 163)
        question_writer.write("Enter a name for your pet:",move=False,align='center',font=("Century Gothic",30,("bold","normal")))
        set_up_window(self.wn)
        self.wn.listen()                                                             #The window listens for key presses

        while input_string.writing:                                             #Waits for user input, ends with Enter
            question_writer.write("Enter a name for your pet:",move=False,align='center',font=("Century Gothic",30,("bold","normal")))
        name = input_string.get_string()

        question_writer.clear()
        unbind_keys(self.wn)
        input_string.clear_string()

        return name


    def _initialize_turtle(self, turtle):
        """Initializes the given turtle to be hidden, up, at the highest speed,
        and as the color for the game.
        pre: turtle is a Turtle object
        post: returns the turtle"""
        turtle.color(71, 230, 163)
        turtle.hideturtle()
        turtle.up()
        turtle.speed(0)
        return turtle


    def pet_dead(self):
        """When pet is dead, this displays all the appropriate things on the
        Home Screen.
        post: Game can only be quit"""
        self.hide_home_screen()
        time.sleep(2)
        self.pet_turtle.shape("thePet_dead.gif")
        self.pet_turtle.showturtle()
        self.messenger.setpos(0,70)
        self.messenger.write("Your pet died!",move=False,align='center',font=("Century Gothic",30,("bold","normal")))
        self.messenger.setpos(0,40)
        self.messenger.write("Press 'q' to quit.",move=False,align='center',font=("Century Gothic",15,("bold","normal")))



    def Quit(self):
        """Quits the program by closing window and then exiting using sys."""
        self.wn.bye()
        sys.exit()


#------------ Home Screen -----------------------------------------------------#

    #------------ Screen Settings ---------------------------------------------#
    def setup_home_screen(self):
        """Sets up the Home Screen.
        post: The Home Screen is shown."""
        self.hide_store_screen()

        self.pet_turtle.setpos(0, 200)   #Display pet name
        self.pet_turtle.write(self.owner.pet.name,move=False,align='center',font=("Century Gothic",30,("bold","normal")))

        self.pet_turtle.setpos(0,-75)    #Display pet
        self.pet_turtle.shape("thePet1.gif")
        self.pet_turtle.showturtle()

        self.shop_button.setpos(-230, 220)  #Display shop button
        self.shop_button.write("Shop",move=False,align='center',font=("Century Gothic",15,("bold","normal")))
        self.shop_button.setpos(-300, 210)
        self.shop_button.shape("shop.gif")
        self.shop_button.showturtle()

        self.balance.setpos(340, 190)       #Display CASH MONEY
        self.balance.write(self.owner.money_balance(),move=False,align='right',font=("Century Gothic",25,("bold","normal")))
        self.balance.shape("money2.gif")
        self.balance.setpos(200, 210)
        self.balance.showturtle()

        self.doctor.setpos(230, -240)       #Pet Status
        self.doctor.write("Status",move=False,align='center',font=("Century Gothic",15,("bold","normal")))
        self.doctor.setpos(300, -200)
        self.doctor.shape("doctor.gif")
        self.doctor.showturtle()

        self.bag.setpos(-230, -240)         #Display bag button
        self.bag.write("Items",move=False,align='center',font=("Century Gothic",15,("bold","normal")))
        self.bag.setpos(-300, -200)
        self.bag.shape("pack.gif")
        self.bag.showturtle()

        self.messenger.setpos(0,70)         #Message box

        self.__activate_home_keypresses()
        self.display_home_cursor(self._home_cursor_positions[0])

        if not self.owner.pet.is_alive():
            self.pet_dead()


    def hide_home_screen(self):
        """Hides the Home Screen, leaving the window blank except the background.
        post: A blank blue screen will be shown."""
        self.bag.clear()
        self.bag.ht()
        self.messenger.clear()
        self.doctor.clear()
        self.doctor.ht()
        self.balance.clear()
        self.balance.ht()
        self.shop_button.clear()
        self.shop_button.ht()
        self.pet_turtle.clear()
        self.pet_turtle.ht()
        self.inventory_clerk.ht()

        self.wn.onkey(None, 'Return')
        self.wn.onkey(None, 'p')
        self.wn.onkey(None, 'P')
        self.wn.onkey(None, 'Up')
        self.wn.onkey(None, 'Down')
        self.wn.onkey(None, 'Left')
        self.wn.onkey(None, 'Right')
        self.wn.onkey(None, 'BackSpace')

    #------------ Keypresses --------------------------------------------------#
    def __activate_home_keypresses(self):
        """Activates the onkey functions for the Home Screen and makes the
        window listen."""
        self.wn.onkey(self.home_cursor_selection, 'Return')
        self.wn.onkey(None, 'p')
        self.wn.onkey(None, 'P')
        self.wn.onkey(self.home_cursor_up, 'Up')
        self.wn.onkey(self.home_cursor_down, 'Down')
        self.wn.onkey(self.home_cursor_left, 'Left')
        self.wn.onkey(self.home_cursor_right, 'Right')
        self.wn.onkey(None, 'BackSpace')

        self.wn.listen()

    #------------ Cursors -----------------------------------------------------#
    def home_cursor_down(self):
        """Moves the cursor down if possible."""
        (old_x, old_y) = self.inventory_clerk.pos()                             #Get the current pos
        if old_y == abs(old_y):                                                 #If the y value is positive it can move down, so...
            if old_x != abs(old_x):                                                 #If the x is negative, it's at Shop
                self.display_home_cursor(self._home_cursor_positions[3])                #Move cursor to Items
            else:                                                                   #Otherwise,
                self.display_home_cursor(self._home_cursor_positions[2])                #Move to Status


    def home_cursor_up(self):
        """Moves the cursor up if possible."""
        (old_x, old_y) = self.inventory_clerk.pos()                             #Get the current pos
        if old_y != abs(old_y):                                                 #If the y value is negative it can move up, so...
            if old_x != abs(old_x):                                                 #If the x is negative, it's at Items
                self.display_home_cursor(self._home_cursor_positions[0])                #Move cursor to Shop
            else:                                                                   #Otherwise,
                self.display_home_cursor(self._home_cursor_positions[1])                #Move to Money


    def home_cursor_right(self):
        """Moves the cursor right if possible."""
        (old_x, old_y) = self.inventory_clerk.pos()                             #Get the current pos
        if old_x != abs(old_x):                                                 #If the x value is negative it can move right, so...
            if old_y == abs(old_y):                                                 #If the y is positive, it's at Shop
                self.display_home_cursor(self._home_cursor_positions[1])                #Move the cursor to Money
            else:                                                                   #Otherwise,
                self.display_home_cursor(self._home_cursor_positions[2])                #Move to Status


    def home_cursor_left(self):
        """Moves the cursor left if possible."""
        (old_x, old_y) = self.inventory_clerk.pos()                             #Get the current pos
        if old_x == abs(old_x):                                                 #If the x value is positive it can move left, so...
            if old_y == abs(old_y):                                                 #If the y is also positive, it's at money
                self.display_home_cursor(self._home_cursor_positions[0])                #Move the cursor to Shop
            else:                                                                   #If negative,
                self.display_home_cursor(self._home_cursor_positions[3])                #Move to Items


    def display_home_cursor(self, option_pos):
        """Moves the home cursor to point at a something from a given point.
        pre: option_pos is a tuple representing a position, (x, y).
        post: The cursor will be at to this location."""
        self.update_home_money()                                                #Updates the money on the screen everytime the cursor is moved
        self.update_time_events()                                               #Updates time events
        self.messenger.clear()                                                  #Clears messages when cursor is moved

        cursor_x, cursor_y = option_pos                                         #Get the x and y for the given position
        if cursor_y == abs(cursor_y):                                           #If the y is positive (ie, in the upper two quadrants)
            self.inventory_clerk.shape("arrow_up.gif")                              #use the up arrow
        else:                                                                   #If not,
            self.inventory_clerk.shape("arrow_down.gif")                            #Use the down arrow
        self.inventory_clerk.setpos(cursor_x, cursor_y)                         #Move cursor to the given position
        self.inventory_clerk.showturtle()                                       #Show the turtle

        if not self.owner.pet.is_alive():                                       #If Pet is dead, end game
            self.pet_dead()


    def home_cursor_selection(self):
        """When the user selects something on the Home Screen with the cursor,
        this method is used to determine what to do. It then does the appropriate
        action."""
        self.update_time_events()                                               #Updates time events
        if not self.owner.pet.is_alive():                                       #If Pet is dead, end game
            self.pet_dead()

        pos = self.inventory_clerk.pos()
        index = None
        for i, p in enumerate(self._home_cursor_positions):     #Finds which item was the selection
            if p == pos:
                index = i
                break

        if i == 0:
            self.setup_store()                                                  #Go to store
        elif i == 1:
            self.messenger.clear()                                              #Output money info
            self.messenger.write("You have $"+str(self.owner.money_balance())+", and your salary is $"+str(self.owner.get_salary())+".",move=False,align='center',font=("Century Gothic",15,("bold","normal")))
        elif i == 2:
            self.messenger.clear()                                              #Output Pet status
            self.messenger.setpos(0, 20)
            self.messenger.write(str(self.owner.pet),move=False,align='center',font=("Century Gothic",15,("bold","normal")))
            self.messenger.setpos(0,70)
        elif i == 3:
            if self.owner.get_num_items() > 0:  #If Owner has items, open the item menu
                self.open_item_menu()
            else:                               #If not, output that they don't have items
                self.messenger.setpos(0,70)
                self.messenger.write("You don't have any items!",move=False,align='center',font=("Century Gothic",15,("bold","normal")))

    #------------ Item Menu Cursor --------------------------------------------#
    def item_menu_cursor_up(self):
        """Moves the item menu cursor up if possible."""
        self.messenger.clear()

        (old_x, old_y) = self.inventory_clerk.pos()                             #Get the current position of the cursor
        if old_y < self._positions_in_item_menu[0][1]:                              #If the cursor can still go up,
            self.inventory_clerk.setpos(old_x, old_y + 20)                             #Move it up!


    def item_menu_cursor_down(self):
        """Moves the item menu cursor down if possible."""
        self.messenger.clear()

        (old_x, old_y) = self.inventory_clerk.pos()                             #Get the current position of the cursor
        if old_y > self._positions_in_item_menu[-1][1] + 15:                    #If the cursor can still go down, (position of last option on screen)
            self.inventory_clerk.setpos(old_x, old_y - 20)                          #Move it down!


    def display_item_menu_cursor(self, option_pos):
        """Moves the item menu cursor to point at the option that is located at
        the provided point position.
        pre: option_pos is a tuple representing a position, (x, y).
        post: The cursor will be pointing to this location."""
        self.update_home_money()                                                #Updates the money on the screen everytime the cursor is moved
        self.update_time_events()                                               #Updates time events
        self.messenger.clear()                                                  #Clears messages

        self.inventory_clerk.shape("arrow_right.gif")
        (cursor_x, cursor_y) = option_pos
        cursor_x -= 25
        cursor_y += 15
        self.inventory_clerk.setpos(cursor_x, cursor_y)
        self.inventory_clerk.st()


    def item_menu_cursor_selection(self):
        """When the user selects something in the Item Menu with the cursor,
        this method is used to determine what to do. It then does the appropriate
        action."""
        self.update_time_events()                                               #Updates time events
        self.messenger.clear()

        pos = self.inventory_clerk.pos()                                        #Get cursor's position
        pos = (pos[0]+25, pos[1]-15)                                            #Realign position of cursor with item
        index = None                                                            #To hold the index of the selected item in Owner's items
        for i, p in enumerate( self._positions_in_item_menu ):                  #For each item in their possesstion...
            if p == pos:                                                            #If the positions are the same
                index = i                                                               #Store the index
                break

        self.instructor.setpos(0,90)                                            #Write that item was used
        self.instructor.clear()
        self.instructor.write("You use the "+self.owner.items[index].get_name()+".",move=False,align='center',font=("Century Gothic",20,("bold","normal")))
        self.owner.use_item( self.owner.items[index] )                          #Use the item!
        self.update_item_menu_screen()                                          #Reloads the menu
        if self.owner.get_num_items() == 0:                                     #If the owner has no more items, close the menu.
            self.close_item_menu()

    #------------ Money -------------------------------------------------------#
    def update_home_money(self):
        """Updates the money display on the Home Screen."""
        self.balance.clear()
        self.balance.ht()
        self.balance.setpos(340, 190)
        self.balance.write(self.owner.money_balance(),move=False,align='right',font=("Century Gothic",25,("bold","normal")))
        self.balance.shape("money2.gif")
        self.balance.setpos(200, 210)
        self.balance.showturtle()

    #------------ Item Menu ---------------------------------------------------#
    def open_item_menu(self):
        """Displays the list of items currently in the owner's possession. If
        they have no items, that is outputted instead."""
        self.inventory_clerk.clear()

        self.wn.onkey(None, 'Return')
        self.wn.onkey(None, 'Up')
        self.wn.onkey(None, 'Down')
        self.wn.onkey(None, 'Left')
        self.wn.onkey(None, 'Right')

        if self.owner.get_num_items() > 0:
            positions = self.__calculate_item_menu_positions()
            for i, item in enumerate( self.owner.get_items() ):
                self.inventory_clerk.setpos( positions[i] )
                self.inventory_clerk.write(item.get_name(), move=False,align='left',font=("Century Gothic",20,("bold","normal")))

            self.display_item_menu_cursor(positions[0])

            self.wn.onkey(self.item_menu_cursor_selection, 'Return')
            self.wn.onkey(self.item_menu_cursor_up, 'Up')
            self.wn.onkey(self.item_menu_cursor_down, 'Down')
            self.wn.onkey(self.display_item_menu_item_properties,'p')
            self.wn.onkey(self.display_item_menu_item_properties,'P')
            self.wn.onkey(self.close_item_menu, 'BackSpace')

            self.messenger.setpos(0, 80)
            self.messenger.write("Press 'P' to view the properties of an item.", move=False,align='center',font=("Century Gothic",20,("bold","normal")))
            self.instructor.setpos(-300, 50)
            self.instructor.write("Press 'Backspace' to", move=False,align='left',font=("Century Gothic",10,("bold","normal")))
            self.instructor.setpos(-300, 30)
            self.instructor.write("exit the item menu.", move=False,align='left',font=("Century Gothic",10,("bold","normal")))


    def update_item_menu_screen(self):
        """Updates the item menu to show any changes in the Owner's possessions."""
        self.inventory_clerk.clear()
        if self.owner.get_num_items() > 0:
            positions = self.__calculate_item_menu_positions()
            for i, item in enumerate( self.owner.get_items() ):
                self.inventory_clerk.setpos( positions[i] )
                self.inventory_clerk.write(item.get_name(), move=False,align='left',font=("Century Gothic",20,("bold","normal")))
            self.display_item_menu_cursor(positions[0])


    def close_item_menu(self):
        """Closes the Item Menu."""
        self.messenger.clear()
        self.inventory_clerk.clear()

        self.wn.onkey(None, 'Return')
        self.wn.onkey(None, 'Up')
        self.wn.onkey(None, 'Down')
        self.wn.onkey(None,'p')
        self.wn.onkey(None,'P')
        self.wn.onkey(None,'BackSpace')

        self.setup_home_screen()


    def __calculate_item_menu_positions(self):
        """This method will find each of the positions of the items in the item
        menu.
        pre: The owner must have items in their possession.
        post: Returns a list of tuples containing the positions of each, in order."""
        x, y = (-300, 0)
        positions = []

        for i, item in enumerate( self.owner.get_items() ):
            positions.append( (x,y) )
            y -= 20

        self._positions_in_item_menu = positions                                #Needed for cursor onkey methods
        return positions


    def display_item_menu_item_properties(self):
        """Displays the Item properties on the Home Screen when an Item is
        selected in the Item Menu by the Return key."""
        self.messenger.clear()                                                  #Clear screen first

        item_selected = ""                                                      #Will contain the Item object that was chosen
        (x, y) = self.inventory_clerk.pos()                                     #Get the current position of the cursor
        pos = (x+25, y-15)                                                      #Realign the cursor's position with the printed options

        for i, p in enumerate( self._positions_in_item_menu ):                  #For every item position,
            if pos == p:                                                            #If the cursor is at that option position,
                item_selected = self.owner.items[i]                                      #Find the option/item that it is.

        self.messenger.setpos(180, -20)                                               #Use turtle to display the Item properties
        if type(item_selected) is not str:
            self.messenger.write(str(item_selected),move=False,align='center',font=("Century Gothic",15,("bold","normal")))







#------------ Store Screen ----------------------------------------------------#

    #------------ Screen Settings ---------------------------------------------#
    def setup_store(self):
        """Sets up the Store Screen.
        post: The Home Screen is cleared and the Store Screen is shown"""
        self.hide_home_screen()

        self.instructor.setpos(0, 200)      #Instructions
        self.instructor.write("Welcome to the Shop!",move=False,align='center',font=("Century Gothic",30,("bold","normal")))
        self.instructor.setpos(0, 180)
        self.instructor.write("Choose a category using the arrow keys and choose with Enter.",move=False,align='center',font=("Century Gothic",13,("bold","normal")))
        self.instructor.setpos(0, 160)
        self.instructor.write("To see an item's properties, press 'P' while it is selected. Go back with 'Backspace'.",move=False,align='center',font=("Century Gothic",13,("bold","normal")))

        self.shop_button.shape("home.gif")  #Home Button
        self.shop_button.setpos(240, -240)
        self.shop_button.write("Home",move=False,align='center',font=("Century Gothic",12,("bold","normal")))
        self.shop_button.setpos(300, -200)
        self.shop_button.showturtle()

        self.inventory_clerk.shape("arrow_right.gif")
        self.update_store_screen()

        self.__activate_store_keypresses()


    def update_shop_money(self):
        """Updates the money display on the Store Screen."""
        self.balance.clear()
        self.balance.write("$"+str(self.owner.money_balance()),move=False,align='center',font=("Century Gothic",15,("bold","normal")))


    def update_store_screen(self, last_choice=None):
        """Updates the Store Screen to show any selections in the Store and any
        messages.
        pre: last_choice is the previously selected option from the Shop (string
        or Item), or is None if there is no previously selected option."""
        self.inventory_clerk.clear()                                            #Clear writing
        self.balance.clear()
        self.bag.clear()

        self.balance.setpos(0, -220)                                            #Write money balance on the screen
        self.balance.write("$"+str(self.owner.money_balance()),move=False,align='center',font=("Century Gothic",15,("bold","normal")))

        options = self.get_shop_options(last_choice)                            #The options at store
        if len(options) > 0:
            self.__calculate_shop_option_positions(options)                         #The positions of these options on screen
            self.display_options(options, self._positions_of_shop_options)          #Displays the store options
            self.display_shop_cursor(self._positions_of_shop_options[0])            #Points the cursor to the first item


    def hide_store_screen(self):
        """Hides the Store Screen from view.
        post: Leaves the window blank except for the background."""
        self.inventory_clerk.clear()    #Clear screen
        self.inventory_clerk.ht()
        self.messenger.clear()
        self.instructor.clear()
        self.balance.clear()
        self.bag.clear()
        self.shop_button.clear()
        self.shop_button.ht()
        self.shop_button.onclick(None)

        self.wn.onkey(None, 'Return')   #Unbind keys
        self.wn.onkey(None, 'p')
        self.wn.onkey(None, 'P')
        self.wn.onkey(None, 'Up')
        self.wn.onkey(None, 'Down')
        self.wn.onkey(None, 'BackSpace')


    #------------ Keypress Functions ------------------------------------------#
    def __activate_store_keypresses(self):
        """Activates the onkey functions for the Store Screen and makes the
        window listen."""
        self.wn.onkey(self.shop_cursor_select, 'Return')
        self.wn.onkey(self.display_shop_item_properties, 'p')
        self.wn.onkey(self.display_shop_item_properties, 'P')
        self.wn.onkey(self.shop_cursor_up, 'Up')
        self.wn.onkey(self.shop_cursor_down, 'Down')
        self.wn.onkey(self.go_back, 'BackSpace')

        self.wn.listen()

    #------------ Cursor ------------------------------------------------------#
    def display_shop_cursor(self, option_pos):
        """Moves the shop cursor to point at an option, given its position.
        pre: option_pos is a tuple representing a position, (x, y).
        post: The shop cursor will be pointing to this location."""
        cursor_x, cursor_y = option_pos
        cursor_x -= 30
        cursor_y += 15
        self.inventory_clerk.setpos(cursor_x, cursor_y)
        self.inventory_clerk.showturtle()


    def shop_cursor_up(self):
        """Moves the shop cursor up, if possible."""
        self.bag.clear()                                                        #Clear any Item Properties that may be showing
        self.update_time_events()
        self.messenger.clear()
        self.update_shop_money()

        (old_x, old_y) = self.inventory_clerk.pos()                             #Get the current position of the cursor
        if (old_x, old_y) == (230, -200):                                       #If on the Home button, go to the last cursor.
            self.inventory_clerk.setpos(self._positions_of_shop_options[-1][0] - 30, self._positions_of_shop_options[-1][1] + 15)
        elif old_y < 120:                                                        #If the cursor can still go up,
            self.inventory_clerk.setpos(old_x, old_y + 50)                          #Move it up!


    def shop_cursor_down(self):
        """Moves the shop cursor down, if possible."""
        self.bag.clear()                                                        #Clear any Item Properties that may be showing
        self.update_time_events()
        self.messenger.clear()
        self.update_shop_money()

        (old_x, old_y) = self.inventory_clerk.pos()                             #Get the current position of the cursos
        if old_y > self._positions_of_shop_options[-1][1] + 15:                 #If the cursor can still go down, (position of last option on screen)
            self.inventory_clerk.setpos(old_x, old_y - 50)                          #Move it down!
        elif old_y == self._positions_of_shop_options[-1][1] + 15:              #If on the last cursor, go to the Home button
            self.inventory_clerk.setpos(230, -200)


    def shop_cursor_select(self):
        """Selects an item that the shop cursor is pointing to and does the
        intended action to it, based on the item."""
        self.bag.clear()                                                        #Clear any Item Properties that may be showing
        self.update_time_events()
        self.messenger.clear()
        self.update_shop_money()

        (x, y) = self.inventory_clerk.pos()                                     #Get the current position of the cursor
        pos = (x+30, y-15)                                                      #Realign the cursor's position with the printed options
        for i, p in enumerate( self._positions_of_shop_options ):               #For every option position,
            if pos == p:                                                            #If the cursor is at that option position,
                option_selected = self._options[i]                                      #Find the option that was chosen.
                self.__handle_selection(option_selected)                                #Handle the chosen option accordingly
        if x == abs(x):                                                         #If the home button was chosen, load home screen (its only option in quads. 2/3)
            self.setup_home_screen()


    def display_shop_item_properties(self):
        """Displays the Item properties on the Store Screen when an Item is
        selected.
        pre: What was selected was an Item."""
        self.update_time_events()                                               #Time events and screen clearing
        self.messenger.clear()
        self.bag.clear()
        self.update_shop_money()

        (x, y) = self.inventory_clerk.pos()                                     #Get the current position of the cursor
        pos = (x+30, y-15)                                                      #Realign the cursor's position with the printed options
        for i, p in enumerate( self._positions_of_shop_options ):               #For every option position,
            if pos == p:                                                            #If the cursor is at that option position,
                option_selected = self._options[i]                                      #Find the option/item that it is.

        self.bag.setpos(180, -20)                                               #Use Bag the Turtle to display the Item properties
        if type(option_selected) is not str:
            self.bag.write(str(option_selected),move=False,align='center',font=("Century Gothic",15,("bold","normal")))

    #------------ Store Misc. -------------------------------------------------#
    def go_back(self):
        """Goes back to the last set of choices in the Shop and displays them."""
        self.update_store_screen(self.shop.inventory.find_grandparent(self._options[0]))


    def buy_item(self, bought_Item):
        """Buys the provided Item.
        pre: bought_Item is in the Shop's inventory.
        post: Removes Item from the Shop, puts it in the Owner's inventory and
        updates the screen to the front of the store."""
        did_sell = self.shop.sell(bought_Item, self.owner)
        if did_sell:
            self.owner.add_item(bought_Item)
        self.bought_message(did_sell)
        self.update_store_screen(bought_Item)


    def bought_message(self, did_sell):
        """Outputs to the screen whether the item was bought or not.
        pre: did_sell is True or False."""
        self.messenger.clear()
        self.messenger.setpos(0, -240)
        if did_sell:
            self.messenger.write("You bought the item.",move=False,align='center',font=("Century Gothic",15,("bold","normal")))
        else:
            self.messenger.write("You have have too little money or too many items!",move=False,align='center',font=("Century Gothic",12,("bold","normal")))


    #------------ Store Options -----------------------------------------------#
    def get_shop_options(self, last_choice=None):
        """Gets the current options for the shop based on last_choice.
        pre: last_choice is a string (category in the store), an Item (bought
        from the store), or None, meaning to start from the front of the store.
        post: Returns the options as a list of strings or Items."""
        options = self.shop.get_choices(last_choice)                            #The options at store
        self._options = options                                                 #This stores the current options in the Store; needed for cursor onkey methods
        return options


    def display_options(self, options, positions):
        """Displays the provided store options onscreen.
        pre: options is a list of strings or Items."""
        positions = self.__calculate_shop_option_positions(options) #Calculate positioning

        for i, item in enumerate(options):
            self.inventory_clerk.setpos( positions[i] ) #Put each option into position according to previously calculated ones
            if type(item) is str:
                self.inventory_clerk.write(item, move=False,align='left',font=("Century Gothic",20,("bold","normal"))) #Display a string
            else:
                self.inventory_clerk.write(item.get_name(), move=False,align='left',font=("Century Gothic",20,("bold","normal"))) #Display an item


    def __calculate_shop_option_positions(self, options):
        """Given a list of options to write to the screen, this method will find
        each of their positions.
        pre: options is a list of strings or Items.
        post: Returns a list of tuples containing the positions of each, in order."""
        x, y = (-250, 120)  #Top most option

        positions = []
        for i, item in enumerate(options):
            if i > 7:
                x = 250
                y = 120
            positions.append( (x,y) )
            y -= 50                                                                 #Options are 50 pixels apart
        self._positions_of_shop_options = positions                             #The position of the options currently in the Shop; Needed for cursor onkey methods
        return positions


    def __handle_selection(self, option_selected):
        """Handles the selected option, doing one of the following:
            -If the option is a string (therefore a category), get the next
            set of options and display them.
                -If there are no options in the next menu, do not change.
            -If the option is an Item
                -Buy the Item, removing it from the store.
                -Add it to Owner's items
                -Reset the Store Screen to the front of the store.
        pre: option_seleted is a valid option in the Shop (string or Item)"""
        if type(option_selected) is str:
            if len( self.shop.get_choices(option_selected) ) == 0:
                pass
            else:
                self.update_store_screen(option_selected)
        else:
            self.buy_item(option_selected)

#------------------------------------------------------------------------------#
