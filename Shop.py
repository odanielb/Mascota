#-------------------------------------------------------------------------------
# Name:        Shop.py
# Purpose: To create class objects that represent a Shop in a tree format, with
#    categories of items as the nodes and the items themselves stored in the
#    leaves. Works closely with the Item class.
#
# Author:      odanielb, Bridget O'Daniel
#
# Acknowledgements:
#-------------------------------------------------------------------------------

from TreeNode import TreeNode
from Tree import Tree
from Item import Item
import time

class Shop(object):
    """This class defines a Shop object that utilizes a tree format to house the
    Item objects for use by Pet objects available for purchase in the store."""

    RESTOCK_TIME = 90 #Every 90 seconds, the Shop is restocked

    def __init__(self):
        """Creates a Shop object to house Item objects available for purchase
        and fills it with a default inventory."""
        self.inventory = Tree()                                                 #The inventory of the store is a Tree object
        self.default_stock()                                                    #Stock the inventory!
        self.__time_last_restocked = time.time()                                #Keeps track of when the last restock was

#------------ Shopping/Traversal ----------------------------------------------#

    def get_choices(self, last_choice=None):
        """Returns a list of the choices based on the last choice. For example,
        you have to decide that you want clothing rather than food before you
        can pick a hat.

        pre: The Shop is not empty, and last_choice is the category or option
        that was last chosen during this visit to the store (string or Item).
        If not provided, there was no previous choice (None).

        post: The choices will be returned, either a list of strings or Item
        objects. If the choice is not in the store, an empty list will be returned."""
        #Note: The choices are the contents of all the nodes at the particular depth of the Shop's tree.

        if type(last_choice) is str:                                            #If the last choice was a string, ie not an Item,
            last_node = self.__find_node_containing(last_choice)                    #Find the node that contains the last choice
            if last_node is None:                                                   #If no node containing it was found
                return []                                                               #Return an empty list

        else:                                                                   #If there was no previous choice or the last choice was an Item,
            last_node = self.inventory.get_root()                                   #We start from the root again

        choices = []                                                            #choices will hold the new choices
        children = last_node.get_all_children()                                 #The children of the last node are the new possible choices
        for node in children:                                                   #For each node in the collection of children,
            choices.append(node.get_item())                                         #Add its item as a possible choice.

        return choices


    def go_back(self, item):
        """Returns the previous set of choices.
        pre: item is an option in the current set of choices (that you wish to
        leave from) and is either a string or an Item.
        post: Returns the previous set of choices as a list. If there are no
        choices before the given item, then an empty list will be returned."""
        current_node = self.__find_node_containing(item)
        if current_node is not None:
            parent = self.inventory.find_parent(current_node)
            grandparent = self.inventory.find_parent(current_node)
            children = grandparent.get_all_children()
            choices = []
            for child in children:
                choices.append(child.get_item())
        else:
            choices = []

        return choices


    def __find_node_containing(self, target):
        """Returns the node in the Shop's Tree that contains the provided target.
        If target is not found, returns None.
        pre: target is either an Item object or a string.
        post: returns a TreeNode object."""
        for node in self.inventory.breadth_first_generator():
            if node.get_item() is target:
                return node
        return None

#------------ Selling ---------------------------------------------------------#

    def sell(self, item, owner):
        """Sells an item from the Shop. Returns True if transaction was possible,
        False if not.
        pre: owner is an Owner object and item is an Item object that is in the
        Shop's inventory.
        post: The provided owner is charged with the price of the item and the
        item is removed from the Shop, or nothing happens if the owner can't
        afford it. returns True if item is sold, False if not."""
        if owner.is_affordable( item.get_cost() ) and (not owner.is_items_full()):  #If item is affordable and the Owner can have more items
            self._charge(item, owner)                                               #Charge owner for price of item
            self.inventory.delete_leaf(self.__find_node_containing(item))           #Delete the item from the Tree/inventory
            return True
        return False


    def _charge(self, item, owner):
        """Charges the Owner for the price of the Item they are buying, provided
        the Owner has enough money.
        pre: item is an Item object in the Shop, owner is an Owner object.
        post: The owner is charged the price of the item."""
        if owner.is_affordable( item.get_cost() ):                              #If the owner can afford the cost,
            owner.pay( item.get_cost() )                                            #Have the owner pay for the item

