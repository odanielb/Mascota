#-------------------------------------------------------------------------------
# Name:        TreeNode.py
# Purpose:  Create a class for a node of a binary tree
#
# Author:      odanielb, Bridget O'Daniel
#
# Acknowledgements:
#-------------------------------------------------------------------------------

class TreeNode(object):

    def __init__(self, item=None):
        """Creates a tree node with the specified item and no children.
        pre: item is any value type, will default to None."""
        self.item = item
        self.children = []                                                      #List to hold all child nodes of this Node


    def set_item(self, item):
        """Method that sets the Node to contain the provided item."""
        self.item = item


    def get_item(self):
        """Method that returns the item contained in the Node."""
        return self.item


    def get_num_children(self):
        """Method that returns the number of children the Node has."""
        return len(self.children)


    def add_child(self, node):
        """Method that adds a child to the Node, will be added as the rightmost
        child.
        pre: node is a TreeNode object that is not already a child.
        post: node will be added as the rightmost child of Node."""
        if node not in self.children:                                           #If the node isn't already a child of Node,
            self.children.append(node)                                              #Add it to the end of the list of children


    def delete_child(self, child):
        """Method that deletes the provided child node from the children of self.
        pre: child is a TreeNode object that is a child of self.
        post: child is no longer a child of self."""
        for i, c in enumerate(self.children):                                   #For each child in the Node's children
            if c is child and c.is_leaf():                                          #If that child is the one we're looking for and it has no children
                del self.children[i]                                                    #Delete it.


    def set_child(self, child_index, node):
        """Method that sets the Node's specified child to contain the provided node.
        pre: node is a TreeNode object. child_index is an int representing which
        child of self to set. The possible range is 0 - (self.get_num_children()-1),
        where 0 is the first, leftmost child. If child_index is invalid, no
        change will be made.
        post: The child will be set to be the provided node."""
        try:
            self.children[child_index] = node                                   #Set the node to be the child at the provided index.
        except:                                                                 #If the index is invalid,
            pass                                                                    #Make no changes


    def get_child(self, child_index):
        """Method that returns the specified child of the Node.
        pre: child_index is an int between 0 and (num_children-1). If the child
        is invalid, None will be returned.
        post: Returns the child (TreeNode object or None)"""
        try:
            return self.children[child_indexndex]                               #Return the child at the provided index
        except:                                                                 #If the index is invalid,
            return None                                                             #Returns None


    def get_all_children(self):
        """Method that returns all the children of the Node.
        post: returns the children in a tuple."""
        return tuple(self.children)


    def is_leaf(self):
        """Method that checks if the Node is a leaf (ie, has no children).
        post: Returns True or False."""
        if len(self.children) == 0:                                             #If the Node has no children, it's a leaf
            return True
        else:
            return False
