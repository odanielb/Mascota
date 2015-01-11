#-------------------------------------------------------------------------------
# Name:        Tree
# Purpose: To make a class for the creation of a Tree container class without a
#    a maximum number of children per node, and to which more children can be
#    added at any point.
#
# Author:      odanielb, Bridget O'Daniel
#
# Acknowledgements:
#    Help with breadth-first algorithm: http://en.wikipedia.org/wiki/Breadth-first_search
#-------------------------------------------------------------------------------

from TreeNode import TreeNode
from MyQueue import Queue

class Tree(object):
    """A Tree container class without a set number of children per node and
    allows for additional children to be added to nodes as well as the ability
    to traverse the items using a pointer and to delete nodes as needed. Works
    with the TreeNode class."""


    def __init__(self):
        """Creates an empty Tree object.
        post: Tree's root is initialized to None."""
        self.root = None

#------------ Root methods ----------------------------------------------------#

    def set_root(self, item):
        """If the Trees's root is None, creates a TreeNode object containing item
        and sets this node as the root. If the Tree already has a root, alters
        the root to contain item.
        post: The Tree will have a root node containing item."""
        if self.root is None:
            self.root = TreeNode(item)
        else:
            self.root.set_item(item)


    def get_root(self):
        """Method that returns the root of the Tree.
        post: Returns the root, which is either a TreeNode object or None."""
        return self.root

#------------ Deletion --------------------------------------------------------#

    def delete_leaf(self, leaf):
        """Deletes the provided leaf node of the tree.
        pre: leaf is a TreeNode object with no children and is within self.
        post: The leaf node will be deleted from the tree."""
        if leaf.is_leaf():
            parent = self.find_parent(leaf)
            parent.delete_child(leaf)


########## USED FOR BIG-O IN THE REPORT ########################################
    def find_parent(self, node):
        """Finds and returns the parent of the provided node.
        pre: node is a TreeNode object.
        post: Returns a TreeNode object that is the parent of node. If the node
        is not in the tree or is the root node, returns None."""
        for n in self.breadth_first_generator():
            if node in n.get_all_children():
                return n
        return None
################################################################################

    def find_grandparent(self, node):
        """Finds and returns the grandparent of the provided node.
        pre: node is a TreeNode object.
        post: Returns a TreeNode object that is the grandparent of node. If the
        node is not in the tree or is the root node, returns None."""
        prnt = self.find_parent(node)
        gran = self.find_parent(node)
        return gran

#------------ Preorder Transversals -------------------------------------------#

    # ------- List of Nodes ---------------------------------------------------#
    def nodes(self):
        """Returns all nodes in the tree as a nested list. For example:
        [ root, [  [ branch1, [leaf1, leaf2, leaf3] ], [ branch2, [leaf4, leaf5] ] ]  ]

        In each level of the list, there is a list containing the node at list[0]
        and the children of that node in a list at list[1].

        Note: If the tree is empty, this method will return [None]."""
        return self._preorder_list_maker(self.root)


    def _preorder_node_list_maker(self, root):
        """Creates a nested list of nodes in the tree and returns it. For example:
        [ root, [  [ branch1, [leaf1, leaf2, leaf3] ], [ branch2, [leaf4, leaf5] ] ]  ]
        pre: root should be the root of the tree on the initial call.
        post: returns a nested list of nodes."""
        root_children = []
        if root is not None:
            if root.get_num_children() == 0:
                return root
            else:
                for child in root.get_all_children():
                    root_children.append( self._preorder_node_list_maker(child) )
                return [root, root_children]
        else:
            return [None]

    #-------- List of items ---------------------------------------------------#
    def items(self):
        """Returns all the nodes' items in the tree as a nested list. For example:
        [ root, [  [ branch1, [leaf1, leaf2, leaf3] ], [ branch2, [leaf4, leaf5] ] ]  ]

        In each level of the list, there is a list containing the node's item at list[0]
        and those of the children of that node in a list at list[1].

        Note: If the tree is empty, this method will return [None]."""
        return self._preorder_item_list_maker(self.root)


    def _preorder_item_list_maker(self, root):
        """Creates a nested list of the node's item in the tree and returns it. For example:
        [ root, [  [ branch1, [leaf1, leaf2, leaf3] ], [ branch2, [leaf4, leaf5] ] ]  ]
        pre: root should be the root of the tree on the initial call.
        post: returns a nested list of values."""
        root_children = []
        if root is not None:
            if root.get_num_children() == 0:
                return root.get_item()
            else:
                for child in root.get_all_children():
                    root_children.append( self._preorder_node_list_maker(child) )
                return [root.get_item(), root_children]
        else:
            return [None]

    #-------- Preorder Iterator -----------------------------------------------#
    def preorder_node_iterator(self):
        """Returns a preorder iterator of the tree that will return nodes"""
        return self._preorder_node_generator(self.root)


    def _preorder_node_generator(self, root):
        """A recursive generator that yields the current node in a preoder
        transversal of the tree, starting with the root node.
        pre: If self.root is None, it will yield None."""
        yield root
        for child in root.children:
            yield self._preorder_node_generator(child)


#------------ Breadth-first generator -----------------------------------------#

    def breadth_first_generator(self):
        """A generator that yields the current node in a breadth first transversal
        of the tree, starting with the root node.
        pre: If self.root is None, it will yield None."""
        queue = Queue()                                                         #Queue to store the nodes to traverse through
        queue.enqueue(self.root)                                                #Start the traversal with the root of the tree

        while queue.size() != 0:                                                #While the queue of nodes isn't empty:
            current_node = queue.dequeue()                                          #Look at the node from the front of the queue
            yield current_node                                                      #Yield that node

            if current_node is not None:                                        #If the current node isn't None (ie, an empty tree):
                for child in current_node.children:                                 #For every child the node has:
                    queue.enqueue(child)                                                #Add each to the end of the queue