#------------ Stocking --------------------------------------------------------#

    def check_if_restock(self):
        """Checks if its been long enough for Shop to be restocked. If so, it is
        restocked.
        pre: The Shop has been stocked before.
        post: The Shop is restocked with Items if necessary, or nothing is
        changed."""
        if time.time() - self.__time_last_restocked >= self.RESTOCK_TIME:       #if it's time to restock,
            self.restock()                                                          #Do it


    def restock(self):
        """Restocks the Shop with the appropriate Items.
        post: The Shop's inventory is full again."""
        self.default_stock()                                                    #Restock using the default stock option.
        self.__time_last_restocked = time.time()                                #Change time inventory was last restocked


    def default_stock(self):
        """Stocks a Shop object with a default inventory.
        Note: if Shop has already been stocked, this method resets the inventory.
        Items are the leaf nodes of the Tree representing the inventory.
        post: The Shop will be stocked with Item objects according to the default."""
        self.inventory = Tree()                                                 #Sets inventory as a new Tree
        self.inventory.set_root("Shop")                                         #Make the root node contain "Shop"
        generator = self.inventory.breadth_first_generator()                    #Create a generator to iterate through the tree while we add nodes

        root = generator.next()                                                 #Starting from the root, add the categories as children
        root.add_child ( TreeNode("Clothing") )
        root.add_child ( TreeNode("Hygiene") )
        root.add_child ( TreeNode("Food") )
        root.add_child ( TreeNode("Toys") )

        #Since the generator traverses breadth-first, it will go through all the just-added categories first.
        clothing = generator.next()                                             #Add Items under the category Clothing
        clothing.add_child( TreeNode( Item("Baseball Cap", 50, 0, 25, 0, 0) ) )
        clothing.add_child( TreeNode( Item("Cool Cape", 150, 0, 70, 5, 0) ) )
        clothing.add_child( TreeNode( Item("Feather Hat", 1000, 0, 50, 5, 0) ) ) #name, cost, hunger, happy, health, friendship
        clothing.add_child( TreeNode( Item("Crown", 10000, 0, 100, 10, 1) ) )

        hygiene = generator.next()                                              #Add Items under the category Hygiene
        hygiene.add_child( TreeNode( Item("Soap", 50, -10, 5, 20, 0) ) )
        hygiene.add_child( TreeNode( Item("Toothbrush", 100, -5, 10, 20, 0) ) )
        hygiene.add_child( TreeNode( Item("Shampoo", 200, 0, 15, 50, 0) ) )
        hygiene.add_child( TreeNode( Item("Brush", 500, 0, 50, 60, 0) ) )

        food = generator.next()                                                 #Add Items under the category Food
        food.add_child( TreeNode( Item("Apple", 50, 20, 0, 40, 0) ) )
        food.add_child( TreeNode( Item("Hamburger", 150, 45, 15, -30, 0) ) )
        food.add_child( TreeNode( Item("Salad", 300, 40, -15, 20, 0) ) )
        food.add_child( TreeNode( Item("Cake", 10000, 70, 80, -20, 1) ) )

        toys = generator.next()                                                 #Add Items under the category Toys
        toys.add_child( TreeNode( Item("Toy Ball", 100, -20, 25, 5, 0) ) )
        toys.add_child( TreeNode( Item("Kite", 250, -25, 40, 15, 0) ) )
        toys.add_child( TreeNode( Item("Chess", 550, -5, 60, 10, 0) ) )
        toys.add_child( TreeNode( Item("Videogame", 10000, -10, 70, -10, 1) ) )










